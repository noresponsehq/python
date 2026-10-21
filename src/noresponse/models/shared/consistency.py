from __future__ import annotations
from .consistencyvalue import ConsistencyValue
from .country import Country
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ConsistencyTypedDict(TypedDict):
    r"""Cross-identifier agreement, computed from facts only. Every member is optional; absent makes no claim."""

    name: NotRequired[ConsistencyValue]
    r"""How a submitted identifier agrees with what the evidence holds for the other identifiers. unknown is a definite 'cannot tell' (for example a truncated or too-common breach result); absent means the comparison was not made."""
    phone: NotRequired[ConsistencyValue]
    r"""How a submitted identifier agrees with what the evidence holds for the other identifiers. unknown is a definite 'cannot tell' (for example a truncated or too-common breach result); absent means the comparison was not made."""
    ip: NotRequired[ConsistencyValue]
    r"""How a submitted identifier agrees with what the evidence holds for the other identifiers. unknown is a definite 'cannot tell' (for example a truncated or too-common breach result); absent means the comparison was not made."""
    country: NotRequired[Country]
    r"""IP country, phone country, breach countries and policy_context.region together."""


class Consistency(BaseModel):
    r"""Cross-identifier agreement, computed from facts only. Every member is optional; absent makes no claim."""

    name: Optional[ConsistencyValue] = None
    r"""How a submitted identifier agrees with what the evidence holds for the other identifiers. unknown is a definite 'cannot tell' (for example a truncated or too-common breach result); absent means the comparison was not made."""

    phone: Optional[ConsistencyValue] = None
    r"""How a submitted identifier agrees with what the evidence holds for the other identifiers. unknown is a definite 'cannot tell' (for example a truncated or too-common breach result); absent means the comparison was not made."""

    ip: Optional[ConsistencyValue] = None
    r"""How a submitted identifier agrees with what the evidence holds for the other identifiers. unknown is a definite 'cannot tell' (for example a truncated or too-common breach result); absent means the comparison was not made."""

    country: Optional[Country] = None
    r"""IP country, phone country, breach countries and policy_context.region together."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["name", "phone", "ip", "country"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
