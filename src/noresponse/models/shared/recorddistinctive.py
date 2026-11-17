from __future__ import annotations
from .rating import Rating
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RecordDistinctiveTypedDict(TypedDict):
    r"""How distinctive a searchable value is: an email, phone, username, password, hash, person name or IP. Absent for other values, for a field with no value, and when its rating could not be worked out, such as when a count failed. Linkage weighs a password, hash or username by these numbers: the rarer the value, the more a shared one counts."""

    rating: Rating
    r"""unique: an email or phone, which belongs to one person by design. distinctive: rare enough that a new search on it likely finds one person. common: shared by many people, so a search on it finds strangers. A new search is suggested for unique and distinctive values only; any value can still be searched."""
    reason: str
    r"""Why, in plain words, such as \"seen 3,861,493 times in breach data\", \"in 4 breach rows\" or \"38 bits, about one in 430 billion usernames\"."""
    rows: NotRequired[int]
    r"""How many breach rows hold the value, when they were counted. Set for a username, password, hash or person name."""
    pwned: NotRequired[int]
    r"""How many times the Pwned Passwords list holds the password, when it was asked. Set for a password only."""
    bits: NotRequired[float]
    r"""How surprising the username is, to one decimal place: a character model spells it about once in 2^bits usernames. Set for a username the model can spell."""


class RecordDistinctive(BaseModel):
    r"""How distinctive a searchable value is: an email, phone, username, password, hash, person name or IP. Absent for other values, for a field with no value, and when its rating could not be worked out, such as when a count failed. Linkage weighs a password, hash or username by these numbers: the rarer the value, the more a shared one counts."""

    rating: Rating
    r"""unique: an email or phone, which belongs to one person by design. distinctive: rare enough that a new search on it likely finds one person. common: shared by many people, so a search on it finds strangers. A new search is suggested for unique and distinctive values only; any value can still be searched."""

    reason: str
    r"""Why, in plain words, such as \"seen 3,861,493 times in breach data\", \"in 4 breach rows\" or \"38 bits, about one in 430 billion usernames\"."""

    rows: Optional[int] = None
    r"""How many breach rows hold the value, when they were counted. Set for a username, password, hash or person name."""

    pwned: Optional[int] = None
    r"""How many times the Pwned Passwords list holds the password, when it was asked. Set for a password only."""

    bits: Optional[float] = None
    r"""How surprising the username is, to one decimal place: a character model spells it about once in 2^bits usernames. Set for a username the model can spell."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["rows", "pwned", "bits"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
