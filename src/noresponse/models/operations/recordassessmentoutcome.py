from __future__ import annotations
from noresponse.models.shared import (
    assessmentoutcome as shared_assessmentoutcome,
    assessmentoutcomerequest as shared_assessmentoutcomerequest,
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


class RecordAssessmentOutcomeRequestTypedDict(TypedDict):
    assessment_id: str
    r"""Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400."""
    idempotency_key: str
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the tenant principal and bound to the canonical body for 24 hours."""
    body: shared_assessmentoutcomerequest.AssessmentOutcomeRequestTypedDict


class RecordAssessmentOutcomeRequest(BaseModel):
    assessment_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400."""

    idempotency_key: Annotated[
        str,
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the tenant principal and bound to the canonical body for 24 hours."""

    body: Annotated[
        shared_assessmentoutcomerequest.AssessmentOutcomeRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class RecordAssessmentOutcomeResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_assessmentoutcome.AssessmentOutcomeTypedDict


class RecordAssessmentOutcomeResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_assessmentoutcome.AssessmentOutcome
