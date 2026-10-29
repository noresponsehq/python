from __future__ import annotations
from .policypreviewcoverage import PolicyPreviewCoverage, PolicyPreviewCoverageTypedDict
from .policypreviewtransition import (
    PolicyPreviewTransition,
    PolicyPreviewTransitionTypedDict,
)
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal
from typing_extensions import Annotated, TypedDict


class PolicyPreviewTypedDict(TypedDict):
    r"""Exact threshold transitions among eligible retained first answers, newest first within the limit. Partial older revisions without a frozen hold snapshot are reported as unsupported. Preview leaves account state, outcomes and source evidence unchanged."""

    policy_version: int
    from_: str
    to: str
    retention_from: str
    coverage: PolicyPreviewCoverageTypedDict
    changed: int
    unchanged: int
    transitions: List[PolicyPreviewTransitionTypedDict]
    scope: Literal["retained_first_answer_thresholds"]


class PolicyPreview(BaseModel):
    r"""Exact threshold transitions among eligible retained first answers, newest first within the limit. Partial older revisions without a frozen hold snapshot are reported as unsupported. Preview leaves account state, outcomes and source evidence unchanged."""

    policy_version: int

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str

    retention_from: str

    coverage: PolicyPreviewCoverage

    changed: int

    unchanged: int

    transitions: List[PolicyPreviewTransition]

    scope: Annotated[
        Annotated[
            Literal["retained_first_answer_thresholds"],
            AfterValidator(validate_const("retained_first_answer_thresholds")),
        ],
        pydantic.Field(alias="scope"),
    ] = "retained_first_answer_thresholds"


try:
    PolicyPreview.model_rebuild()
except NameError:
    pass
