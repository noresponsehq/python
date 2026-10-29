from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RemoveMemberRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    member_id: str
    r"""The member's mem_ id. A member of another workspace, or a removed one, answers 404."""


class RemoveMemberRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    member_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The member's mem_ id. A member of another workspace, or a removed one, answers 404."""


class RemoveMemberResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]


class RemoveMemberResponse(BaseModel):
    headers: Dict[str, List[str]]
