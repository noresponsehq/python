from __future__ import annotations
from noresponse.models.shared import (
    enforcement as shared_enforcement,
    enforcementrequest as shared_enforcementrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RecordEnforcementRequestTypedDict(TypedDict):
    account_id: str
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""
    body: shared_enforcementrequest.EnforcementRequestTypedDict


class RecordEnforcementRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""

    body: Annotated[
        shared_enforcementrequest.EnforcementRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class RecordEnforcementResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_enforcement.EnforcementTypedDict


class RecordEnforcementResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_enforcement.Enforcement
