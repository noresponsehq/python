from typing import Any, TYPE_CHECKING

from noresponse.utils.dynamic_imports import lazy_getattr, lazy_dir

if TYPE_CHECKING:
    from .createassessment import (
        CreateAssessmentRequest,
        CreateAssessmentRequestTypedDict,
        CreateAssessmentResponse,
        CreateAssessmentResponseTypedDict,
    )
    from .createintegration import (
        CreateIntegrationResponse,
        CreateIntegrationResponseTypedDict,
    )
    from .createwebhookendpoint import (
        CreateWebhookEndpointResponse,
        CreateWebhookEndpointResponseTypedDict,
    )
    from .deleteintegration import (
        DeleteIntegrationRequest,
        DeleteIntegrationRequestTypedDict,
        DeleteIntegrationResponse,
        DeleteIntegrationResponseTypedDict,
    )
    from .deletewebhookendpoint import (
        DeleteWebhookEndpointRequest,
        DeleteWebhookEndpointRequestTypedDict,
        DeleteWebhookEndpointResponse,
        DeleteWebhookEndpointResponseTypedDict,
    )
    from .getassessment import (
        GetAssessmentRequest,
        GetAssessmentRequestTypedDict,
        GetAssessmentResponse,
        GetAssessmentResponseTypedDict,
    )
    from .listintegrations import (
        ListIntegrationsResponse,
        ListIntegrationsResponseTypedDict,
    )
    from .listwebhookendpoints import (
        ListWebhookEndpointsResponse,
        ListWebhookEndpointsResponseTypedDict,
    )
    from .queryaccountassessments import (
        QueryAccountAssessmentsResponse,
        QueryAccountAssessmentsResponseTypedDict,
    )
    from .recordassessmentoutcome import (
        RecordAssessmentOutcomeRequest,
        RecordAssessmentOutcomeRequestTypedDict,
        RecordAssessmentOutcomeResponse,
        RecordAssessmentOutcomeResponseTypedDict,
    )
    from .rotateapikey import RotateAPIKeyResponse, RotateAPIKeyResponseTypedDict
    from .rotateintegrationsecret import (
        RotateIntegrationSecretRequest,
        RotateIntegrationSecretRequestTypedDict,
        RotateIntegrationSecretResponse,
        RotateIntegrationSecretResponseTypedDict,
    )
    from .rotatewebhooksigningkey import (
        RotateWebhookSigningKeyRequest,
        RotateWebhookSigningKeyRequestTypedDict,
        RotateWebhookSigningKeyResponse,
        RotateWebhookSigningKeyResponseTypedDict,
    )
    from .sendwebhooktestevent import (
        SendWebhookTestEventRequest,
        SendWebhookTestEventRequestTypedDict,
        SendWebhookTestEventResponse,
        SendWebhookTestEventResponseTypedDict,
    )

__all__ = [
    "CreateAssessmentRequest",
    "CreateAssessmentRequestTypedDict",
    "CreateAssessmentResponse",
    "CreateAssessmentResponseTypedDict",
    "CreateIntegrationResponse",
    "CreateIntegrationResponseTypedDict",
    "CreateWebhookEndpointResponse",
    "CreateWebhookEndpointResponseTypedDict",
    "DeleteIntegrationRequest",
    "DeleteIntegrationRequestTypedDict",
    "DeleteIntegrationResponse",
    "DeleteIntegrationResponseTypedDict",
    "DeleteWebhookEndpointRequest",
    "DeleteWebhookEndpointRequestTypedDict",
    "DeleteWebhookEndpointResponse",
    "DeleteWebhookEndpointResponseTypedDict",
    "GetAssessmentRequest",
    "GetAssessmentRequestTypedDict",
    "GetAssessmentResponse",
    "GetAssessmentResponseTypedDict",
    "ListIntegrationsResponse",
    "ListIntegrationsResponseTypedDict",
    "ListWebhookEndpointsResponse",
    "ListWebhookEndpointsResponseTypedDict",
    "QueryAccountAssessmentsResponse",
    "QueryAccountAssessmentsResponseTypedDict",
    "RecordAssessmentOutcomeRequest",
    "RecordAssessmentOutcomeRequestTypedDict",
    "RecordAssessmentOutcomeResponse",
    "RecordAssessmentOutcomeResponseTypedDict",
    "RotateAPIKeyResponse",
    "RotateAPIKeyResponseTypedDict",
    "RotateIntegrationSecretRequest",
    "RotateIntegrationSecretRequestTypedDict",
    "RotateIntegrationSecretResponse",
    "RotateIntegrationSecretResponseTypedDict",
    "RotateWebhookSigningKeyRequest",
    "RotateWebhookSigningKeyRequestTypedDict",
    "RotateWebhookSigningKeyResponse",
    "RotateWebhookSigningKeyResponseTypedDict",
    "SendWebhookTestEventRequest",
    "SendWebhookTestEventRequestTypedDict",
    "SendWebhookTestEventResponse",
    "SendWebhookTestEventResponseTypedDict",
]

