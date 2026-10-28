from __future__ import annotations
from typing import Literal


Decision = Literal[
    "allow",
    "step_up",
    "review",
    "block",
]
r"""The decision of the assessment's latest stored revision: block when its stored risk.block is true, otherwise its recommendation. This is not the account's current decision or held-admission state. Combined with recommendation using AND."""
