from __future__ import annotations
from .accountdecision import AccountDecision
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AccountDecisionsByFlowTypedDict(TypedDict):
    r"""The decision for each flow. Every flow uses the tenant's signup thresholds today, so all three equal risk.decision."""

    signup: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""
    login: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""
    purchase: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""


class AccountDecisionsByFlow(BaseModel):
    r"""The decision for each flow. Every flow uses the tenant's signup thresholds today, so all three equal risk.decision."""

    signup: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""

    login: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""

    purchase: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""
