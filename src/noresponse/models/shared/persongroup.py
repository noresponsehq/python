from __future__ import annotations
from .personrole import PersonRole
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import TypedDict


class PersonGroupTypedDict(TypedDict):
    r"""One group the person belongs to and their role in it."""

    group_id: str
    group_name: str
    group_starts_at: Nullable[str]
    r"""The group's optional event start; null for an ongoing group."""
    role: Nullable[PersonRole]
    r"""The person's role in the group: guest, crew, vendor or press, or null when it was not given."""
    added_at: str
    r"""When the person was added to the group."""


class PersonGroup(BaseModel):
    r"""One group the person belongs to and their role in it."""

    group_id: str

    group_name: str

    group_starts_at: Nullable[str]
    r"""The group's optional event start; null for an ongoing group."""

    role: Nullable[PersonRole]
    r"""The person's role in the group: guest, crew, vendor or press, or null when it was not given."""

    added_at: str
    r"""When the person was added to the group."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                m[k] = val

        return m
