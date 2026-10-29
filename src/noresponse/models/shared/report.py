from __future__ import annotations
from .resultstatus import ResultStatus
from .thresholds import Thresholds, ThresholdsTypedDict
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class ReportScopeTypedDict(TypedDict):
    pass


class ReportScope(BaseModel):
    pass


class ReportTypedDict(TypedDict):
    input_sha256: str
    cohort_sha256: str
    status: ResultStatus
    candidate: ThresholdsTypedDict
    scope: ReportScopeTypedDict
    evaluator_version: Literal["identity-threshold-evaluator-v2"]


class Report(BaseModel):
    input_sha256: str

    cohort_sha256: str

    status: ResultStatus

    candidate: Thresholds

    scope: ReportScope

    evaluator_version: Annotated[
        Annotated[
            Literal["identity-threshold-evaluator-v2"],
            AfterValidator(validate_const("identity-threshold-evaluator-v2")),
        ],
        pydantic.Field(alias="evaluator_version"),
    ] = "identity-threshold-evaluator-v2"


try:
    Report.model_rebuild()
except NameError:
    pass
