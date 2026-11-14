from __future__ import annotations
from noresponse.models.shared import (
    group as shared_group,
    grouprequest as shared_grouprequest,
    keyenvironment as shared_keyenvironment,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class CreateGroupRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_keyenvironment.KeyEnvironment
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""
    body: shared_grouprequest.GroupRequestTypedDict


class CreateGroupRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_keyenvironment.KeyEnvironment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""

    body: Annotated[
        shared_grouprequest.GroupRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CreateGroupResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_group.GroupTypedDict


class CreateGroupResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_group.Group
