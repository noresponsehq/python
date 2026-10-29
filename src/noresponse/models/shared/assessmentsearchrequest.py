from __future__ import annotations
from .answerrevision import AnswerRevision
from .band import Band
from .decision import Decision
from .flow import Flow
from .impact import Impact
from .lane import Lane
from .listmatch import ListMatch
from .reasoncode import ReasonCode
from .recommendation import Recommendation
from .responsemode import ResponseMode
from .status import Status
from noresponse.types import BaseModel, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssessmentSearchRequestTypedDict(TypedDict):
    r"""Search retained assessments created in [from,to), over at most 366 days. Filters use each assessment decision, rather than the current account decision. Results can change between pages. Keep the assessment version to retrieve the exact decision later. This read does not require an idempotency key."""

    from_: str
    to: str
    account_id: NotRequired[str]
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id} and its /assessments. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    email: NotRequired[str]
    r"""Assessments of every account that one of its retained admitted assessments sent this mailbox as identifiers.email, matched as lists match an email entry: case-insensitive, a +tag removed and, at gmail.com and googlemail.com, the dots of the local part ignored. Only assessments stored since email list matching began carry the mailbox. An address that is not a valid mailbox is refused with 400."""
    flow: NotRequired[Flow]
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""
    status: NotRequired[Status]
    r"""complete: final; nothing is still running. A lane that failed or missed its 10 s deadline stays listed in incomplete_sources, and confidence is lower. partial: a recommendation exists and at least one lane is still running or did not settle (see incomplete_sources). pending: nothing usable before the deadline; no recommendation yet, poll or wait for the webhook."""
    recommendation: NotRequired[Recommendation]
    r"""The recommended action: allow, step_up or review. Your application applies it."""
    limit: NotRequired[int]
    cursor: NotRequired[str]
    r"""Opaque, expiring cursor bound to this environment, operation and every filter. Keep the filters unchanged."""
    response_mode: NotRequired[ResponseMode]
    r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""
    decision: NotRequired[Decision]
    r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""
    revision: NotRequired[AnswerRevision]
    r"""Which answer of each assessment the filters describe: latest, the latest stored revision, or first, the first answer, as served when the assessment was first answered (POST /v1/assessments/aggregate counts first answers). A cell of an aggregate drills down to POST /v1/assessments/search with the same filters, revision first and the cell's bucket as from and to."""
    band: NotRequired[Band]
    reason: NotRequired[ReasonCode]
    r"""A stable reason code. New codes may appear; ignore any you do not know."""
    impact: NotRequired[Impact]
    r"""The selected reason's served impact band. Requires reason."""
    lane: NotRequired[Lane]
    r"""An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip."""
    country: NotRequired[str]
    asn: NotRequired[int]
    score_min: NotRequired[int]
    r"""Inclusive lower score bound. Pending answers without a score do not match."""
    score_max: NotRequired[int]
    r"""Inclusive upper score bound, at least score_min when both are supplied."""
    list_match: NotRequired[ListMatch]
    r"""The list action captured at the first answer. Requires revision first. Older answers without captured list state do not match, including none."""
    changed: NotRequired[bool]
    r"""true returns only assessments whose latest stored revision's decision differs from their first answer's decision (see decision); false only the others. An assessment whose first answer or latest revision has no decision yet is not changed. Cannot be combined with revision first."""


class AssessmentSearchRequest(BaseModel):
    r"""Search retained assessments created in [from,to), over at most 366 days. Filters use each assessment decision, rather than the current account decision. Results can change between pages. Keep the assessment version to retrieve the exact decision later. This read does not require an idempotency key."""

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str

    account_id: Optional[str] = None
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id} and its /assessments. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    email: Optional[str] = None
    r"""Assessments of every account that one of its retained admitted assessments sent this mailbox as identifiers.email, matched as lists match an email entry: case-insensitive, a +tag removed and, at gmail.com and googlemail.com, the dots of the local part ignored. Only assessments stored since email list matching began carry the mailbox. An address that is not a valid mailbox is refused with 400."""

    flow: Optional[Flow] = None
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""

    status: Optional[Status] = None
    r"""complete: final; nothing is still running. A lane that failed or missed its 10 s deadline stays listed in incomplete_sources, and confidence is lower. partial: a recommendation exists and at least one lane is still running or did not settle (see incomplete_sources). pending: nothing usable before the deadline; no recommendation yet, poll or wait for the webhook."""

    recommendation: Optional[Recommendation] = None
    r"""The recommended action: allow, step_up or review. Your application applies it."""

    limit: Optional[int] = 20

    cursor: Optional[str] = None
    r"""Opaque, expiring cursor bound to this environment, operation and every filter. Keep the filters unchanged."""

    response_mode: Optional[ResponseMode] = None
    r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""

    decision: Optional[Decision] = None
    r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""

    revision: Optional[AnswerRevision] = None
    r"""Which answer of each assessment the filters describe: latest, the latest stored revision, or first, the first answer, as served when the assessment was first answered (POST /v1/assessments/aggregate counts first answers). A cell of an aggregate drills down to POST /v1/assessments/search with the same filters, revision first and the cell's bucket as from and to."""

    band: Optional[Band] = None

    reason: Optional[ReasonCode] = None
    r"""A stable reason code. New codes may appear; ignore any you do not know."""

    impact: Optional[Impact] = None
    r"""The selected reason's served impact band. Requires reason."""

    lane: Optional[Lane] = None
    r"""An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip."""

    country: Optional[str] = None

    asn: Optional[int] = None

    score_min: Optional[int] = None
    r"""Inclusive lower score bound. Pending answers without a score do not match."""

    score_max: Optional[int] = None
    r"""Inclusive upper score bound, at least score_min when both are supplied."""

    list_match: Optional[ListMatch] = None
    r"""The list action captured at the first answer. Requires revision first. Older answers without captured list state do not match, including none."""

    changed: Optional[bool] = None
    r"""true returns only assessments whose latest stored revision's decision differs from their first answer's decision (see decision); false only the others. An assessment whose first answer or latest revision has no decision yet is not changed. Cannot be combined with revision first."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "account_id",
                "email",
                "flow",
                "status",
                "recommendation",
                "limit",
                "cursor",
                "response_mode",
                "decision",
                "revision",
                "band",
                "reason",
                "impact",
                "lane",
                "country",
                "asn",
                "score_min",
                "score_max",
                "list_match",
                "changed",
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


try:
    AssessmentSearchRequest.model_rebuild()
except NameError:
    pass
