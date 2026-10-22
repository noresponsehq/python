"""Response types the client returns. Hand-written; not generated.

Each is the generated model with a meta attribute that carries what the API said
in headers. meta is not part of the body: it is left out of model_dump() and
repr().
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, AsyncIterator, Callable, Iterator, List, Mapping, Optional, Sequence, Type, TypeVar

from pydantic import BaseModel, PrivateAttr

from .models.shared.assessment import Assessment as _Assessment
from .models.shared.assessmentoutcome import AssessmentOutcome as _AssessmentOutcome
from .models.shared.keyrotation import KeyRotation as _KeyRotation

__all__ = [
    "Assessment",
    "AssessmentOutcome",
    "AssessmentPage",
    "KeyRotation",
    "ResponseMeta",
]


def _header(headers: Mapping[str, Sequence[str]], name: str) -> Optional[str]:
    for key, values in headers.items():
        if key.lower() == name and values:
            return values[0]
    return None


@dataclass(frozen=True)
class ResponseMeta:
    """What the API said in the response headers."""

    request_id: Optional[str] = None
    """X-Request-ID, to quote when you contact support."""
    retry_after: Optional[int] = None
    """Retry-After in whole seconds, when the API sent one."""
    location: Optional[str] = None
    """The polling path of a pending assessment."""
    idempotent_replayed: bool = False
    """True when the answer replays an earlier request with the same idempotency_key."""
    headers: Mapping[str, Sequence[str]] = field(default_factory=dict, repr=False)
    """Every response header, lower-cased names to values."""

    @classmethod
    def from_headers(cls, headers: Mapping[str, Sequence[str]]) -> "ResponseMeta":
        retry_after = _header(headers, "retry-after")
        return cls(
            request_id=_header(headers, "x-request-id"),
            retry_after=int(retry_after) if retry_after is not None and retry_after.strip().isdecimal() else None,
            location=_header(headers, "location"),
            idempotent_replayed=(_header(headers, "idempotent-replayed") or "").lower() == "true",
            headers=dict(headers),
        )


_EMPTY = ResponseMeta()
M = TypeVar("M", bound=BaseModel)


def _attach(cls: Type[M], source: BaseModel, meta: ResponseMeta) -> M:
    """The source model as cls, validated already, with meta attached."""
    values = {name: getattr(source, name) for name in type(source).model_fields}
    out = cls.model_construct(_fields_set=set(source.model_fields_set), **values)
    out._meta = meta  # type: ignore[attr-defined]  # pylint: disable=protected-access
    return out


class Assessment(_Assessment):
    """An assessment: what to do about a signup, login or other event, and why."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        """Response headers. Empty on an assessment that came from a webhook or a page."""
        return self._meta


class AssessmentOutcome(_AssessmentOutcome):
    """The record of an outcome you reported."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta


class KeyRotation(_KeyRotation):
    """A new API key, shown once, and when the key that signed the request stops working."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta


def as_assessment(source: _Assessment, meta: ResponseMeta = _EMPTY) -> Assessment:
    return _attach(Assessment, source, meta)


def as_outcome(source: _AssessmentOutcome, meta: ResponseMeta) -> AssessmentOutcome:
    return _attach(AssessmentOutcome, source, meta)


def as_rotation(source: _KeyRotation, meta: ResponseMeta) -> KeyRotation:
    return _attach(KeyRotation, source, meta)


class AssessmentPage:
    """One page of an account's unexpired assessments, newest first.

    Iterate it to walk every item across every page, fetching pages as needed:
    ``for assessment in page`` or, from async code, ``async for assessment in
    page``. Call next_page() (next_page_async() in async code) to take one page
    at a time; it returns None after the last.
    """

    def __init__(
        self,
        *,
        account_id: str,
        items: List[Assessment],
        next_cursor: Optional[str],
        retention_days: Optional[int],
        meta: ResponseMeta,
        fetch: Callable[[str], Any],
    ) -> None:
        self.account_id = account_id
        self.items = items
        """The assessments on this page, each at its latest assessment_version."""
        self.next_cursor = next_cursor
        """Opaque; pass it back as cursor to continue from this page."""
        self.retention_days = retention_days
        self.meta = meta
        self._fetch = fetch

    @property
    def has_more(self) -> bool:
        """True when another page exists."""
        return bool(self.next_cursor)

    def next_page(self) -> Optional["AssessmentPage"]:
        """The next page, or None after the last."""
        if not self.next_cursor:
            return None
        page: "AssessmentPage" = self._fetch(self.next_cursor)
        return page

    async def next_page_async(self) -> Optional["AssessmentPage"]:
        """The next page, or None after the last. Use from async code."""
        if not self.next_cursor:
            return None
        page: "AssessmentPage" = await self._fetch(self.next_cursor)
        return page

    def __iter__(self) -> Iterator[Assessment]:
        page: Optional[AssessmentPage] = self
        while page is not None:
            yield from page.items
            page = page.next_page()

    async def __aiter__(self) -> AsyncIterator[Assessment]:
        page: Optional[AssessmentPage] = self
        while page is not None:
            for item in page.items:
                yield item
            page = await page.next_page_async()

    def __repr__(self) -> str:
        return f"AssessmentPage(account_id={self.account_id!r}, items={len(self.items)}, has_more={self.has_more})"
