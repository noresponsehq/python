from __future__ import annotations
from .breachsummary import BreachSummary, BreachSummaryTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RiskSummaryEmailTypedDict(TypedDict):
    disposable: NotRequired[bool]
    accounts_found: NotRequired[int]
    r"""Accounts found for the email."""
    breach: NotRequired[BreachSummaryTypedDict]
    r"""Breach facts for one selector. found is the one required member: false is a definite 'in no breach table'. Every other member is optional, and absent makes no claim. No member carries a breach value, password or hash, and unknown members are refused. truncated means the value matched more tables or records than the lookup keeps, so absence-based claims (a missing name match, for example) are withheld; a truncated result is always found."""


class RiskSummaryEmail(BaseModel):
    disposable: Optional[bool] = None

    accounts_found: Optional[int] = None
    r"""Accounts found for the email."""

    breach: Optional[BreachSummary] = None
    r"""Breach facts for one selector. found is the one required member: false is a definite 'in no breach table'. Every other member is optional, and absent makes no claim. No member carries a breach value, password or hash, and unknown members are refused. truncated means the value matched more tables or records than the lookup keeps, so absence-based claims (a missing name match, for example) are withheld; a truncated result is always found."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["disposable", "accounts_found", "breach"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
