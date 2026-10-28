from __future__ import annotations
from .breach import Breach, BreachTypedDict
from .riskdetailsbreachname import RiskDetailsBreachName, RiskDetailsBreachNameTypedDict
from .riskdetailsevent import RiskDetailsEvent, RiskDetailsEventTypedDict
from .riskdetailsphonename import RiskDetailsPhoneName, RiskDetailsPhoneNameTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class RiskDetailsTypedDict(TypedDict):
    r"""Detailed view only (response_mode=detailed, which needs the detailed scope); a standard answer leaves it out. Merged observations without provider, source, origin, raw breach record, value or score."""

    phone_names: NotRequired[List[RiskDetailsPhoneNameTypedDict]]
    breaches: NotRequired[List[BreachTypedDict]]
    r"""The matching breach tables, newest first, at most 100."""
    breach_names: NotRequired[List[RiskDetailsBreachNameTypedDict]]
    r"""Names found next to the identifiers in breach records, merged, with the number of distinct tables each was seen in."""
    events: NotRequired[List[RiskDetailsEventTypedDict]]
    r"""The identity's dated footprint events, newest first, at most 300: the year and month, what happened (created, last_active, breached), the site, its category, the kind of evidence and the identifier it belongs to. No breach value: dates are coarsened to the month."""


class RiskDetails(BaseModel):
    r"""Detailed view only (response_mode=detailed, which needs the detailed scope); a standard answer leaves it out. Merged observations without provider, source, origin, raw breach record, value or score."""

    phone_names: Optional[List[RiskDetailsPhoneName]] = None

    breaches: Optional[List[Breach]] = None
    r"""The matching breach tables, newest first, at most 100."""

    breach_names: Optional[List[RiskDetailsBreachName]] = None
    r"""Names found next to the identifiers in breach records, merged, with the number of distinct tables each was seen in."""

    events: Optional[List[RiskDetailsEvent]] = None
    r"""The identity's dated footprint events, newest first, at most 300: the year and month, what happened (created, last_active, breached), the site, its category, the kind of evidence and the identifier it belongs to. No breach value: dates are coarsened to the month."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["phone_names", "breaches", "breach_names", "events"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
