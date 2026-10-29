from __future__ import annotations
from .requestaggregaterequestbucket import RequestAggregateRequestBucket
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class WebhookAggregateRequestTypedDict(TypedDict):
    r"""Count every retained matching attempt in [from,to). Capture is best effort; missing attempts cannot be inferred. UTC buckets may be partial at the edges. The window is at most 30 days."""

    from_: str
    to: str
    bucket: NotRequired[RequestAggregateRequestBucket]
    status: NotRequired[int]
    endpoint_id: NotRequired[str]
    r"""Opaque id of the endpoint registration."""


class WebhookAggregateRequest(BaseModel):
    r"""Count every retained matching attempt in [from,to). Capture is best effort; missing attempts cannot be inferred. UTC buckets may be partial at the edges. The window is at most 30 days."""

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str

    bucket: Optional[RequestAggregateRequestBucket] = None

    status: Optional[int] = None

    endpoint_id: Optional[str] = None
    r"""Opaque id of the endpoint registration."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["bucket", "status", "endpoint_id"])
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
    WebhookAggregateRequest.model_rebuild()
except NameError:
    pass
