from __future__ import annotations
from noresponse.models.shared import assessmentlist as shared_assessmentlist
from noresponse.types import BaseModel
from typing import Awaitable, Callable, Dict, List, Optional, Union
from typing_extensions import TypedDict


class QueryAccountAssessmentsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_assessmentlist.AssessmentListTypedDict


class QueryAccountAssessmentsResponse(BaseModel):
    next: Union[
        Callable[[], Optional[QueryAccountAssessmentsResponse]],
        Callable[[], Awaitable[Optional[QueryAccountAssessmentsResponse]]],
    ]

    headers: Dict[str, List[str]]

    result: shared_assessmentlist.AssessmentList
