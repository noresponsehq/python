from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class RiskCoverageTypedDict(TypedDict):
    r"""Sources counted by state, not named."""

    answered: int
    r"""Sources that gave a definite answer."""
    failed: int
    r"""Sources that could not answer."""
    pending: int
    r"""Sources still being asked."""


class RiskCoverage(BaseModel):
    r"""Sources counted by state, not named."""

    answered: int
    r"""Sources that gave a definite answer."""

    failed: int
    r"""Sources that could not answer."""

    pending: int
    r"""Sources still being asked."""
