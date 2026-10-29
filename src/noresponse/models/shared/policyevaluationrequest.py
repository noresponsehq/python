from __future__ import annotations
from .policyevaluationrequestcosts import (
    PolicyEvaluationRequestCosts,
    PolicyEvaluationRequestCostsTypedDict,
)
from .policyevaluationrequestlimits import (
    PolicyEvaluationRequestLimits,
    PolicyEvaluationRequestLimitsTypedDict,
)
from .thresholds import Thresholds, ThresholdsTypedDict
from noresponse.types import BaseModel
import pydantic
from typing import List
from typing_extensions import Annotated, TypedDict


class PolicyEvaluationRequestTypedDict(TypedDict):
    expected_policy_version: int
    from_: str
    to: str
    candidates: List[ThresholdsTypedDict]
    costs: PolicyEvaluationRequestCostsTypedDict
    limits: PolicyEvaluationRequestLimitsTypedDict
    label_collection: str
    split_seed: str


class PolicyEvaluationRequest(BaseModel):
    expected_policy_version: int

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str

    candidates: List[Thresholds]

    costs: PolicyEvaluationRequestCosts

    limits: PolicyEvaluationRequestLimits

    label_collection: str

    split_seed: str


try:
    PolicyEvaluationRequest.model_rebuild()
except NameError:
    pass
