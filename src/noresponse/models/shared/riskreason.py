from __future__ import annotations
from .direction import Direction
from .impact import Impact
from .reasoncode import ReasonCode
from .reasonidentifier import ReasonIdentifier
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RiskReasonTypedDict(TypedDict):
    r"""One reason that fired. direction is whether it raises or lowers the score, or is neutral (informational, it moves nothing). impact is a coarse band of how much it moves the score: none for a neutral reason, otherwise low, medium or high."""

    code: ReasonCode
    r"""A stable reason code. New codes may appear; ignore any you do not know."""
    direction: Direction
    impact: Impact
    identifier: NotRequired[ReasonIdentifier]
    r"""The submitted identifier or client context field a reason concerns; absent when it concerns the whole assessment. Client context is a claimed hint, not a device fingerprint."""
    list_entry_id: NotRequired[str]
    r"""The list entry a list_match reason applied. No other reason carries it."""


class RiskReason(BaseModel):
    r"""One reason that fired. direction is whether it raises or lowers the score, or is neutral (informational, it moves nothing). impact is a coarse band of how much it moves the score: none for a neutral reason, otherwise low, medium or high."""

    code: ReasonCode
    r"""A stable reason code. New codes may appear; ignore any you do not know."""

    direction: Direction

    impact: Impact

    identifier: Optional[ReasonIdentifier] = None
    r"""The submitted identifier or client context field a reason concerns; absent when it concerns the whole assessment. Client context is a claimed hint, not a device fingerprint."""

    list_entry_id: Optional[str] = None
    r"""The list entry a list_match reason applied. No other reason carries it."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["identifier", "list_entry_id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
