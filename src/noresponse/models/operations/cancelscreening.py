from __future__ import annotations
from noresponse.models.shared import (
    keyenvironment as shared_keyenvironment,
    screening as shared_screening,
    screeningcancelrequest as shared_screeningcancelrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class CancelScreeningRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_keyenvironment.KeyEnvironment
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""
    group_id: str
    screening_id: str
    body: shared_screeningcancelrequest.ScreeningCancelRequestTypedDict


class CancelScreeningRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_keyenvironment.KeyEnvironment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""

    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    screening_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    body: Annotated[
        shared_screeningcancelrequest.ScreeningCancelRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CancelScreeningResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_screening.ScreeningTypedDict


class CancelScreeningResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_screening.Screening
