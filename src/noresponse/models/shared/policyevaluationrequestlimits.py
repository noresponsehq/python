from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class PolicyEvaluationRequestLimitsTypedDict(TypedDict):
    review_rate: float
    server_error_rate: float
    unavailable_result_rate: float
    p95_ms: float


class PolicyEvaluationRequestLimits(BaseModel):
    review_rate: float

    server_error_rate: float

    unavailable_result_rate: float

    p95_ms: float
