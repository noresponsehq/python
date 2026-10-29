from __future__ import annotations
from noresponse.models.shared import (
    workspaceoperationssummary as shared_workspaceoperationssummary,
    workspaceoperationssummaryrequest as shared_workspaceoperationssummaryrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class SummarizeWorkspaceOperationsRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    body: shared_workspaceoperationssummaryrequest.WorkspaceOperationsSummaryRequestTypedDict


class SummarizeWorkspaceOperationsRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    body: Annotated[
        shared_workspaceoperationssummaryrequest.WorkspaceOperationsSummaryRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class SummarizeWorkspaceOperationsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_workspaceoperationssummary.WorkspaceOperationsSummaryTypedDict


class SummarizeWorkspaceOperationsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_workspaceoperationssummary.WorkspaceOperationsSummary
