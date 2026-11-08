from __future__ import annotations
from typing import Literal


ScreeningCompletedStatus = Literal[
    "completed",
    "partial",
    "failed",
]
r"""completed reached every attendee; partial left some not fully covered (partial_coverage); failed covered nobody."""
