import httpx
import json
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field


@dataclass(unsafe_hash=True)
class NoResponseError(Exception):
    """The base class for all HTTP error responses.

    When the body is an RFC 9457 problem document, status, type, title, detail,
    code, request_id and invalid_params read its members; a body that is not a
    problem document leaves them None. retry_after reads the Retry-After header.
    """

    message: str
    status_code: int
    body: str
    headers: httpx.Headers = field(hash=False)
    raw_response: httpx.Response = field(hash=False)

    def __init__(
        self, message: str, raw_response: httpx.Response, body: Optional[str] = None
    ):
        object.__setattr__(self, "message", message)
        object.__setattr__(self, "status_code", raw_response.status_code)
        object.__setattr__(
            self, "body", body if body is not None else raw_response.text
        )
        object.__setattr__(self, "headers", raw_response.headers)
        object.__setattr__(self, "raw_response", raw_response)

    def _problem(self) -> Dict[str, Any]:
        cached = self.__dict__.get("_problem_document")
        if cached is not None:
            return cached  # type: ignore[no-any-return]
        document: Dict[str, Any] = {}
        try:
            value = json.loads(self.body)
            if isinstance(value, dict):
                document = value
        except ValueError:
            pass
        object.__setattr__(self, "_problem_document", document)
        return document

    @property
    def status(self) -> int:
        """The HTTP status. Same value as status_code."""
        return self.status_code

    @property
    def type(self) -> Optional[str]:
        """The problem document's type URI."""
        value = self._problem().get("type")
        return value if isinstance(value, str) else None

    @property
    def title(self) -> Optional[str]:
        value = self._problem().get("title")
        return value if isinstance(value, str) else None

    @property
    def detail(self) -> Optional[str]:
        value = self._problem().get("detail")
        return value if isinstance(value, str) else None

    @property
    def code(self) -> Optional[str]:
        """The stable machine code, for example rate_limited. invalid_response for a 2xx the client could not read."""
        if self.status_code < 400:
            return "invalid_response"
        value = self._problem().get("code")
        return value if isinstance(value, str) else None

    @property
    def request_id(self) -> Optional[str]:
        """The X-Request-ID of the failed request, to quote when you contact support."""
        value = self._problem().get("request_id")
        return value if isinstance(value, str) else self.headers.get("x-request-id")

    @property
    def retry_after(self) -> Optional[int]:
        """Retry-After in whole seconds, or None when absent."""
        value = self.headers.get("retry-after")
        return int(value) if value is not None and value.strip().isdecimal() else None

    @property
    def invalid_params(self) -> Optional[List[Dict[str, Any]]]:
        """The offending fields of a 400, without their values."""
        value = self._problem().get("invalid_params")
        return value if isinstance(value, list) else None

    def __str__(self):
        text = self.title or self.detail
        if not text:
            return self.message
        summary = f"HTTP {self.status_code}"
        if self.code:
            summary += f" {self.code}"
        summary += f": {text}"
        if self.title and self.detail:
            summary += f". {self.detail}"
        if self.request_id:
            summary += f" (request {self.request_id})"
        return summary
