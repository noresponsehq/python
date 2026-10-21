from __future__ import annotations
from noresponse.types import BaseModel, UnrecognizedStr
from typing import List, Literal, Union
from typing_extensions import TypedDict


Scope = Union[
    Literal[
        "assess",
        "history",
        "webhooks",
        "detailed",
    ],
    UnrecognizedStr,
]


class KeyRotationTypedDict(TypedDict):
    r"""The 201 answer of POST /v1/keys/rotate: the new key, shown once, and when the key that was presented stops working. The new key has the scopes of the presented key."""

    key: str
    r"""The new credential, nrk_<key id>_<secret>. It is shown only in this answer; store it now."""
    key_id: str
    r"""The public id of the new key."""
    scopes: List[Scope]
    r"""The scopes of the new key: those of the presented key."""
    created_at: str
    previous_key_id: str
    r"""The id of the key that signed this request."""
    previous_key_expires_at: str
    r"""When the previous key stops authenticating. Until then both keys work."""


class KeyRotation(BaseModel):
    r"""The 201 answer of POST /v1/keys/rotate: the new key, shown once, and when the key that was presented stops working. The new key has the scopes of the presented key."""

    key: str
    r"""The new credential, nrk_<key id>_<secret>. It is shown only in this answer; store it now."""

    key_id: str
    r"""The public id of the new key."""

    scopes: List[Scope]
    r"""The scopes of the new key: those of the presented key."""

    created_at: str

    previous_key_id: str
    r"""The id of the key that signed this request."""

    previous_key_expires_at: str
    r"""When the previous key stops authenticating. Until then both keys work."""
