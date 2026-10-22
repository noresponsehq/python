from __future__ import annotations
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class IntegrationRotationRequestTypedDict(TypedDict):
    r"""POST /v1/integrations/{integration_id}/rotate body. For an Auth0 integration send {}: NoResponse generates a new shared secret and returns it once. For a WorkOS integration send the new signing_secret after regenerating it in the WorkOS dashboard. Either way the previous secret is still accepted for 24 hours, so the provider can be switched over without a refused call."""

    signing_secret: NotRequired[str]
    r"""The WorkOS Actions signing secret, as the WorkOS dashboard shows it: 16 to 256 printable ASCII characters with no spaces. It is stored sealed and is not returned."""


class IntegrationRotationRequest(BaseModel):
    r"""POST /v1/integrations/{integration_id}/rotate body. For an Auth0 integration send {}: NoResponse generates a new shared secret and returns it once. For a WorkOS integration send the new signing_secret after regenerating it in the WorkOS dashboard. Either way the previous secret is still accepted for 24 hours, so the provider can be switched over without a refused call."""

    signing_secret: Optional[str] = None
    r"""The WorkOS Actions signing secret, as the WorkOS dashboard shows it: 16 to 256 printable ASCII characters with no spaces. It is stored sealed and is not returned."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["signing_secret"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
