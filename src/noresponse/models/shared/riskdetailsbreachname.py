from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class RiskDetailsBreachNameTypedDict(TypedDict):
    value: str
    seen_in: int
    sites: NotRequired[List[str]]
    r"""The domains of the breached sites whose tables hold the name, lower case, each once, newest breach first, at most 32: the domain values of breaches[]. Covers the email's and the username's tables together. Absent when none of the tables has a site."""
    unsited: NotRequired[int]
    r"""How many of the tables that hold the name have no site, such as a credential list or a stealer log. Absent when none."""


class RiskDetailsBreachName(BaseModel):
    value: str

    seen_in: int

    sites: Optional[List[str]] = None
    r"""The domains of the breached sites whose tables hold the name, lower case, each once, newest breach first, at most 32: the domain values of breaches[]. Covers the email's and the username's tables together. Absent when none of the tables has a site."""

    unsited: Optional[int] = None
    r"""How many of the tables that hold the name have no site, such as a credential list or a stealer log. Absent when none."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["sites", "unsited"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
