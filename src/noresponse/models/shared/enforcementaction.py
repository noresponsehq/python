from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


EnforcementAction = Union[
    Literal[
        "revoke_sessions",
        "restrict",
        "unrestrict",
        "fail_onboarding",
        "reject_activation",
        "none",
    ],
    UnrecognizedStr,
]
r"""What the workspace did in its identity provider: revoke_sessions (signed the account out everywhere), restrict (limited what the account can do), unrestrict (lifted an earlier restriction), fail_onboarding (stopped an account that was still onboarding), reject_activation (refused to activate a provisional account) or none (decided to take no action)."""
