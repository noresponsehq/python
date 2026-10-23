from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AssessmentRequestIssuedCredentialTypedDict(TypedDict):
    r"""Optional. When your platform issues an API key to the new account, send SHA-256 of that key, so later usage of the key, or a leaked copy, ties back to this assessment. Each SDK has a helper that computes it. Send only the hash: customer keys are high-entropy, so the hash reveals nothing about them. The assessment stores it, and no response, webhook or log carries it."""

    sha256: str
    r"""SHA-256 of the issued key's UTF-8 bytes, as 64 lower-case hex characters."""


class AssessmentRequestIssuedCredential(BaseModel):
    r"""Optional. When your platform issues an API key to the new account, send SHA-256 of that key, so later usage of the key, or a leaked copy, ties back to this assessment. Each SDK has a helper that computes it. Send only the hash: customer keys are high-entropy, so the hash reveals nothing about them. The assessment stores it, and no response, webhook or log carries it."""

    sha256: str
    r"""SHA-256 of the issued key's UTF-8 bytes, as 64 lower-case hex characters."""
