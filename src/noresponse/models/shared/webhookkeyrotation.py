from __future__ import annotations
from .signingsecret import SigningSecret, SigningSecretTypedDict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class WebhookKeyRotationTypedDict(TypedDict):
    r"""The 201 answer of POST /v1/webhooks/{endpoint_id}/rotate: the new signing secret, shown once, which signs every delivery from now on, and when the key it replaced stops verifying. Until then a receiver accepts both."""

    endpoint_id: str
    r"""Opaque id of the endpoint registration."""
    signing_secret: SigningSecretTypedDict
    r"""A newly issued signing key with its secret, shown only in this answer. A receiver verifies NR-Webhook-Signature with the secret's UTF-8 bytes as the HMAC-SHA256 key."""
    previous_key_id: str
    r"""The key that signed until this rotation."""
    previous_key_expires_at: str
    r"""When the previous key stops verifying: 7 days after the rotation."""


class WebhookKeyRotation(BaseModel):
    r"""The 201 answer of POST /v1/webhooks/{endpoint_id}/rotate: the new signing secret, shown once, which signs every delivery from now on, and when the key it replaced stops verifying. Until then a receiver accepts both."""

    endpoint_id: str
    r"""Opaque id of the endpoint registration."""

    signing_secret: SigningSecret
    r"""A newly issued signing key with its secret, shown only in this answer. A receiver verifies NR-Webhook-Signature with the secret's UTF-8 bytes as the HMAC-SHA256 key."""

    previous_key_id: str
    r"""The key that signed until this rotation."""

    previous_key_expires_at: str
    r"""When the previous key stops verifying: 7 days after the rotation."""
