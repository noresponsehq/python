from __future__ import annotations
from .attendeeflaggedmatchstate import AttendeeFlaggedMatchState
from .highestband import HighestBand
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AttendeeFlaggedTypedDict(TypedDict):
    r"""A screening recorded a finding on an attendee. It says which attendee and how severe, not what they posted, who they are or why: GET the attendee report for the findings. Sent once per screening that flags the attendee, so a re-screen of someone on watch announces them again."""

    event_id: str
    r"""The attendee's event."""
    attendee_id: str
    r"""The flagged attendee."""
    screening_id: str
    r"""The screening that flagged them."""
    highest_band: HighestBand
    match_state: AttendeeFlaggedMatchState
    r"""How sure the screening is that the accounts it read are the attendee's. A finding on a possible match is at most moderate, on a probable match at most high."""
    flagged_at: str
    r"""When the screening recorded the finding; equal to the event's created_at."""


class AttendeeFlagged(BaseModel):
    r"""A screening recorded a finding on an attendee. It says which attendee and how severe, not what they posted, who they are or why: GET the attendee report for the findings. Sent once per screening that flags the attendee, so a re-screen of someone on watch announces them again."""

    event_id: str
    r"""The attendee's event."""

    attendee_id: str
    r"""The flagged attendee."""

    screening_id: str
    r"""The screening that flagged them."""

    highest_band: HighestBand

    match_state: AttendeeFlaggedMatchState
    r"""How sure the screening is that the accounts it read are the attendee's. A finding on a possible match is at most moderate, on a probable match at most high."""

    flagged_at: str
    r"""When the screening recorded the finding; equal to the event's created_at."""
