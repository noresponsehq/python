from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class SigningSecretTypedDict(TypedDict):
    r"""A newly issued signing key with its secret, shown only in this answer. A receiver verifies NR-Webhook-Signature with the secret's UTF-8 bytes as the HMAC-SHA256 key."""

    key_id: str
    r"""The signing key id, sent as NR-Webhook-Key-Id on every delivery it signs."""
    secret: str
    r"""The signing secret: 32 random bytes as 43 characters of unpadded base64url. It is not stored in readable form or returned again."""
    created_at: str


class SigningSecret(BaseModel):
    r"""A newly issued signing key with its secret, shown only in this answer. A receiver verifies NR-Webhook-Signature with the secret's UTF-8 bytes as the HMAC-SHA256 key."""

    key_id: str
    r"""The signing key id, sent as NR-Webhook-Key-Id on every delivery it signs."""

    secret: str
    r"""The signing secret: 32 random bytes as 43 characters of unpadded base64url. It is not stored in readable form or returned again."""

    created_at: str
