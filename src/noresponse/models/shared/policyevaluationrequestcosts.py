from __future__ import annotations
from .cost import Cost, CostTypedDict
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class PolicyEvaluationRequestCostsTypedDict(TypedDict):
    legitimate: CostTypedDict
    abuse: CostTypedDict


class PolicyEvaluationRequestCosts(BaseModel):
    legitimate: Cost

    abuse: Cost
