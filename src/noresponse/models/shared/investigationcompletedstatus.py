from __future__ import annotations
from typing import Literal


InvestigationCompletedStatus = Literal[
    "completed",
    "partial",
    "failed",
    "cancelled",
]