_dynamic_imports: dict[str, str] = {
    "CreateAssessmentRequest": ".createassessment",
    "CreateAssessmentRequestTypedDict": ".createassessment",
    "CreateAssessmentResponse": ".createassessment",
    "CreateAssessmentResponseTypedDict": ".createassessment",
    "CreateIntegrationResponse": ".createintegration",
    "CreateIntegrationResponseTypedDict": ".createintegration",
    "CreateWebhookEndpointResponse": ".createwebhookendpoint",
    "CreateWebhookEndpointResponseTypedDict": ".createwebhookendpoint",
    "DeleteIntegrationRequest": ".deleteintegration",
    "DeleteIntegrationRequestTypedDict": ".deleteintegration",
    "DeleteIntegrationResponse": ".deleteintegration",
    "DeleteIntegrationResponseTypedDict": ".deleteintegration",
    "DeleteWebhookEndpointRequest": ".deletewebhookendpoint",
    "DeleteWebhookEndpointRequestTypedDict": ".deletewebhookendpoint",
    "DeleteWebhookEndpointResponse": ".deletewebhookendpoint",
    "DeleteWebhookEndpointResponseTypedDict": ".deletewebhookendpoint",
    "GetAssessmentRequest": ".getassessment",
    "GetAssessmentRequestTypedDict": ".getassessment",
    "GetAssessmentResponse": ".getassessment",
    "GetAssessmentResponseTypedDict": ".getassessment",
    "ListIntegrationsResponse": ".listintegrations",
    "ListIntegrationsResponseTypedDict": ".listintegrations",
    "ListWebhookEndpointsResponse": ".listwebhookendpoints",
    "ListWebhookEndpointsResponseTypedDict": ".listwebhookendpoints",
    "QueryAccountAssessmentsResponse": ".queryaccountassessments",
    "QueryAccountAssessmentsResponseTypedDict": ".queryaccountassessments",
    "RecordAssessmentOutcomeRequest": ".recordassessmentoutcome",
    "RecordAssessmentOutcomeRequestTypedDict": ".recordassessmentoutcome",
    "RecordAssessmentOutcomeResponse": ".recordassessmentoutcome",
    "RecordAssessmentOutcomeResponseTypedDict": ".recordassessmentoutcome",
    "RotateAPIKeyResponse": ".rotateapikey",
    "RotateAPIKeyResponseTypedDict": ".rotateapikey",
    "RotateIntegrationSecretRequest": ".rotateintegrationsecret",
    "RotateIntegrationSecretRequestTypedDict": ".rotateintegrationsecret",
    "RotateIntegrationSecretResponse": ".rotateintegrationsecret",
    "RotateIntegrationSecretResponseTypedDict": ".rotateintegrationsecret",
    "RotateWebhookSigningKeyRequest": ".rotatewebhooksigningkey",
    "RotateWebhookSigningKeyRequestTypedDict": ".rotatewebhooksigningkey",
    "RotateWebhookSigningKeyResponse": ".rotatewebhooksigningkey",
    "RotateWebhookSigningKeyResponseTypedDict": ".rotatewebhooksigningkey",
    "SendWebhookTestEventRequest": ".sendwebhooktestevent",
    "SendWebhookTestEventRequestTypedDict": ".sendwebhooktestevent",
    "SendWebhookTestEventResponse": ".sendwebhooktestevent",
    "SendWebhookTestEventResponseTypedDict": ".sendwebhooktestevent",
}


def __getattr__(attr_name: str) -> Any:
    return lazy_getattr(
        attr_name, package=__package__, dynamic_imports=_dynamic_imports
    )


def __dir__():
    return lazy_dir(dynamic_imports=_dynamic_imports)
