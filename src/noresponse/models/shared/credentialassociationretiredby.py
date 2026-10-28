from __future__ import annotations
from noresponse.types import BaseModel
from noresponse.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class CredentialAssociationRetiredByTypedDict(TypedDict):
    key_id: str
    type: Literal["api_key"]


class CredentialAssociationRetiredBy(BaseModel):
    key_id: str

    type: Annotated[
        Annotated[Literal["api_key"], AfterValidator(validate_const("api_key"))],
        pydantic.Field(alias="type"),
    ] = "api_key"


try:
    CredentialAssociationRetiredBy.model_rebuild()
except NameError:
    pass
