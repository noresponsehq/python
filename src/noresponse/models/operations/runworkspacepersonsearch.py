from __future__ import annotations
from noresponse.models.shared import (
    screeningcancelrequest as shared_screeningcancelrequest,
    search as shared_search,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RunWorkspacePersonSearchRequestTypedDict(TypedDict):
    person_id: str
    search_id: str
    body: shared_screeningcancelrequest.ScreeningCancelRequestTypedDict


class RunWorkspacePersonSearchRequest(BaseModel):
    person_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    search_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_screeningcancelrequest.ScreeningCancelRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class RunWorkspacePersonSearchResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_search.SearchTypedDict


class RunWorkspacePersonSearchResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_search.Search
