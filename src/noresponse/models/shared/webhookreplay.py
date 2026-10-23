from __future__ import annotations
from .eventtype import EventType
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class WebhookReplayTypedDict(TypedDict):
    r"""The 202 answer of POST /v1/webhooks/{endpoint_id}/deliveries/{event_id}/replay: the event queued to be sent again."""

    endpoint_id: str
    r"""Opaque id of the endpoint registration."""
    event_id: str
    r"""The replayed event's id. The receiver sees the same id and body as the first time, with a new NR-Webhook-Timestamp and signature."""
    event_type: EventType


class WebhookReplay(BaseModel):
    r"""The 202 answer of POST /v1/webhooks/{endpoint_id}/deliveries/{event_id}/replay: the event queued to be sent again."""

    endpoint_id: str
    r"""Opaque id of the endpoint registration."""

    event_id: str
    r"""The replayed event's id. The receiver sees the same id and body as the first time, with a new NR-Webhook-Timestamp and signature."""

    event_type: EventType
