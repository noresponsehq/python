from __future__ import annotations
from .recordsource import RecordSource, RecordSourceTypedDict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class RecordRemainingTypedDict(TypedDict):
    r"""Rows one search matched in one source that the lookup's records leave out, so no answer is cut short in silence."""

    source: RecordSourceTypedDict
    r"""Where a record came from."""
    by: str
    r"""The kind of searched value whose search matched the rows, as a record's matched names it."""
    rows: int
    r"""How many rows of the source that search matched beyond the records the lookup carries."""


class RecordRemaining(BaseModel):
    r"""Rows one search matched in one source that the lookup's records leave out, so no answer is cut short in silence."""

    source: RecordSource
    r"""Where a record came from."""

    by: str
    r"""The kind of searched value whose search matched the rows, as a record's matched names it."""

    rows: int
    r"""How many rows of the source that search matched beyond the records the lookup carries."""
