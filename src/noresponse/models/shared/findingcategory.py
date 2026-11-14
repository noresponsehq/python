from __future__ import annotations
from noresponse.types import UnrecognizedStr
from typing import Literal, Union


FindingCategory = Union[
    Literal[
        "direct_threat",
        "harm_intent",
        "fixation",
        "grievance",
        "security_research",
        "weapons",
        "disruption",
        "violent_extremism",
        "harassment",
        "movement_exposure",
    ],
    UnrecognizedStr,
]
r"""What a finding is about: a direct threat to the principal or the group, intent to harm without a named target, fixation on the principal, a grievance against the host, research into the venue, route or security, weapons tied to any of these, disruption or protest planning toward this group, violent extremist content or identification, prior harassment or stalking of staff or principals, or posting the principal's addresses or movements."""
