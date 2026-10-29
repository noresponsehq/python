from __future__ import annotations
from .auditsettingsenvironment import AuditSettingsEnvironment
from noresponse.types import BaseModel, UNSET_SENTINEL
from noresponse.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AuditSettingsTypedDict(TypedDict):
    r"""Read audit retention and available history."""

    environment: AuditSettingsEnvironment
    retention_days: int
    oldest_available_at: NotRequired[str]
    capture: Literal["available_events_only"]


class AuditSettings(BaseModel):
    r"""Read audit retention and available history."""

    environment: AuditSettingsEnvironment

    retention_days: int

    oldest_available_at: Optional[str] = None

    capture: Annotated[
        Annotated[
            Literal["available_events_only"],
            AfterValidator(validate_const("available_events_only")),
        ],
        pydantic.Field(alias="capture"),
    ] = "available_events_only"

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["oldest_available_at"])
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
    AuditSettings.model_rebuild()
except NameError:
    pass
