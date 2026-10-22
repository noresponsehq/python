from __future__ import annotations
from .webhooktestrequestevent import WebhookTestRequestEvent
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class WebhookTestRequestTypedDict(TypedDict):
    r"""POST /v1/webhooks/{endpoint_id}/test body: which event to send."""

    event: WebhookTestRequestEvent
    r"""endpoint.verification sends a fresh challenge now, in this call, and the endpoint is verified if it echoes it. assessment.updated queues an event whose data is a fixed example assessment, with test true, delivered and retried like any other; the endpoint must be verified."""


class WebhookTestRequest(BaseModel):
    r"""POST /v1/webhooks/{endpoint_id}/test body: which event to send."""

    event: WebhookTestRequestEvent
    r"""endpoint.verification sends a fresh challenge now, in this call, and the endpoint is verified if it echoes it. assessment.updated queues an event whose data is a fixed example assessment, with test true, delivered and retried like any other; the endpoint must be verified."""
