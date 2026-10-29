from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AccountDeletionTypedDict(TypedDict):
    r"""Body of the 200 answer to DELETE /v1/accounts/{account_id}: the calling workspace's account was erased in the environment of the calling key. Every assessment of the account went, with its revisions, evidence, outcomes and the identity-graph marks its outcomes set, and an assessment that was still running when the call arrived is stopped. Afterwards GET /v1/accounts/{account_id} and GET /v1/assessments/{assessment_id} of each erased assessment answer 404, and the history page is empty. The call is idempotent: a repeat, or an account with nothing to erase, answers 200 with assessments_deleted 0. The account_id can be assessed again later, as a new account."""

    id: str
    r"""The account_id that was erased."""
    assessments_deleted: int
    r"""How many assessments this call deleted. 0 when the account had none left, so a repeat answers 0."""
    deleted_at: str
    r"""When the erasure took effect. An assessment of the account begun before this time is refused or stopped."""
    schema_version: Literal["1"]
    r"""Version of the body shape."""
    deleted: Literal[True]
    erasure_id: NotRequired[str]
    r"""Receipt for GET /v1/erasures/{erasure_id}, when durable storage issued one."""


class AccountDeletion(BaseModel):
    r"""Body of the 200 answer to DELETE /v1/accounts/{account_id}: the calling workspace's account was erased in the environment of the calling key. Every assessment of the account went, with its revisions, evidence, outcomes and the identity-graph marks its outcomes set, and an assessment that was still running when the call arrived is stopped. Afterwards GET /v1/accounts/{account_id} and GET /v1/assessments/{assessment_id} of each erased assessment answer 404, and the history page is empty. The call is idempotent: a repeat, or an account with nothing to erase, answers 200 with assessments_deleted 0. The account_id can be assessed again later, as a new account."""

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
    AccountDeletion.model_rebuild()
except NameError:
    pass
