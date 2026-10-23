from __future__ import annotations
from .band import Band
from .recommendation import Recommendation
from .riskconfidence import RiskConfidence
from .riskcoverage import RiskCoverage, RiskCoverageTypedDict
from .riskdetails import RiskDetails, RiskDetailsTypedDict
from .riskreason import RiskReason, RiskReasonTypedDict
from .risksummary import RiskSummary, RiskSummaryTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RiskTypedDict(TypedDict):
    r"""The one risk decision for this event. score is 0 (safe) to 100 (risky): the sum of the weights of the reasons that fired, clamped to 0 to 100, from hand-set versioned weights. Every answer with a recommendation carries it, and the top-level recommendation equals risk.recommendation. It names no source or provider."""

    score: int
    band: Band
    r"""low 0-29, medium 30-59, high 60-84, critical 85-100."""
    recommendation: Recommendation
    r"""The recommended action: allow, step_up or review. Your application applies it."""
    confidence: RiskConfidence
    r"""How much of the planned evidence answered; it says nothing about risk."""
    policy_version: str
    r"""Version of the hand-authored heuristic weights that produced the recommendation, for example 'risk-2026-10.7'. A workspace threshold override adds a +t<N> suffix, e.g. 'risk-2026-10.7+t3'."""
    reasons: List[RiskReasonTypedDict]
    r"""Every reason that fired, highest weight first. The weights sum to score before clamping."""
    coverage: RiskCoverageTypedDict
    r"""Sources counted by state, not named."""
    block: NotRequired[bool]
    r"""true when the workspace's block threshold is set and score reached it. A provider hook can deny the account creation on it; the provider decides and enforces. It does not change recommendation. It is false while blocking is off, the default, and a body from before the flag existed omits it: read absent as false."""
    block_threshold: NotRequired[int]
    r"""The block threshold this answer used: block is true exactly when score is at least this value. Absent while blocking is off. NoResponse sets it per workspace on request, at or above the review threshold."""
    policy_basis: Literal["heuristic_unvalidated"]
    r"""Labels the v0 policy as hand-authored and not statistically validated."""
    summary: NotRequired[RiskSummaryTypedDict]
    r"""A few typed facts per identifier. Every fact is optional: absent means the evidence did not answer and makes no claim, while false or 0 is a definite answer. Lanes that do not exist yet leave their members absent."""
    details: NotRequired[RiskDetailsTypedDict]
    r"""Detailed view only (response_mode=detailed, which needs the detailed scope); a standard answer leaves it out. Merged observations without provider, source, origin, raw breach record, value or score."""


class Risk(BaseModel):
    r"""The one risk decision for this event. score is 0 (safe) to 100 (risky): the sum of the weights of the reasons that fired, clamped to 0 to 100, from hand-set versioned weights. Every answer with a recommendation carries it, and the top-level recommendation equals risk.recommendation. It names no source or provider."""

    score: int

    band: Band
    r"""low 0-29, medium 30-59, high 60-84, critical 85-100."""

    recommendation: Recommendation
    r"""The recommended action: allow, step_up or review. Your application applies it."""

    confidence: RiskConfidence
    r"""How much of the planned evidence answered; it says nothing about risk."""

    policy_version: str
    r"""Version of the hand-authored heuristic weights that produced the recommendation, for example 'risk-2026-10.7'. A workspace threshold override adds a +t<N> suffix, e.g. 'risk-2026-10.7+t3'."""

    reasons: List[RiskReason]
    r"""Every reason that fired, highest weight first. The weights sum to score before clamping."""

    coverage: RiskCoverage
    r"""Sources counted by state, not named."""

    block: Optional[bool] = None
    r"""true when the workspace's block threshold is set and score reached it. A provider hook can deny the account creation on it; the provider decides and enforces. It does not change recommendation. It is false while blocking is off, the default, and a body from before the flag existed omits it: read absent as false."""

    block_threshold: Optional[int] = None
    r"""The block threshold this answer used: block is true exactly when score is at least this value. Absent while blocking is off. NoResponse sets it per workspace on request, at or above the review threshold."""

    policy_basis: Annotated[
        Annotated[
            Literal["heuristic_unvalidated"],
            AfterValidator(validate_const("heuristic_unvalidated")),
        ],
        pydantic.Field(alias="policy_basis"),
    ] = "heuristic_unvalidated"
    r"""Labels the v0 policy as hand-authored and not statistically validated."""

    summary: Optional[RiskSummary] = None
    r"""A few typed facts per identifier. Every fact is optional: absent means the evidence did not answer and makes no claim, while false or 0 is a definite answer. Lanes that do not exist yet leave their members absent."""

    details: Optional[RiskDetails] = None
    r"""Detailed view only (response_mode=detailed, which needs the detailed scope); a standard answer leaves it out. Merged observations without provider, source, origin, raw breach record, value or score."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["block", "block_threshold", "summary", "details"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


try:
    Risk.model_rebuild()
except NameError:
    pass
