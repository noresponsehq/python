from __future__ import annotations
from .thresholds import Thresholds, ThresholdsTypedDict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class PolicyEvaluationPublishRequestTypedDict(TypedDict):
    expected_policy_version: int
    manifest_sha256: str
    input_sha256: str
    result_sha256: str
    candidate: ThresholdsTypedDict
    change_reason: str


class PolicyEvaluationPublishRequest(BaseModel):
    expected_policy_version: int

    manifest_sha256: str

    input_sha256: str

    result_sha256: str

    candidate: Thresholds

    change_reason: str
