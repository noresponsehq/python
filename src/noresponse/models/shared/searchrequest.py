from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SearchRequestTypedDict(TypedDict):
    r"""The value to search again, named by the record and field that hold it rather than sent again."""

    record_id: str
    r"""One of the person's records: a lookup's, a profile's or one an earlier search found."""
    field: str
    r"""The name of the record's field whose value to search. Its kind must be email, phone, username, person_name, password, hash, ip or domain, and it must have a value: a field the source masked or that could not be cleaned is not searched."""
    table: NotRequired[str]
    r"""Search only this breach table, as a remaining entry names it, to fetch the rows an earlier search left out. Not for a phone."""


class SearchRequest(BaseModel):
    r"""The value to search again, named by the record and field that hold it rather than sent again."""

    record_id: str
    r"""One of the person's records: a lookup's, a profile's or one an earlier search found."""

    field: str
    r"""The name of the record's field whose value to search. Its kind must be email, phone, username, person_name, password, hash, ip or domain, and it must have a value: a field the source masked or that could not be cleaned is not searched."""

    table: Optional[str] = None
    r"""Search only this breach table, as a remaining entry names it, to fetch the rows an earlier search left out. Not for a phone."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["table"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
