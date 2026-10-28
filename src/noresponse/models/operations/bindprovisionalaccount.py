from __future__ import annotations
from noresponse.models.shared import (
    accountbinding as shared_accountbinding,
    accountbindingrequest as shared_accountbindingrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class BindProvisionalAccountRequestTypedDict(TypedDict):
    assessment_id: str
    r"""Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400."""
    body: shared_accountbindingrequest.AccountBindingRequestTypedDict


class BindProvisionalAccountRequest(BaseModel):
    assessment_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Path segment, matched case-sensitively. A value that does not match the assessment_id shape answers 404, not 400."""

    body: Annotated[
        shared_accountbindingrequest.AccountBindingRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class BindProvisionalAccountResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_accountbinding.AccountBindingTypedDict


class BindProvisionalAccountResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_accountbinding.AccountBinding
