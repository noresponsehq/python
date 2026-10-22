from __future__ import annotations
from .signingsecret import SigningSecret, SigningSecretTypedDict
from .webhookendpoint import WebhookEndpoint, WebhookEndpointTypedDict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class WebhookEndpointCreatedTypedDict(TypedDict):
    r"""The 201 answer of POST /v1/webhooks: the new endpoint, unverified, and its first signing secret, shown once. Store the secret where the receiver reads it, then send endpoint.verification with POST /v1/webhooks/{endpoint_id}/test."""

    endpoint: WebhookEndpointTypedDict
    r"""One of the tenant's registered webhook endpoints. Signing secrets are not part of it: a secret is shown once, when it is issued (POST /v1/webhooks and POST /v1/webhooks/{endpoint_id}/rotate)."""
    signing_secret: SigningSecretTypedDict
    r"""A newly issued signing key with its secret, shown only in this answer. A receiver verifies NR-Webhook-Signature with the secret's UTF-8 bytes as the HMAC-SHA256 key."""


class WebhookEndpointCreated(BaseModel):
    r"""The 201 answer of POST /v1/webhooks: the new endpoint, unverified, and its first signing secret, shown once. Store the secret where the receiver reads it, then send endpoint.verification with POST /v1/webhooks/{endpoint_id}/test."""

    endpoint: WebhookEndpoint
    r"""One of the tenant's registered webhook endpoints. Signing secrets are not part of it: a secret is shown once, when it is issued (POST /v1/webhooks and POST /v1/webhooks/{endpoint_id}/rotate)."""

    signing_secret: SigningSecret
    r"""A newly issued signing key with its secret, shown only in this answer. A receiver verifies NR-Webhook-Signature with the secret's UTF-8 bytes as the HMAC-SHA256 key."""
