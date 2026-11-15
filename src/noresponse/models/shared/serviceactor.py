from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class ServiceActorTypedDict(TypedDict):
    name: str
    r"""The NoResponse service that made the change with no person acting, such as replenisher, which replaces dead platform sessions in NoResponse's own workspace."""
    type: Literal["service"]


class ServiceActor(BaseModel):
    name: str
    r"""The NoResponse service that made the change with no person acting, such as replenisher, which replaces dead platform sessions in NoResponse's own workspace."""

    type: Annotated[
        Annotated[Literal["service"], AfterValidator(validate_const("service"))],
        pydantic.Field(alias="type"),
    ] = "service"


try:
    ServiceActor.model_rebuild()
except NameError:
    pass
