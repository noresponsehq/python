from __future__ import annotations
from .assessmenttiming import AssessmentTiming, AssessmentTimingTypedDict
from .confidence import Confidence
from .incompletesource import IncompleteSource, IncompleteSourceTypedDict
from .recommendation import Recommendation
from .risk import Risk, RiskTypedDict
from .signal import Signal, SignalTypedDict
from .status import Status
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssessmentTypedDict(TypedDict):
    r"""One assessment of one account, as POST /v1/assessments, GET /v1/assessments/{assessment_id} and the assessment.updated webhook return it. status says whether it is final (complete), usable with a source still running (partial) or not yet usable (pending). risk and recommendation are present for complete and partial; assessment_url is present for pending. Keep the highest assessment_version."""

    assessment_id: str
    r"""Opaque, server-assigned assessment id: 'asm_' and a 26-character Crockford base32 ULID. Unique within the tenant; another tenant's assessment id answers 404."""
    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your tenant. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused, as is a JWT; a hex digest such as a SHA-256 is allowed. It travels only in request bodies. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    status: Status
    r"""complete: final; nothing is still running. A lane that failed or missed its 10 s deadline stays listed in incomplete_sources, and confidence is lower. partial: a recommendation exists and at least one lane is still running or did not settle (see incomplete_sources). pending: nothing usable before the deadline; no recommendation yet, poll or wait for the webhook."""
    confidence: Confidence
    r"""Ordinal confidence in the recommendation under the current policy: low, medium, high or unavailable."""
    incomplete_sources: List[IncompleteSourceTypedDict]
    r"""The lanes that did not settle, each listed once with a reason; lanes, not sources. In a detailed view a lane is listed exactly when one of its signals did not settle; a standard view carries no signals to match."""
    policy_version: str
    r"""Version of the hand-authored heuristic weights that produced the recommendation, for example 'risk-2026-10.7'. A tenant threshold override adds a +t<N> suffix, e.g. 'risk-2026-10.7+t3'."""
    assessment_version: int
    r"""Monotonic revision of this assessment. 1 on the synchronous answer; each material change while the assessment is served (an async continuation settling a source, a change of recommendation, confidence or status) increments it. Expiry does not increment it: an expired assessment is gone, not revised, and the expiry webhook carries the last served version."""
    created_at: str
    r"""When the assessment was created. Fixed for the life of the assessment: every revision carries the same created_at."""
    updated_at: str
    expires_at: str
    r"""After this instant the assessment is no longer served: GET /v1/assessments/{assessment_id} answers 404 and it leaves the account history. It is created_at plus your retention period at creation (default and maximum 365 days) and is fixed per record: a later revision keeps it, and a new assessment for the same account starts its own clock. If you later shorten retention, the effective expiry becomes created_at plus the shorter of the two periods."""
    timing: AssessmentTimingTypedDict
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    request_id: NotRequired[str]
    r"""An optional provider correlation id, echoed back. It is not an idempotency key. Refuses an exact-shape JWT or a bare 40, 64 or 128 character hex digest; a UUID is accepted."""
    recommendation: NotRequired[Recommendation]
    r"""The recommended action: allow, step_up or review. Your application applies it."""
    risk: NotRequired[RiskTypedDict]
    r"""The one risk decision for this event. score is 0 (safe) to 100 (risky): the sum of the weights of the reasons that fired, clamped to 0 to 100, from hand-set versioned weights. Every answer with a recommendation carries it, and the top-level recommendation equals risk.recommendation. It names no source or provider."""
    signals: NotRequired[List[SignalTypedDict]]
    r"""Detailed view only (response_mode=detailed, which needs the detailed scope): a standard answer omits signals[], and a detailed one always carries it, possibly empty. The body does not name its mode, so that rule is the serving gate's; the schema states the half it can: an answer with risk.details is a detailed view and carries signals[]. At most one signal per (type, source_id, identifier)."""
    policy_basis: Literal["heuristic_unvalidated"]
    r"""Labels the v0 policy as hand-authored and not statistically validated."""
    assessment_url: NotRequired[str]
    r"""Server-relative path of the authoritative assessment, GET /v1/assessments/{assessment_id}."""


