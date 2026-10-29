from __future__ import annotations
from .coverage import Coverage, CoverageTypedDict
from .reviewsconclusions import ReviewsConclusions, ReviewsConclusionsTypedDict
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class ReviewsTypedDict(TypedDict):
    r"""Reviews created in [from,to) whose review and current account assessment remain retained. Status and assignment are current at as_of, not a transition history. label_coverage numerator is resolved reviews labeled benign or abuse; denominator is resolved reviews. Inconclusive is not a known outcome. Review conclusions do not change account feedback or enforcement."""

    denominator: int
    open: int
    in_progress: int
    resolved: int
    assigned: int
    unassigned: int
    label_coverage: CoverageTypedDict
    r"""Counts only; a zero denominator means no eligible retained records and does not imply a zero rate."""
    conclusions: ReviewsConclusionsTypedDict
    r"""Current resolution of each resolved retained review; prior resolutions and reopened reviews do not count. Missing keys mean zero. These investigation conclusions are independent of account feedback."""
    population: Literal["retained_reviews_by_created_at"]


class Reviews(BaseModel):
    r"""Reviews created in [from,to) whose review and current account assessment remain retained. Status and assignment are current at as_of, not a transition history. label_coverage numerator is resolved reviews labeled benign or abuse; denominator is resolved reviews. Inconclusive is not a known outcome. Review conclusions do not change account feedback or enforcement."""

    denominator: int

    open: int

    in_progress: int

    resolved: int

    assigned: int

    unassigned: int

    label_coverage: Coverage
    r"""Counts only; a zero denominator means no eligible retained records and does not imply a zero rate."""

    conclusions: ReviewsConclusions
    r"""Current resolution of each resolved retained review; prior resolutions and reopened reviews do not count. Missing keys mean zero. These investigation conclusions are independent of account feedback."""

    population: Annotated[
        Annotated[
            Literal["retained_reviews_by_created_at"],
            AfterValidator(validate_const("retained_reviews_by_created_at")),
        ],
        pydantic.Field(alias="population"),
    ] = "retained_reviews_by_created_at"


try:
    Reviews.model_rebuild()
except NameError:
    pass
