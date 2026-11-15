from __future__ import annotations
from noresponse.models.shared import (
    investigation as shared_investigation,
    screeningcancelrequest as shared_screeningcancelrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class CancelInvestigationRequestTypedDict(TypedDict):
    investigation_id: str
    body: shared_screeningcancelrequest.ScreeningCancelRequestTypedDict


class CancelInvestigationRequest(BaseModel):
    investigation_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_screeningcancelrequest.ScreeningCancelRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CancelInvestigationResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_investigation.InvestigationTypedDict


class CancelInvestigationResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_investigation.Investigation
