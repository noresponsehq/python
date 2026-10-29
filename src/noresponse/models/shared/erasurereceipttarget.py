from __future__ import annotations
from .erasurereceipttargetname import ErasureReceiptTargetName
from .erasurereceipttargetstatus import ErasureReceiptTargetStatus
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ErasureReceiptTargetTypedDict(TypedDict):
    name: ErasureReceiptTargetName
    status: ErasureReceiptTargetStatus
    completed_at: NotRequired[str]


class ErasureReceiptTarget(BaseModel):
    name: ErasureReceiptTargetName

    status: ErasureReceiptTargetStatus

    completed_at: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["completed_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
