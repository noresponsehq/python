from __future__ import annotations
from noresponse.models.shared import (
    attendeebatch as shared_attendeebatch,
    attendeebatchrequest as shared_attendeebatchrequest,
    keyenvironment as shared_keyenvironment,
)
from noresponse.types import BaseModel
from noresponse.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class AddAttendeesRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_keyenvironment.KeyEnvironment
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""
    event_id: str
    idempotency_key: str
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""
    body: shared_attendeebatchrequest.AttendeeBatchRequestTypedDict


class AddAttendeesRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_keyenvironment.KeyEnvironment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""

    event_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    idempotency_key: Annotated[
        str,
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""

    body: Annotated[
        shared_attendeebatchrequest.AttendeeBatchRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class AddAttendeesResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_attendeebatch.AttendeeBatchTypedDict


class AddAttendeesResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_attendeebatch.AttendeeBatch
