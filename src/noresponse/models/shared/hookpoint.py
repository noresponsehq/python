from __future__ import annotations
from typing import Literal


HookPoint = Literal[
    "pre_registration",
    "post_registration",
    "pre_login",
    "post_login",
    "token_issuance",
]
r"""The provider event a provider_hook context was sent for. pre_registration runs before the user exists, so subject and the request's account_id may be absent there. Sent only with transport provider_hook."""
