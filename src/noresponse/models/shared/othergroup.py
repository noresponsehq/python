from __future__ import annotations
from .highestband import HighestBand
from .matchstate import MatchState
from .persondecision import PersonDecision
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL, UnrecognizedStr
from pydantic import model_serializer
from typing import List, Literal, Optional, Union
from typing_extensions import NotRequired, TypedDict


MatchedOn = Union[
    Literal[
        "email",
        "phone",
        "external_id",
    ],
    UnrecognizedStr,
]


class OtherGroupTypedDict(TypedDict):
    r"""A person of another group in the same environment who shares an email or phone with this one, as that group recorded them."""

    group_id: str
    group_name: str
    group_starts_at: str
    person_id: str
    r"""The person on that group's list."""
    matched_on: List[MatchedOn]
    r"""Which identifiers match, in this order. external_id appears only beside email or phone: the same external id alone is not a match, since ticket numbers may be reused across groups."""
    match_state: MatchState
    r"""How sure the latest screening is that it found the person's accounts. unscreened until a screening reaches the person, and after one that had no profile to check (no_profile_to_check)."""
    highest_band: Nullable[HighestBand]
    r"""That person's most severe band in that group, or null."""
    decision: Nullable[PersonDecision]
    r"""The latest reviewer decision in that group, or null before any."""
    no_profile_to_check: NotRequired[bool]
    r"""true when that person's latest screening had no profile to check (see the person's no_profile_to_check). Left out otherwise."""
    decided_by: NotRequired[str]
    r"""Who made that decision."""
    decided_at: NotRequired[str]
    r"""When that decision was made."""


class OtherGroup(BaseModel):
    r"""A person of another group in the same environment who shares an email or phone with this one, as that group recorded them."""

    group_id: str

    group_name: str

    group_starts_at: str

    person_id: str
    r"""The person on that group's list."""

    matched_on: List[MatchedOn]
    r"""Which identifiers match, in this order. external_id appears only beside email or phone: the same external id alone is not a match, since ticket numbers may be reused across groups."""

    match_state: MatchState
    r"""How sure the latest screening is that it found the person's accounts. unscreened until a screening reaches the person, and after one that had no profile to check (no_profile_to_check)."""

    highest_band: Nullable[HighestBand]
    r"""That person's most severe band in that group, or null."""

    decision: Nullable[PersonDecision]
    r"""The latest reviewer decision in that group, or null before any."""

    no_profile_to_check: Optional[bool] = None
    r"""true when that person's latest screening had no profile to check (see the person's no_profile_to_check). Left out otherwise."""

    decided_by: Optional[str] = None
    r"""Who made that decision."""

    decided_at: Optional[str] = None
    r"""When that decision was made."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["no_profile_to_check", "decided_by", "decided_at"])
        nullable_fields = set(["highest_band", "decision"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))
            is_nullable_and_explicitly_set = (
                k in nullable_fields
                and (self.__pydantic_fields_set__.intersection({n}))  # pylint: disable=no-member
            )

            if val != UNSET_SENTINEL:
                if (
                    val is not None
                    or k not in optional_fields
                    or is_nullable_and_explicitly_set
                ):
                    m[k] = val

        return m
