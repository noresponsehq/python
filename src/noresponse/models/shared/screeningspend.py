from __future__ import annotations
from .screeningspendline import ScreeningSpendLine, ScreeningSpendLineTypedDict
from noresponse.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ScreeningSpendTypedDict(TypedDict):
    r"""What screening cost, in US cents, in total and per implementation."""

    total_minor: int
    r"""The total, in US cents."""
    by_implementation: List[ScreeningSpendLineTypedDict]


class ScreeningSpend(BaseModel):
    r"""What screening cost, in US cents, in total and per implementation."""

    total_minor: int
    r"""The total, in US cents."""

    by_implementation: List[ScreeningSpendLine]
