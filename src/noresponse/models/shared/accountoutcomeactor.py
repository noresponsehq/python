from __future__ import annotations
from .accountoutcomeactortype import AccountOutcomeActorType
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AccountOutcomeActorTypedDict(TypedDict):
    type: AccountOutcomeActorType
    key_id: NotRequired[str]
    external_user_id: NotRequired[str]
    r"""The user's id at the identity provider the console signs people in with: 1 to 256 printable ASCII characters with no space, compared exactly."""
    console_credential_id: NotRequired[str]
    principal_id: NotRequired[str]
    r"""Opaque, server-assigned member id: mem_ and a 26-character ULID. It stays the same when a removed member is invited back."""


class AccountOutcomeActor(BaseModel):
    type: AccountOutcomeActorType

    key_id: Optional[str] = None

    external_user_id: Optional[str] = None
    r"""The user's id at the identity provider the console signs people in with: 1 to 256 printable ASCII characters with no space, compared exactly."""

    console_credential_id: Optional[str] = None

    principal_id: Optional[str] = None
    r"""Opaque, server-assigned member id: mem_ and a 26-character ULID. It stays the same when a removed member is invited back."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["key_id", "external_user_id", "console_credential_id", "principal_id"]
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
