from __future__ import annotations
from noresponse.models.shared import (
    keyusagebatch as shared_keyusagebatch,
    keyusagebatchrequest as shared_keyusagebatchrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RecordKeyUsageRequestTypedDict(TypedDict):
    idempotency_key: str
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""
    body: shared_keyusagebatchrequest.KeyUsageBatchRequestTypedDict


class RecordKeyUsageRequest(BaseModel):
    idempotency_key: Annotated[
        str,
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""

    body: Annotated[
        shared_keyusagebatchrequest.KeyUsageBatchRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class RecordKeyUsageResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_keyusagebatch.KeyUsageBatchTypedDict


class RecordKeyUsageResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_keyusagebatch.KeyUsageBatch
