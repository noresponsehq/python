from __future__ import annotations
from noresponse.models.shared import (
    member as shared_member,
    memberupdaterequest as shared_memberupdaterequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class UpdateMemberRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    member_id: str
    r"""The member's mem_ id. A member of another workspace, or a removed one, answers 404."""
    body: shared_memberupdaterequest.MemberUpdateRequestTypedDict


class UpdateMemberRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    member_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The member's mem_ id. A member of another workspace, or a removed one, answers 404."""

    body: Annotated[
        shared_memberupdaterequest.MemberUpdateRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class UpdateMemberResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_member.MemberTypedDict


class UpdateMemberResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_member.Member
