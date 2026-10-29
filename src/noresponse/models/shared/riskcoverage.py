from __future__ import annotations
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class RiskCoverageTypedDict(TypedDict):
    r"""Counts of planned source-identifier pairs by evidence outcome, deduplicated across signals and incomplete entries. These counts do not measure identity agreement or prove that processing is still running. A lane that was not searched is not an answered source."""

    answered: int
    r"""Source-identifier pairs that gave a definite found or not_found answer."""
    failed: int
    r"""Source-identifier pairs that could not answer, including unsupported coverage markers and source failures. Read detailed signals to distinguish Not covered from Failed."""
    pending: int
    r"""Source-identifier pairs with deferred or timed_out evidence. A terminal timeout can remain here after processing finishes; use assessment status and continuation metadata to determine whether work is still running."""


class RiskCoverage(BaseModel):
    r"""Counts of planned source-identifier pairs by evidence outcome, deduplicated across signals and incomplete entries. These counts do not measure identity agreement or prove that processing is still running. A lane that was not searched is not an answered source."""

    answered: int
    r"""Source-identifier pairs that gave a definite found or not_found answer."""

    failed: int
    r"""Source-identifier pairs that could not answer, including unsupported coverage markers and source failures. Read detailed signals to distinguish Not covered from Failed."""

    pending: int
    r"""Source-identifier pairs with deferred or timed_out evidence. A terminal timeout can remain here after processing finishes; use assessment status and continuation metadata to determine whether work is still running."""
