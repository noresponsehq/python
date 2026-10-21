from __future__ import annotations
from typing import Literal


ResponseMode = Literal[
    "standard",
    "detailed",
]
r"""standard returns the consolidated risk response; detailed adds merged provider-neutral facts when the key has detailed scope. There is no raw mode."""
