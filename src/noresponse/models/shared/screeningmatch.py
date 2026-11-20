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
    r"""How a profile was matched to the person: the state its evidence earns, and the evidence."""

    state: ProfileMatchState
    r"""How sure the screening is that a profile is the person's, from the likelihood its record scores. Confirmed reaches the join bar of 0.9. Probable reaches 0.85, which takes a shared value beyond the one that found the account. Possible is the rest."""
    evidence: List[ScreeningMatchEvidenceTypedDict]


class ScreeningMatch(BaseModel):
    r"""How a profile was matched to the person: the state its evidence earns, and the evidence."""

    state: ProfileMatchState
    r"""How sure the screening is that a profile is the person's, from the likelihood its record scores. Confirmed reaches the join bar of 0.9. Probable reaches 0.85, which takes a shared value beyond the one that found the account. Possible is the rest."""

    evidence: List[ScreeningMatchEvidence]
