from __future__ import annotations
from .assessmentdetail import AssessmentDetail, AssessmentDetailTypedDict
from .decision import Decision
from .depth import Depth
from .flow import Flow
from .identifiermatch import IdentifierMatch, IdentifierMatchTypedDict
from .identifiertermmatch import IdentifierTermMatch, IdentifierTermMatchTypedDict
from .status import Status
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssessmentSearchItemTypedDict(TypedDict):
    r"""One stored assessment revision, exactly as GET /v1/assessments/{assessment_id}/versions/{version} returns it, with the decision of the assessment's first answer. It is not re-scored and carries no current account risk."""

    id: str
    r"""This assessment's id, equal to detail.assessment_id."""
    status: Status
    r"""Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered."""
    flow: Flow
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""
    depth: Depth
    r"""How long the synchronous answer waits for sources. quick waits only for the fast sources, those that answer within 500 ms of ingress (or deadline_ms when lower); full waits for the whole budget, up to 3000 ms. Sources still running at the cut continue asynchronously and update the assessment either way."""
    detail: AssessmentDetailTypedDict
    r"""One assessment's own facts: its score and recommendation, the signals behind them, the lanes still running and its timing. risk here is this assessment's own score; the account's current risk is the account member of the assessment. risk and recommendation are present for complete and partial; assessment_url is present for pending."""
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    first_decision: NotRequired[Decision]
    r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""
    matched_identifier: NotRequired[IdentifierMatchTypedDict]
    r"""Why this result matched a typed identifier search. value is the original value submitted in assessment_id. Provenance records a customer submission, not a source discovery or verified ownership. Equality is deterministic and has no inferred confidence score. An account result names its newest retained matching assessment, which can differ from latest."""
    matched_identifiers: NotRequired[List[IdentifierTermMatchTypedDict]]
    r"""Present only for identifier_expression. All satisfied unique terms, ordered by term_index, with original submitted values and retained assessment witnesses. A duplicate normalized term appears once at its first raw leaf index. The legacy single identifier filter instead returns matched_identifier."""


class AssessmentSearchItem(BaseModel):
    r"""One stored assessment revision, exactly as GET /v1/assessments/{assessment_id}/versions/{version} returns it, with the decision of the assessment's first answer. It is not re-scored and carries no current account risk."""

    id: str
    r"""This assessment's id, equal to detail.assessment_id."""

    status: Status
    r"""Processing state, separate from evidence coverage. complete: final; nothing is still running, but unsupported, failed or unanswered lanes remain in incomplete_sources. partial: a recommendation exists and evidence is incomplete; assessment_url identifies continuing work when present. pending: no recommendation yet; poll or wait for the webhook. Finished processing does not mean all sources answered."""

    flow: Flow
    r"""The event an assessment is made for: account_creation (a user creates an account), login (a user returns to an existing account) or purchase (a payment or a credit grant). The account's risk is reported with the decision for this flow."""

    depth: Depth
    r"""How long the synchronous answer waits for sources. quick waits only for the fast sources, those that answer within 500 ms of ingress (or deadline_ms when lower); full waits for the whole budget, up to 3000 ms. Sources still running at the cut continue asynchronously and update the assessment either way."""

    detail: AssessmentDetail
    r"""One assessment's own facts: its score and recommendation, the signals behind them, the lanes still running and its timing. risk here is this assessment's own score; the account's current risk is the account member of the assessment. risk and recommendation are present for complete and partial; assessment_url is present for pending."""

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"
    r"""Version of the body shape."""

    first_decision: Optional[Decision] = None
    r"""An assessment's own decision: block when its stored risk.block is true, otherwise its recommendation. It is not the account's decision or held-admission state."""

    matched_identifier: Optional[IdentifierMatch] = None
    r"""Why this result matched a typed identifier search. value is the original value submitted in assessment_id. Provenance records a customer submission, not a source discovery or verified ownership. Equality is deterministic and has no inferred confidence score. An account result names its newest retained matching assessment, which can differ from latest."""

    matched_identifiers: Optional[List[IdentifierTermMatch]] = None
    r"""Present only for identifier_expression. All satisfied unique terms, ordered by term_index, with original submitted values and retained assessment witnesses. A duplicate normalized term appears once at its first raw leaf index. The legacy single identifier filter instead returns matched_identifier."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            ["first_decision", "matched_identifier", "matched_identifiers"]
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
    AssessmentSearchItem.model_rebuild()
except NameError:
    pass
