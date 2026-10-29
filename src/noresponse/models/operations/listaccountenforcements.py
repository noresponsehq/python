from __future__ import annotations
from noresponse.models.shared import (
    accountenforcementlist as shared_accountenforcementlist,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Awaitable, Callable, Dict, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListAccountEnforcementsRequestTypedDict(TypedDict):
    account_id: str
    r"""The account_id the workspace sends with its assessments, as one path segment (percent-encode '|' and ':' if the client requires it). A value that does not match the account_id shape answers 400 invalid_request."""
    limit: NotRequired[int]
    r"""Items per page."""
    cursor: NotRequired[str]
    r"""next_cursor from the previous page, unchanged."""


class ListAccountEnforcementsRequest(BaseModel):
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


class ListAccountEnforcementsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_accountenforcementlist.AccountEnforcementListTypedDict


class ListAccountEnforcementsResponse(BaseModel):
    next: Union[
        Callable[[], Optional[ListAccountEnforcementsResponse]],
        Callable[[], Awaitable[Optional[ListAccountEnforcementsResponse]]],
    ]

    headers: Dict[str, List[str]]

    result: shared_accountenforcementlist.AccountEnforcementList
