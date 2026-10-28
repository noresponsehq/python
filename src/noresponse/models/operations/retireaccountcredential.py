from __future__ import annotations
from noresponse.models.shared import (
    credentialassociation as shared_credentialassociation,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class RetireAccountCredentialRequestTypedDict(TypedDict):
    account_id: str
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""
    credential_id: str


class RetireAccountCredentialRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""

    credential_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


class RetireAccountCredentialResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_credentialassociation.CredentialAssociationTypedDict


class RetireAccountCredentialResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_credentialassociation.CredentialAssociation
