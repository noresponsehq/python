from __future__ import annotations
from .record import Record, RecordTypedDict
from .recordremaining import RecordRemaining, RecordRemainingTypedDict
from .riskdetails import RiskDetails, RiskDetailsTypedDict
from .risksummary import RiskSummary, RiskSummaryTypedDict
from .screeninglookupanswer import ScreeningLookupAnswer, ScreeningLookupAnswerTypedDict
from .screeninglookupcheck import ScreeningLookupCheck, ScreeningLookupCheckTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningLookupTypedDict(TypedDict):
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Context and coverage for the reviewer, not a finding: nothing here sets a band or a match state."""

    checks: List[ScreeningLookupCheckTypedDict]
    r"""Each lane each identifier was looked up in, identifiers in the order email, phone, username and lanes in the order accounts, phone, breach, domain. Every lane the person's identifiers are looked up in is listed: one that no source answered, or that no source could be asked in, is not_covered. Empty when the person has no email, phone or handle to look up."""
    looked_at: str
    r"""When the lookups ran."""
    answers: NotRequired[List[ScreeningLookupAnswerTypedDict]]
    r"""Each source asked, with what it answered and when. answered_at is absent while the source has not answered."""
    summary: NotRequired[RiskSummaryTypedDict]
    r"""A few typed facts per identifier: an assessment's risk.summary, and a screened person's lookup summary. Every fact is optional: absent means the evidence did not answer and makes no claim, while false or 0 is a definite answer."""
    details: NotRequired[RiskDetailsTypedDict]
    r"""Merged observations behind the summary, served only to a caller who may read evidence: no provider, source, origin, raw breach record or score."""
    records: NotRequired[List[RecordTypedDict]]
    r"""What each source answered, whole, each answer once: every field of each account a connector found, and every column of each breach row the person's email or usernames matched, under the source's own names, and what each search a person started found, each match naming its search. Anyone who may read the person reads them: no extra permission applies, breach passwords and hashes included."""
    remaining: NotRequired[List[RecordRemainingTypedDict]]
    r"""For each search and source whose matched rows records leave out, how many: a breach search returns at most 20 rows of a table and 100 in all, from its first 64 tables by name. A search a person starts on one table of its source fetches the rest of that table, up to 100 rows. Absent when records hold every matched row."""


class ScreeningLookup(BaseModel):
    r"""What the signup check's lookups found for a person: account presence for the email, phone and usernames (the person's handles), the phone lookup, the email domain's registration and the breach search. Context and coverage for the reviewer, not a finding: nothing here sets a band or a match state."""

    checks: List[ScreeningLookupCheck]
    r"""Each lane each identifier was looked up in, identifiers in the order email, phone, username and lanes in the order accounts, phone, breach, domain. Every lane the person's identifiers are looked up in is listed: one that no source answered, or that no source could be asked in, is not_covered. Empty when the person has no email, phone or handle to look up."""

    looked_at: str
    r"""When the lookups ran."""

    answers: Optional[List[ScreeningLookupAnswer]] = None
    r"""Each source asked, with what it answered and when. answered_at is absent while the source has not answered."""

    summary: Optional[RiskSummary] = None
    r"""A few typed facts per identifier: an assessment's risk.summary, and a screened person's lookup summary. Every fact is optional: absent means the evidence did not answer and makes no claim, while false or 0 is a definite answer."""

    details: Optional[RiskDetails] = None
    r"""Merged observations behind the summary, served only to a caller who may read evidence: no provider, source, origin, raw breach record or score."""

    records: Optional[List[Record]] = None
    r"""What each source answered, whole, each answer once: every field of each account a connector found, and every column of each breach row the person's email or usernames matched, under the source's own names, and what each search a person started found, each match naming its search. Anyone who may read the person reads them: no extra permission applies, breach passwords and hashes included."""

    remaining: Optional[List[RecordRemaining]] = None
    r"""For each search and source whose matched rows records leave out, how many: a breach search returns at most 20 rows of a table and 100 in all, from its first 64 tables by name. A search a person starts on one table of its source fetches the rest of that table, up to 100 rows. Absent when records hold every matched row."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["answers", "summary", "details", "records", "remaining"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
