from __future__ import annotations
from noresponse.models.shared import (
    investigation as shared_investigation,
    personreviewrequest as shared_personreviewrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class ReviewInvestigationRequestTypedDict(TypedDict):
    investigation_id: str
    body: shared_personreviewrequest.PersonReviewRequestTypedDict


class ReviewInvestigationRequest(BaseModel):
    investigation_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_personreviewrequest.PersonReviewRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class ReviewInvestigationResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_investigation.InvestigationTypedDict


class ReviewInvestigationResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_investigation.Investigation
