from __future__ import annotations
from .accountdecision import AccountDecision
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AccountDecisionsByFlowTypedDict(TypedDict):
    r"""The decision for each flow: the account's score under that flow's thresholds. A flow the workspace has not set uses its account_creation thresholds, so the flows differ only where it set them."""

    account_creation: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""
    login: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""
    purchase: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""


class AccountDecisionsByFlow(BaseModel):
    r"""The decision for each flow: the account's score under that flow's thresholds. A flow the workspace has not set uses its account_creation thresholds, so the flows differ only where it set them."""

    account_creation: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""

    login: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""

    purchase: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. Your application applies it."""
