from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


EnforcementState = Union[
    Literal[
        "onboarding",
        "provisional",
        "active",
        "restricted",
        "rejected",
    ],
    UnrecognizedStr,
]
r"""The account's state in the workspace's identity provider just before the action: onboarding, provisional (created, not yet activated), active, restricted or rejected."""
