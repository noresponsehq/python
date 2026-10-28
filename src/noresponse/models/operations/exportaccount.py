from __future__ import annotations
from noresponse.models.shared import (
    accountexport as shared_accountexport,
    responsemode as shared_responsemode,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ExportAccountRequestTypedDict(TypedDict):
    account_id: str
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""
    response_mode: NotRequired[shared_responsemode.ResponseMode]
    r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""


class ExportAccountRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""

    response_mode: Annotated[
        Optional[shared_responsemode.ResponseMode],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""

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


class ExportAccountResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_accountexport.AccountExportTypedDict


class ExportAccountResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_accountexport.AccountExport
