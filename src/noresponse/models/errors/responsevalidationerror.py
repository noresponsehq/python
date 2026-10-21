import httpx
from typing import Optional
from dataclasses import dataclass

from noresponse.models.errors import APIError


@dataclass(unsafe_hash=True)
class ResponseValidationError(APIError):
    """Error raised when there is a type mismatch between the response data and the expected Pydantic model."""

    def __init__(
        self,
        message: str,
        raw_response: httpx.Response,
        cause: Exception,
        body: Optional[str] = None,
    ):
        message = f"{message}: {cause}"
        super().__init__(message, raw_response, body)

    @property
    def cause(self):
        """Normally the Pydantic ValidationError"""
        return self.__cause__

    @property
    def code(self) -> Optional[str]:
        """Always invalid_response: the body did not match the contract."""
        return "invalid_response"
