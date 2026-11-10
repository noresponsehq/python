from __future__ import annotations
from .attendeedecision import AttendeeDecision
from .highestband import HighestBand
from .matchstate import MatchState
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


class OtherEventTypedDict(TypedDict):
    r"""An attendee of another event in the same environment who shares an email or phone with this one, as that event recorded them."""

    event_id: str
    event_name: str
    event_starts_at: str
    attendee_id: str
    r"""The attendee on that event's list."""
    matched_on: List[MatchedOn]
    r"""Which identifiers match, in this order. external_id appears only beside email or phone: the same external id alone is not a match, since ticket numbers may be reused across events."""
    match_state: MatchState
    r"""How sure the latest screening is that it found the attendee's accounts. unscreened until a screening reaches the attendee."""
    highest_band: Nullable[HighestBand]
    r"""That attendee's most severe band at that event, or null."""
    decision: Nullable[AttendeeDecision]
    r"""The latest reviewer decision at that event, or null before any."""
    decided_by: NotRequired[str]
    r"""Who made that decision."""
    decided_at: NotRequired[str]
    r"""When that decision was made."""


class OtherEvent(BaseModel):
    r"""An attendee of another event in the same environment who shares an email or phone with this one, as that event recorded them."""

    event_id: str

    event_name: str

    event_starts_at: str

    attendee_id: str
    r"""The attendee on that event's list."""

    matched_on: List[MatchedOn]
    r"""Which identifiers match, in this order. external_id appears only beside email or phone: the same external id alone is not a match, since ticket numbers may be reused across events."""

    match_state: MatchState
    r"""How sure the latest screening is that it found the attendee's accounts. unscreened until a screening reaches the attendee."""

    highest_band: Nullable[HighestBand]
    r"""That attendee's most severe band at that event, or null."""

    decision: Nullable[AttendeeDecision]
    r"""The latest reviewer decision at that event, or null before any."""

    decided_by: Optional[str] = None
    r"""Who made that decision."""

    decided_at: Optional[str] = None
    r"""When that decision was made."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["decided_by", "decided_at"])
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
