from __future__ import annotations
from dataclasses import dataclass, field
import httpx
from noresponse.models.errors import NoResponseError
from noresponse.models.shared import (
    badrequesterrorcode as shared_badrequesterrorcode,
    probleminvalidparam as shared_probleminvalidparam,
)
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated


class BadRequestErrorData(BaseModel):
    type: str
    title: str
    detail: str
    code: shared_badrequesterrorcode.BadRequestErrorCode
    r"""Machine codes an HTTP 400 answer can carry."""
    request_id: str
    status: Annotated[
        Annotated[Literal[400], AfterValidator(validate_const(400))],
        pydantic.Field(alias="status"),
    ] = 400
    instance: Optional[str] = None
    invalid_params: Optional[List[shared_probleminvalidparam.ProblemInvalidParam]] = (
        None
    )


@dataclass(unsafe_hash=True)
class BadRequestError(NoResponseError):
    r"""HTTP 400 problem document."""

    data: BadRequestErrorData = field(hash=False)

    def __init__(
        self,
        data: BadRequestErrorData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        object.__setattr__(self, "data", data)
