from __future__ import annotations
from noresponse.models.shared import (
    group as shared_group,
    groupupdate as shared_groupupdate,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class UpdateGroupRequestTypedDict(TypedDict):
    group_id: str
    body: shared_groupupdate.GroupUpdateTypedDict


class UpdateGroupRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_groupupdate.GroupUpdate,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class UpdateGroupResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_group.GroupTypedDict


class UpdateGroupResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_group.Group
