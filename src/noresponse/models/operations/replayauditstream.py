from __future__ import annotations
from noresponse.models.shared import (
    auditstreamlist as shared_auditstreamlist,
    auditstreamreplayrequest as shared_auditstreamreplayrequest,
    environment as shared_environment,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class ReplayAuditStreamRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_environment.Environment
    endpoint_id: str
    body: shared_auditstreamreplayrequest.AuditStreamReplayRequestTypedDict


class ReplayAuditStreamRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_environment.Environment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]

    endpoint_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_auditstreamreplayrequest.AuditStreamReplayRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class ReplayAuditStreamResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_auditstreamlist.AuditStreamListTypedDict


class ReplayAuditStreamResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_auditstreamlist.AuditStreamList
