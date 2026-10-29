from __future__ import annotations
from typing import Literal


ListMatch = Literal[
    "allow",
    "block",
    "none",
]
r"""The list action captured at the first answer. Requires revision first. Older answers without captured list state do not match, including none."""
