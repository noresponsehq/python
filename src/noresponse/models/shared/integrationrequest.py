from __future__ import annotations
from .integrationhookpoint import IntegrationHookPoint
from .integrationplatform import IntegrationPlatform
from noresponse.types import BaseModel, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class IntegrationRequestTypedDict(TypedDict):
    r"""POST /v1/integrations body. Registers a hosted endpoint for one authentication provider. The tenant is the API key that signs the request, so the body has no tenant field and refuses one like any other unknown member. A WorkOS integration needs signing_secret, the Actions secret shown in the WorkOS dashboard, which NoResponse uses to verify each Action request and to sign its answer. An Auth0 integration sends no signing_secret: NoResponse generates the shared secret and returns it once."""

    platform: IntegrationPlatform
    r"""The authentication provider that calls the endpoint."""
    hook_points: NotRequired[List[IntegrationHookPoint]]
    r"""The provider events the endpoint scores. Default both: pre_registration (WorkOS user registration Action, Auth0 pre-user-registration trigger) and post_login (WorkOS authentication Action, Auth0 post-login trigger). An event that is not listed is answered allow without an assessment."""
    signing_secret: NotRequired[str]
    r"""The WorkOS Actions signing secret, as the WorkOS dashboard shows it: 16 to 256 printable ASCII characters with no spaces. It is stored sealed and is not returned."""


class IntegrationRequest(BaseModel):
    r"""POST /v1/integrations body. Registers a hosted endpoint for one authentication provider. The tenant is the API key that signs the request, so the body has no tenant field and refuses one like any other unknown member. A WorkOS integration needs signing_secret, the Actions secret shown in the WorkOS dashboard, which NoResponse uses to verify each Action request and to sign its answer. An Auth0 integration sends no signing_secret: NoResponse generates the shared secret and returns it once."""

    platform: IntegrationPlatform
    r"""The authentication provider that calls the endpoint."""

    hook_points: Optional[List[IntegrationHookPoint]] = None
    r"""The provider events the endpoint scores. Default both: pre_registration (WorkOS user registration Action, Auth0 pre-user-registration trigger) and post_login (WorkOS authentication Action, Auth0 post-login trigger). An event that is not listed is answered allow without an assessment."""

    signing_secret: Optional[str] = None
    r"""The WorkOS Actions signing secret, as the WorkOS dashboard shows it: 16 to 256 printable ASCII characters with no spaces. It is stored sealed and is not returned."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = set(["hook_points", "signing_secret"])
        serialized = handler(self)
        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k, serialized.get(n))

            if val != UNSET_SENTINEL:
                if val is not None or k not in optional_fields:
                    m[k] = val

        return m
