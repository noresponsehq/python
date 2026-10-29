from __future__ import annotations
from .conclusion import Conclusion
from noresponse.types import BaseModel
from typing_extensions import TypedDict


class ReviewResolveRequestTypedDict(TypedDict):
    expected_version: int
    expected_risk_version: int
    conclusion: Conclusion
    note: str


class ReviewResolveRequest(BaseModel):
    expected_version: int

    expected_risk_version: int

    conclusion: Conclusion

    note: str
