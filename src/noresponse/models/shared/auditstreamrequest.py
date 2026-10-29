from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class AuditStreamRequestTypedDict(TypedDict):
    endpoint_id: str
    actions: NotRequired[List[str]]


class AuditStreamRequest(BaseModel):
    endpoint_id: str

    actions: Optional[List[str]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["actions"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
