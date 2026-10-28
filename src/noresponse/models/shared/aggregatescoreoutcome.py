from __future__ import annotations
from .flow import Flow
from .outcome import Outcome
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AggregateScoreOutcomeTypedDict(TypedDict):
    r"""First answers of one flow whose risk.score is in [score_min, score_max] and whose assessment's latest reported outcome (the latest received) is outcome. Counted when the first answer is counted and moved when a later outcome wins; outcomes reported before the first answer was counted are counted with it. An outcome reported before this count existed is counted only once another outcome is reported for the assessment."""

    flow: Flow
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""
    score_min: int
    r"""A multiple of 5."""
    score_max: int
    outcome: Outcome
    r"""What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this workspace for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins."""
    count: int


class AggregateScoreOutcome(BaseModel):
    r"""First answers of one flow whose risk.score is in [score_min, score_max] and whose assessment's latest reported outcome (the latest received) is outcome. Counted when the first answer is counted and moved when a later outcome wins; outcomes reported before the first answer was counted are counted with it. An outcome reported before this count existed is counted only once another outcome is reported for the assessment."""

    flow: Flow
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""

    score_min: int
    r"""A multiple of 5."""

    score_max: int

    outcome: Outcome
    r"""What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this workspace for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins."""

    count: int
