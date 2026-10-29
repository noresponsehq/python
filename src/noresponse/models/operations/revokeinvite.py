from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RevokeInviteRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    invite_id: str
    r"""The invite's inv_ id. An invite of another workspace, or one no longer pending, answers 404."""


class RevokeInviteRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    invite_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The invite's inv_ id. An invite of another workspace, or one no longer pending, answers 404."""


class RevokeInviteResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]


class RevokeInviteResponse(BaseModel):
    headers: Dict[str, List[str]]
