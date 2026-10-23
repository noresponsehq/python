from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Outcome = Union[
    Literal[
        "confirmed_abuse",
        "account_takeover",
        "chargeback",
        "false_positive",
        "legitimate",
        "unknown",
    ],
    UnrecognizedStr,
]
r"""What the provider later learned about the assessed account. confirmed_abuse, account_takeover and chargeback report abuse; false_positive and legitimate withdraw an earlier abuse report of this workspace for the assessment; unknown is recorded only. Outcomes are append-only and the latest one recorded for an assessment wins."""
