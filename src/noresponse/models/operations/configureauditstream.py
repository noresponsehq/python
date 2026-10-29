from __future__ import annotations
from noresponse.models.shared import (
    auditstreamlist as shared_auditstreamlist,
    auditstreamrequest as shared_auditstreamrequest,
    environment as shared_environment,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class ConfigureAuditStreamRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_environment.Environment
    body: shared_auditstreamrequest.AuditStreamRequestTypedDict


class ConfigureAuditStreamRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_environment.Environment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    body: Annotated[
        shared_auditstreamrequest.AuditStreamRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class ConfigureAuditStreamResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_auditstreamlist.AuditStreamListTypedDict


class ConfigureAuditStreamResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_auditstreamlist.AuditStreamList
