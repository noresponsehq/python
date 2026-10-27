from __future__ import annotations
from .responsemode import ResponseMode
from .signingkey import SigningKey, SigningKeyTypedDict
from .webhookendpointstate import WebhookEndpointState
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class WebhookEndpointTypedDict(TypedDict):
    r"""One of the workspace's registered webhook endpoints. Signing secrets are not part of it: a secret is shown once, when it is issued (POST /v1/webhooks and POST /v1/webhooks/{endpoint_id}/rotate)."""

    endpoint_id: str
    r"""Opaque id of the endpoint registration."""
    url: str
    r"""The destination URL, as registered."""
    state: WebhookEndpointState
    r"""unverified until the endpoint echoes an endpoint.verification challenge (send one with POST /v1/webhooks/{endpoint_id}/test); verified receives assessment.updated events; disabled after 72 hours of continuous delivery failure, and verified again by the same challenge."""
    response_mode: ResponseMode
    r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""
    created_at: str
    signing_keys: List[SigningKeyTypedDict]
    r"""The keys a receiver may see in NR-Webhook-Key-Id, oldest first. The last one signs every new delivery; an older one keeps verifying until its expires_at."""
    verified_at: NotRequired[str]
    r"""When the endpoint last echoed a challenge. Absent until it first does."""
    failing_since: NotRequired[str]
    r"""The first failed delivery attempt of the endpoint's current failure streak. Absent while its latest attempt succeeded, before any attempt failed, and after it is verified again."""
    last_failure_at: NotRequired[str]
    r"""The latest failed delivery attempt of the current failure streak; present exactly when failing_since is. A failure more than 2 hours after it starts a new streak."""
    disabled_at: NotRequired[str]
    r"""When the endpoint was disabled after failing continuously for 72 hours, as in the webhook_endpoint.disabled event. Present while state is disabled; absent before and after it is verified again."""


class WebhookEndpoint(BaseModel):
    r"""One of the workspace's registered webhook endpoints. Signing secrets are not part of it: a secret is shown once, when it is issued (POST /v1/webhooks and POST /v1/webhooks/{endpoint_id}/rotate)."""

    endpoint_id: str
    r"""Opaque id of the endpoint registration."""

    url: str
    r"""The destination URL, as registered."""

    state: WebhookEndpointState
    r"""unverified until the endpoint echoes an endpoint.verification challenge (send one with POST /v1/webhooks/{endpoint_id}/test); verified receives assessment.updated events; disabled after 72 hours of continuous delivery failure, and verified again by the same challenge."""

    response_mode: ResponseMode
    r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""

    created_at: str

    signing_keys: List[SigningKey]
    r"""The keys a receiver may see in NR-Webhook-Key-Id, oldest first. The last one signs every new delivery; an older one keeps verifying until its expires_at."""

    verified_at: Optional[str] = None
    r"""When the endpoint last echoed a challenge. Absent until it first does."""

    failing_since: Optional[str] = None
    r"""The first failed delivery attempt of the endpoint's current failure streak. Absent while its latest attempt succeeded, before any attempt failed, and after it is verified again."""

    last_failure_at: Optional[str] = None
    r"""The latest failed delivery attempt of the current failure streak; present exactly when failing_since is. A failure more than 2 hours after it starts a new streak."""

    disabled_at: Optional[str] = None
    r"""When the endpoint was disabled after failing continuously for 72 hours, as in the webhook_endpoint.disabled event. Present while state is disabled; absent before and after it is verified again."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["verified_at", "failing_since", "last_failure_at", "disabled_at"]
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
