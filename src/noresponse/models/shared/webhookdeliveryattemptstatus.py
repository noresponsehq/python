from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


WebhookDeliveryAttemptStatus = Union[
    Literal[
        "delivered",
        "failed",
    ],
    UnrecognizedStr,
]
r"""delivered when the endpoint answered 2xx; failed otherwise, with failure naming why."""
