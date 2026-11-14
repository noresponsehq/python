from __future__ import annotations
from .recordsource import RecordSource, RecordSourceTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RecordRemainingTypedDict(TypedDict):
    r"""Rows one search matched in one source that the lookup's records leave out, so no answer is cut short in silence."""

    source: RecordSourceTypedDict
    r"""Where a record came from."""
    by: str
    r"""The kind of searched value whose search matched the rows, as a record's matched names it."""
    rows: int
    r"""How many rows of the source that search matched beyond the records the lookup carries."""
    search: NotRequired[str]
    r"""The search a person started that matched the rows. Searching the same field again with this source's table fetches them."""


class RecordRemaining(BaseModel):
    r"""Rows one search matched in one source that the lookup's records leave out, so no answer is cut short in silence."""

    source: RecordSource
    r"""Where a record came from."""

    by: str
    r"""The kind of searched value whose search matched the rows, as a record's matched names it."""

    rows: int
    r"""How many rows of the source that search matched beyond the records the lookup carries."""

    search: Optional[str] = None
    r"""The search a person started that matched the rows. Searching the same field again with this source's table fetches them."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["search"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
