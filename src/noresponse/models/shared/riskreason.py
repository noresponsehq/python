from __future__ import annotations
from .reasoncode import ReasonCode
from .reasonidentifier import ReasonIdentifier
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RiskReasonTypedDict(TypedDict):
    code: ReasonCode
    r"""A stable reason code. New codes may appear; ignore any you do not know."""
    weight: int
    identifier: NotRequired[ReasonIdentifier]
    r"""The submitted identifier or client context field a reason concerns; absent when it concerns the whole assessment. Client context is a claimed hint, not a device fingerprint."""


class RiskReason(BaseModel):
    code: ReasonCode
    r"""A stable reason code. New codes may appear; ignore any you do not know."""

    weight: int

    identifier: Optional[ReasonIdentifier] = None
    r"""The submitted identifier or client context field a reason concerns; absent when it concerns the whole assessment. Client context is a claimed hint, not a device fingerprint."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["identifier"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
