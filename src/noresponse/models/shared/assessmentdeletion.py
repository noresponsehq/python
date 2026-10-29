from __future__ import annotations
from .assessmentdeletionaccount import (
    AssessmentDeletionAccount,
    AssessmentDeletionAccountTypedDict,
)
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssessmentDeletionTypedDict(TypedDict):
    r"""Body of the 200 answer to DELETE /v1/assessments/{assessment_id}: one of the calling workspace's assessments was deleted, with its versions, evidence, outcomes and the identity-graph marks its outcomes set. Afterwards GET /v1/assessments/{assessment_id} answers 404 and the assessment leaves the account's history. The account is scored again from what remains: account.current_assessment_id names the assessment GET /v1/accounts/{account_id} now serves its risk from, and is absent when the account has no assessment with a decision left. Deleting an assessment that is already gone answers 404."""

    id: str
    r"""The assessment that was deleted."""
    account: AssessmentDeletionAccountTypedDict
    deleted_at: str
    r"""When the deletion took effect."""
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    deleted: Literal[True]
    erasure_id: NotRequired[str]
    r"""Receipt for GET /v1/erasures/{erasure_id}, when durable storage issued one."""


class AssessmentDeletion(BaseModel):
    r"""Body of the 200 answer to DELETE /v1/assessments/{assessment_id}: one of the calling workspace's assessments was deleted, with its versions, evidence, outcomes and the identity-graph marks its outcomes set. Afterwards GET /v1/assessments/{assessment_id} answers 404 and the assessment leaves the account's history. The account is scored again from what remains: account.current_assessment_id names the assessment GET /v1/accounts/{account_id} now serves its risk from, and is absent when the account has no assessment with a decision left. Deleting an assessment that is already gone answers 404."""

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

    erasure_id: Optional[str] = None
    r"""Receipt for GET /v1/erasures/{erasure_id}, when durable storage issued one."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["erasure_id"])
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
    AssessmentDeletion.model_rebuild()
except NameError:
    pass
