"""Webhook verification. Hand-written beside the generated client.

Verify the exact bytes received: the signature is HMAC-SHA256 over
``<timestamp>.<raw body>``, so re-serialising parsed JSON breaks it.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import re
import time
from datetime import datetime
from dataclasses import dataclass
from typing import Any, Iterable, List, Literal, Mapping, Optional, Tuple, Union

import pydantic

from .responses import Assessment

__all__ = [
    "DEFAULT_TOLERANCE_SECONDS",
    "AccountDeleted",
    "AssessmentExpired",
    "EndpointDisabled",
    "EndpointVerification",
    "TenantDeleted",
    "Webhook",
    "WebhookEvent",
    "WebhookVerificationError",
    "construct_event",
    "verification_response",
]

DEFAULT_TOLERANCE_SECONDS = 300

_REQUIRED = ("nr-webhook-id", "nr-webhook-timestamp", "nr-webhook-key-id", "nr-webhook-signature")
_KEY_ID = re.compile(r"\Awhk_[A-Za-z0-9]{8,64}\Z")
_SIGNATURE = re.compile(r"\Av1=[0-9a-f]{64}\Z")
_TIMESTAMP = re.compile(r"\A[0-9]{1,12}\Z")
_CHALLENGE = re.compile(r"\A[A-Za-z0-9_-]{43}\Z")
_EVENT_ID = re.compile(r"\Aevt_[0-9A-HJKMNP-TV-Z]{26}\Z")
_ASSESSMENT_ID = re.compile(r"\Aasm_[0-9A-HJKMNP-TV-Z]{26}\Z")
_ACCOUNT_ID = re.compile(r"\A[A-Za-z0-9][A-Za-z0-9._:|-]{0,127}\Z")
_ENDPOINT_ID = re.compile(r"\Awhe_[0-9A-HJKMNP-TV-Z]{26}\Z")
_WORKSPACE_ID = re.compile(r"\A[A-Za-z0-9][A-Za-z0-9_.-]{0,122}\Z")
_DATETIME = re.compile(r"\A\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})\Z")

WebhookErrorCode = Literal[
    "missing_header",
    "duplicate_header",
    "invalid_timestamp",
    "unknown_key",
    "invalid_signature",
    "invalid_payload",
]

Headers = Union[Mapping[str, Any], Iterable[Tuple[str, str]]]


class WebhookVerificationError(Exception):
    """Raised by construct_event. Answer 400 and do not process the delivery."""

    def __init__(self, code: WebhookErrorCode, message: str) -> None:
        super().__init__(message)
        self.code: WebhookErrorCode = code


@dataclass(frozen=True)
class AssessmentExpired:
    """The final event for an assessment: it has expired and get now answers 404.

    assessment_version is the last served version; expiry is not a revision.
    """

    assessment_id: str
    account_id: str
    assessment_version: int
    status: Literal["expired"] = "expired"
    change_reason: Literal["expired"] = "expired"


@dataclass(frozen=True)
class EndpointVerification:
    endpoint_id: str
    challenge: str


@dataclass(frozen=True)
class AccountDeleted:
    """An account you erased with accounts.delete: delete what you hold for it."""

    account_id: str
    assessments_deleted: int
    """How many assessments the erasure deleted, at least 1."""
    deleted_at: str
    """When the erasure took effect, as deleted_at in the accounts.delete answer."""


@dataclass(frozen=True)
class TenantDeleted:
    """The workspace was deleted. Sent once per environment before its endpoints
    are torn down: the last event this endpoint receives."""

    workspace_id: str
    environment: Literal["live", "test"]
    deleted_at: str


@dataclass(frozen=True)
class EndpointDisabled:
    """Another endpoint of this environment was disabled after failing
    continuously for 72 hours. It receives nothing more until it is verified again."""

    endpoint_id: str
    failing_since: str
    """When its deliveries started failing."""
    disabled_at: str


@dataclass(frozen=True)
class WebhookEvent:
    """A verified delivery.

    data is an Assessment (exactly as assessments.get returns it) or an
    AssessmentExpired for type "assessment.updated", an EndpointVerification
    for type "endpoint.verification", an AccountDeleted for type
    "account.deleted", a TenantDeleted for type "tenant.deleted" and an
    EndpointDisabled for type "webhook_endpoint.disabled". Deliveries are at
    least once and unordered: deduplicate on id and keep the highest
    detail.assessment_version per assessment.
    """

    id: str
    type: Literal[
        "assessment.updated", "endpoint.verification", "account.deleted", "tenant.deleted", "webhook_endpoint.disabled"
    ]
    created_at: str
    data: Union[Assessment, AssessmentExpired, EndpointVerification, AccountDeleted, TenantDeleted, EndpointDisabled]
    test: bool = False
    """True on an event sent by webhook_endpoints.send_test_event: data is a fixed
    example assessment, not one of yours. Acknowledge it and apply nothing."""

    @property
    def expired(self) -> bool:
        """True for the terminal expiry event: delete what you hold and fetch nothing."""
        return isinstance(self.data, AssessmentExpired)


def _fail(code: WebhookErrorCode, message: str) -> WebhookVerificationError:
    return WebhookVerificationError(code, message)


def _date_time(value: str) -> bool:
    if not _DATETIME.fullmatch(value):
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def _pairs(headers: Headers) -> List[Tuple[str, Any]]:
    # httpx.Headers, starlette Headers and werkzeug Headers all keep repeated
    # values apart through multi_items() or items(multi=True).
    source: Any = headers
    if callable(getattr(source, "multi_items", None)):
        return list(source.multi_items())
    if isinstance(source, Mapping):
        try:
            return list(source.items(multi=True))  # type: ignore[call-arg]
        except TypeError:
            return list(source.items())
    return list(source)


def _collect(headers: Headers) -> dict[str, str]:
    found: dict[str, str] = {}
    for name, raw in _pairs(headers):
        key = name.lower()
        if key not in _REQUIRED:
            continue
        values = list(raw) if isinstance(raw, (list, tuple)) else [raw]
        if len(values) != 1 or key in found:
            raise _fail("duplicate_header", f"Webhook header {key} is repeated")
        if isinstance(values[0], str):
            found[key] = values[0]
    for key in _REQUIRED:
        if not found.get(key):
            raise _fail("missing_header", f"Webhook header {key} is missing")
    return found


def construct_event(
    payload: Union[bytes, str],
    headers: Headers,
    secrets: Mapping[str, Union[str, bytes]],
    *,
    tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
    now: Optional[float] = None,
) -> WebhookEvent:
    """Verify one delivery and return the typed event.

    payload is the raw request body. headers is any header mapping or list of
    pairs; each NR-Webhook-* header must appear exactly once, in any letter
    case. secrets maps each whk_ key id NoResponse gave you to its secret, so
    two can be held during a rotation.
    """
    raw = payload.encode("utf-8") if isinstance(payload, str) else bytes(payload)
    found = _collect(headers)
    timestamp = found["nr-webhook-timestamp"]
    current = time.time() if now is None else now
    if not _TIMESTAMP.match(timestamp) or abs(int(current) - int(timestamp)) > tolerance_seconds:
        raise _fail("invalid_timestamp", "Webhook timestamp is outside the replay window")
    key_id = found["nr-webhook-key-id"]
    if not _KEY_ID.match(key_id) or key_id not in secrets:
        raise _fail("unknown_key", "Webhook key id is not one this receiver holds")
    signature = found["nr-webhook-signature"]
    if not _SIGNATURE.match(signature):
        raise _fail("invalid_signature", "Webhook signature is malformed")
    secret = secrets[key_id]
    key = secret.encode("utf-8") if isinstance(secret, str) else bytes(secret)
    expected = hmac.new(key, timestamp.encode("ascii") + b"." + raw, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature[3:]):
        raise _fail("invalid_signature", "Webhook signature does not match")
    try:
        body = json.loads(raw)
    except ValueError:
        raise _fail("invalid_payload", "Webhook body is not JSON") from None
    if not isinstance(body, dict) or body.get("id") != found["nr-webhook-id"]:
        raise _fail("invalid_payload", "Webhook event id does not match NR-Webhook-Id")
    event_id, event_type, created_at, data = body["id"], body.get("type"), body.get("created_at"), body.get("data")
    if (
        not isinstance(event_id, str)
        or _EVENT_ID.fullmatch(event_id) is None
        or not isinstance(created_at, str)
        or not _date_time(created_at)
        or not isinstance(data, dict)
    ):
        raise _fail("invalid_payload", "Webhook event envelope is malformed")
    if event_type == "endpoint.verification":
        endpoint_id, challenge = data.get("endpoint_id"), data.get("challenge")
        if (
            not isinstance(endpoint_id, str)
            or _ENDPOINT_ID.fullmatch(endpoint_id) is None
            or not isinstance(challenge, str)
            or _CHALLENGE.fullmatch(challenge) is None
        ):
            raise _fail("invalid_payload", "Endpoint verification event is malformed")
        return WebhookEvent(event_id, "endpoint.verification", created_at, EndpointVerification(endpoint_id, challenge))
    if event_type == "account.deleted":
        account_id, deleted, deleted_at = data.get("account_id"), data.get("assessments_deleted"), data.get("deleted_at")
        if (
            not isinstance(account_id, str)
            or _ACCOUNT_ID.fullmatch(account_id) is None
            or not isinstance(deleted, int)
            or isinstance(deleted, bool)
            or deleted < 1
            or not isinstance(deleted_at, str)
            or not _date_time(deleted_at)
        ):
            raise _fail("invalid_payload", "Account deleted event is malformed")
        return WebhookEvent(event_id, "account.deleted", created_at, AccountDeleted(account_id, deleted, deleted_at))
    if event_type == "tenant.deleted":
        workspace_id, environment, deleted_at = data.get("workspace_id"), data.get("environment"), data.get("deleted_at")
        if (
            not isinstance(workspace_id, str)
            or _WORKSPACE_ID.fullmatch(workspace_id) is None
            or environment not in ("live", "test")
            or not isinstance(deleted_at, str)
            or not _date_time(deleted_at)
        ):
            raise _fail("invalid_payload", "Tenant deleted event is malformed")
        return WebhookEvent(event_id, "tenant.deleted", created_at, TenantDeleted(workspace_id, environment, deleted_at))
    if event_type == "webhook_endpoint.disabled":
        endpoint_id, failing_since, disabled_at = data.get("endpoint_id"), data.get("failing_since"), data.get("disabled_at")
        if (
            not isinstance(endpoint_id, str)
            or _ENDPOINT_ID.fullmatch(endpoint_id) is None
            or not isinstance(failing_since, str)
            or not _date_time(failing_since)
            or not isinstance(disabled_at, str)
            or not _date_time(disabled_at)
        ):
            raise _fail("invalid_payload", "Endpoint disabled event is malformed")
        return WebhookEvent(
            event_id, "webhook_endpoint.disabled", created_at, EndpointDisabled(endpoint_id, failing_since, disabled_at)
        )
    if event_type != "assessment.updated":
        raise _fail("invalid_payload", "Unknown webhook event type")
    if data.get("status") == "expired":
        assessment_id, account_id, version = data.get("assessment_id"), data.get("account_id"), data.get("assessment_version")
        if (
            not isinstance(assessment_id, str)
            or _ASSESSMENT_ID.fullmatch(assessment_id) is None
            or not isinstance(account_id, str)
            or _ACCOUNT_ID.fullmatch(account_id) is None
            or not isinstance(version, int)
            or isinstance(version, bool)
            or version < 1
            or data.get("change_reason") != "expired"
        ):
            raise _fail("invalid_payload", "Expired assessment event is malformed")
        return WebhookEvent(event_id, "assessment.updated", created_at, AssessmentExpired(assessment_id, account_id, version))
    try:
        assessment = Assessment.model_validate(data)
    except pydantic.ValidationError:
        raise _fail("invalid_payload", "Webhook data is not an assessment") from None
    return WebhookEvent(event_id, "assessment.updated", created_at, assessment, test=body.get("test") is True)


def verification_response(event: WebhookEvent) -> dict[str, str]:
    """The body to answer an endpoint.verification event with, as JSON, status 200."""
    if not isinstance(event.data, EndpointVerification):
        raise _fail("invalid_payload", "Not an endpoint.verification event")
    return {"challenge": event.data.challenge}


class Webhook:
    """The verification functions as one namespace: ``Webhook.construct_event(payload, headers, secrets)``."""

    construct_event = staticmethod(construct_event)
    verification_response = staticmethod(verification_response)
