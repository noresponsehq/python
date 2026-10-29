from __future__ import annotations
from .conclusion import Conclusion
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ResolutionTypedDict(TypedDict):
    review_version: int
    risk_version: int
    assessment_version: int
    assessment_id: str
    conclusion: Conclusion
    note: str
    created_by: str
    created_at: str


class Resolution(BaseModel):
    review_version: int

    risk_version: int

    assessment_version: int

    assessment_id: str

    conclusion: Conclusion

    note: str

    created_by: str

    created_at: str
