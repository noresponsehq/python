from __future__ import annotations
from dataclasses import dataclass, field
import httpx
from noresponse.models.errors import NoResponseError
from noresponse.models.shared import (
    authenticationerrorcode as shared_authenticationerrorcode,
    probleminvalidparam as shared_probleminvalidparam,
)
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated


class AuthenticationErrorData(BaseModel):
    type: str
    title: str
    detail: str
    code: shared_authenticationerrorcode.AuthenticationErrorCode
    r"""Machine codes an HTTP 401 answer can carry."""
    request_id: str
    status: Annotated[
        Annotated[Literal[401], AfterValidator(validate_const(401))],
        pydantic.Field(alias="status"),
    ] = 401
    instance: Optional[str] = None
    invalid_params: Optional[List[shared_probleminvalidparam.ProblemInvalidParam]] = (
        None
    )


@dataclass(unsafe_hash=True)
class AuthenticationError(NoResponseError):
    r"""HTTP 401 problem document."""

    data: AuthenticationErrorData = field(hash=False)

    def __init__(
        self,
        data: AuthenticationErrorData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        object.__setattr__(self, "data", data)
