from __future__ import annotations
from .auditsettingsenvironment import AuditSettingsEnvironment
from .handleplatform import HandlePlatform
from .screeningdepth import ScreeningDepth
from .screeningspend import ScreeningSpend, ScreeningSpendTypedDict
from .screeningstatus import ScreeningStatus
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ScreeningTypedDict(TypedDict):
    r"""A screening and its progress."""

    id: str
    group_id: str
    environment: AuditSettingsEnvironment
    status: ScreeningStatus
    r"""partial finished with some people or platforms not covered; people_failed and people_partial count them."""
    depth: ScreeningDepth
    platforms: List[HandlePlatform]
    requested_by: str
    created_at: str
    expires_at: str
    r"""A screening still running then fails with error_code expired."""
    people_total: int
    r"""People selected when the screening started."""
    people_done: int
    r"""People screened so far, failed ones included."""
    people_flagged: int
    people_failed: int
    people_partial: int
    r"""People screened with some requested platform not covered; their coverage names which."""
    estimated_spend: int
    r"""What the screening was estimated to cost when it started, in minor units of USD (cents): its people at its depth and platforms. Until the screening finishes, what it has not yet spent counts against the environment's screening_daily_cap."""
    spent: int
    r"""What the people it has screened recorded, in minor units of USD. Each counts toward the UTC day it was recorded on; a failed person records nothing."""
    spend: ScreeningSpendTypedDict
    r"""What screening cost, in US cents, in total and per implementation."""
    started_at: NotRequired[str]
    finished_at: NotRequired[str]
    error_code: NotRequired[str]
    r"""Why a failed or cancelled screening stopped."""


class Screening(BaseModel):
    r"""A screening and its progress."""

    id: str

    group_id: str

    environment: AuditSettingsEnvironment

    status: ScreeningStatus
    r"""partial finished with some people or platforms not covered; people_failed and people_partial count them."""

    depth: ScreeningDepth

    platforms: List[HandlePlatform]

    requested_by: str

    created_at: str

    expires_at: str
    r"""A screening still running then fails with error_code expired."""

    people_total: int
    r"""People selected when the screening started."""

    people_done: int
    r"""People screened so far, failed ones included."""

    people_flagged: int

    people_failed: int

    people_partial: int
    r"""People screened with some requested platform not covered; their coverage names which."""

    estimated_spend: int
    r"""What the screening was estimated to cost when it started, in minor units of USD (cents): its people at its depth and platforms. Until the screening finishes, what it has not yet spent counts against the environment's screening_daily_cap."""

    spent: int
    r"""What the people it has screened recorded, in minor units of USD. Each counts toward the UTC day it was recorded on; a failed person records nothing."""

    spend: ScreeningSpend
    r"""What screening cost, in US cents, in total and per implementation."""

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
