from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class DeleteGroupRequestTypedDict(TypedDict):
    group_id: str


class DeleteGroupRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class DeleteGroupResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]


class DeleteGroupResponse(BaseModel):
    headers: Dict[str, List[str]]
