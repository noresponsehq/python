from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class EndpointVerificationTypedDict(TypedDict):
    endpoint_id: str
    r"""Opaque id of the endpoint registration being verified."""
    challenge: str
    r"""Endpoint verification nonce: 32 random bytes, unpadded base64url (43 characters). Fresh per verification."""


class EndpointVerification(BaseModel):
    endpoint_id: str
    r"""Opaque id of the endpoint registration being verified."""

    challenge: str
    r"""Endpoint verification nonce: 32 random bytes, unpadded base64url (43 characters). Fresh per verification."""
