from __future__ import annotations
from noresponse.models.shared import (
    auditsettings as shared_auditsettings,
    auditsettingsrequest as shared_auditsettingsrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List, Literal
from typing_extensions import Annotated, TypedDict


Environment = Literal["test",]


class UpdateAuditRetentionRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: Environment
    body: shared_auditsettingsrequest.AuditSettingsRequestTypedDict


class UpdateAuditRetentionRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        Environment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    body: Annotated[
        shared_auditsettingsrequest.AuditSettingsRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class UpdateAuditRetentionResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_auditsettings.AuditSettingsTypedDict


class UpdateAuditRetentionResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_auditsettings.AuditSettings
