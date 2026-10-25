from __future__ import annotations
from .keyenvironment import KeyEnvironment
from .keystatus import KeyStatus
from noresponse.types import BaseModel, UNSET_SENTINEL, UnrecognizedStr
from pydantic import model_serializer
from typing import List, Literal, Optional, Union
from typing_extensions import NotRequired, TypedDict


KeyScope = Union[
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


class KeyTypedDict(TypedDict):
    r"""One API key of your workspace. A key belongs to exactly one environment. key, the secret credential, is present only in the answer that created the key: NoResponse keeps a peppered digest of it, so store it now. Every other field is safe to show."""

    id: str
    r"""The key's public id, a 26-character ULID."""
    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""
    environment: KeyEnvironment
    r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""
    prefix: str
    r"""The public start of the credential, nrk_<environment>_<key id>, which identifies the key in logs and secret stores without its secret."""
    scopes: List[KeyScope]
    r"""The key's scopes, each at most once."""
    status: KeyStatus
    r"""active: the key authenticates. expired: a rotation's overlap window has ended (expires_at). revoked: the key was revoked (revoked_at) and answers 401."""
    created_at: str
    created_by: NotRequired[str]
    r"""The external user id of the member who created the key through the console, or the prefix (nrk_<environment>_<key id>) of the management key that created it. Absent for a key NoResponse issued or a rotation made."""
    expires_at: NotRequired[str]
    r"""When a rotated key stops authenticating (POST /v1/keys/rotate). Absent for a key with no end."""
    revoked_at: NotRequired[str]
    revoked_by: NotRequired[str]
    r"""The external user id of the member who revoked the key through the console, or the prefix of the management key that revoked it. Absent when the key is not revoked or NoResponse revoked it."""
    key: NotRequired[str]
    r"""The credential, nrk_<environment>_<key id>_<secret>. Present only in the 201 answer that created the key."""


class Key(BaseModel):
    r"""One API key of your workspace. A key belongs to exactly one environment. key, the secret credential, is present only in the answer that created the key: NoResponse keeps a peppered digest of it, so store it now. Every other field is safe to show."""

    id: str
    r"""The key's public id, a 26-character ULID."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""

    environment: KeyEnvironment
    r"""The environment the key belongs to. A live key assesses with live sources; a test key answers from the deterministic simulator."""

    prefix: str
    r"""The public start of the credential, nrk_<environment>_<key id>, which identifies the key in logs and secret stores without its secret."""

    scopes: List[KeyScope]
    r"""The key's scopes, each at most once."""

    status: KeyStatus
    r"""active: the key authenticates. expired: a rotation's overlap window has ended (expires_at). revoked: the key was revoked (revoked_at) and answers 401."""

    created_at: str

    created_by: Optional[str] = None
    r"""The external user id of the member who created the key through the console, or the prefix (nrk_<environment>_<key id>) of the management key that created it. Absent for a key NoResponse issued or a rotation made."""

    expires_at: Optional[str] = None
    r"""When a rotated key stops authenticating (POST /v1/keys/rotate). Absent for a key with no end."""

    revoked_at: Optional[str] = None

    revoked_by: Optional[str] = None
    r"""The external user id of the member who revoked the key through the console, or the prefix of the management key that revoked it. Absent when the key is not revoked or NoResponse revoked it."""

    key: Optional[str] = None
    r"""The credential, nrk_<environment>_<key id>_<secret>. Present only in the 201 answer that created the key."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["created_by", "expires_at", "revoked_at", "revoked_by", "key"]
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
