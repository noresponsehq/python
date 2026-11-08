from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


Metric = Union[
    Literal[
        "assessments",
        "webhook_deliveries",
        "key_usage_events",
        "screenings",
    ],
    UnrecognizedStr,
]
r"""assessments: assessments admitted. webhook_deliveries: events sent to endpoints, one per event per endpoint. key_usage_events: key-usage events accepted. screenings: attendees a screening recorded a final result for, one per attendee per screening; a failed attendee counts nothing."""
