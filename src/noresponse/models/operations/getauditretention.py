from __future__ import annotations
from noresponse.models.shared import (
    auditsettings as shared_auditsettings,
    auditsettingsenvironment as shared_auditsettingsenvironment,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetAuditRetentionRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_auditsettingsenvironment.AuditSettingsEnvironment


class GetAuditRetentionRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_auditsettingsenvironment.AuditSettingsEnvironment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]


class GetAuditRetentionResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_auditsettings.AuditSettingsTypedDict


class GetAuditRetentionResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_auditsettings.AuditSettings
