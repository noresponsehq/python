from __future__ import annotations
from .profilematchstate import ProfileMatchState
from .screeningmatchevidence import (
    ScreeningMatchEvidence,
    ScreeningMatchEvidenceTypedDict,
)
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ScreeningMatchTypedDict(TypedDict):
    r"""How a profile was matched to the attendee: the state its evidence earns, and the evidence."""

    state: ProfileMatchState
    r"""How sure the screening is that a profile is the attendee's, from its evidence: confirmed is two or more hard identifiers (email, phone, a supplied handle, or a fact an existing source returned), probable is one identifier beyond the name, possible is the name alone."""
    evidence: List[ScreeningMatchEvidenceTypedDict]


class ScreeningMatch(BaseModel):
    r"""How a profile was matched to the attendee: the state its evidence earns, and the evidence."""

    state: ProfileMatchState
    r"""How sure the screening is that a profile is the attendee's, from its evidence: confirmed is two or more hard identifiers (email, phone, a supplied handle, or a fact an existing source returned), probable is one identifier beyond the name, possible is the name alone."""

    evidence: List[ScreeningMatchEvidence]
