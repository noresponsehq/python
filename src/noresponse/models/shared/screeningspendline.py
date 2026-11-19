from __future__ import annotations
from .screeningspendlinerole import ScreeningSpendLineRole
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ScreeningSpendLineTypedDict(TypedDict):
    r"""What one implementation cost."""

    implementation: str
    r"""The resolver or collector that produced a record, by its catalogue name."""
    role: ScreeningSpendLineRole
    r"""What the implementation did. analyser appears only on spend recorded before the engine stopped analysing posts."""
    spend_minor: int


class ScreeningSpendLine(BaseModel):
    r"""What one implementation cost."""

    implementation: str
    r"""The resolver or collector that produced a record, by its catalogue name."""

    role: ScreeningSpendLineRole
    r"""What the implementation did. analyser appears only on spend recorded before the engine stopped analysing posts."""

    spend_minor: int
