from __future__ import annotations
from .footprintfamily import FootprintFamily
from .identifier import Identifier
from .riskdetailseventkind import RiskDetailsEventKind
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RiskDetailsEventTypedDict(TypedDict):
    year: int
    kind: RiskDetailsEventKind
    site: str
    category: str
    family: FootprintFamily
    r"""The source-neutral kind of evidence: account_presence (an account found on a site), auth_provider (the account at your auth provider), breach (breach and credential tables), breach_abuse (abuse and fraud communities' tables) and code_hosting (a code hosting profile)."""
    identifier: Identifier
    month: NotRequired[int]


class RiskDetailsEvent(BaseModel):
    year: int

    kind: RiskDetailsEventKind

    site: str

    category: str

    family: FootprintFamily
    r"""The source-neutral kind of evidence: account_presence (an account found on a site), auth_provider (the account at your auth provider), breach (breach and credential tables), breach_abuse (abuse and fraud communities' tables) and code_hosting (a code hosting profile)."""

    identifier: Identifier

    month: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["month"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
