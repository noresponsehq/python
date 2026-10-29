from __future__ import annotations
from .environment import Environment
from .webhookendpointstate import WebhookEndpointState
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AuditStreamTypedDict(TypedDict):
    endpoint_id: str
    environment: Environment
    actions: List[str]
    created_at: str
    endpoint_state: WebhookEndpointState
    r"""unverified until the endpoint echoes an endpoint.verification challenge (send one with POST /v1/webhooks/{endpoint_id}/test); verified receives assessment.updated events; disabled after 72 hours of continuous delivery failure, and verified again by the same challenge."""
    last_attempt_at: NotRequired[str]
    last_delivered_at: NotRequired[str]


class AuditStream(BaseModel):
    endpoint_id: str

    environment: Environment

    actions: List[str]

    created_at: str

    endpoint_state: WebhookEndpointState
    r"""unverified until the endpoint echoes an endpoint.verification challenge (send one with POST /v1/webhooks/{endpoint_id}/test); verified receives assessment.updated events; disabled after 72 hours of continuous delivery failure, and verified again by the same challenge."""

    last_attempt_at: Optional[str] = None

    last_delivered_at: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["last_attempt_at", "last_delivered_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
