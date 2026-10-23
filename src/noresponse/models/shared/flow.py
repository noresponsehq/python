from __future__ import annotations
from typing import Literal


Flow = Literal[
    "signup",
    "login",
    "recovery",
    "profile_change",
]
r"""The provider flow the assessment gates. Use the top-level flow instead; this member is ignored when the top-level flow is present. Absent means signup."""
