from __future__ import annotations
from noresponse.models.shared import invitelist as shared_invitelist
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class ListInvitesRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""


class ListInvitesRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""


class ListInvitesResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_invitelist.InviteListTypedDict


class ListInvitesResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_invitelist.InviteList
