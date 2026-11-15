from __future__ import annotations
from noresponse.models.shared import group as shared_group
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetGroupRequestTypedDict(TypedDict):
    group_id: str


class GetGroupRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetGroupResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_group.GroupTypedDict


class GetGroupResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_group.Group
