from __future__ import annotations
from .accountbinding import AccountBinding, AccountBindingTypedDict
from .accountdecisionsnapshot import (
    AccountDecisionSnapshot,
    AccountDecisionSnapshotTypedDict,
)
from .accountoutcome import AccountOutcome, AccountOutcomeTypedDict
from .assessmentrevision import AssessmentRevision, AssessmentRevisionTypedDict
from .credentialassociation import CredentialAssociation, CredentialAssociationTypedDict
from .enforcement import Enforcement, EnforcementTypedDict
from .exportassessmentoutcome import (
    ExportAssessmentOutcome,
    ExportAssessmentOutcomeTypedDict,
)
from .requestdiagnostic import RequestDiagnostic, RequestDiagnosticTypedDict
from noresponse.types import BaseModel, UnrecognizedStr
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Union
from typing_extensions import Annotated, TypedDict


Exclusion = Union[
    Literal[
        "expired_or_erased_records",
        "secrets_and_credential_digests",
        "private_source_and_work_payloads",
        "cross_customer_data",
        "legacy_outcome_notes",
        "uncaptured_historical_decisions",
        "investigator_reviews_require_review_export",
    ],
    UnrecognizedStr,
]


class AccountExportTypedDict(TypedDict):
    r"""Retrieve one consistent snapshot of retained customer-accessible records, including assessment revisions, account decisions, feedback, key associations, enforcements and request diagnostics. Secrets, restricted source information, other customers' data and legacy free-text notes are excluded. The same standard/detailed permissions apply. An export exceeding 10000 records or 8 MiB returns export_too_large without a partial result. Historical decisions that were not captured are identified as an exclusion."""

    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""
    exported_at: str
    current_risk_version: int
    assessments: List[AssessmentRevisionTypedDict]
    decisions: List[AccountDecisionSnapshotTypedDict]
    outcomes: List[AccountOutcomeTypedDict]
    assessment_outcomes: List[ExportAssessmentOutcomeTypedDict]
    credentials: List[CredentialAssociationTypedDict]
    bindings: List[AccountBindingTypedDict]
    enforcements: List[EnforcementTypedDict]
    requests: List[RequestDiagnosticTypedDict]
    exclusions: List[Exclusion]
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    complete: Literal[True]


class AccountExport(BaseModel):
    r"""Retrieve one consistent snapshot of retained customer-accessible records, including assessment revisions, account decisions, feedback, key associations, enforcements and request diagnostics. Secrets, restricted source information, other customers' data and legacy free-text notes are excluded. The same standard/detailed permissions apply. An export exceeding 10000 records or 8 MiB returns export_too_large without a partial result. Historical decisions that were not captured are identified as an exclusion."""

    account_id: str
    r"""Your own opaque identifier for the account being checked, scoped to your workspace. Use an id you mint, with no direct identifier (email, phone, name or national id) in it. '|' is accepted so an Auth0 user id such as 'auth0|64abc' passes unchanged; '@', '+', '$' and whitespace are refused by the pattern, as is an exact-shape JWT; a hex digest such as a SHA-256 is allowed, because hashing an internal id is a common pseudonymous scheme. A value such as '07700900123' or 'jane.doe.gmail.com' cannot be told apart from an opaque id. It travels in bodies, and in a URL only as the path segment of GET /v1/accounts/{account_id}, its /assessments and its /linked_accounts. An assessment requested by a provider hook at pre_registration, which has no account yet, carries the server-issued account_id pre: followed by its assessment_id."""

    exported_at: str

    current_risk_version: int

    assessments: List[AssessmentRevision]

    decisions: List[AccountDecisionSnapshot]

    outcomes: List[AccountOutcome]

    assessment_outcomes: List[ExportAssessmentOutcome]

    credentials: List[CredentialAssociation]

    bindings: List[AccountBinding]

    enforcements: List[Enforcement]

    requests: List[RequestDiagnostic]

    exclusions: List[Exclusion]

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"
    r"""Version of the body shape."""

    complete: Annotated[
        Annotated[Literal[True], AfterValidator(validate_const(True))],
        pydantic.Field(alias="complete"),
    ] = True


try:
    AccountExport.model_rebuild()
except NameError:
    pass
