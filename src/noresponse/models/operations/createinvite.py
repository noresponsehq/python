from __future__ import annotations
from noresponse.models.shared import (
    invite as shared_invite,
    inviterequest as shared_inviterequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class CreateInviteRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    body: shared_inviterequest.InviteRequestTypedDict


class CreateInviteRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    body: Annotated[
        shared_inviterequest.InviteRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CreateInviteResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_invite.InviteTypedDict


class CreateInviteResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_invite.Invite
