from __future__ import annotations
from .accountdecisionsbyflow import (
    AccountDecisionsByFlow,
    AccountDecisionsByFlowTypedDict,
)
from .accountrisk import AccountRisk, AccountRiskTypedDict
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class AccountTypedDict(TypedDict):
    r"""Body of the 200 answer to GET /v1/accounts/{account_id}: the one current risk of one of the calling tenant's accounts. It is the risk of the account's latest assessment that has a decision (status complete or partial), by created_at and then assessment_id, scored exactly as GET /v1/assessments/{assessment_id} scores that assessment, plus the account's own reason shared_api_key when a key issued to the account was used from many IP addresses or countries (POST /v1/key_usage/batches). Its assessments are the account's history (GET /v1/accounts/{account_id}/assessments)."""

    id: str
    r"""The account_id the tenant sends with its assessments."""
    risk: AccountRiskTypedDict
    decisions_by_flow: AccountDecisionsByFlowTypedDict
    r"""The decision for each flow. Every flow uses the tenant's signup thresholds today, so all three are equal."""
    assessment_id: str
    r"""The assessment the current risk comes from."""
    updated_at: str
    r"""updated_at of that assessment's latest revision."""
    schema_version: Literal["1"]
    r"""Version of the body shape."""


class Account(BaseModel):
    r"""Body of the 200 answer to GET /v1/accounts/{account_id}: the one current risk of one of the calling tenant's accounts. It is the risk of the account's latest assessment that has a decision (status complete or partial), by created_at and then assessment_id, scored exactly as GET /v1/assessments/{assessment_id} scores that assessment, plus the account's own reason shared_api_key when a key issued to the account was used from many IP addresses or countries (POST /v1/key_usage/batches). Its assessments are the account's history (GET /v1/accounts/{account_id}/assessments)."""

    id: str
    r"""The account_id the tenant sends with its assessments."""

    risk: AccountRisk

    decisions_by_flow: AccountDecisionsByFlow
    r"""The decision for each flow. Every flow uses the tenant's signup thresholds today, so all three are equal."""

    assessment_id: str
    r"""The assessment the current risk comes from."""

    updated_at: str
    r"""updated_at of that assessment's latest revision."""

    schema_version: Annotated[
        Annotated[Literal["1"], AfterValidator(validate_const("1"))],
        pydantic.Field(alias="schema_version"),
    ] = "1"
    r"""Version of the body shape."""


try:
    Account.model_rebuild()
except NameError:
    pass
