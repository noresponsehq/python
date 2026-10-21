from __future__ import annotations
from dataclasses import dataclass, field
import httpx
from noresponse.models.errors import APIError
from noresponse.models.shared import (
    notfounderrorcode as shared_notfounderrorcode,
    probleminvalidparam as shared_probleminvalidparam,
)
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated


class NotFoundErrorData(BaseModel):
    type: str
    title: str
    detail: str
    code: shared_notfounderrorcode.NotFoundErrorCode
    r"""Machine codes an HTTP 404 answer can carry."""
    request_id: str
    status: Annotated[
        Annotated[Literal[404], AfterValidator(validate_const(404))],
        pydantic.Field(alias="status"),
    ] = 404
    instance: Optional[str] = None
    invalid_params: Optional[List[shared_probleminvalidparam.ProblemInvalidParam]] = (
        None
    )


@dataclass(unsafe_hash=True)
class NotFoundError(APIError):
    r"""HTTP 404 problem document."""

    data: NotFoundErrorData = field(hash=False)

    def __init__(
        self,
        data: NotFoundErrorData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        object.__setattr__(self, "data", data)
