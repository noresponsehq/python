from __future__ import annotations
from .requestaggregaterequestbucket import RequestAggregateRequestBucket
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RequestAggregateRequestTypedDict(TypedDict):
    r"""Count every retained matching attempt in [from,to). Capture is best effort; missing attempts cannot be inferred. UTC buckets may be partial at the edges. The window is at most 7 days."""

    from_: str
    to: str
    bucket: NotRequired[RequestAggregateRequestBucket]
    status: NotRequired[int]
    route: NotRequired[str]
    api_key_id: NotRequired[str]


class RequestAggregateRequest(BaseModel):
    r"""Count every retained matching attempt in [from,to). Capture is best effort; missing attempts cannot be inferred. UTC buckets may be partial at the edges. The window is at most 7 days."""

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str

    bucket: Optional[RequestAggregateRequestBucket] = None

    status: Optional[int] = None

    route: Optional[str] = None

    api_key_id: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["bucket", "status", "route", "api_key_id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


try:
    RequestAggregateRequest.model_rebuild()
except NameError:
    pass
