from __future__ import annotations
from noresponse.types import BaseModel, UnrecognizedStr
from typing import List, Literal, Union
from typing_extensions import TypedDict


KeyRotationScope = Union[
    Literal[
        "assess",
        "history",
        "delete",
        "webhooks",
        "detailed",
        "integrations",
        "management",
    ],
    UnrecognizedStr,
]


class KeyRotationTypedDict(TypedDict):
    r"""The 201 answer of POST /v1/keys/rotate: the new key, shown once, and when the key that was presented stops working. The new key has the scopes and the environment of the presented key."""

    key: str
    r"""The new credential, nrk_<mode>_<key id>_<secret>, in the environment of the presented key: nrk_live_ or nrk_test_. It is shown only in this answer; store it now."""
    key_id: str
    r"""The public id of the new key."""
    scopes: List[KeyRotationScope]
    r"""The scopes of the new key: those of the presented key."""
    created_at: str
    previous_key_id: str
    r"""The id of the key that signed this request."""
    previous_key_expires_at: str
    r"""When the previous key stops authenticating. Until then both keys work."""


class KeyRotation(BaseModel):
    r"""The 201 answer of POST /v1/keys/rotate: the new key, shown once, and when the key that was presented stops working. The new key has the scopes and the environment of the presented key."""

    key: str
    r"""The new credential, nrk_<mode>_<key id>_<secret>, in the environment of the presented key: nrk_live_ or nrk_test_. It is shown only in this answer; store it now."""

    key_id: str
    r"""The public id of the new key."""

    scopes: List[KeyRotationScope]
    r"""The scopes of the new key: those of the presented key."""

    created_at: str

    previous_key_id: str
    r"""The id of the key that signed this request."""

    previous_key_expires_at: str
    r"""When the previous key stops authenticating. Until then both keys work."""
