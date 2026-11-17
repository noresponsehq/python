from __future__ import annotations
from .enrichmentmode import EnrichmentMode
from noresponse.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Literal, Optional
from typing_extensions import NotRequired, TypedDict


EnrichmentChangeKind = Literal[
    "username",
    "email",
    "phone",
]


class EnrichmentChangeTypedDict(TypedDict):
    r"""A change to enrichment. A field left out keeps the value in force; max_spend or deadline null removes the bound."""

    mode: NotRequired[EnrichmentMode]
    r"""off: enrichment starts no search. suggest: enrichment starts no search by itself. automatic: after a workspace person's own investigation, and each time a search on that person finishes, enrichment starts searches by itself."""
    min_likelihood: NotRequired[float]
    r"""Enrichment searches values only from records more likely than this to be the person's, 0 to 0.99."""
    kinds: NotRequired[List[EnrichmentChangeKind]]
    r"""The kinds of value enrichment searches: distinctive usernames, and email addresses and phone numbers, which belong to one person each."""
    max_spend: NotRequired[Nullable[int]]
    r"""The most enrichment may spend on a person from one investigation, in minor units of USD (cents): each search it started after that investigation started counts its estimate or what it spent, whichever is more. At the bound enrichment starts nothing more for that investigation. null: only the environment's screening_daily_cap bounds it."""
    deadline: NotRequired[Nullable[int]]
    r"""How long enrichment may start searches after an investigation starts, 60 to 2592000 seconds. null: no deadline."""


class EnrichmentChange(BaseModel):
    r"""A change to enrichment. A field left out keeps the value in force; max_spend or deadline null removes the bound."""

    mode: Optional[EnrichmentMode] = None
    r"""off: enrichment starts no search. suggest: enrichment starts no search by itself. automatic: after a workspace person's own investigation, and each time a search on that person finishes, enrichment starts searches by itself."""

    min_likelihood: Optional[float] = None
    r"""Enrichment searches values only from records more likely than this to be the person's, 0 to 0.99."""

    kinds: Optional[List[EnrichmentChangeKind]] = None
    r"""The kinds of value enrichment searches: distinctive usernames, and email addresses and phone numbers, which belong to one person each."""

    max_spend: OptionalNullable[int] = UNSET
    r"""The most enrichment may spend on a person from one investigation, in minor units of USD (cents): each search it started after that investigation started counts its estimate or what it spent, whichever is more. At the bound enrichment starts nothing more for that investigation. null: only the environment's screening_daily_cap bounds it."""

    deadline: OptionalNullable[int] = UNSET
    r"""How long enrichment may start searches after an investigation starts, 60 to 2592000 seconds. null: no deadline."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["mode", "min_likelihood", "kinds", "max_spend", "deadline"]
        )
        nullable_fields = set(["max_spend", "deadline"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))
            is_nullable_and_explicitly_set = (
                k in nullable_fields
                and (self.__pydantic_fields_set__.intersection({n}))  # pylint: disable=no-member
            )

            if val != UNSET_SENTINEL:
                if (
                    val is not None
                    or k not in optional_fields
                    or is_nullable_and_explicitly_set
                ):
                    m[k] = val

        return m
