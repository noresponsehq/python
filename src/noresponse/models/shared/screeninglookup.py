from __future__ import annotations
from .riskdetails import RiskDetails, RiskDetailsTypedDict
from .risksummary import RiskSummary, RiskSummaryTypedDict
from .screeninglookupcheck import ScreeningLookupCheck, ScreeningLookupCheckTypedDict
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningLookupTypedDict(TypedDict):
    r"""What the signup check's lookups found for an attendee: account presence for the email, phone and usernames (the attendee's handles), the phone lookup, the email domain's registration and the breach search. Context and coverage for the reviewer, not a finding: nothing here sets a band or a match state."""

    checks: List[ScreeningLookupCheckTypedDict]
    r"""Each lane each identifier was looked up in, identifiers in the order email, phone, username and lanes in the order accounts, phone, breach, domain. Every lane the attendee's identifiers are looked up in is listed: one that no source answered, or that no source could be asked in, is not_covered. Empty when the attendee has no email, phone or handle to look up."""
    looked_at: str
    r"""When the lookups ran."""
    summary: NotRequired[RiskSummaryTypedDict]
    r"""A few typed facts per identifier: an assessment's risk.summary, and an event screening attendee's lookup summary. Every fact is optional: absent means the evidence did not answer and makes no claim, while false or 0 is a definite answer."""
    details: NotRequired[RiskDetailsTypedDict]
    r"""Merged observations behind the summary, served only to a caller who may read evidence: no provider, source, origin, raw breach record or score."""


class ScreeningLookup(BaseModel):
    r"""What the signup check's lookups found for an attendee: account presence for the email, phone and usernames (the attendee's handles), the phone lookup, the email domain's registration and the breach search. Context and coverage for the reviewer, not a finding: nothing here sets a band or a match state."""

    checks: List[ScreeningLookupCheck]
    r"""Each lane each identifier was looked up in, identifiers in the order email, phone, username and lanes in the order accounts, phone, breach, domain. Every lane the attendee's identifiers are looked up in is listed: one that no source answered, or that no source could be asked in, is not_covered. Empty when the attendee has no email, phone or handle to look up."""

    looked_at: str
    r"""When the lookups ran."""

    summary: Optional[RiskSummary] = None
    r"""A few typed facts per identifier: an assessment's risk.summary, and an event screening attendee's lookup summary. Every fact is optional: absent means the evidence did not answer and makes no claim, while false or 0 is a definite answer."""

    details: Optional[RiskDetails] = None
    r"""Merged observations behind the summary, served only to a caller who may read evidence: no provider, source, origin, raw breach record or score."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["summary", "details"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