class Assessment(BaseModel):
    r"""One assessment of one account, as POST /v1/assessments, GET /v1/assessments/{assessment_id} and the assessment.updated webhook return it. status says whether it is final (complete), usable with a source still running (partial) or not yet usable (pending). risk and recommendation are present for complete and partial; assessment_url is present for pending. Keep the highest assessment_version."""

    assessment_id: str
    r"""Opaque, server-assigned assessment id: 'asm_' and a 26-character Crockford base32 ULID. Unique within the tenant; another tenant's assessment id answers 404."""

    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your tenant. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused, as is a JWT; a hex digest such as a SHA-256 is allowed. It travels only in request bodies. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    status: Status
    r"""complete: final; nothing is still running. A lane that failed or missed its 10 s deadline stays listed in incomplete_sources, and confidence is lower. partial: a recommendation exists and at least one lane is still running or did not settle (see incomplete_sources). pending: nothing usable before the deadline; no recommendation yet, poll or wait for the webhook."""

    confidence: Confidence
    r"""Ordinal confidence in the recommendation under the current policy: low, medium, high or unavailable."""

    incomplete_sources: List[IncompleteSource]
    r"""The lanes that did not settle, each listed once with a reason; lanes, not sources. In a detailed view a lane is listed exactly when one of its signals did not settle; a standard view carries no signals to match."""

    policy_version: str
    r"""Version of the hand-authored heuristic weights that produced the recommendation, for example 'risk-2026-10.7'. A tenant threshold override adds a +t<N> suffix, e.g. 'risk-2026-10.7+t3'."""

    assessment_version: int
    r"""Monotonic revision of this assessment. 1 on the synchronous answer; each material change while the assessment is served (an async continuation settling a source, a change of recommendation, confidence or status) increments it. Expiry does not increment it: an expired assessment is gone, not revised, and the expiry webhook carries the last served version."""

    created_at: str
    r"""When the assessment was created. Fixed for the life of the assessment: every revision carries the same created_at."""

    updated_at: str

    expires_at: str
    r"""After this instant the assessment is no longer served: GET /v1/assessments/{assessment_id} answers 404 and it leaves the account history. It is created_at plus your retention period at creation (default and maximum 365 days) and is fixed per record: a later revision keeps it, and a new assessment for the same account starts its own clock. If you later shorten retention, the effective expiry becomes created_at plus the shorter of the two periods."""

    timing: AssessmentTiming

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"
    r"""Version of the body shape."""

    request_id: Optional[str] = None
    r"""An optional provider correlation id, echoed back. It is not an idempotency key. Refuses an exact-shape JWT or a bare 40, 64 or 128 character hex digest; a UUID is accepted."""

    recommendation: Optional[Recommendation] = None
    r"""The recommended action: allow, step_up or review. Your application applies it."""

    risk: Optional[Risk] = None
    r"""The one risk decision for this event. score is 0 (safe) to 100 (risky): the sum of the weights of the reasons that fired, clamped to 0 to 100, from hand-set versioned weights. Every answer with a recommendation carries it, and the top-level recommendation equals risk.recommendation. It names no source or provider."""

    signals: Optional[List[Signal]] = None
    r"""Detailed view only (response_mode=detailed, which needs the detailed scope): a standard answer omits signals[], and a detailed one always carries it, possibly empty. The body does not name its mode, so that rule is the serving gate's; the schema states the half it can: an answer with risk.details is a detailed view and carries signals[]. At most one signal per (type, source_id, identifier)."""

    policy_basis: Annotated[
        Annotated[
            Literal["heuristic_unvalidated"],
            AfterValidator(validate_const("heuristic_unvalidated")),
        ],
        pydantic.Field(alias="policy_basis"),
    ] = "heuristic_unvalidated"
    r"""Labels the v0 policy as hand-authored and not statistically validated."""

    assessment_url: Optional[str] = None
    r"""Server-relative path of the authoritative assessment, GET /v1/assessments/{assessment_id}."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["request_id", "recommendation", "risk", "signals", "assessment_url"]
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
    Assessment.model_rebuild()
except NameError:
    pass
