from __future__ import annotations
from noresponse.models.shared import accountdeletion as shared_accountdeletion
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class DeleteAccountRequestTypedDict(TypedDict):
    account_id: str
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""


class DeleteAccountRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""


class DeleteAccountResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_accountdeletion.AccountDeletionTypedDict


class DeleteAccountResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_accountdeletion.AccountDeletion
