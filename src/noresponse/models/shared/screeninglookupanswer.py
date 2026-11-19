from __future__ import annotations
from .identifier import Identifier
from .signaloutcome import SignalOutcome
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningLookupAnswerTypedDict(TypedDict):
    connector: str
    r"""The id of the connector asked: breach for the breach search."""
    identifier: Identifier
    outcome: SignalOutcome
    r"""Per-signal outcome. A source that timed out, was blocked or errored reports blocked, unavailable or inconclusive with a reason and is listed in incomplete_sources; not_found is a definite absence."""
    answered_at: NotRequired[str]


class ScreeningLookupAnswer(BaseModel):
    connector: str
    r"""The id of the connector asked: breach for the breach search."""

    identifier: Identifier

    outcome: SignalOutcome
    r"""Per-signal outcome. A source that timed out, was blocked or errored reports blocked, unavailable or inconclusive with a reason and is listed in incomplete_sources; not_found is a definite absence."""

    answered_at: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["answered_at"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
