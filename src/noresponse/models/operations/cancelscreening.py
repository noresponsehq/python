from __future__ import annotations
from noresponse.models.shared import (
    screening as shared_screening,
    screeningcancelrequest as shared_screeningcancelrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class CancelScreeningRequestTypedDict(TypedDict):
    group_id: str
    screening_id: str
    body: shared_screeningcancelrequest.ScreeningCancelRequestTypedDict


class CancelScreeningRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    screening_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_screeningcancelrequest.ScreeningCancelRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CancelScreeningResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_screening.ScreeningTypedDict


class CancelScreeningResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_screening.Screening
