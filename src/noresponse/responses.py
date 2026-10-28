"""Response types the client returns. Hand-written; not generated.

Each is the generated model with a meta attribute that carries what the API said
in headers. meta is not part of the body: it is left out of model_dump() and
repr().
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass, field
from typing import Any, AsyncIterator, Callable, Iterator, List, Mapping, Optional, Sequence, Type, TypeVar

from pydantic import BaseModel, PrivateAttr

from .models import shared as _shared

from .models.shared.account import Account as _Account
from .models.shared.accountdeletion import AccountDeletion as _AccountDeletion
from .models.shared.accountlist import AccountList as _AccountList
from .models.shared.assessmentdeletion import AssessmentDeletion as _AssessmentDeletion
from .models.shared.assessment import Assessment as _Assessment
from .models.shared.assessmentdetail import AssessmentDetail
from .models.shared.assessmentoutcome import AssessmentOutcome as _AssessmentOutcome
from .models.shared.enforcement import Enforcement as _Enforcement
from .models.shared.integration import Integration as _Integration
from .models.shared.integrationlist import IntegrationList as _IntegrationList
from .models.shared.key import Key as _Key
from .models.shared.keylist import KeyList as _KeyList
from .models.shared.keyrotation import KeyRotation as _KeyRotation
from .models.shared.keyusagebatch import KeyUsageBatch as _KeyUsageBatch
from .models.shared.settings import Settings as _Settings

__all__ = [
    "AssessmentSearchPage",
    "AssessmentRevision",
    "AccountBinding",
    "AccountOutcome",
    "AccountOutcomePage",
    "AccountDecisionSnapshot",
    "CredentialAssociation",
    "CredentialPage",
    "AccountExport",
    "RequestDiagnosticPage",
    "Account",
    "AccountDeletion",
    "AccountList",
    "AssessmentDeletion",
    "Assessment",
    "AssessmentDetail",
    "AssessmentOutcome",
    "AssessmentPage",
    "Enforcement",
    "Integration",
    "IntegrationList",
    "Key",
    "KeyList",
    "KeyRotation",
    "KeyUsageBatch",
    "ResponseMeta",
    "Settings",
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


class _WithMeta(BaseModel):
    """Response metadata is private state, never an extra wire member."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta


class AssessmentSearchPage(_WithMeta, _shared.AssessmentSearchPage):
    """The validated AssessmentSearchPage response with HTTP metadata."""


def as_assessment_search_page(source: _shared.AssessmentSearchPage, meta: ResponseMeta) -> AssessmentSearchPage:
    return _attach(AssessmentSearchPage, source, meta)


class AssessmentRevision(_WithMeta, _shared.AssessmentRevision):
    """The validated AssessmentRevision response with HTTP metadata."""


def as_assessment_revision(source: _shared.AssessmentRevision, meta: ResponseMeta) -> AssessmentRevision:
    return _attach(AssessmentRevision, source, meta)


class AccountBinding(_WithMeta, _shared.AccountBinding):
    """The validated AccountBinding response with HTTP metadata."""


def as_account_binding(source: _shared.AccountBinding, meta: ResponseMeta) -> AccountBinding:
    return _attach(AccountBinding, source, meta)


class AccountOutcome(_WithMeta, _shared.AccountOutcome):
    """The validated AccountOutcome response with HTTP metadata."""


def as_account_outcome(source: _shared.AccountOutcome, meta: ResponseMeta) -> AccountOutcome:
    return _attach(AccountOutcome, source, meta)


class AccountOutcomePage(_WithMeta, _shared.AccountOutcomePage):
    """The validated AccountOutcomePage response with HTTP metadata."""


def as_account_outcome_page(source: _shared.AccountOutcomePage, meta: ResponseMeta) -> AccountOutcomePage:
    return _attach(AccountOutcomePage, source, meta)


class AccountDecisionSnapshot(_WithMeta, _shared.AccountDecisionSnapshot):
    """The validated AccountDecisionSnapshot response with HTTP metadata."""


def as_account_decision_snapshot(source: _shared.AccountDecisionSnapshot, meta: ResponseMeta) -> AccountDecisionSnapshot:
    return _attach(AccountDecisionSnapshot, source, meta)


