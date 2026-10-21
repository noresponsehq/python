from __future__ import annotations
from typing import Literal


Transport = Literal[
    "backend",
    "browser",
]
r"""Where the customer derived this context. Backend is the trusted integration path; browser values are treated as weak hints."""
