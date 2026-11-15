from __future__ import annotations
from noresponse.models.shared import screening as shared_screening
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetScreeningRequestTypedDict(TypedDict):
    group_id: str
    screening_id: str


class GetScreeningRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    screening_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetScreeningResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_screening.ScreeningTypedDict


class GetScreeningResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_screening.Screening
