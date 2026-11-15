from __future__ import annotations
from noresponse.models.shared import (
    workspacepersonreport as shared_workspacepersonreport,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetWorkspacePersonRequestTypedDict(TypedDict):
    person_id: str


class GetWorkspacePersonRequest(BaseModel):
    person_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class GetWorkspacePersonResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_workspacepersonreport.WorkspacePersonReportTypedDict


class GetWorkspacePersonResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_workspacepersonreport.WorkspacePersonReport
