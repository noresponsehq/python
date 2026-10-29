from __future__ import annotations
from .assessmentdetail import AssessmentDetail, AssessmentDetailTypedDict
from .depth import Depth
from .flow import Flow
from .status import Status
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class AssessmentRevisionTypedDict(TypedDict):
    r"""Retrieve a retained assessment version with its original decision, policy, flow and depth. This response excludes the current account decision. Current retention and response-mode permissions still apply."""

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


class AssessmentRevision(BaseModel):
    r"""Retrieve a retained assessment version with its original decision, policy, flow and depth. This response excludes the current account decision. Current retention and response-mode permissions still apply."""

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


try:
    AssessmentRevision.model_rebuild()
except NameError:
    pass
