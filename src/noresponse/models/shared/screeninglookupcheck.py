from __future__ import annotations
from .failurereason import FailureReason
from .identifiersearchkind import IdentifierSearchKind
from .lane import Lane
from .screeninglookupcheckstatus import ScreeningLookupCheckStatus
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningLookupCheckTypedDict(TypedDict):
    r"""What came of one lane of the lookups for one identifier."""

    identifier: IdentifierSearchKind
    lane: Lane
    r"""An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip."""
    status: ScreeningLookupCheckStatus
    r"""found: a source found the identifier. not_found: every source answered and none found it. partial: the sources that answered found nothing and the others did not answer. not_covered: no source answered. A lookup that failed reads partial or not_covered, not not_found."""
    sources: int
    r"""Sources asked: none when no source could be, as when the source is stopped or your workspace refuses it."""
    answered: int
    r"""Sources that gave a definite answer."""
    found: int
    r"""Sources that found the identifier."""
    reason: NotRequired[FailureReason]
    r"""Why a signal or source did not produce a definite found/not_found. timed_out means the source missed the request deadline; a continuation may still settle it. deferred means the (source, identifier) pair is async-only and was not attempted on the synchronous path; a continuation settles it."""


class ScreeningLookupCheck(BaseModel):
    r"""What came of one lane of the lookups for one identifier."""

    identifier: IdentifierSearchKind

    lane: Lane
    r"""An evidence lane: accounts (account presence for email and username), phone, breach, domain (the email domain's registration) and ip."""

    status: ScreeningLookupCheckStatus
    r"""found: a source found the identifier. not_found: every source answered and none found it. partial: the sources that answered found nothing and the others did not answer. not_covered: no source answered. A lookup that failed reads partial or not_covered, not not_found."""

    sources: int
    r"""Sources asked: none when no source could be, as when the source is stopped or your workspace refuses it."""

    answered: int
    r"""Sources that gave a definite answer."""

    found: int
    r"""Sources that found the identifier."""

    reason: Optional[FailureReason] = None
    r"""Why a signal or source did not produce a definite found/not_found. timed_out means the source missed the request deadline; a continuation may still settle it. deferred means the (source, identifier) pair is async-only and was not attempted on the synchronous path; a continuation settles it."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["reason"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
