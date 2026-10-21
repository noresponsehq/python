from __future__ import annotations
from .linetype import LineType
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RiskSummaryPhoneTypedDict(TypedDict):
    line_type: NotRequired[LineType]
    country: NotRequired[str]
    report_count: NotRequired[int]
    r"""Highest report count any source gave for the number."""
    carrier: NotRequired[str]
    r"""Carrier-network metadata from privately weighted sources; not upstream provider attribution."""


class RiskSummaryPhone(BaseModel):
    line_type: Optional[LineType] = None

    country: Optional[str] = None

    report_count: Optional[int] = None
    r"""Highest report count any source gave for the number."""

    carrier: Optional[str] = None
    r"""Carrier-network metadata from privately weighted sources; not upstream provider attribution."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["line_type", "country", "report_count", "carrier"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
