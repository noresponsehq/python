from __future__ import annotations
from .listentryrequest import ListEntryRequest, ListEntryRequestTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ListBulkRequestTypedDict(TypedDict):
    r"""At most 100 additions and removals combined. One transaction applies all changes or none. Idempotency-Key prevents duplicate changes for 24 hours; a different body under the same key returns 409. Matching reads see the new list immediately, while bounded durable jobs propagate account risk notifications."""

    add: NotRequired[List[ListEntryRequestTypedDict]]
    remove: NotRequired[List[str]]


class ListBulkRequest(BaseModel):
    r"""At most 100 additions and removals combined. One transaction applies all changes or none. Idempotency-Key prevents duplicate changes for 24 hours; a different body under the same key returns 409. Matching reads see the new list immediately, while bounded durable jobs propagate account risk notifications."""

    add: Optional[List[ListEntryRequest]] = None

    remove: Optional[List[str]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["add", "remove"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
