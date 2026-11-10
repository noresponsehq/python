from __future__ import annotations
from .attendeedecision import AttendeeDecision
from .attendeerole import AttendeeRole
from .handle import Handle, HandleTypedDict
from .highestband import HighestBand
from .matchstate import MatchState
from .screeningcoverage import ScreeningCoverage, ScreeningCoverageTypedDict
from .screeningspend import ScreeningSpend, ScreeningSpendTypedDict
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AttendeeTypedDict(TypedDict):
    r"""An attendee and where their screening and review stand."""

    id: str
    event_id: str
    name: str
    r"""The attendee's full name."""
    match_state: MatchState
    r"""How sure the latest screening is that it found the attendee's accounts. unscreened until a screening reaches the attendee."""
    highest_band: Nullable[HighestBand]
    r"""The most severe finding's band, or null when nothing was flagged."""
    decision: Nullable[AttendeeDecision]
    r"""The latest reviewer decision, or null before any."""
    coverage: ScreeningCoverageTypedDict
    r"""The denominator of a screening: accounts found, how many could be read, items read and the period they span, so a clean result is distinct from a person nobody could see."""
    created_at: str
    updated_at: str
    spend: ScreeningSpendTypedDict
    r"""What screening cost, in US cents, in total and per implementation."""
    external_id: NotRequired[str]
    r"""Your own id for the attendee, unique within the event. A later row with the same external id updates this attendee."""
    email: NotRequired[str]
    r"""The attendee's email."""
    phone: NotRequired[str]
    r"""The attendee's phone in E.164 form."""
    company: NotRequired[str]
    r"""Where the attendee works."""
    city: NotRequired[str]
    r"""Where the attendee lives."""
    handles: NotRequired[List[HandleTypedDict]]
    r"""Accounts the attendee is known to hold, at most 20."""
    role: NotRequired[AttendeeRole]
    r"""The attendee's role at the event: guest (a ticket holder), crew, vendor or press. Leave it out when you do not know it: an attendee without one has no role, not guest. A later row naming the same attendee replaces it, and a change of role alone keeps the attendee's screening results."""
    decision_note: NotRequired[str]
    decided_by: NotRequired[str]
    decided_at: NotRequired[str]
    last_screening_id: NotRequired[str]
    screened_at: NotRequired[str]


class Attendee(BaseModel):
    r"""An attendee and where their screening and review stand."""

    id: str

    event_id: str

    name: str
    r"""The attendee's full name."""

    match_state: MatchState
    r"""How sure the latest screening is that it found the attendee's accounts. unscreened until a screening reaches the attendee."""

    highest_band: Nullable[HighestBand]
    r"""The most severe finding's band, or null when nothing was flagged."""

    decision: Nullable[AttendeeDecision]
    r"""The latest reviewer decision, or null before any."""

    coverage: ScreeningCoverage
    r"""The denominator of a screening: accounts found, how many could be read, items read and the period they span, so a clean result is distinct from a person nobody could see."""

    created_at: str

    updated_at: str

    spend: ScreeningSpend
    r"""What screening cost, in US cents, in total and per implementation."""

    external_id: Optional[str] = None
    r"""Your own id for the attendee, unique within the event. A later row with the same external id updates this attendee."""

    email: Optional[str] = None
    r"""The attendee's email."""

    phone: Optional[str] = None
    r"""The attendee's phone in E.164 form."""

    company: Optional[str] = None
    r"""Where the attendee works."""

    city: Optional[str] = None
    r"""Where the attendee lives."""

    handles: Optional[List[Handle]] = None
    r"""Accounts the attendee is known to hold, at most 20."""

    role: Optional[AttendeeRole] = None
    r"""The attendee's role at the event: guest (a ticket holder), crew, vendor or press. Leave it out when you do not know it: an attendee without one has no role, not guest. A later row naming the same attendee replaces it, and a change of role alone keeps the attendee's screening results."""

    decision_note: Optional[str] = None

    decided_by: Optional[str] = None

    decided_at: Optional[str] = None

    last_screening_id: Optional[str] = None

    screened_at: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "external_id",
                "email",
                "phone",
                "company",
                "city",
                "handles",
                "role",
                "decision_note",
                "decided_by",
                "decided_at",
                "last_screening_id",
                "screened_at",
            ]
        )
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
