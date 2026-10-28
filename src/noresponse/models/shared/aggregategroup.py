from __future__ import annotations
from .band import Band
from .decision import Decision
from .flow import Flow
from .impact import Impact
from .lane import Lane
from .listmatch import ListMatch
from .reasoncode import ReasonCode
from .recommendation import Recommendation
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AggregateGroupTypedDict(TypedDict):
    r"""One group's count in one bucket. It holds each grouped dimension the counted assessments had a value for: a pending first answer has no decision, recommendation or band; an answer that fired no reason, listed no incomplete lane, matched no list entry or whose IP has no known country or ASN leaves that dimension out."""

    count: int
    decision: NotRequired[Decision]
    r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""
    flow: NotRequired[Flow]
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""
    recommendation: NotRequired[Recommendation]
    r"""The recommended action: allow, step_up or review. Your application applies it."""
    band: NotRequired[Band]
    r"""low 0-29, medium 30-59, high 60-84, critical 85-100."""
    list_match: NotRequired[ListMatch]
    r"""The action of the list entry that decided the account."""
    reason: NotRequired[ReasonCode]
    r"""A stable reason code. New codes may appear; ignore any you do not know."""
    impact: NotRequired[Impact]
    lane: NotRequired[Lane]
    r"""An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip."""
    country: NotRequired[str]
    asn: NotRequired[int]


class AggregateGroup(BaseModel):
    r"""One group's count in one bucket. It holds each grouped dimension the counted assessments had a value for: a pending first answer has no decision, recommendation or band; an answer that fired no reason, listed no incomplete lane, matched no list entry or whose IP has no known country or ASN leaves that dimension out."""

    count: int

    decision: Optional[Decision] = None
    r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""

    flow: Optional[Flow] = None
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""

    recommendation: Optional[Recommendation] = None
    r"""The recommended action: allow, step_up or review. Your application applies it."""

    band: Optional[Band] = None
    r"""low 0-29, medium 30-59, high 60-84, critical 85-100."""

    list_match: Optional[ListMatch] = None
    r"""The action of the list entry that decided the account."""

    reason: Optional[ReasonCode] = None
    r"""A stable reason code. New codes may appear; ignore any you do not know."""

    impact: Optional[Impact] = None

    lane: Optional[Lane] = None
    r"""An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip."""

    country: Optional[str] = None

    asn: Optional[int] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "decision",
                "flow",
                "recommendation",
                "band",
                "list_match",
                "reason",
                "impact",
                "lane",
                "country",
                "asn",
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
