from __future__ import annotations
from .webhookdeliveryattempt import (
    WebhookDeliveryAttempt,
    WebhookDeliveryAttemptTypedDict,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class WebhookDeliveryListTypedDict(TypedDict):
    r"""The 200 answer of GET /v1/webhooks/{endpoint_id}/deliveries: one page of the endpoint's delivery attempts, newest first. Each item is one POST to the endpoint. Attempts are kept for 30 days, or the workspace's retention_days when that is shorter, and are deleted with the assessment they carried. next_cursor is present only when another page exists."""

    endpoint_id: str
    r"""Opaque id of the endpoint registration."""
    items: List[WebhookDeliveryAttemptTypedDict]
    next_cursor: NotRequired[str]
    r"""Opaque cursor for the next page, MAC'd by the server and bound to the workspace and endpoint it was issued for. Pass it back unchanged as cursor; a tampered, foreign or expired cursor answers 400 invalid_cursor."""


class WebhookDeliveryList(BaseModel):
    r"""The 200 answer of GET /v1/webhooks/{endpoint_id}/deliveries: one page of the endpoint's delivery attempts, newest first. Each item is one POST to the endpoint. Attempts are kept for 30 days, or the workspace's retention_days when that is shorter, and are deleted with the assessment they carried. next_cursor is present only when another page exists."""

    endpoint_id: str
    r"""Opaque id of the endpoint registration."""

    items: List[WebhookDeliveryAttempt]

    next_cursor: Optional[str] = None
    r"""Opaque cursor for the next page, MAC'd by the server and bound to the workspace and endpoint it was issued for. Pass it back unchanged as cursor; a tampered, foreign or expired cursor answers 400 invalid_cursor."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["next_cursor"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
