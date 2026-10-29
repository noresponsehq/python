from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UserActorTypedDict(TypedDict):
    external_user_id: str
    r"""The user's id at the identity provider the console signs people in with: 1 to 256 printable ASCII characters with no space, compared exactly."""
    console_credential_id: str
    r"""The public id of the console credential the user acted through."""
    type: Literal["user"]
    principal_id: NotRequired[str]
    r"""Stable workspace principal id, retained across identity-provider subject migration. Absent for older events."""


class UserActor(BaseModel):
    external_user_id: str
    r"""The user's id at the identity provider the console signs people in with: 1 to 256 printable ASCII characters with no space, compared exactly."""

    console_credential_id: str
    r"""The public id of the console credential the user acted through."""

    type: Annotated[
        Annotated[Literal["user"], AfterValidator(validate_const("user"))],
        pydantic.Field(alias="type"),
    ] = "user"

    principal_id: Optional[str] = None
    r"""Stable workspace principal id, retained across identity-provider subject migration. Absent for older events."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["principal_id"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m


try:
    UserActor.model_rebuild()
except NameError:
    pass
