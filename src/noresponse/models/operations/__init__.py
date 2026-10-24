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
    from .deleteaccount import (
        DeleteAccountRequest,
        DeleteAccountRequestTypedDict,
        DeleteAccountResponse,
        DeleteAccountResponseTypedDict,
    )
    from .deleteassessment import (
        DeleteAssessmentRequest,
        DeleteAssessmentRequestTypedDict,
        DeleteAssessmentResponse,
        DeleteAssessmentResponseTypedDict,
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
    from .getaccount import (
        GetAccountRequest,
        GetAccountRequestTypedDict,
        GetAccountResponse,
        GetAccountResponseTypedDict,
    )
    from .getassessment import (
        GetAssessmentRequest,
        GetAssessmentRequestTypedDict,
        GetAssessmentResponse,
        GetAssessmentResponseTypedDict,
    )
    from .listaccountassessments import (
        ListAccountAssessmentsRequest,
        ListAccountAssessmentsRequestTypedDict,
        ListAccountAssessmentsResponse,
        ListAccountAssessmentsResponseTypedDict,
    )
    from .listaccounts import (
        ListAccountsRequest,
        ListAccountsRequestTypedDict,
        ListAccountsResponse,
        ListAccountsResponseTypedDict,
    )
    from .listintegrations import (
        ListIntegrationsResponse,
        ListIntegrationsResponseTypedDict,
    )
    from .listwebhookdeliveries import (
        ListWebhookDeliveriesRequest,
        ListWebhookDeliveriesRequestTypedDict,
        ListWebhookDeliveriesResponse,
        ListWebhookDeliveriesResponseTypedDict,
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
    from .recordenforcement import (
        RecordEnforcementRequest,
        RecordEnforcementRequestTypedDict,
        RecordEnforcementResponse,
        RecordEnforcementResponseTypedDict,
    )
    from .recordkeyusage import (
        RecordKeyUsageRequest,
        RecordKeyUsageRequestTypedDict,
        RecordKeyUsageResponse,
        RecordKeyUsageResponseTypedDict,
    )
    from .replaywebhookdelivery import (
        ReplayWebhookDeliveryRequest,
        ReplayWebhookDeliveryRequestTypedDict,
        ReplayWebhookDeliveryResponse,
        ReplayWebhookDeliveryResponseTypedDict,
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
    "DeleteAccountRequest",
    "DeleteAccountRequestTypedDict",
    "DeleteAccountResponse",
    "DeleteAccountResponseTypedDict",
    "DeleteAssessmentRequest",
    "DeleteAssessmentRequestTypedDict",
    "DeleteAssessmentResponse",
    "DeleteAssessmentResponseTypedDict",
    "DeleteIntegrationRequest",
    "DeleteIntegrationRequestTypedDict",
    "DeleteIntegrationResponse",
    "DeleteIntegrationResponseTypedDict",
    "DeleteWebhookEndpointRequest",
    "DeleteWebhookEndpointRequestTypedDict",
    "DeleteWebhookEndpointResponse",
    "DeleteWebhookEndpointResponseTypedDict",
    "GetAccountRequest",
    "GetAccountRequestTypedDict",
    "GetAccountResponse",
    "GetAccountResponseTypedDict",
    "GetAssessmentRequest",
    "GetAssessmentRequestTypedDict",
    "GetAssessmentResponse",
    "GetAssessmentResponseTypedDict",
    "ListAccountAssessmentsRequest",
    "ListAccountAssessmentsRequestTypedDict",
    "ListAccountAssessmentsResponse",
    "ListAccountAssessmentsResponseTypedDict",
    "ListAccountsRequest",
    "ListAccountsRequestTypedDict",
    "ListAccountsResponse",
    "ListAccountsResponseTypedDict",
    "ListIntegrationsResponse",
    "ListIntegrationsResponseTypedDict",
    "ListWebhookDeliveriesRequest",
    "ListWebhookDeliveriesRequestTypedDict",
    "ListWebhookDeliveriesResponse",
    "ListWebhookDeliveriesResponseTypedDict",
    "ListWebhookEndpointsResponse",
    "ListWebhookEndpointsResponseTypedDict",
    "QueryAccountAssessmentsResponse",
    "QueryAccountAssessmentsResponseTypedDict",
    "RecordAssessmentOutcomeRequest",
    "RecordAssessmentOutcomeRequestTypedDict",
    "RecordAssessmentOutcomeResponse",
    "RecordAssessmentOutcomeResponseTypedDict",
    "RecordEnforcementRequest",
    "RecordEnforcementRequestTypedDict",
    "RecordEnforcementResponse",
    "RecordEnforcementResponseTypedDict",
    "RecordKeyUsageRequest",
    "RecordKeyUsageRequestTypedDict",
    "RecordKeyUsageResponse",
    "RecordKeyUsageResponseTypedDict",
    "ReplayWebhookDeliveryRequest",
    "ReplayWebhookDeliveryRequestTypedDict",
    "ReplayWebhookDeliveryResponse",
    "ReplayWebhookDeliveryResponseTypedDict",
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
    "DeleteAccountRequest": ".deleteaccount",
    "DeleteAccountRequestTypedDict": ".deleteaccount",
    "DeleteAccountResponse": ".deleteaccount",
    "DeleteAccountResponseTypedDict": ".deleteaccount",
    "DeleteAssessmentRequest": ".deleteassessment",
    "DeleteAssessmentRequestTypedDict": ".deleteassessment",
    "DeleteAssessmentResponse": ".deleteassessment",
    "DeleteAssessmentResponseTypedDict": ".deleteassessment",
    "DeleteIntegrationRequest": ".deleteintegration",
    "DeleteIntegrationRequestTypedDict": ".deleteintegration",
    "DeleteIntegrationResponse": ".deleteintegration",
    "DeleteIntegrationResponseTypedDict": ".deleteintegration",
    "DeleteWebhookEndpointRequest": ".deletewebhookendpoint",
    "DeleteWebhookEndpointRequestTypedDict": ".deletewebhookendpoint",
    "DeleteWebhookEndpointResponse": ".deletewebhookendpoint",
    "DeleteWebhookEndpointResponseTypedDict": ".deletewebhookendpoint",
    "GetAccountRequest": ".getaccount",
    "GetAccountRequestTypedDict": ".getaccount",
    "GetAccountResponse": ".getaccount",
    "GetAccountResponseTypedDict": ".getaccount",
    "GetAssessmentRequest": ".getassessment",
    "GetAssessmentRequestTypedDict": ".getassessment",
    "GetAssessmentResponse": ".getassessment",
    "GetAssessmentResponseTypedDict": ".getassessment",
    "ListAccountAssessmentsRequest": ".listaccountassessments",
    "ListAccountAssessmentsRequestTypedDict": ".listaccountassessments",
    "ListAccountAssessmentsResponse": ".listaccountassessments",
    "ListAccountAssessmentsResponseTypedDict": ".listaccountassessments",
    "ListAccountsRequest": ".listaccounts",
    "ListAccountsRequestTypedDict": ".listaccounts",
    "ListAccountsResponse": ".listaccounts",
    "ListAccountsResponseTypedDict": ".listaccounts",
    "ListIntegrationsResponse": ".listintegrations",
    "ListIntegrationsResponseTypedDict": ".listintegrations",
    "ListWebhookDeliveriesRequest": ".listwebhookdeliveries",
    "ListWebhookDeliveriesRequestTypedDict": ".listwebhookdeliveries",
    "ListWebhookDeliveriesResponse": ".listwebhookdeliveries",
    "ListWebhookDeliveriesResponseTypedDict": ".listwebhookdeliveries",
    "ListWebhookEndpointsResponse": ".listwebhookendpoints",
    "ListWebhookEndpointsResponseTypedDict": ".listwebhookendpoints",
    "QueryAccountAssessmentsResponse": ".queryaccountassessments",
    "QueryAccountAssessmentsResponseTypedDict": ".queryaccountassessments",
    "RecordAssessmentOutcomeRequest": ".recordassessmentoutcome",
    "RecordAssessmentOutcomeRequestTypedDict": ".recordassessmentoutcome",
    "RecordAssessmentOutcomeResponse": ".recordassessmentoutcome",
    "RecordAssessmentOutcomeResponseTypedDict": ".recordassessmentoutcome",
    "RecordEnforcementRequest": ".recordenforcement",
    "RecordEnforcementRequestTypedDict": ".recordenforcement",
    "RecordEnforcementResponse": ".recordenforcement",
    "RecordEnforcementResponseTypedDict": ".recordenforcement",
    "RecordKeyUsageRequest": ".recordkeyusage",
    "RecordKeyUsageRequestTypedDict": ".recordkeyusage",
    "RecordKeyUsageResponse": ".recordkeyusage",
    "RecordKeyUsageResponseTypedDict": ".recordkeyusage",
    "ReplayWebhookDeliveryRequest": ".replaywebhookdelivery",
    "ReplayWebhookDeliveryRequestTypedDict": ".replaywebhookdelivery",
    "ReplayWebhookDeliveryResponse": ".replaywebhookdelivery",
    "ReplayWebhookDeliveryResponseTypedDict": ".replaywebhookdelivery",
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
