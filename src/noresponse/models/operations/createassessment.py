from __future__ import annotations
from noresponse.models.shared import (
    assessment as shared_assessment,
    assessmentrequest as shared_assessmentrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class CreateAssessmentRequestTypedDict(TypedDict):
    idempotency_key: str
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""
    body: shared_assessmentrequest.AssessmentRequestTypedDict


class CreateAssessmentRequest(BaseModel):
    idempotency_key: Annotated[
        str,
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""

    body: Annotated[
        shared_assessmentrequest.AssessmentRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CreateAssessmentResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_assessment.AssessmentTypedDict


class CreateAssessmentResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_assessment.Assessment
