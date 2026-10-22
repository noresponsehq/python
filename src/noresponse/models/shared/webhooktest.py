from __future__ import annotations
from .webhookendpointstate import WebhookEndpointState
from .webhooktestrequestevent import WebhookTestRequestEvent
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class WebhookTestTypedDict(TypedDict):
    r"""The 202 answer of POST /v1/webhooks/{endpoint_id}/test: the event that was sent or queued."""

    delivery_id: str
    r"""The event id the receiver sees as NR-Webhook-Id and as the body's id."""
    endpoint_id: str
    r"""Opaque id of the endpoint registration."""
    event: WebhookTestRequestEvent
    r"""endpoint.verification sends a fresh challenge now, in this call, and the endpoint is verified if it echoes it. assessment.updated queues an event whose data is a fixed example assessment, with test true, delivered and retried like any other; the endpoint must be verified."""
    state: WebhookEndpointState
    r"""unverified until the endpoint echoes an endpoint.verification challenge (send one with POST /v1/webhooks/{endpoint_id}/test); verified receives assessment.updated events; disabled after 72 hours of continuous delivery failure, and verified again by the same challenge."""
    verified: NotRequired[bool]
    r"""endpoint.verification only: true when the endpoint echoed the challenge within 5 seconds. A false answer leaves the endpoint's state as it was."""


class WebhookTest(BaseModel):
    r"""The 202 answer of POST /v1/webhooks/{endpoint_id}/test: the event that was sent or queued."""

    delivery_id: str
    r"""The event id the receiver sees as NR-Webhook-Id and as the body's id."""

    endpoint_id: str
    r"""Opaque id of the endpoint registration."""

    event: WebhookTestRequestEvent
    r"""endpoint.verification sends a fresh challenge now, in this call, and the endpoint is verified if it echoes it. assessment.updated queues an event whose data is a fixed example assessment, with test true, delivered and retried like any other; the endpoint must be verified."""

    state: WebhookEndpointState
    r"""unverified until the endpoint echoes an endpoint.verification challenge (send one with POST /v1/webhooks/{endpoint_id}/test); verified receives assessment.updated events; disabled after 72 hours of continuous delivery failure, and verified again by the same challenge."""

    verified: Optional[bool] = None
    r"""endpoint.verification only: true when the endpoint echoed the challenge within 5 seconds. A false answer leaves the endpoint's state as it was."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["verified"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
