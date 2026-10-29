from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class KeyActorTypedDict(TypedDict):
    key_id: str
    r"""The public id of the workspace API key that made the change."""
    type: Literal["api_key"]


class KeyActor(BaseModel):
    key_id: str
    r"""The public id of the workspace API key that made the change."""

    type: Annotated[
        Annotated[Literal["api_key"], AfterValidator(validate_const("api_key"))],
        pydantic.Field(alias="type"),
    ] = "api_key"


try:
    KeyActor.model_rebuild()
except NameError:
    pass
