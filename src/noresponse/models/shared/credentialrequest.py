from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class CredentialRequestTypedDict(TypedDict):
    r"""Associate the SHA-256 of a high-entropy key issued by your service. Send the hash instead of the key. Repeating a hash returns its original association, including its retirement state. A hash associated with another account returns a conflict."""

    sha256: str


class CredentialRequest(BaseModel):
    r"""Associate the SHA-256 of a high-entropy key issued by your service. Send the hash instead of the key. Repeating a hash returns its original association, including its retirement state. A hash associated with another account returns a conflict."""

    sha256: str
