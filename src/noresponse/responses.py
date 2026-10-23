"""Response types the client returns. Hand-written; not generated.

Each is the generated model with a meta attribute that carries what the API said
in headers. meta is not part of the body: it is left out of model_dump() and
repr().
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, AsyncIterator, Callable, Iterator, List, Mapping, Optional, Sequence, Type, TypeVar

from pydantic import BaseModel, PrivateAttr

from .models.shared.account import Account as _Account
from .models.shared.accountdeletion import AccountDeletion as _AccountDeletion
from .models.shared.assessmentdeletion import AssessmentDeletion as _AssessmentDeletion
from .models.shared.assessment import Assessment as _Assessment
from .models.shared.assessmentdetail import AssessmentDetail
from .models.shared.assessmentoutcome import AssessmentOutcome as _AssessmentOutcome
from .models.shared.integration import Integration as _Integration
from .models.shared.integrationlist import IntegrationList as _IntegrationList
from .models.shared.keyrotation import KeyRotation as _KeyRotation

__all__ = [
    "Account",
    "AccountDeletion",
    "AssessmentDeletion",
    "Assessment",
    "AssessmentDetail",
    "AssessmentOutcome",
    "AssessmentPage",
    "Integration",
    "IntegrationList",
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
    """An assessment of a signup, login or purchase.

    account.risk.decision is what to do (allow, step_up, review or block); account
    is None while the account's first assessment is pending. detail holds this
    assessment's own facts: risk, recommendation, signals and assessment_version.
    """

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


class Account(_Account):
    """An account's one current risk: the risk of its latest assessment with a decision, and a decision per flow."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta


class AccountDeletion(_AccountDeletion):
    """An erased account: how many assessments the call deleted (0 on a repeat) and when."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta


class AssessmentDeletion(_AssessmentDeletion):
    """A deleted assessment, its account and the assessment the account's risk now comes from (None when none is left)."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta


class Integration(_Integration):
    """A hosted provider integration. secret is set only by create and rotate for Auth0, and shown once."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta


class IntegrationList(_IntegrationList):
    """Every integration of the account, oldest first, with no secrets."""

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


def as_account(source: _Account, meta: ResponseMeta) -> Account:
    return _attach(Account, source, meta)


def as_account_deletion(source: _AccountDeletion, meta: ResponseMeta) -> AccountDeletion:
    return _attach(AccountDeletion, source, meta)


def as_assessment_deletion(source: _AssessmentDeletion, meta: ResponseMeta) -> AssessmentDeletion:
    return _attach(AssessmentDeletion, source, meta)


def as_integration(source: _Integration, meta: ResponseMeta) -> Integration:
    return _attach(Integration, source, meta)


def as_integration_list(source: _IntegrationList, meta: ResponseMeta) -> IntegrationList:
    return _attach(IntegrationList, source, meta)


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
        items: List[AssessmentDetail],
        next_cursor: Optional[str],
        retention_days: Optional[int],
        meta: ResponseMeta,
        fetch: Callable[[str], Any],
    ) -> None:
        self.account_id = account_id
        self.items = items
        """The assessment details on this page, each at its latest assessment_version."""
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

    def __iter__(self) -> Iterator[AssessmentDetail]:
        page: Optional[AssessmentPage] = self
        while page is not None:
            yield from page.items
            page = page.next_page()

    async def __aiter__(self) -> AsyncIterator[AssessmentDetail]:
        page: Optional[AssessmentPage] = self
        while page is not None:
            for item in page.items:
                yield item
            page = await page.next_page_async()

    def __repr__(self) -> str:
        return f"AssessmentPage(account_id={self.account_id!r}, items={len(self.items)}, has_more={self.has_more})"
