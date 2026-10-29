from __future__ import annotations
from .coverage import Coverage, CoverageTypedDict
from .outcomesbyoutcome import OutcomesByOutcome, OutcomesByOutcomeTypedDict
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class OutcomesTypedDict(TypedDict):
    r"""Accounts whose current completed assessment was created in the selected window and remains retained at as_of. The effective account feedback head is observed at as_of, including explicit unknown reports. Customer-reported labels and unlabelled accounts have separate counts. Superseded labels are excluded."""

    denominator: int
    reported: int
    unreported: int
    label_coverage: CoverageTypedDict
    r"""Counts only; a zero denominator means no eligible retained records and does not imply a zero rate."""
    by_outcome: OutcomesByOutcomeTypedDict
    r"""Current customer-reported labels, not independently established ground truth. Missing keys mean zero. Unknown is an explicit report; absent or expired feedback is unreported."""
    population: Literal["retained_current_accounts_by_current_assessment_created_at"]


class Outcomes(BaseModel):
    r"""Accounts whose current completed assessment was created in the selected window and remains retained at as_of. The effective account feedback head is observed at as_of, including explicit unknown reports. Customer-reported labels and unlabelled accounts have separate counts. Superseded labels are excluded."""

    denominator: int

    reported: int

    unreported: int

    label_coverage: Coverage
    r"""Counts only; a zero denominator means no eligible retained records and does not imply a zero rate."""

    by_outcome: OutcomesByOutcome
    r"""Current customer-reported labels, not independently established ground truth. Missing keys mean zero. Unknown is an explicit report; absent or expired feedback is unreported."""

    population: Annotated[
        Annotated[
            Literal["retained_current_accounts_by_current_assessment_created_at"],
            AfterValidator(
                validate_const(
                    "retained_current_accounts_by_current_assessment_created_at"
                )
            ),
        ],
        pydantic.Field(alias="population"),
    ] = "retained_current_accounts_by_current_assessment_created_at"


try:
    Outcomes.model_rebuild()
except NameError:
    pass
