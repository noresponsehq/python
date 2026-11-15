from __future__ import annotations
from noresponse.models.shared import (
    screening as shared_screening,
    screeningrequest as shared_screeningrequest,
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


class StartScreeningRequestTypedDict(TypedDict):
    group_id: str
    idempotency_key: str
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""
    body: shared_screeningrequest.ScreeningRequestTypedDict


class StartScreeningRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    idempotency_key: Annotated[
        str,
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""

    body: Annotated[
        shared_screeningrequest.ScreeningRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class StartScreeningResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_screening.ScreeningTypedDict


class StartScreeningResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_screening.Screening
