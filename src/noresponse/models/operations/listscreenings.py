from __future__ import annotations
from noresponse.models.shared import screeninglist as shared_screeninglist
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from pydantic import model_serializer
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListScreeningsRequestTypedDict(TypedDict):
    group_id: str
    limit: NotRequired[int]
    r"""At most this many items."""
    before: NotRequired[str]
    r"""Read screenings older than this one."""


class ListScreeningsRequest(BaseModel):
    group_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""At most this many items."""

    before: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Read screenings older than this one."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["limit", "before"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


class ListScreeningsResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_screeninglist.ScreeningListTypedDict


class ListScreeningsResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_screeninglist.ScreeningList
