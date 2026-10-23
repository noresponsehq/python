from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class AccountDeletionTypedDict(TypedDict):
    r"""Body of the 200 answer to DELETE /v1/accounts/{account_id}: the calling tenant's account was erased in the environment of the calling key. Every assessment of the account went, with its revisions, evidence, outcomes and the identity-graph marks its outcomes set, and an assessment that was still running when the call arrived is stopped. Afterwards GET /v1/accounts/{account_id} and GET /v1/assessments/{assessment_id} of each erased assessment answer 404, and the history page is empty. The call is idempotent: a repeat, or an account with nothing to erase, answers 200 with assessments_deleted 0. The account_id can be assessed again later, as a new account."""

    id: str
    r"""The account_id that was erased."""
    assessments_deleted: int
    r"""How many assessments this call deleted. 0 when the account had none left, so a repeat answers 0."""
    deleted_at: str
    r"""When the erasure took effect. An assessment of the account begun before this time is refused or stopped."""
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    deleted: Literal[True]


class AccountDeletion(BaseModel):
    r"""Body of the 200 answer to DELETE /v1/accounts/{account_id}: the calling tenant's account was erased in the environment of the calling key. Every assessment of the account went, with its revisions, evidence, outcomes and the identity-graph marks its outcomes set, and an assessment that was still running when the call arrived is stopped. Afterwards GET /v1/accounts/{account_id} and GET /v1/assessments/{assessment_id} of each erased assessment answer 404, and the history page is empty. The call is idempotent: a repeat, or an account with nothing to erase, answers 200 with assessments_deleted 0. The account_id can be assessed again later, as a new account."""

    id: str
    r"""The account_id that was erased."""

    assessments_deleted: int
    r"""How many assessments this call deleted. 0 when the account had none left, so a repeat answers 0."""

    deleted_at: str
    r"""When the erasure took effect. An assessment of the account begun before this time is refused or stopped."""

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
    AccountDeletion.model_rebuild()
except NameError:
    pass
