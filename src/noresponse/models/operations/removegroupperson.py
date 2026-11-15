from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RemoveGroupPersonRequestTypedDict(TypedDict):
    group_id: str
    person_id: str


class RemoveGroupPersonRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    person_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class RemoveGroupPersonResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]


class RemoveGroupPersonResponse(BaseModel):
    headers: Dict[str, List[str]]
