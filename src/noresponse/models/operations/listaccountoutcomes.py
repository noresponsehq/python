from __future__ import annotations
from noresponse.models.shared import accountoutcomepage as shared_accountoutcomepage
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListAccountOutcomesRequestTypedDict(TypedDict):
    account_id: str
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""
    limit: NotRequired[int]
    r"""Items per page."""
    cursor: NotRequired[str]
    r"""next_cursor from the previous page, unchanged."""


class ListAccountOutcomesRequest(BaseModel):
    account_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Items per page."""

    cursor: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""next_cursor from the previous page, unchanged."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["limit", "cursor"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListAccountOutcomesResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_accountoutcomepage.AccountOutcomePageTypedDict


class ListAccountOutcomesResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_accountoutcomepage.AccountOutcomePage
