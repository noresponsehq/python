from __future__ import annotations
from noresponse.models.shared import assessmentdeletion as shared_assessmentdeletion
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class DeleteAssessmentRequestTypedDict(TypedDict):
    assessment_id: str
    r"""Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400."""


class DeleteAssessmentRequest(BaseModel):
    assessment_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400."""


class DeleteAssessmentResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_assessmentdeletion.AssessmentDeletionTypedDict


class DeleteAssessmentResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_assessmentdeletion.AssessmentDeletion
