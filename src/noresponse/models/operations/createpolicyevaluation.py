from __future__ import annotations
from noresponse.models.shared import (
    keyenvironment as shared_keyenvironment,
    policyevaluation as shared_policyevaluation,
    policyevaluationrequest as shared_policyevaluationrequest,
)
from noresponse.types import BaseModel
from noresponse.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Dict, List
from typing_extensions import Annotated, TypedDict


class CreatePolicyEvaluationRequestTypedDict(TypedDict):
    workspace_id: str
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""
    environment: shared_keyenvironment.KeyEnvironment
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""
    idempotency_key: str
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""
    body: shared_policyevaluationrequest.PolicyEvaluationRequestTypedDict


class CreatePolicyEvaluationRequest(BaseModel):
    workspace_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Your workspace id, as each key lists it in workspace_id. Another workspace, a malformed id and a test environment's id answer 404."""

    environment: Annotated[
        shared_keyenvironment.KeyEnvironment,
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The environment: live or test. Each has its own settings. Any other value answers 400. An API key reads and changes only its own environment's; the other answers 404."""

    idempotency_key: Annotated[
        str,
        pydantic.Field(alias="Idempotency-Key"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]
    r"""Opaque client key, 16 to 128 characters of [A-Za-z0-9._:-] (a UUID or ULID fits). Scoped to the workspace principal and bound to the canonical body for 24 hours."""

    body: Annotated[
        shared_policyevaluationrequest.PolicyEvaluationRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


class CreatePolicyEvaluationResponseTypedDict(TypedDict):
    headers: Dict[str, List[str]]
    result: shared_policyevaluation.PolicyEvaluationTypedDict


class CreatePolicyEvaluationResponse(BaseModel):
    headers: Dict[str, List[str]]

    result: shared_policyevaluation.PolicyEvaluation
