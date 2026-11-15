from __future__ import annotations
from noresponse.models.shared import personreport as shared_personreport
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetPersonRequestTypedDict(TypedDict):
    group_id: str
    person_id: str


class GetPersonRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    person_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetPersonResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_personreport.PersonReportTypedDict


class GetPersonResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_personreport.PersonReport
