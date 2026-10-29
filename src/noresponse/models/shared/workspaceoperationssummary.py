from __future__ import annotations
from .auditsettingsenvironment import AuditSettingsEnvironment
from .enforcements import Enforcements, EnforcementsTypedDict
from .outcomes import Outcomes, OutcomesTypedDict
from .reviews import Reviews, ReviewsTypedDict
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class WorkspaceOperationsSummaryTypedDict(TypedDict):
    r"""Three separately defined populations with independent denominators. Interpret each section within its own population; their totals do not form a conversion funnel. All counts and retention come from one snapshot. Requests above the population or query budget are refused without truncation."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""
    environment: AuditSettingsEnvironment
    from_: str
    to: str
    as_of: str
    retained_from: str
    retention_days: int
    records_read: int
    outcomes: OutcomesTypedDict
    r"""Accounts whose current completed assessment was created in the selected window and remains retained at as_of. The effective account feedback head is observed at as_of, including explicit unknown reports. Customer-reported labels and unlabelled accounts have separate counts. Superseded labels are excluded."""
    enforcements: EnforcementsTypedDict
    r"""Retained customer enforcement report rows created in [from,to), one row per account/risk_version/flow/action. A later applied report can replace failed at the original created_at; retries are not additional attempts here. applied_coverage divides reported_applied by report rows, including explicit action none; it is not independently verified execution, all requested actions, or prevented fraud. Unreported actions are unknown."""
    reviews: ReviewsTypedDict
    r"""Reviews created in [from,to) whose review and current account assessment remain retained. Status and assignment are current at as_of, not a transition history. label_coverage numerator is resolved reviews labeled benign or abuse; denominator is resolved reviews. Inconclusive is not a known outcome. Review conclusions do not change account feedback or enforcement."""
    row_budget: Literal[100000]
    truncated: Literal[False]


class WorkspaceOperationsSummary(BaseModel):
    r"""Three separately defined populations with independent denominators. Interpret each section within its own population; their totals do not form a conversion funnel. All counts and retention come from one snapshot. Requests above the population or query budget are refused without truncation."""

    workspace_id: str
    r"""The workspace id, which is also its live environment's workspace id; the test environment's is the same id with :test appended. A workspace created through the API is tnt_ and a 26-character ULID."""

    environment: AuditSettingsEnvironment

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str

    as_of: str

    retained_from: str

    retention_days: int

    records_read: int

    outcomes: Outcomes
    r"""Accounts whose current completed assessment was created in the selected window and remains retained at as_of. The effective account feedback head is observed at as_of, including explicit unknown reports. Customer-reported labels and unlabelled accounts have separate counts. Superseded labels are excluded."""

    enforcements: Enforcements
    r"""Retained customer enforcement report rows created in [from,to), one row per account/risk_version/flow/action. A later applied report can replace failed at the original created_at; retries are not additional attempts here. applied_coverage divides reported_applied by report rows, including explicit action none; it is not independently verified execution, all requested actions, or prevented fraud. Unreported actions are unknown."""

    reviews: Reviews
    r"""Reviews created in [from,to) whose review and current account assessment remain retained. Status and assignment are current at as_of, not a transition history. label_coverage numerator is resolved reviews labeled benign or abuse; denominator is resolved reviews. Inconclusive is not a known outcome. Review conclusions do not change account feedback or enforcement."""

    row_budget: Annotated[
        Annotated[Literal[100000], AfterValidator(validate_const(100000))],
        pydantic.Field(alias="row_budget"),
    ] = 100000

    truncated: Annotated[
        Annotated[Literal[False], AfterValidator(validate_const(False))],
        pydantic.Field(alias="truncated"),
    ] = False


try:
    WorkspaceOperationsSummary.model_rebuild()
except NameError:
    pass
