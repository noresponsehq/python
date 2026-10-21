from __future__ import annotations
from typing import Literal


Platform = Literal[
    "web",
    "ios",
    "android",
    "other",
]
r"""Client platform. Closed vocabulary keeps integrations stable."""
