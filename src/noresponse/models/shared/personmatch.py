from __future__ import annotations
from noresponse.types import BaseModel, UnrecognizedStr
from typing import List, Literal, Union
from typing_extensions import TypedDict


PersonMatchMatchedOn = Union[
    Literal[
        "email",
        "phone",
    ],
    UnrecognizedStr,
]


class PersonMatchTypedDict(TypedDict):
    person_id: str
    matched_on: List[PersonMatchMatchedOn]


class PersonMatch(BaseModel):
    person_id: str

    matched_on: List[PersonMatchMatchedOn]
