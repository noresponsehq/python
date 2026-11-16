from __future__ import annotations
from .profilecitationkind import ProfileCitationKind
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ProfileCitationTypedDict(TypedDict):
    kind: ProfileCitationKind
    r"""record: a record in lookup.records or profiles[].record. post: an item in posts. check: an item in lookup.checks."""
    id: str
    r"""The record or post id. For a check, c followed by its 1-based position in lookup.checks."""


class ProfileCitation(BaseModel):
    kind: ProfileCitationKind
    r"""record: a record in lookup.records or profiles[].record. post: an item in posts. check: an item in lookup.checks."""

    id: str
    r"""The record or post id. For a check, c followed by its 1-based position in lookup.checks."""
