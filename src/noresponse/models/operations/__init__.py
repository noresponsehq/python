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
    from .deleteintegration import (
        DeleteIntegrationRequest,
        DeleteIntegrationRequestTypedDict,
        DeleteIntegrationResponse,
        DeleteIntegrationResponseTypedDict,
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

__all__ = [
    "CreateAssessmentRequest",
    "CreateAssessmentRequestTypedDict",
    "CreateAssessmentResponse",
    "CreateAssessmentResponseTypedDict",
    "CreateIntegrationResponse",
    "CreateIntegrationResponseTypedDict",
    "DeleteIntegrationRequest",
    "DeleteIntegrationRequestTypedDict",
    "DeleteIntegrationResponse",
    "DeleteIntegrationResponseTypedDict",
    "GetAssessmentRequest",
    "GetAssessmentRequestTypedDict",
    "GetAssessmentResponse",
    "GetAssessmentResponseTypedDict",
    "ListIntegrationsResponse",
    "ListIntegrationsResponseTypedDict",
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
]

_dynamic_imports: dict[str, str] = {
    "CreateAssessmentRequest": ".createassessment",
    "CreateAssessmentRequestTypedDict": ".createassessment",
    "CreateAssessmentResponse": ".createassessment",
    "CreateAssessmentResponseTypedDict": ".createassessment",
    "CreateIntegrationResponse": ".createintegration",
    "CreateIntegrationResponseTypedDict": ".createintegration",
    "DeleteIntegrationRequest": ".deleteintegration",
    "DeleteIntegrationRequestTypedDict": ".deleteintegration",
    "DeleteIntegrationResponse": ".deleteintegration",
    "DeleteIntegrationResponseTypedDict": ".deleteintegration",
    "GetAssessmentRequest": ".getassessment",
    "GetAssessmentRequestTypedDict": ".getassessment",
    "GetAssessmentResponse": ".getassessment",
    "GetAssessmentResponseTypedDict": ".getassessment",
    "ListIntegrationsResponse": ".listintegrations",
    "ListIntegrationsResponseTypedDict": ".listintegrations",
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
}


def __getattr__(attr_name: str) -> Any:
    return lazy_getattr(
        attr_name, package=__package__, dynamic_imports=_dynamic_imports
    )


def __dir__():
    return lazy_dir(dynamic_imports=_dynamic_imports)
