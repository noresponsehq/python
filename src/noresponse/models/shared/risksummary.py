from __future__ import annotations
from .consistency import Consistency, ConsistencyTypedDict
from .ipsummary import IPSummary, IPSummaryTypedDict
from .risksummaryemail import RiskSummaryEmail, RiskSummaryEmailTypedDict
from .risksummaryphone import RiskSummaryPhone, RiskSummaryPhoneTypedDict
from .risksummaryusername import RiskSummaryUsername, RiskSummaryUsernameTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RiskSummaryTypedDict(TypedDict):
    r"""A few typed facts per identifier. Every fact is optional: absent means the evidence did not answer and makes no claim, while false or 0 is a definite answer. Lanes that do not exist yet leave their members absent."""

    phone: NotRequired[RiskSummaryPhoneTypedDict]
    email: NotRequired[RiskSummaryEmailTypedDict]
    username: NotRequired[RiskSummaryUsernameTypedDict]
    ip: NotRequired[IPSummaryTypedDict]
    r"""Facts about the submitted IP from the offline database and this tenant's own recent assessments. Every member is optional; absent makes no claim."""
    consistency: NotRequired[ConsistencyTypedDict]
    r"""Cross-identifier agreement, computed from facts only. Every member is optional; absent makes no claim."""


class RiskSummary(BaseModel):
    r"""A few typed facts per identifier. Every fact is optional: absent means the evidence did not answer and makes no claim, while false or 0 is a definite answer. Lanes that do not exist yet leave their members absent."""

    phone: Optional[RiskSummaryPhone] = None

    email: Optional[RiskSummaryEmail] = None

    username: Optional[RiskSummaryUsername] = None

    ip: Optional[IPSummary] = None
    r"""Facts about the submitted IP from the offline database and this tenant's own recent assessments. Every member is optional; absent makes no claim."""

    consistency: Optional[Consistency] = None
    r"""Cross-identifier agreement, computed from facts only. Every member is optional; absent makes no claim."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["phone", "email", "username", "ip", "consistency"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
