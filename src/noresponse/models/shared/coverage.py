from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class CoverageTypedDict(TypedDict):
    r"""Counts only; a zero denominator means no eligible retained records and does not imply a zero rate."""

    numerator: int
    denominator: int


class Coverage(BaseModel):
    r"""Counts only; a zero denominator means no eligible retained records and does not imply a zero rate."""

    numerator: int

    denominator: int
