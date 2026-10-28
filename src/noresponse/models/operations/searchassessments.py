from __future__ import annotations
from noresponse.models.shared import assessmentsearchpage as shared_assessmentsearchpage
from noresponse.types import BaseModel
from typing import Dict, List
from typing_extensions import TypedDict


class SearchAssessmentsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_assessmentsearchpage.AssessmentSearchPageTypedDict


class SearchAssessmentsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_assessmentsearchpage.AssessmentSearchPage
