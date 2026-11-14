from __future__ import annotations
from .recordfield import RecordField, RecordFieldTypedDict
from .recordmatch import RecordMatch, RecordMatchTypedDict
from .recordsource import RecordSource, RecordSourceTypedDict
from .verdict import Verdict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class RecordTypedDict(TypedDict):
    r"""One answer from one source: where it came from, what found it and every field it holds. A person's lookup records also say how likely each is the person."""

    id: str
    r"""Made from the source and the fields' names and original values, so the same answer found twice is one record with the same id."""
    source: RecordSourceTypedDict
    r"""Where a record came from."""
    matched: List[RecordMatchTypedDict]
    r"""Each kind of searched value that found the record."""
    fields: List[RecordFieldTypedDict]
    r"""Every field the source returned, in the order the source's connector lists them; a breach row's columns in name order. Nothing is withheld: a breach row's passwords, hashes and salts are fields like any other."""
    observed_at: str
    r"""When the source last gave this answer."""
    likelihood: NotRequired[float]
    r"""How likely the record is the person it was found for, from 0.01 to 0.99, to two places. A record found by the person's own email or phone starts as theirs; any other starts lower the more people its search found on its site. Each value it shares with what is known of the person raises it, a rare value more than a common one, and a different birth date or full name lowers it. What is known is what the person's row gives and the values of their own records: those found by their email or phone, and those a reviewer joined. Present on a person's lookup records, with agreed, clashed and joined."""
    agreed: NotRequired[List[str]]
    r"""The fields of this record whose values agreed with what is known of the person, by their field names, in the record's order. The value that found the record is not among them."""
    clashed: NotRequired[List[str]]
    r"""The fields of this record that clashed with what is known of the person: a birth date or a full name that differs from the person's."""
    joined: NotRequired[bool]
    r"""Whether the record joins the person: its likelihood reached 0.9 or a reviewer joined it, and no reviewer rejected it. A record that does not join stays a lead."""
    verdict: NotRequired[Verdict]
    r"""A reviewer's overrule (POST .../people/{person_id}/records), which decides joined whatever the likelihood and sticks for as long as a lookup finds the same record. Absent when nobody overruled it."""


class Record(BaseModel):
    r"""One answer from one source: where it came from, what found it and every field it holds. A person's lookup records also say how likely each is the person."""

    id: str
    r"""Made from the source and the fields' names and original values, so the same answer found twice is one record with the same id."""

    source: RecordSource
    r"""Where a record came from."""

    matched: List[RecordMatch]
    r"""Each kind of searched value that found the record."""

    fields: List[RecordField]
    r"""Every field the source returned, in the order the source's connector lists them; a breach row's columns in name order. Nothing is withheld: a breach row's passwords, hashes and salts are fields like any other."""

    observed_at: str
    r"""When the source last gave this answer."""

    likelihood: Optional[float] = None
    r"""How likely the record is the person it was found for, from 0.01 to 0.99, to two places. A record found by the person's own email or phone starts as theirs; any other starts lower the more people its search found on its site. Each value it shares with what is known of the person raises it, a rare value more than a common one, and a different birth date or full name lowers it. What is known is what the person's row gives and the values of their own records: those found by their email or phone, and those a reviewer joined. Present on a person's lookup records, with agreed, clashed and joined."""

    agreed: Optional[List[str]] = None
    r"""The fields of this record whose values agreed with what is known of the person, by their field names, in the record's order. The value that found the record is not among them."""

    clashed: Optional[List[str]] = None
    r"""The fields of this record that clashed with what is known of the person: a birth date or a full name that differs from the person's."""

    joined: Optional[bool] = None
    r"""Whether the record joins the person: its likelihood reached 0.9 or a reviewer joined it, and no reviewer rejected it. A record that does not join stays a lead."""

    verdict: Optional[Verdict] = None
    r"""A reviewer's overrule (POST .../people/{person_id}/records), which decides joined whatever the likelihood and sticks for as long as a lookup finds the same record. Absent when nobody overruled it."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["likelihood", "agreed", "clashed", "joined", "verdict"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
