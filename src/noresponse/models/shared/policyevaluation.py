from __future__ import annotations
from .auditsettingsenvironment import AuditSettingsEnvironment
from .policyevaluationstatus import PolicyEvaluationStatus
from .resultstatus import ResultStatus
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PolicyEvaluationTypedDict(TypedDict):
    id: str
    environment: AuditSettingsEnvironment
    status: PolicyEvaluationStatus
    policy_version: int
    scoring_policy: str
    created_at: str
    expires_at: str
    accounts: int
    requests: int
    evaluator_sha256: str
    captured_at: NotRequired[str]
    finished_at: NotRequired[str]
    evaluator_version: Literal["identity-threshold-evaluator-v2"]
    build_version: NotRequired[str]
    result_status: NotRequired[ResultStatus]
    error_code: NotRequired[str]
    published_policy_version: NotRequired[int]
    manifest_sha256: NotRequired[str]
    input_sha256: NotRequired[str]
    cohort_sha256: NotRequired[str]
    result_sha256: NotRequired[str]


class PolicyEvaluation(BaseModel):
    id: str

    environment: AuditSettingsEnvironment

    status: PolicyEvaluationStatus

    policy_version: int

    scoring_policy: str

    created_at: str

    expires_at: str

    accounts: int

    requests: int

    evaluator_sha256: str

    captured_at: Optional[str] = None

    finished_at: Optional[str] = None

    evaluator_version: Annotated[
        Annotated[
            Literal["identity-threshold-evaluator-v2"],
            AfterValidator(validate_const("identity-threshold-evaluator-v2")),
        ],
        pydantic.Field(alias="evaluator_version"),
    ] = "identity-threshold-evaluator-v2"

    build_version: Optional[str] = None

    result_status: Optional[ResultStatus] = None

    error_code: Optional[str] = None

    published_policy_version: Optional[int] = None

    manifest_sha256: Optional[str] = None

    input_sha256: Optional[str] = None

    cohort_sha256: Optional[str] = None

    result_sha256: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "captured_at",
                "finished_at",
                "build_version",
                "result_status",
                "error_code",
                "published_policy_version",
                "manifest_sha256",
                "input_sha256",
                "cohort_sha256",
                "result_sha256",
            ]
        )
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
    PolicyEvaluation.model_rebuild()
except NameError:
    pass
