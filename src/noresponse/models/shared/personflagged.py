from __future__ import annotations
from .highestband import HighestBand
from .personflaggedmatchstate import PersonFlaggedMatchState
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class PersonFlaggedTypedDict(TypedDict):
    r"""A screening recorded a finding on a person. It says which person and how severe, not what they posted, who they are or why: GET the person report for the findings. Sent once per screening that flags the person, so a re-screen of someone on watch announces them again."""

    group_id: str
    r"""The person's group."""
    person_id: str
    r"""The flagged person."""
    screening_id: str
    r"""The screening that flagged them."""
    highest_band: HighestBand
    match_state: PersonFlaggedMatchState
    r"""How sure the screening is that the accounts it read are the person's. A finding on a possible match is at most moderate, on a probable match at most high."""
    flagged_at: str
    r"""When the screening recorded the finding; equal to the event's created_at."""


class PersonFlagged(BaseModel):
    r"""A screening recorded a finding on a person. It says which person and how severe, not what they posted, who they are or why: GET the person report for the findings. Sent once per screening that flags the person, so a re-screen of someone on watch announces them again."""

    group_id: str
    r"""The person's group."""

    person_id: str
    r"""The flagged person."""

    screening_id: str
    r"""The screening that flagged them."""

    highest_band: HighestBand

    match_state: PersonFlaggedMatchState
    r"""How sure the screening is that the accounts it read are the person's. A finding on a possible match is at most moderate, on a probable match at most high."""

    flagged_at: str
    r"""When the screening recorded the finding; equal to the event's created_at."""