class CredentialAssociation(_WithMeta, _shared.CredentialAssociation):
    """The validated CredentialAssociation response with HTTP metadata."""


def as_credential_association(source: _shared.CredentialAssociation, meta: ResponseMeta) -> CredentialAssociation:
    return _attach(CredentialAssociation, source, meta)


class CredentialPage(_WithMeta, _shared.CredentialPage):
    """The validated CredentialPage response with HTTP metadata."""


def as_credential_page(source: _shared.CredentialPage, meta: ResponseMeta) -> CredentialPage:
    return _attach(CredentialPage, source, meta)


class AccountExport(_WithMeta, _shared.AccountExport):
    """The validated AccountExport response with HTTP metadata."""


def as_account_export(source: _shared.AccountExport, meta: ResponseMeta) -> AccountExport:
    return _attach(AccountExport, source, meta)


class RequestDiagnosticPage(_WithMeta, _shared.RequestDiagnosticPage):
    """The validated RequestDiagnosticPage response with HTTP metadata."""


def as_request_diagnostic_page(source: _shared.RequestDiagnosticPage, meta: ResponseMeta) -> RequestDiagnosticPage:
    return _attach(RequestDiagnosticPage, source, meta)


class Assessment(_Assessment):
    """An assessment of an account creation, login or purchase.

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


class KeyUsageBatch(_KeyUsageBatch):
    """A recorded key usage batch: its id and how many events were accepted and ignored."""

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


class _Enveloped(BaseModel):
    """A model with meta that still answers headers, and in each subclass
    result, as the response envelope did that accounts.list_changed and
    accounts.record_enforcement returned before 8.1. Code written for the
    envelope keeps running; read the model and its meta instead."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta

    @property
    def headers(self) -> Mapping[str, Sequence[str]]:
        """Deprecated: meta.headers. Removed in 9.0."""
        warnings.warn("headers moved to meta.headers", DeprecationWarning, stacklevel=2)
        return self._meta.headers


class AccountList(_Enveloped, _AccountList):
    """One page of the accounts whose risk changed. Pass next_cursor back as changed_since."""

    @property
    def result(self) -> "AccountList":
        """Deprecated: the page itself. Removed in 9.0."""
        warnings.warn("list_changed returns the AccountList now; read it directly", DeprecationWarning, stacklevel=2)
        return self


class Enforcement(_Enveloped, _Enforcement):
    """The record of what you did to an account in your auth provider."""

    @property
    def result(self) -> "Enforcement":
        """Deprecated: the record itself. Removed in 9.0."""
        warnings.warn("record_enforcement returns the Enforcement now; read it directly", DeprecationWarning, stacklevel=2)
        return self


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


class Key(_Key):
    """One API key. key, the secret, is set only by keys.create, and shown once."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta


class KeyList(_KeyList):
    """The keys of the signing key's environment, newest first, with no secrets."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta


class Settings(_Settings):
    """The settings of one environment."""

    _meta: ResponseMeta = PrivateAttr(default=_EMPTY)

    @property
    def meta(self) -> ResponseMeta:
        return self._meta


def as_key(source: _Key, meta: ResponseMeta) -> Key:
    return _attach(Key, source, meta)


def as_key_list(source: _KeyList, meta: ResponseMeta) -> KeyList:
    return _attach(KeyList, source, meta)


def as_settings(source: _Settings, meta: ResponseMeta) -> Settings:
    return _attach(Settings, source, meta)


def as_assessment(source: _Assessment, meta: ResponseMeta = _EMPTY) -> Assessment:
    return _attach(Assessment, source, meta)


def as_outcome(source: _AssessmentOutcome, meta: ResponseMeta) -> AssessmentOutcome:
    return _attach(AssessmentOutcome, source, meta)


def as_key_usage_batch(source: _KeyUsageBatch, meta: ResponseMeta) -> KeyUsageBatch:
    return _attach(KeyUsageBatch, source, meta)


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


def as_account_list(source: _AccountList, meta: ResponseMeta) -> AccountList:
    return _attach(AccountList, source, meta)


def as_enforcement(source: _Enforcement, meta: ResponseMeta) -> Enforcement:
    return _attach(Enforcement, source, meta)
