from __future__ import annotations
from .errorcode import ErrorCode
from .searchkind import SearchKind
from .searchstatus import SearchStatus
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SearchTypedDict(TypedDict):
    r"""One search a person started on a value of one of a person's records. Nothing searches again by itself."""

    search_id: str
    record_id: str
    r"""The record whose value led to the search."""
    field: str
    r"""The field of that record that holds the value."""
    kind: SearchKind
    r"""The kind of the value searched."""
    value: str
    r"""The value searched: the field's cleaned value, else as the source wrote it."""
    status: SearchStatus
    r"""A password or hash search is counting, then counted: rows says how many breach rows hold the value, and nothing runs until a person runs it (POST .../searches/{search_id}/run). Any other search is queued, then running. completed: every source it asked answered. partial: some did not. failed: none answered or none could be asked, which says nothing about whether the value is held anywhere."""
    sources: int
    r"""How many sources the search asked: the breach search and the account and phone lookups that take the value's kind."""
    answered: int
    r"""How many of them gave a definite answer, found or not found."""
    found: int
    r"""How many records the search found. They are among the person report's lookup records, each match naming this search."""
    estimated_spend: int
    r"""What the search may spend, in US cents, held against the environment's daily screening cap while it runs."""
    spent: int
    r"""What the search spent, in US cents, metered as screening work."""
    requested_by: str
    r"""Who started the search."""
    created_at: str
    table: NotRequired[str]
    r"""The one breach table searched, when the search was of one table."""
    rows: NotRequired[int]
    r"""How many breach rows hold the password or hash, counted before the search runs."""
    error_code: NotRequired[ErrorCode]
    r"""Why a failed search found nothing: its sources did not answer, none could be asked, or it could not run before its attempts were spent."""
    finished_at: NotRequired[str]


class Search(BaseModel):
    r"""One search a person started on a value of one of a person's records. Nothing searches again by itself."""

    search_id: str

    record_id: str
    r"""The record whose value led to the search."""

    field: str
    r"""The field of that record that holds the value."""

    kind: SearchKind
    r"""The kind of the value searched."""

    value: str
    r"""The value searched: the field's cleaned value, else as the source wrote it."""

    status: SearchStatus
    r"""A password or hash search is counting, then counted: rows says how many breach rows hold the value, and nothing runs until a person runs it (POST .../searches/{search_id}/run). Any other search is queued, then running. completed: every source it asked answered. partial: some did not. failed: none answered or none could be asked, which says nothing about whether the value is held anywhere."""

    sources: int
    r"""How many sources the search asked: the breach search and the account and phone lookups that take the value's kind."""

    answered: int
    r"""How many of them gave a definite answer, found or not found."""

    found: int
    r"""How many records the search found. They are among the person report's lookup records, each match naming this search."""

    estimated_spend: int
    r"""What the search may spend, in US cents, held against the environment's daily screening cap while it runs."""

    spent: int
    r"""What the search spent, in US cents, metered as screening work."""

    requested_by: str
    r"""Who started the search."""

    created_at: str

    table: Optional[str] = None
    r"""The one breach table searched, when the search was of one table."""

    rows: Optional[int] = None
    r"""How many breach rows hold the password or hash, counted before the search runs."""

    error_code: Optional[ErrorCode] = None
    r"""Why a failed search found nothing: its sources did not answer, none could be asked, or it could not run before its attempts were spent."""

    finished_at: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["table", "rows", "error_code", "finished_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
