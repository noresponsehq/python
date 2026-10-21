from typing import Any, TYPE_CHECKING

from noresponse.utils.dynamic_imports import lazy_getattr, lazy_dir

if TYPE_CHECKING:
    from .createassessment import (
        CreateAssessmentRequest,
        CreateAssessmentRequestTypedDict,
        CreateAssessmentResponse,
        CreateAssessmentResponseTypedDict,
    )
    from .getassessment import (
        GetAssessmentRequest,
        GetAssessmentRequestTypedDict,
        GetAssessmentResponse,
        GetAssessmentResponseTypedDict,
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

__all__ = [
    "CreateAssessmentRequest",
    "CreateAssessmentRequestTypedDict",
    "CreateAssessmentResponse",
    "CreateAssessmentResponseTypedDict",
    "GetAssessmentRequest",
    "GetAssessmentRequestTypedDict",
    "GetAssessmentResponse",
    "GetAssessmentResponseTypedDict",
    "QueryAccountAssessmentsResponse",
    "QueryAccountAssessmentsResponseTypedDict",
    "RecordAssessmentOutcomeRequest",
    "RecordAssessmentOutcomeRequestTypedDict",
    "RecordAssessmentOutcomeResponse",
    "RecordAssessmentOutcomeResponseTypedDict",
    "RotateAPIKeyResponse",
    "RotateAPIKeyResponseTypedDict",
]

_dynamic_imports: dict[str, str] = {
    "CreateAssessmentRequest": ".createassessment",
    "CreateAssessmentRequestTypedDict": ".createassessment",
    "CreateAssessmentResponse": ".createassessment",
    "CreateAssessmentResponseTypedDict": ".createassessment",
    "GetAssessmentRequest": ".getassessment",
    "GetAssessmentRequestTypedDict": ".getassessment",
    "GetAssessmentResponse": ".getassessment",
    "GetAssessmentResponseTypedDict": ".getassessment",
    "QueryAccountAssessmentsResponse": ".queryaccountassessments",
    "QueryAccountAssessmentsResponseTypedDict": ".queryaccountassessments",
    "RecordAssessmentOutcomeRequest": ".recordassessmentoutcome",
    "RecordAssessmentOutcomeRequestTypedDict": ".recordassessmentoutcome",
    "RecordAssessmentOutcomeResponse": ".recordassessmentoutcome",
    "RecordAssessmentOutcomeResponseTypedDict": ".recordassessmentoutcome",
    "RotateAPIKeyResponse": ".rotateapikey",
    "RotateAPIKeyResponseTypedDict": ".rotateapikey",
}


def __getattr__(attr_name: str) -> Any:
    return lazy_getattr(
        attr_name, package=__package__, dynamic_imports=_dynamic_imports
    )


def __dir__():
    return lazy_dir(dynamic_imports=_dynamic_imports)
