from __future__ import annotations
from typing import Literal


ScopeEnum = Literal[
    "assessment",
    "account",
]
r"""assessment requires one submission to satisfy the complete expression. account permits witnesses across retained submissions of one account and is supported only by POST /v1/accounts/search. No default: select scope explicitly."""
