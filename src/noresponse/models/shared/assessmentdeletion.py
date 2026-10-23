from __future__ import annotations
from .assessmentdeletionaccount import (
    AssessmentDeletionAccount,
    AssessmentDeletionAccountTypedDict,
)
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class AssessmentDeletionTypedDict(TypedDict):
    r"""Body of the 200 answer to DELETE /v1/assessments/{assessment_id}: one of the calling tenant's assessments was deleted, with its versions, evidence, outcomes and the identity-graph marks its outcomes set. Afterwards GET /v1/assessments/{assessment_id} answers 404 and the assessment leaves the account's history. The account is scored again from what remains: account.current_assessment_id names the assessment GET /v1/accounts/{account_id} now serves its risk from, and is absent when the account has no assessment with a decision left. Deleting an assessment that is already gone answers 404."""

    id: str
    r"""The assessment that was deleted."""
    account: AssessmentDeletionAccountTypedDict
    deleted_at: str
    r"""When the deletion took effect."""
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    deleted: Literal[True]


class AssessmentDeletion(BaseModel):
    r"""Body of the 200 answer to DELETE /v1/assessments/{assessment_id}: one of the calling tenant's assessments was deleted, with its versions, evidence, outcomes and the identity-graph marks its outcomes set. Afterwards GET /v1/assessments/{assessment_id} answers 404 and the assessment leaves the account's history. The account is scored again from what remains: account.current_assessment_id names the assessment GET /v1/accounts/{account_id} now serves its risk from, and is absent when the account has no assessment with a decision left. Deleting an assessment that is already gone answers 404."""

    id: str
    r"""The assessment that was deleted."""

    account: AssessmentDeletionAccount

    deleted_at: str
    r"""When the deletion took effect."""

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"
    r"""Version of the body shape."""

    deleted: Annotated[
        Annotated[Literal[True], AfterValidator(validate_const(True))],
        pydantic.Field(alias="deleted"),
    ] = True


try:
    AssessmentDeletion.model_rebuild()
except NameError:
    pass
