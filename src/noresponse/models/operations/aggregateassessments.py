from __future__ import annotations
from noresponse.models.shared import assessmentaggregate as shared_assessmentaggregate
from noresponse.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class AggregateAssessmentsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_assessmentaggregate.AssessmentAggregateTypedDict


class AggregateAssessmentsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_assessmentaggregate.AssessmentAggregate
