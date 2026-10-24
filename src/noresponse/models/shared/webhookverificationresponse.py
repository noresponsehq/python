from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class WebhookVerificationResponseTypedDict(TypedDict):
    r"""The body an endpoint returns, with status 200 and Content-Type application/json within 5 seconds, to an endpoint.verification event. A 2xx without the echoed challenge does not verify the endpoint."""

    challenge: str
    r"""Endpoint verification nonce: 32 random bytes, unpadded base64url (43 characters). Fresh per verification."""


class WebhookVerificationResponse(BaseModel):
    r"""The body an endpoint returns, with status 200 and Content-Type application/json within 5 seconds, to an endpoint.verification event. A 2xx without the echoed challenge does not verify the endpoint."""

    challenge: str
    r"""Endpoint verification nonce: 32 random bytes, unpadded base64url (43 characters). Fresh per verification."""
