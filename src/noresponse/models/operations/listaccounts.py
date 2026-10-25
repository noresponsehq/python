from __future__ import annotations
from noresponse.models.shared import accountlist as shared_accountlist
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListAccountsRequestTypedDict(TypedDict):
    changed_since: NotRequired[str]
    r"""next_cursor from an earlier page, unchanged. Absent, the list starts from the oldest change."""
    limit: NotRequired[int]
    r"""Most accounts per page."""
    unenforced: NotRequired[bool]
    r"""true lists only accounts with no applied enforcement at their current risk_version that have a decision other than allow for some flow or a hold no later applied enforcement resolved."""


class ListAccountsRequest(BaseModel):
    changed_since: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""next_cursor from an earlier page, unchanged. Absent, the list starts from the oldest change."""

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 50
    r"""Most accounts per page."""

    unenforced: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""true lists only accounts with no applied enforcement at their current risk_version that have a decision other than allow for some flow or a hold no later applied enforcement resolved."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["changed_since", "limit", "unenforced"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListAccountsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_accountlist.AccountListTypedDict


class ListAccountsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_accountlist.AccountList
