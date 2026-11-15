from __future__ import annotations
from noresponse.models.shared import (
    investigation as shared_investigation,
    investigationrequest as shared_investigationrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class CreateInvestigationRequestTypedDict(TypedDict):
    idempotency_key: str
    r"""Opaque request key, 16 to 128 characters. Repeating the key and request returns the same resource in its current state while it is retained. A different request with the same key answers 409. Use a new key for a deliberate new operation. Keys are scoped to the environment and operation; person searches also scope them to the group and person."""
    body: shared_investigationrequest.InvestigationRequestTypedDict


class CreateInvestigationRequest(BaseModel):
    idempotency_key: Annotated[
        str,
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""Opaque request key, 16 to 128 characters. Repeating the key and request returns the same resource in its current state while it is retained. A different request with the same key answers 409. Use a new key for a deliberate new operation. Keys are scoped to the environment and operation; person searches also scope them to the group and person."""

    body: Annotated[
        shared_investigationrequest.InvestigationRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CreateInvestigationResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_investigation.InvestigationTypedDict


class CreateInvestigationResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_investigation.Investigation
