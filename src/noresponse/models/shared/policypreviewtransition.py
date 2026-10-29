from __future__ import annotations
from .from_ import From
from noresponse.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class PolicyPreviewTransitionTypedDict(TypedDict):
    from_: From
    to: From
    count: int


class PolicyPreviewTransition(BaseModel):
    from_: Annotated[From, pydantic.Field(alias="from")]

    to: From

    count: int


try:
    PolicyPreviewTransition.model_rebuild()
except NameError:
    pass
