from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


WebhookTestRequestEvent = Union[
    Literal[
        "endpoint.verification",
        "assessment.updated",
    ],
    UnrecognizedStr,
]
r"""endpoint.verification sends a fresh challenge now, in this call, and the endpoint is verified if it echoes it. assessment.updated queues an event whose data is a fixed example assessment, with test true, delivered and retried like any other; the endpoint must be verified."""
