from __future__ import annotations
from .rating import Rating
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class RecordDistinctiveTypedDict(TypedDict):
    r"""How distinctive a searchable value is: an email, phone, username, password, hash, person name or IP. Absent for other values, for a field with no value, and when its rating could not be worked out, such as when a count failed."""

    rating: Rating
    r"""unique: an email or phone, which belongs to one person by design. distinctive: rare enough that a new search on it likely finds one person. common: shared by many people, so a search on it finds strangers. A new search is suggested for unique and distinctive values only; any value can still be searched."""
    reason: str
    r"""Why, in plain words, such as \"seen 3,861,493 times in breach data\", \"in 4 breach rows\" or \"38 bits, about one in 430 billion usernames\"."""


class RecordDistinctive(BaseModel):
    r"""How distinctive a searchable value is: an email, phone, username, password, hash, person name or IP. Absent for other values, for a field with no value, and when its rating could not be worked out, such as when a count failed."""

    rating: Rating
    r"""unique: an email or phone, which belongs to one person by design. distinctive: rare enough that a new search on it likely finds one person. common: shared by many people, so a search on it finds strangers. A new search is suggested for unique and distinctive values only; any value can still be searched."""

    reason: str
    r"""Why, in plain words, such as \"seen 3,861,493 times in breach data\", \"in 4 breach rows\" or \"38 bits, about one in 430 billion usernames\"."""
