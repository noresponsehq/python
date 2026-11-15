from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class DeleteWorkspacePersonRequestTypedDict(TypedDict):
    person_id: str


class DeleteWorkspacePersonRequest(BaseModel):
    person_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class DeleteWorkspacePersonResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]


class DeleteWorkspacePersonResponse(BaseModel):
    headers: Dict[str, List[str]]
