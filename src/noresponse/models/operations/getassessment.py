from __future__ import annotations
from noresponse.models.shared import (
    assessment as shared_assessment,
    responsemode as shared_responsemode,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetAssessmentRequestTypedDict(TypedDict):
    assessment_id: str
    r"""Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400."""
    response_mode: NotRequired[shared_responsemode.ResponseMode]
    r"""Optional standard or separately authorised detailed customer view; raw is rejected."""


class GetAssessmentRequest(BaseModel):
    assessment_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400."""

    response_mode: Annotated[
        Optional[shared_responsemode.ResponseMode],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Optional standard or separately authorised detailed customer view; raw is rejected."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["response_mode"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class GetAssessmentResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_assessment.AssessmentTypedDict


class GetAssessmentResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_assessment.Assessment
