from __future__ import annotations
from dataclasses import dataclass, field
import httpx
from noresponse.models.errors import APIError
from noresponse.models.shared import (
    probleminvalidparam as shared_probleminvalidparam,
    ratelimiterrorcode as shared_ratelimiterrorcode,
)
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated


class RateLimitErrorData(BaseModel):
    type: str
    title: str
    detail: str
    code: shared_ratelimiterrorcode.RateLimitErrorCode
    r"""Machine codes an HTTP 429 answer can carry."""
    request_id: str
    status: Annotated[
        Annotated[Literal[429], AfterValidator(validate_const(429))],
        pydantic.Field(alias="status"),
    ] = 429
    instance: Optional[str] = None
    invalid_params: Optional[List[shared_probleminvalidparam.ProblemInvalidParam]] = (
        None
    )


@dataclass(unsafe_hash=True)
class RateLimitError(APIError):
    r"""HTTP 429 problem document."""

    data: RateLimitErrorData = field(hash=False)

    def __init__(
        self,
        data: RateLimitErrorData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        object.__setattr__(self, "data", data)
