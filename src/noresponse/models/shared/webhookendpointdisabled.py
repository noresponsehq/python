from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class WebhookEndpointDisabledTypedDict(TypedDict):
    r"""One of the environment's endpoints stopped receiving events: every delivery attempt to it failed from failing_since until disabled_at, 72 hours or more. Its queued deliveries are dropped. Fix the receiver and verify it again with POST /v1/webhooks/{endpoint_id}/test (type endpoint.verification) to resume delivery."""

    endpoint_id: str
    r"""The endpoint that was disabled."""
    failing_since: str
    r"""The first failed attempt of the unbroken failure streak."""
    disabled_at: str
    r"""When the endpoint was disabled; equal to the event's created_at."""


class WebhookEndpointDisabled(BaseModel):
    r"""One of the environment's endpoints stopped receiving events: every delivery attempt to it failed from failing_since until disabled_at, 72 hours or more. Its queued deliveries are dropped. Fix the receiver and verify it again with POST /v1/webhooks/{endpoint_id}/test (type endpoint.verification) to resume delivery."""

    endpoint_id: str
    r"""The endpoint that was disabled."""

    failing_since: str
    r"""The first failed attempt of the unbroken failure streak."""

    disabled_at: str
    r"""When the endpoint was disabled; equal to the event's created_at."""
