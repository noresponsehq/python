from __future__ import annotations
from typing import Literal


Environment = Literal[
    "live",
    "test",
]
r"""The environment whose endpoints receive this event: live, or test for the workspace's test environment."""
