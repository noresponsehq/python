from __future__ import annotations
from .population import Population
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class AssessmentAggregateCoverageTypedDict(TypedDict):
    r"""Captured in the same database snapshot as the counts. Capture start times describe when counting began, not the earliest creation time counted: an older assessment may first answer later. Older outcomes are not inferred to be absent. Erased detail cannot be returned by drill-down even while its anonymous count remains."""

    as_of: str
    first_answers_started_at: str
    score_outcomes_started_at: str
    retained_from: str
    population: Population
    r"""first_answers uses anonymous counters that can include erased detail. retained_first_answers computes exact intersections over retained first answers within 31 days. Requests exceeding the 100000-record work budget are refused."""
    erased_records_included: bool
    overlapping_groups: bool
    late_flip_unit: Literal["decision_transitions"]
    historical_backfill: Literal[False]


class AssessmentAggregateCoverage(BaseModel):
    r"""Captured in the same database snapshot as the counts. Capture start times describe when counting began, not the earliest creation time counted: an older assessment may first answer later. Older outcomes are not inferred to be absent. Erased detail cannot be returned by drill-down even while its anonymous count remains."""

    as_of: str

    first_answers_started_at: str

    score_outcomes_started_at: str

    retained_from: str

    population: Population
    r"""first_answers uses anonymous counters that can include erased detail. retained_first_answers computes exact intersections over retained first answers within 31 days. Requests exceeding the 100000-record work budget are refused."""

    erased_records_included: bool

    overlapping_groups: bool

    late_flip_unit: Annotated[
        Annotated[
            Literal["decision_transitions"],
            AfterValidator(validate_const("decision_transitions")),
        ],
        pydantic.Field(alias="late_flip_unit"),
    ] = "decision_transitions"

    historical_backfill: Annotated[
        Annotated[Literal[False], AfterValidator(validate_const(False))],
        pydantic.Field(alias="historical_backfill"),
    ] = False


try:
    AssessmentAggregateCoverage.model_rebuild()
except NameError:
    pass
