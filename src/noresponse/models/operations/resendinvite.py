from __future__ import annotations
from noresponse.models.shared import (
    invite as shared_invite,
    inviteresendrequest as shared_inviteresendrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class ResendInviteRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    invite_id: str
    r"""The invite's inv_ id. An invite of another workspace, or one no longer pending, answers 404."""
    body: shared_inviteresendrequest.InviteResendRequestTypedDict


class ResendInviteRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    invite_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The invite's inv_ id. An invite of another workspace, or one no longer pending, answers 404."""

    body: Annotated[
        shared_inviteresendrequest.InviteResendRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class ResendInviteResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_invite.InviteTypedDict


class ResendInviteResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_invite.Invite
