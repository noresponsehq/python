from __future__ import annotations
from noresponse.models.shared import (
    accountoutcome as shared_accountoutcome,
    accountoutcomerequest as shared_accountoutcomerequest,
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


class RecordAccountOutcomeRequestTypedDict(TypedDict):
    account_id: str
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""
    idempotency_key: str
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""
    body: shared_accountoutcomerequest.AccountOutcomeRequestTypedDict


class RecordAccountOutcomeRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""

    idempotency_key: Annotated[
        str,
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""

    body: Annotated[
        shared_accountoutcomerequest.AccountOutcomeRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class RecordAccountOutcomeResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_accountoutcome.AccountOutcomeTypedDict


class RecordAccountOutcomeResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_accountoutcome.AccountOutcome
