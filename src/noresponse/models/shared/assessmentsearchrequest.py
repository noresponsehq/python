from __future__ import annotations
from .answerrevision import AnswerRevision
from .band import Band
from .decision import Decision
from .flow import Flow
from .identifierexpression import IdentifierExpression, IdentifierExpressionTypedDict
from .identifiersearch import IdentifierSearch, IdentifierSearchTypedDict
from .impact import Impact
from .lane import Lane
from .listmatch import ListMatch
from .origin import Origin
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
    r"""Search retained assessments created in [from,to), at most 366 days. identifier matches the submitted value of each returned assessment directly. The legacy email filter keeps its account-wide mailbox semantics and cannot be combined with identifier. Other filters combine using AND and describe assessment decisions, separate from current account decisions. Results use newest-created order with an assessment-ID tie break and are live, not a snapshot across pages. Requires history or investigate authority; identifier, identifier_expression and email filtering also require identifier-read permission. Detailed response mode additionally requires detailed permission. No Idempotency-Key. identifier_expression requires scope assessment and matches the complete expression within each returned submission; account scope returns 400 invalid_request. At most 8 raw terms and 3 group levels. Mutually exclusive with identifier and email."""

    from_: str
    to: str
    account_id: NotRequired[str]
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    email: NotRequired[str]
    r"""Assessments of every account that one of its retained admitted assessments sent this mailbox as identifiers.email, matched as lists match an email entry: case-insensitive, a +tag removed and, at gmail.com and googlemail.com, the dots of the local part ignored. Only assessments stored since email list matching began carry the mailbox. An address that is not a valid mailbox is refused with 400."""
    flow: NotRequired[Flow]
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""
    status: NotRequired[Status]
    r"""Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered."""
    origin: NotRequired[Origin]
    r"""api (the default) searches the assessments your integration sent. lookup searches the assessments your team ran by hand on the console's Lookup page. The API sets an assessment's origin from the credential that sent it. A lookup is not in any other list, count, webhook event or account."""
    recommendation: NotRequired[Recommendation]
    r"""The recommended action: allow, step_up or review. Your application applies it."""
    limit: NotRequired[int]
    cursor: NotRequired[str]
    r"""Opaque, expiring cursor bound to workspace, environment, operation and all filters, including expression scope, ordered structure and original term values. Keep grouping, operand order, matching modes and values unchanged; an omitted match is equivalent to exact. The page limit may change."""
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
    identifier: NotRequired[IdentifierSearchTypedDict]
    r"""One customer-submitted identifier. Defaults to exact comparison of the original submitted value. canonical uses the supported identifier normalisation without an ownership claim: email preserves local-part case, NFC-normalises it and lowercases the domain without removing dots or tags; phone uses international E.164 without extensions or an inferred region; username uses NFC and Unicode case folding within the customer namespace. mailbox is email-only and explicitly selects existing list rules: case-insensitive, remove +tag, and ignore local-part dots at gmail.com and googlemail.com; googlemail.com maps to gmail.com. Username requires namespace customer. Email and phone forbid namespace. Source-discovered identifiers and platform handles are not searched. Unsupported kinds, namespaces, modes and invalid values return 400. Search equality does not establish verified ownership or merge accounts."""
    identifier_expression: NotRequired[IdentifierExpressionTypedDict]
    r"""A bounded AND/OR expression over submitted identifiers. Required scope assessment means the entire expression must match one retained assessment. Scope account permits each term to match a different retained assessment of the same account and is accepted only by account search. Exactly one of term, and or or is allowed at every node. Groups contain 2 to 8 operands, with at most 3 nested group levels and 8 raw term occurrences over the entire expression. A root term is allowed. Duplicate terms with the same kind, match rule, namespace and normalized comparison are idempotent, but count toward the raw limit. Match rules default to exact and preserve the existing identifier contract. Only retained submitted identifiers can satisfy a term. Unknown fields, unsupported scopes and malformed or oversized expressions return 400 invalid_request."""


class AssessmentSearchRequest(BaseModel):
    r"""Search retained assessments created in [from,to), at most 366 days. identifier matches the submitted value of each returned assessment directly. The legacy email filter keeps its account-wide mailbox semantics and cannot be combined with identifier. Other filters combine using AND and describe assessment decisions, separate from current account decisions. Results use newest-created order with an assessment-ID tie break and are live, not a snapshot across pages. Requires history or investigate authority; identifier, identifier_expression and email filtering also require identifier-read permission. Detailed response mode additionally requires detailed permission. No Idempotency-Key. identifier_expression requires scope assessment and matches the complete expression within each returned submission; account scope returns 400 invalid_request. At most 8 raw terms and 3 group levels. Mutually exclusive with identifier and email."""

    from_: Annotated[str, pydantic.Field(alias="from")]

    to: str

    account_id: Optional[str] = None
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    email: Optional[str] = None
    r"""Assessments of every account that one of its retained admitted assessments sent this mailbox as identifiers.email, matched as lists match an email entry: case-insensitive, a +tag removed and, at gmail.com and googlemail.com, the dots of the local part ignored. Only assessments stored since email list matching began carry the mailbox. An address that is not a valid mailbox is refused with 400."""

    flow: Optional[Flow] = None
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""

    status: Optional[Status] = None
    r"""Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered."""

    origin: Optional[Origin] = None
    r"""api (the default) searches the assessments your integration sent. lookup searches the assessments your team ran by hand on the console's Lookup page. The API sets an assessment's origin from the credential that sent it. A lookup is not in any other list, count, webhook event or account."""

    recommendation: Optional[Recommendation] = None
    r"""The recommended action: allow, step_up or review. Your application applies it."""

    limit: Optional[int] = 20

    cursor: Optional[str] = None
    r"""Opaque, expiring cursor bound to workspace, environment, operation and all filters, including expression scope, ordered structure and original term values. Keep grouping, operand order, matching modes and values unchanged; an omitted match is equivalent to exact. The page limit may change."""

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

    identifier: Optional[IdentifierSearch] = None
    r"""One customer-submitted identifier. Defaults to exact comparison of the original submitted value. canonical uses the supported identifier normalisation without an ownership claim: email preserves local-part case, NFC-normalises it and lowercases the domain without removing dots or tags; phone uses international E.164 without extensions or an inferred region; username uses NFC and Unicode case folding within the customer namespace. mailbox is email-only and explicitly selects existing list rules: case-insensitive, remove +tag, and ignore local-part dots at gmail.com and googlemail.com; googlemail.com maps to gmail.com. Username requires namespace customer. Email and phone forbid namespace. Source-discovered identifiers and platform handles are not searched. Unsupported kinds, namespaces, modes and invalid values return 400. Search equality does not establish verified ownership or merge accounts."""

    identifier_expression: Optional[IdentifierExpression] = None
    r"""A bounded AND/OR expression over submitted identifiers. Required scope assessment means the entire expression must match one retained assessment. Scope account permits each term to match a different retained assessment of the same account and is accepted only by account search. Exactly one of term, and or or is allowed at every node. Groups contain 2 to 8 operands, with at most 3 nested group levels and 8 raw term occurrences over the entire expression. A root term is allowed. Duplicate terms with the same kind, match rule, namespace and normalized comparison are idempotent, but count toward the raw limit. Match rules default to exact and preserve the existing identifier contract. Only retained submitted identifiers can satisfy a term. Unknown fields, unsupported scopes and malformed or oversized expressions return 400 invalid_request."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "account_id",
                "email",
                "flow",
                "status",
                "origin",
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
                "identifier",
                "identifier_expression",
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
