from __future__ import annotations
from .investigationstatus import InvestigationStatus
from .matchstate import MatchState
from .screeningcoverage import ScreeningCoverage, ScreeningCoverageTypedDict
from .screeningdepth import ScreeningDepth
from .screeningspend import ScreeningSpend, ScreeningSpendTypedDict
from noresponse.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class InvestigationTypedDict(TypedDict):
    coverage: ScreeningCoverageTypedDict
    r"""The denominator of a screening: accounts found, how many could be read, items read and the period they span, so a clean result is distinct from a person nobody could see."""
    spend: ScreeningSpendTypedDict
    r"""What screening cost, in US cents, in total and per implementation."""
    id: str
    person_id: str
    group_id: Nullable[str]
    status: InvestigationStatus
    depth: ScreeningDepth
    platforms: List[str]
    match_state: Nullable[MatchState]
    created_at: str
    expires_at: str
    deadline_at: str
    error_code: NotRequired[str]
    started_at: NotRequired[str]
    finished_at: NotRequired[str]


class Investigation(BaseModel):
    coverage: ScreeningCoverage
    r"""The denominator of a screening: accounts found, how many could be read, items read and the period they span, so a clean result is distinct from a person nobody could see."""

    spend: ScreeningSpend
    r"""What screening cost, in US cents, in total and per implementation."""

    id: str

    person_id: str

    group_id: Nullable[str]

    status: InvestigationStatus

    depth: ScreeningDepth

    platforms: List[str]

    match_state: Nullable[MatchState]

    created_at: str

    expires_at: str

    deadline_at: str

    error_code: Optional[str] = None

    started_at: Optional[str] = None

    finished_at: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["error_code", "started_at", "finished_at"])
        nullable_fields = set(["group_id", "match_state"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))
            is_nullable_and_explicitly_set = (
                k in nullable_fields
                and (self.__pydantic_fields_set__.intersection({n}))  # pylint: disable=no-member
            )

            if val != UNSET_SENTINEL:
                if (
                    val is not None
                    or k not in optional_fields
                    or is_nullable_and_explicitly_set
                ):
                    m[k] = val

        return m
