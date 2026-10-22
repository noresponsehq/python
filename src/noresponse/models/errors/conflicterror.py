from __future__ import annotations
from dataclasses import dataclass, field
import httpx
from noresponse.models.errors import NoResponseError
from noresponse.models.shared import (
    conflicterrorcode as shared_conflicterrorcode,
    probleminvalidparam as shared_probleminvalidparam,
)
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated


class ConflictErrorData(BaseModel):
    type: str
    title: str
    detail: str
    code: shared_conflicterrorcode.ConflictErrorCode
    r"""Machine codes an HTTP 409 answer can carry."""
    request_id: str
    status: Annotated[
        Annotated[Literal[409], AfterValidator(validate_const(409))],
        pydantic.Field(alias="status"),
    ] = 409
    instance: Optional[str] = None
    invalid_params: Optional[List[shared_probleminvalidparam.ProblemInvalidParam]] = (
        None
    )


@dataclass(unsafe_hash=True)
class ConflictError(NoResponseError):
    r"""HTTP 409 problem document."""

    data: ConflictErrorData = field(hash=False)

    def __init__(
        self,
        data: ConflictErrorData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        object.__setattr__(self, "data", data)
