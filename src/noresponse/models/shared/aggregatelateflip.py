from __future__ import annotations
from .accountdecision import AccountDecision
from .delay import Delay
from noresponse.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class AggregateLateFlipTypedDict(TypedDict):
    r"""Changes of the account decision for an assessment's flow after its first answer, as account.risk_changed announces them, counted in the bucket of the assessment's creation. from is the decision announced before (allow before the first announcement); an assessment that changes twice counts twice."""

    from_: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. held only for a flow whose admission is held (settings flows.<flow>.admission), when the account's current assessment was made for that flow and its investigation has not completed (status partial): the final decision arrives as account.risk_changed when the investigation completes, decided by its score, or when the hold's deadline (hold_seconds after the assessment was created) passes first, as the flow's on_expiry action or the decision the evidence so far gives, whichever is stricter. Your application applies it."""
    to: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. held only for a flow whose admission is held (settings flows.<flow>.admission), when the account's current assessment was made for that flow and its investigation has not completed (status partial): the final decision arrives as account.risk_changed when the investigation completes, decided by its score, or when the hold's deadline (hold_seconds after the assessment was created) passes first, as the flow's on_expiry action or the decision the evidence so far gives, whichever is stricter. Your application applies it."""
    delay: Delay
    r"""How long after the assessment's creation the change was made."""
    count: int


class AggregateLateFlip(BaseModel):
    r"""Changes of the account decision for an assessment's flow after its first answer, as account.risk_changed announces them, counted in the bucket of the assessment's creation. from is the decision announced before (allow before the first announcement); an assessment that changes twice counts twice."""

    from_: Annotated[AccountDecision, pydantic.Field(alias="from")]
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. held only for a flow whose admission is held (settings flows.<flow>.admission), when the account's current assessment was made for that flow and its investigation has not completed (status partial): the final decision arrives as account.risk_changed when the investigation completes, decided by its score, or when the hold's deadline (hold_seconds after the assessment was created) passes first, as the flow's on_expiry action or the decision the evidence so far gives, whichever is stricter. Your application applies it."""

    to: AccountDecision
    r"""block when the score reached your block threshold (risk.block of the assessment), otherwise the assessment's recommendation. held only for a flow whose admission is held (settings flows.<flow>.admission), when the account's current assessment was made for that flow and its investigation has not completed (status partial): the final decision arrives as account.risk_changed when the investigation completes, decided by its score, or when the hold's deadline (hold_seconds after the assessment was created) passes first, as the flow's on_expiry action or the decision the evidence so far gives, whichever is stricter. Your application applies it."""

    delay: Delay
    r"""How long after the assessment's creation the change was made."""

    count: int


try:
    AggregateLateFlip.model_rebuild()
except NameError:
    pass
