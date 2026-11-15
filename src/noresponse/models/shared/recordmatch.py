from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RecordMatchTypedDict(TypedDict):
    r"""One searched value that found the record."""

    by: str
    r"""The kind of searched value: email, phone, username, ip, name, password, hash, domain, or handle for a profile read of a handle."""
    field: NotRequired[str]
    r"""The field the searched value hit, when the record holds it."""
    search: NotRequired[str]
    r"""The search a person started on a value of another record that found this one, among the person report's searches, which names the value and the record and field it came from. A record found only by such searches is a lead, whatever kind of value found it. Absent for a match of the lookups."""


class RecordMatch(BaseModel):
    r"""One searched value that found the record."""

    by: str
    r"""The kind of searched value: email, phone, username, ip, name, password, hash, domain, or handle for a profile read of a handle."""

    field: Optional[str] = None
    r"""The field the searched value hit, when the record holds it."""

    search: Optional[str] = None
    r"""The search a person started on a value of another record that found this one, among the person report's searches, which names the value and the record and field it came from. A record found only by such searches is a lead, whatever kind of value found it. Absent for a match of the lookups."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["field", "search"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
