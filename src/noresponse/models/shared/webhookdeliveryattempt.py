from __future__ import annotations
from .failure import Failure
from .webhookdeliveryattemptstatus import WebhookDeliveryAttemptStatus
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class WebhookDeliveryAttemptTypedDict(TypedDict):
    event_id: str
    r"""The event id the receiver saw as NR-Webhook-Id and as the body's id. Replay it with POST /v1/webhooks/{endpoint_id}/deliveries/{event_id}/replay."""
    event_type: str
    r"""The event's type, as its body's type: assessment.updated, endpoint.verification, account.deleted, workspace.deleted, webhook_endpoint.disabled, account.risk_changed, audit.event, or a type added later."""
    attempt: int
    r"""Which attempt of this delivery this was: 1 for the first send, up to 9 with retries. A replay counts its own attempts from 1."""
    replay: bool
    r"""true for an attempt of a replay you asked for."""
    status: WebhookDeliveryAttemptStatus
    r"""delivered when the endpoint answered 2xx; failed otherwise, with failure naming why."""
    latency_ms: int
    r"""Milliseconds from sending the request to the answer or the failure."""
    attempted_at: str
    r"""When the request was sent. Its NR-Webhook-Timestamp is this time in Unix seconds."""
    assessment_id: NotRequired[str]
    r"""The assessment an assessment.updated event reported, while that assessment is held. Absent on every other event, on a test event and on a notice that the assessment was erased or expired."""
    account_id: NotRequired[str]
    r"""The account an account.risk_changed event reported. Absent on every other event."""
    response_code: NotRequired[int]
    r"""The HTTP status the endpoint answered. Absent when no response was read."""
    failure: NotRequired[Failure]
    r"""Why the attempt failed: the URL is no longer valid, the host did not resolve, it resolved to an address that is not public, no answer within 5 seconds, the connection failed, a 3xx (redirects are not followed) or another non-2xx status. Absent for a delivered attempt."""


class WebhookDeliveryAttempt(BaseModel):
    event_id: str
    r"""The event id the receiver saw as NR-Webhook-Id and as the body's id. Replay it with POST /v1/webhooks/{endpoint_id}/deliveries/{event_id}/replay."""

    event_type: str
    r"""The event's type, as its body's type: assessment.updated, endpoint.verification, account.deleted, workspace.deleted, webhook_endpoint.disabled, account.risk_changed, audit.event, or a type added later."""

    attempt: int
    r"""Which attempt of this delivery this was: 1 for the first send, up to 9 with retries. A replay counts its own attempts from 1."""

    replay: bool
    r"""true for an attempt of a replay you asked for."""

    status: WebhookDeliveryAttemptStatus
    r"""delivered when the endpoint answered 2xx; failed otherwise, with failure naming why."""

    latency_ms: int
    r"""Milliseconds from sending the request to the answer or the failure."""

    attempted_at: str
    r"""When the request was sent. Its NR-Webhook-Timestamp is this time in Unix seconds."""

    assessment_id: Optional[str] = None
    r"""The assessment an assessment.updated event reported, while that assessment is held. Absent on every other event, on a test event and on a notice that the assessment was erased or expired."""

    account_id: Optional[str] = None
    r"""The account an account.risk_changed event reported. Absent on every other event."""

    response_code: Optional[int] = None
    r"""The HTTP status the endpoint answered. Absent when no response was read."""

    failure: Optional[Failure] = None
    r"""Why the attempt failed: the URL is no longer valid, the host did not resolve, it resolved to an address that is not public, no answer within 5 seconds, the connection failed, a 3xx (redirects are not followed) or another non-2xx status. Absent for a delivered attempt."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["assessment_id", "account_id", "response_code", "failure"]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
