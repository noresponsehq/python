from __future__ import annotations
from .breachexposed import BreachExposed
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class BreachSummaryTypedDict(TypedDict):
    r"""Breach facts for one selector. found is the one required member: false is a definite 'in no breach table'. Every other member is optional, and absent makes no claim. No member carries a breach value, password or hash, and unknown members are refused. truncated means the value matched more tables or records than the lookup keeps, so absence-based claims (a missing name match, for example) are withheld; a truncated result is always found."""

    found: bool
    breach_count: NotRequired[int]
    r"""Distinct breach tables the value appears in."""
    first_year: NotRequired[int]
    r"""Year of the oldest dated table."""
    last_year: NotRequired[int]
    r"""Year of the newest dated table."""
    exposed: NotRequired[List[BreachExposed]]
    r"""The union of data kinds the matching tables held, without the values."""
    in_credential_lists: NotRequired[bool]
    r"""The value is in a credential_list or stealer_log table."""
    recent_password_exposure: NotRequired[bool]
    r"""A plaintext password sat next to the value in a table dated two years ago or less, or the value is in a stealer_log table."""
    truncated: NotRequired[bool]


class BreachSummary(BaseModel):
    r"""Breach facts for one selector. found is the one required member: false is a definite 'in no breach table'. Every other member is optional, and absent makes no claim. No member carries a breach value, password or hash, and unknown members are refused. truncated means the value matched more tables or records than the lookup keeps, so absence-based claims (a missing name match, for example) are withheld; a truncated result is always found."""

    found: bool

    breach_count: Optional[int] = None
    r"""Distinct breach tables the value appears in."""

    first_year: Optional[int] = None
    r"""Year of the oldest dated table."""

    last_year: Optional[int] = None
    r"""Year of the newest dated table."""

    exposed: Optional[List[BreachExposed]] = None
    r"""The union of data kinds the matching tables held, without the values."""

    in_credential_lists: Optional[bool] = None
    r"""The value is in a credential_list or stealer_log table."""

    recent_password_exposure: Optional[bool] = None
    r"""A plaintext password sat next to the value in a table dated two years ago or less, or the value is in a stealer_log table."""

    truncated: Optional[bool] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "breach_count",
                "first_year",
                "last_year",
                "exposed",
                "in_credential_lists",
                "recent_password_exposure",
                "truncated",
            ]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
