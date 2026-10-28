from __future__ import annotations
from .flow import Flow
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class AggregateScoreCountTypedDict(TypedDict):
    r"""First answers of one flow whose risk.score is in [score_min, score_max]: 0-4, 5-9 up to 95-100. A pending answer has no score."""

    flow: Flow
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""
    score_min: int
    r"""A multiple of 5."""
    score_max: int
    count: int


class AggregateScoreCount(BaseModel):
    r"""First answers of one flow whose risk.score is in [score_min, score_max]: 0-4, 5-9 up to 95-100. A pending answer has no score."""

    flow: Flow
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""

    score_min: int
    r"""A multiple of 5."""

    score_max: int

    count: int
