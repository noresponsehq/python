from __future__ import annotations
from .accountdecision import AccountDecision
from .accountriskreason import AccountRiskReason, AccountRiskReasonTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class AccountRiskTypedDict(TypedDict):
    score: int
    r"""0 (safe) to 100 (risky), as risk.score of the assessment."""
    decision: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""
    reasons: List[AccountRiskReasonTypedDict]
    r"""Every reason that fired, highest weight first. The weights sum to score before clamping."""


class AccountRisk(BaseModel):
    score: int
    r"""0 (safe) to 100 (risky), as risk.score of the assessment."""

    decision: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""

    reasons: List[AccountRiskReason]
    r"""Every reason that fired, highest weight first. The weights sum to score before clamping."""
