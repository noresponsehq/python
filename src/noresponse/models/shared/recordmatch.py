from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RecordMatchTypedDict(TypedDict):
    r"""One searched value that found the record."""

    by: str
    r"""The kind of searched value: email, phone, username, name, or handle for a profile read of a handle."""
    field: NotRequired[str]
    r"""The field the searched value hit, when the record holds it."""


class RecordMatch(BaseModel):
    r"""One searched value that found the record."""

    by: str
    r"""The kind of searched value: email, phone, username, name, or handle for a profile read of a handle."""

    field: Optional[str] = None
    r"""The field the searched value hit, when the record holds it."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["field"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
