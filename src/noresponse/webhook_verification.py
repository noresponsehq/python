import binascii
import hashlib
import hmac
import json
from noresponse import models, utils
import re
import time
from typing import Any, Iterable, List, Mapping, Optional, Sequence, Tuple, Union, cast
from typing_extensions import Literal

DEFAULT_TOLERANCE_SECONDS = 300
r"""How far the NR-Webhook-Timestamp header may be from the receiver's clock, in seconds."""

WebhookErrorCode = Literal[
    "missing_header",
    "duplicate_header",
    "invalid_timestamp",
    "unknown_key",
    "invalid_signature",
    "invalid_payload",
]

Headers = Union[
    Mapping[str, Union[str, Sequence[str]]],
    Iterable[Tuple[str, str]],
]
r"""Request headers: a mapping of name to value or values, or (name, value) pairs."""


class WebhookVerificationError(Exception):
    r"""A webhook delivery that must not be processed. Answer the delivery with a 400 and do not process it."""

    code: WebhookErrorCode
    message: str

    def __init__(self, code: WebhookErrorCode, message: str):
        super().__init__(f"webhook verification failed: {message} ({code})")
        self.code = code
        self.message = message


_HEADER_NAMES = (
    "NR-Webhook-Id",
    "NR-Webhook-Timestamp",
    "NR-Webhook-Key-Id",
    "NR-Webhook-Signature",
)


def construct_event(
    payload: Union[bytes, str],
    headers: Headers,
    secrets: Mapping[str, str],
    *,
    tolerance_seconds: int = DEFAULT_TOLERANCE_SECONDS,
    now: Optional[float] = None,
) -> models.shared.WebhookEvent:
    r"""Verify a webhook delivery and parse its body.

    :param payload: The raw request body exactly as received; re-encoding parsed JSON breaks the signature.
    :param headers: The request headers. A header repeated in any letter case, or sent as a comma-joined list, is refused.
    :param secrets: Each key id, sent in NR-Webhook-Key-Id, mapped to its secret, so a receiver can hold two during a rotation.
    :param tolerance_seconds: Replaces DEFAULT_TOLERANCE_SECONDS.
    :param now: The receiver's clock in Unix seconds, for the tolerance check; defaults to time.time().
    :raises WebhookVerificationError: The delivery must not be processed.
    """
    body = payload.encode("utf-8") if isinstance(payload, str) else payload
    values = _header_values(headers)
    webhook_id = values["NR-Webhook-Id"]
    timestamp = values["NR-Webhook-Timestamp"]
    key_id = values["NR-Webhook-Key-Id"]
    signature = values["NR-Webhook-Signature"]

    if re.fullmatch(r"[0-9]{1,12}", timestamp) is None:
        raise WebhookVerificationError(
            "invalid_timestamp", "NR-Webhook-Timestamp is not a Unix time in seconds"
        )
    clock = time.time() if now is None else now
    if abs(clock - int(timestamp)) > tolerance_seconds:
        raise WebhookVerificationError(
            "invalid_timestamp", "NR-Webhook-Timestamp is outside the tolerance"
        )
    secret = secrets.get(key_id)
    if secret is None:
        raise WebhookVerificationError(
            "unknown_key", "NR-Webhook-Key-Id names a key this receiver does not hold"
        )
    if not secret:
        raise WebhookVerificationError(
            "invalid_signature", "the webhook secret is empty"
        )

    received = _decode_signature(signature)
    substitutions = {"timestamp": timestamp, "id": webhook_id}
    signed = _substitute("{timestamp}.", substitutions) + body
    expected = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).digest()
    if not hmac.compare_digest(expected, received):
        raise WebhookVerificationError(
            "invalid_signature", "NR-Webhook-Signature does not match"
        )

    try:
        value: Any = json.loads(body)
    except ValueError:
        raise WebhookVerificationError(
            "invalid_payload", "the body is not JSON"
        ) from None
    if not isinstance(value, dict) or value.get("id") != webhook_id:
        raise WebhookVerificationError(
            "invalid_payload", "the body's id does not equal NR-Webhook-Id"
        )

    try:
        event: models.shared.WebhookEvent = utils.unmarshal_json(
            body, models.shared.WebhookEvent
        )
    except ValueError:
        raise WebhookVerificationError(
            "invalid_payload", "the body is not a known webhook event"
        ) from None
    return event


def _header_values(headers: Headers) -> Mapping[str, str]:
    items = (
        cast(Any, headers).items()
        if callable(getattr(headers, "items", None))
        else headers
    )
    pairs: List[Tuple[str, str]] = []
    for name, value in items:
        if isinstance(value, str):
            pairs.append((name.lower(), value))
        else:
            pairs.extend((name.lower(), v) for v in value)

    values = {}
    for name in _HEADER_NAMES:
        found = [v for k, v in pairs if k == name.lower()]
        if len(found) > 1 or (found and "," in found[0]):
            raise WebhookVerificationError("duplicate_header", f"{name} is repeated")
        if not found or not found[0]:
            raise WebhookVerificationError("missing_header", f"{name} is missing")
        values[name] = found[0]
    return values


def _decode_signature(signature: str) -> bytes:
    prefix = "v1="
    encoded = signature[len(prefix) :]
    if signature.startswith(prefix) and re.fullmatch(r"(?:[0-9a-fA-F]{2})+", encoded):
        return binascii.unhexlify(encoded)
    raise WebhookVerificationError(
        "invalid_signature", "NR-Webhook-Signature is malformed"
    )


def _substitute(template: str, substitutions: Mapping[str, str]) -> bytes:
    return re.sub(
        r"\{(timestamp|id)\}",
        lambda m: substitutions.get(m.group(1), m.group(0)),
        template,
    ).encode("utf-8")
