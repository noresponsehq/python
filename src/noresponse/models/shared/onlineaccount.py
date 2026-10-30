from __future__ import annotations
from .accounttype import AccountType
from .failurereason import FailureReason
from .identifier import Identifier
from .signaloutcome import SignalOutcome
from noresponse.types import BaseModel, UNSET_SENTINEL, UnrecognizedStr
from pydantic import model_serializer
from typing import List, Literal, Optional, Union
from typing_extensions import NotRequired, TypedDict


SignIn = Union[
    Literal[
        "password",
        "google",
        "facebook",
        "apple",
        "microsoft",
        "sso",
        "other",
    ],
    UnrecognizedStr,
]


class OnlineAccountTypedDict(TypedDict):
    r"""One online-account search of the signup's email or username, detailed view only. name and domain name the platform searched, not a provider. outcome is the search's signal outcome: found, not_found, or a failure (blocked, unavailable, inconclusive) with its reason; a failure is not reported as not_found. The members after reason are what the platform returned beside an account it found, each absent when it did not say."""

    name: str
    r"""The platform's name, such as Adobe or GitHub."""
    domain: str
    r"""The platform's domain, lower case: the host its logo is fetched for."""
    identifier: Identifier
    outcome: SignalOutcome
    r"""Per-signal outcome. A source that timed out, was blocked or errored reports blocked, unavailable or inconclusive with a reason and is listed in incomplete_sources; not_found is a definite absence."""
    reason: NotRequired[FailureReason]
    r"""Why a signal or source did not produce a definite found/not_found. timed_out means the source missed the request deadline; a continuation may still settle it. deferred means the (source, identifier) pair is async-only and was not attempted on the synchronous path; a continuation settles it."""
    sign_in: NotRequired[List[SignIn]]
    r"""How the account signs in, as the platform reports it, sorted: a password, a Google, Facebook, Apple or Microsoft account, the organisation's single sign-on, or another method."""
    email_verified: NotRequired[bool]
    r"""Whether the platform says the account's email is verified."""
    blocked: NotRequired[bool]
    r"""Whether the platform says the account is blocked or suspended."""
    account_type: NotRequired[AccountType]
    r"""personal, or business: an account a company or school manages."""
    has_avatar: NotRequired[bool]
    r"""Whether the account has its own profile picture rather than the platform's default. The picture is not returned."""
    first_name_prefix: NotRequired[str]
    r"""The first letters of the account holder's first name, as the platform shows them (Life360 shows two and hides the rest). It is evidence only: it does not change the score or the consistency results."""


class OnlineAccount(BaseModel):
    r"""One online-account search of the signup's email or username, detailed view only. name and domain name the platform searched, not a provider. outcome is the search's signal outcome: found, not_found, or a failure (blocked, unavailable, inconclusive) with its reason; a failure is not reported as not_found. The members after reason are what the platform returned beside an account it found, each absent when it did not say."""

    name: str
    r"""The platform's name, such as Adobe or GitHub."""

    domain: str
    r"""The platform's domain, lower case: the host its logo is fetched for."""

    identifier: Identifier

    outcome: SignalOutcome
    r"""Per-signal outcome. A source that timed out, was blocked or errored reports blocked, unavailable or inconclusive with a reason and is listed in incomplete_sources; not_found is a definite absence."""

    reason: Optional[FailureReason] = None
    r"""Why a signal or source did not produce a definite found/not_found. timed_out means the source missed the request deadline; a continuation may still settle it. deferred means the (source, identifier) pair is async-only and was not attempted on the synchronous path; a continuation settles it."""

    sign_in: Optional[List[SignIn]] = None
    r"""How the account signs in, as the platform reports it, sorted: a password, a Google, Facebook, Apple or Microsoft account, the organisation's single sign-on, or another method."""

    email_verified: Optional[bool] = None
    r"""Whether the platform says the account's email is verified."""

    blocked: Optional[bool] = None
    r"""Whether the platform says the account is blocked or suspended."""

    account_type: Optional[AccountType] = None
    r"""personal, or business: an account a company or school manages."""

    has_avatar: Optional[bool] = None
    r"""Whether the account has its own profile picture rather than the platform's default. The picture is not returned."""

    first_name_prefix: Optional[str] = None
    r"""The first letters of the account holder's first name, as the platform shows them (Life360 shows two and hides the rest). It is evidence only: it does not change the score or the consistency results."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(
            [
                "reason",
                "sign_in",
                "email_verified",
                "blocked",
                "account_type",
                "has_avatar",
                "first_name_prefix",
            ]
        )
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
