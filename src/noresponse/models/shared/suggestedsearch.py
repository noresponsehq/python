from __future__ import annotations
from .suggestedsearchkind import SuggestedSearchKind
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class SuggestedSearchTypedDict(TypedDict):
    r"""A search enrichment would start: a distinctive or unique value of a likely record, not yet searched for the person. A person starts it with POST .../searches, naming the record and the field."""

    record_id: str
    r"""The lookup record whose value enrichment would search. It is among the report's lookup records."""
    field: str
    r"""The field of that record that holds the value. Send record_id and field to POST .../searches to start the search."""
    kind: SuggestedSearchKind
    r"""The kind of the value: one of the kinds the environment's enrichment setting names."""
    likelihood: float
    r"""The likelihood of the record that holds the value, from 0.01 to 0.99. Enrichment suggests a value only from a record more likely than the setting's min_likelihood, the likeliest first."""


class SuggestedSearch(BaseModel):
    r"""A search enrichment would start: a distinctive or unique value of a likely record, not yet searched for the person. A person starts it with POST .../searches, naming the record and the field."""

    record_id: str
    r"""The lookup record whose value enrichment would search. It is among the report's lookup records."""

    field: str
    r"""The field of that record that holds the value. Send record_id and field to POST .../searches to start the search."""

    kind: SuggestedSearchKind
    r"""The kind of the value: one of the kinds the environment's enrichment setting names."""

    likelihood: float
    r"""The likelihood of the record that holds the value, from 0.01 to 0.99. Enrichment suggests a value only from a record more likely than the setting's min_likelihood, the likeliest first."""
