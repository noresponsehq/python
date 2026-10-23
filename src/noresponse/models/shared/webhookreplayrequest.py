from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class WebhookReplayRequestTypedDict(TypedDict):
    r"""POST /v1/webhooks/{endpoint_id}/deliveries/{event_id}/replay body: an empty object."""


class WebhookReplayRequest(BaseModel):
    r"""POST /v1/webhooks/{endpoint_id}/deliveries/{event_id}/replay body: an empty object."""
