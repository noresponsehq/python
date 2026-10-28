from __future__ import annotations
from noresponse.models.shared import (
    accountdecisionsnapshot as shared_accountdecisionsnapshot,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class GetAccountDecisionRequestTypedDict(TypedDict):
    account_id: str
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""
    risk_version: int
    r"""The canonical decimal risk_version originally served."""


class GetAccountDecisionRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""

    risk_version: Annotated[
        int, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The canonical decimal risk_version originally served."""


class GetAccountDecisionResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_accountdecisionsnapshot.AccountDecisionSnapshotTypedDict


class GetAccountDecisionResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_accountdecisionsnapshot.AccountDecisionSnapshot
