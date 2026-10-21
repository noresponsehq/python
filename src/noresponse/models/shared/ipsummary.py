from __future__ import annotations
from .ipsummarytype import IPSummaryType
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class IPSummaryTypedDict(TypedDict):
    r"""Facts about the submitted IP from the offline database and this tenant's own recent assessments. Every member is optional; absent makes no claim."""

    country: NotRequired[str]
    r"""ISO 3166-1 alpha-2 country of the address."""
    type: NotRequired[IPSummaryType]
    r"""The address's network type."""
    seen_in_tenant: NotRequired[int]
    r"""Assessments in this tenant with the same IP in the last 24 hours, this one included. A count only."""


class IPSummary(BaseModel):
    r"""Facts about the submitted IP from the offline database and this tenant's own recent assessments. Every member is optional; absent makes no claim."""

    country: Optional[str] = None
    r"""ISO 3166-1 alpha-2 country of the address."""

    type: Optional[IPSummaryType] = None
    r"""The address's network type."""

    seen_in_tenant: Optional[int] = None
    r"""Assessments in this tenant with the same IP in the last 24 hours, this one included. A count only."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["country", "type", "seen_in_tenant"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
