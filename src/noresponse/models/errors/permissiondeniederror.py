from __future__ import annotations
from dataclasses import dataclass, field
import httpx
from noresponse.models.errors import APIError
from noresponse.models.shared import (
    permissiondeniederrorcode as shared_permissiondeniederrorcode,
    probleminvalidparam as shared_probleminvalidparam,
)
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Optional
from typing_extensions import Annotated


class PermissionDeniedErrorData(BaseModel):
    type: str
    title: str
    detail: str
    code: shared_permissiondeniederrorcode.PermissionDeniedErrorCode
    r"""Machine codes an HTTP 403 answer can carry."""
    request_id: str
    status: Annotated[
        Annotated[Literal[403], AfterValidator(validate_const(403))],
        pydantic.Field(alias="status"),
    ] = 403
    instance: Optional[str] = None
    invalid_params: Optional[List[shared_probleminvalidparam.ProblemInvalidParam]] = (
        None
    )


@dataclass(unsafe_hash=True)
class PermissionDeniedError(APIError):
    r"""HTTP 403 problem document."""

    data: PermissionDeniedErrorData = field(hash=False)

    def __init__(
        self,
        data: PermissionDeniedErrorData,
        raw_response: httpx.Response,
        body: Optional[str] = None,
    ):
        message = body or raw_response.text
        super().__init__(message, raw_response, body)
        object.__setattr__(self, "data", data)
