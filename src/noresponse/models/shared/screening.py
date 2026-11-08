from __future__ import annotations
from .auditsettingsenvironment import AuditSettingsEnvironment
from .screeningdepth import ScreeningDepth
from .screeningstatus import ScreeningStatus
from noresponse.types import BaseModel, UNSET_SENTINEL, UnrecognizedStr
from pydantic import model_serializer
from typing import List, Literal, Optional, Union
from typing_extensions import NotRequired, TypedDict


ScreeningPlatform = Union[
    Literal[
        "instagram",
        "x",
        "bluesky",
        "youtube",
        "tiktok",
        "facebook",
        "threads",
        "reddit",
        "telegram",
        "linkedin",
    ],
    UnrecognizedStr,
]


class ScreeningTypedDict(TypedDict):
    r"""A screening and its progress."""

    id: str
    event_id: str
    environment: AuditSettingsEnvironment
    status: ScreeningStatus
    r"""partial finished with some attendees not covered; attendees_failed counts them."""
    depth: ScreeningDepth
    platforms: List[ScreeningPlatform]
    requested_by: str
    created_at: str
    expires_at: str
    r"""A screening still running then fails with error_code expired."""
    attendees_total: int
    r"""Attendees selected when the screening started."""
    attendees_done: int
    r"""Attendees screened so far, failed ones included."""
    attendees_flagged: int
    attendees_failed: int
    started_at: NotRequired[str]
    finished_at: NotRequired[str]
    error_code: NotRequired[str]
    r"""Why a failed or cancelled screening stopped."""


class Screening(BaseModel):
    r"""A screening and its progress."""

    id: str

    event_id: str

    environment: AuditSettingsEnvironment

    status: ScreeningStatus
    r"""partial finished with some attendees not covered; attendees_failed counts them."""

    depth: ScreeningDepth

    platforms: List[ScreeningPlatform]

    requested_by: str

    created_at: str

    expires_at: str
    r"""A screening still running then fails with error_code expired."""

    attendees_total: int
    r"""Attendees selected when the screening started."""

    attendees_done: int
    r"""Attendees screened so far, failed ones included."""

    attendees_flagged: int

    attendees_failed: int

    started_at: Optional[str] = None

    finished_at: Optional[str] = None

    error_code: Optional[str] = None
    r"""Why a failed or cancelled screening stopped."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["started_at", "finished_at", "error_code"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
