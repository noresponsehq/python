from __future__ import annotations
from noresponse.models.shared import (
    keyenvironment as shared_keyenvironment,
    reviewsubjectchange as shared_reviewsubjectchange,
    reviewsubjectrequest as shared_reviewsubjectrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class AddReviewSubjectRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_keyenvironment.KeyEnvironment
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""
    review_id: str
    body: shared_reviewsubjectrequest.ReviewSubjectRequestTypedDict


class AddReviewSubjectRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_keyenvironment.KeyEnvironment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""

    review_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_reviewsubjectrequest.ReviewSubjectRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class AddReviewSubjectResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_reviewsubjectchange.ReviewSubjectChangeTypedDict


class AddReviewSubjectResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_reviewsubjectchange.ReviewSubjectChange
