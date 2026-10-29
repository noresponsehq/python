from __future__ import annotations
from .listimpacttransitionfrom import ListImpactTransitionFrom
from noresponse.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class ListImpactTransitionTypedDict(TypedDict):
    from_: ListImpactTransitionFrom
    to: ListImpactTransitionFrom
    count: int


class ListImpactTransition(BaseModel):
    from_: Annotated[ListImpactTransitionFrom, pydantic.Field(alias="from")]

    to: ListImpactTransitionFrom

    count: int


try:
    ListImpactTransition.model_rebuild()
except NameError:
    pass
