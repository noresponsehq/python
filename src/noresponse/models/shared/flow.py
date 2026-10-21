from __future__ import annotations
from typing import Literal


Flow = Literal[
    "signup",
    "login",
    "recovery",
    "profile_change",
]
r"""The provider flow the assessment gates. Absent means signup."""
