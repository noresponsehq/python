from __future__ import annotations
from .coverage import Coverage, CoverageTypedDict
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class EnforcementsTypedDict(TypedDict):
    r"""Retained customer enforcement report rows created in [from,to), one row per account/risk_version/flow/action. A later applied report can replace failed at the original created_at; retries are not additional attempts here. applied_coverage divides reported_applied by report rows, including explicit action none; it is not independently verified execution, all requested actions, or prevented fraud. Unreported actions are unknown."""

    denominator: int
    accounts: int
    reported_applied: int
    reported_failed: int
    applied_coverage: CoverageTypedDict
    r"""Counts only; a zero denominator means no eligible retained records and does not imply a zero rate."""
    population: Literal["retained_enforcement_reports_by_created_at"]


class Enforcements(BaseModel):
    r"""Retained customer enforcement report rows created in [from,to), one row per account/risk_version/flow/action. A later applied report can replace failed at the original created_at; retries are not additional attempts here. applied_coverage divides reported_applied by report rows, including explicit action none; it is not independently verified execution, all requested actions, or prevented fraud. Unreported actions are unknown."""

    denominator: int

    accounts: int

    reported_applied: int

    reported_failed: int

    applied_coverage: Coverage
    r"""Counts only; a zero denominator means no eligible retained records and does not imply a zero rate."""

    population: Annotated[
        Annotated[
            Literal["retained_enforcement_reports_by_created_at"],
            AfterValidator(
                validate_const("retained_enforcement_reports_by_created_at")
            ),
        ],
        pydantic.Field(alias="population"),
    ] = "retained_enforcement_reports_by_created_at"


try:
    Enforcements.model_rebuild()
except NameError:
    pass
