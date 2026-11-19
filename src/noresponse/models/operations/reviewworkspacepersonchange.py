from __future__ import annotations
from noresponse.models.shared import (
    personchange as shared_personchange,
    screeningcancelrequest as shared_screeningcancelrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class ReviewWorkspacePersonChangeRequestTypedDict(TypedDict):
    person_id: str
    change_id: str
    body: shared_screeningcancelrequest.ScreeningCancelRequestTypedDict


class ReviewWorkspacePersonChangeRequest(BaseModel):
    person_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    change_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_screeningcancelrequest.ScreeningCancelRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class ReviewWorkspacePersonChangeResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_personchange.PersonChangeTypedDict


class ReviewWorkspacePersonChangeResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_personchange.PersonChange
