from __future__ import annotations
from .screeningspendlinerole import ScreeningSpendLineRole
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ScreeningSpendLineTypedDict(TypedDict):
    r"""What one implementation cost."""

    implementation: str
    r"""The resolver, collector or analyser that produced a record, by its catalogue name."""
    role: ScreeningSpendLineRole
    spend_minor: int


class ScreeningSpendLine(BaseModel):
    r"""What one implementation cost."""

    implementation: str
    r"""The resolver, collector or analyser that produced a record, by its catalogue name."""

    role: ScreeningSpendLineRole

    spend_minor: int
