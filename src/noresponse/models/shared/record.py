from __future__ import annotations
from .recordfield import RecordField, RecordFieldTypedDict
from .recordmatch import RecordMatch, RecordMatchTypedDict
from .recordsource import RecordSource, RecordSourceTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class RecordTypedDict(TypedDict):
    r"""One answer from one source: where it came from, what found it and every field it holds."""

    id: str
    r"""Made from the source and the fields' names and original values, so the same answer found twice is one record with the same id."""
    source: RecordSourceTypedDict
    r"""Where a record came from."""
    matched: List[RecordMatchTypedDict]
    r"""Each kind of searched value that found the record."""
    fields: List[RecordFieldTypedDict]
    r"""Every field the source returned, in the order the source's connector lists them."""
    observed_at: str
    r"""When the source last gave this answer."""


class Record(BaseModel):
    r"""One answer from one source: where it came from, what found it and every field it holds."""

    id: str
    r"""Made from the source and the fields' names and original values, so the same answer found twice is one record with the same id."""

    source: RecordSource
    r"""Where a record came from."""

    matched: List[RecordMatch]
    r"""Each kind of searched value that found the record."""

    fields: List[RecordField]
    r"""Every field the source returned, in the order the source's connector lists them."""

    observed_at: str
    r"""When the source last gave this answer."""
