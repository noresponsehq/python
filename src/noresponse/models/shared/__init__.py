from typing import Any, TYPE_CHECKING

from noresponse.utils.dynamic_imports import lazy_getattr, lazy_dir

if TYPE_CHECKING:
    from .assessment import Assessment, AssessmentTypedDict
    from .assessmentlist import AssessmentList, AssessmentListTypedDict
    from .assessmentoutcome import AssessmentOutcome, AssessmentOutcomeTypedDict
    from .assessmentoutcomerequest import (
        AssessmentOutcomeRequest,
        AssessmentOutcomeRequestTypedDict,
    )
    from .assessmentquery import AssessmentQuery, AssessmentQueryTypedDict
    from .assessmentrequest import AssessmentRequest, AssessmentRequestTypedDict
    from .assessmentrequestclientcontext import (
        AssessmentRequestClientContext,
        AssessmentRequestClientContextTypedDict,
    )
    from .assessmentrequestidentifiers import (
        AssessmentRequestIdentifiers,
        AssessmentRequestIdentifiersTypedDict,
    )
    from .assessmentrequestissuedcredential import (
        AssessmentRequestIssuedCredential,
        AssessmentRequestIssuedCredentialTypedDict,
    )
    from .assessmentrequestpolicycontext import (
        AssessmentRequestPolicyContext,
        AssessmentRequestPolicyContextTypedDict,
    )
    from .assessmenttiming import AssessmentTiming, AssessmentTimingTypedDict
    from .assurancelevel import AssuranceLevel
    from .authcontext import AuthContext, AuthContextTypedDict
    from .authcontextmfa import AuthContextMfa, AuthContextMfaTypedDict
    from .authenticationerrorcode import AuthenticationErrorCode
    from .badrequesterrorcode import BadRequestErrorCode
    from .band import Band
    from .breach import Breach, BreachTypedDict
    from .breachexposed import BreachExposed
    from .breachkind import BreachKind
    from .breachselector import BreachSelector
    from .breachsummary import BreachSummary, BreachSummaryTypedDict
    from .confidence import Confidence
    from .conflicterrorcode import ConflictErrorCode
    from .consistency import Consistency, ConsistencyTypedDict
    from .consistencyvalue import ConsistencyValue
    from .country import Country
    from .failurereason import FailureReason
    from .flow import Flow
    from .freshness import Freshness
    from .hookpoint import HookPoint
    from .identifierkind import IdentifierKind
    from .incompletereason import IncompleteReason
    from .incompletesource import IncompleteSource, IncompleteSourceTypedDict
    from .integration import Integration, IntegrationTypedDict
    from .integrationhookpoint import IntegrationHookPoint
    from .integrationlist import IntegrationList, IntegrationListTypedDict
    from .integrationplatform import IntegrationPlatform
    from .integrationrequest import IntegrationRequest, IntegrationRequestTypedDict
    from .integrationrotationrequest import (
        IntegrationRotationRequest,
        IntegrationRotationRequestTypedDict,
    )
    from .ipsummary import IPSummary, IPSummaryTypedDict
    from .ipsummarytype import IPSummaryType
    from .keyrotation import KeyRotation, KeyRotationTypedDict, Scope
    from .keyrotationrequest import KeyRotationRequest, KeyRotationRequestTypedDict
    from .lane import Lane
    from .linetype import LineType
    from .notfounderrorcode import NotFoundErrorCode
    from .outcome import Outcome
    from .permissiondeniederrorcode import PermissionDeniedErrorCode
    from .phoneenrichment import PhoneEnrichment, PhoneEnrichmentTypedDict
    from .phoneenrichmentfields import (
        AlternateName,
        AlternateNameTypedDict,
        AlternateNameUnion,
        AlternateNameUnionTypedDict,
        Email,
        EmailTypedDict,
        EmailUnion,
        EmailUnionTypedDict,
        Location,
        LocationTypedDict,
        LocationUnion,
        LocationUnionTypedDict,
        NameCandidate,
        NameCandidateTypedDict,
        NameCandidateUnion,
        NameCandidateUnionTypedDict,
        PhoneEnrichmentFields,
        PhoneEnrichmentFieldsTypedDict,
        SocialProfile,
        SocialProfileTypedDict,
        SocialProfileUnion,
        SocialProfileUnionTypedDict,
        Timezone,
        TimezoneTypedDict,
        TimezoneUnion,
        TimezoneUnionTypedDict,
        Website,
        WebsiteTypedDict,
        WebsiteUnion,
        WebsiteUnionTypedDict,
    )
    from .platform import Platform
    from .probleminvalidparam import ProblemInvalidParam, ProblemInvalidParamTypedDict
    from .ratelimiterrorcode import RateLimitErrorCode
    from .reasoncode import ReasonCode
    from .reasonidentifier import ReasonIdentifier
    from .recommendation import Recommendation
    from .responsemode import ResponseMode
    from .risk import Risk, RiskTypedDict
    from .riskconfidence import RiskConfidence
    from .riskcoverage import RiskCoverage, RiskCoverageTypedDict
    from .riskdetails import RiskDetails, RiskDetailsTypedDict
    from .riskdetailsbreachname import (
        RiskDetailsBreachName,
        RiskDetailsBreachNameTypedDict,
    )
    from .riskdetailsphonename import (
        RiskDetailsPhoneName,
        RiskDetailsPhoneNameTypedDict,
    )
    from .riskreason import RiskReason, RiskReasonTypedDict
    from .risksummary import RiskSummary, RiskSummaryTypedDict
    from .risksummaryemail import RiskSummaryEmail, RiskSummaryEmailTypedDict
    from .risksummaryphone import RiskSummaryPhone, RiskSummaryPhoneTypedDict
    from .risksummaryusername import RiskSummaryUsername, RiskSummaryUsernameTypedDict
    from .security import Security, SecurityTypedDict
    from .signal import Signal, SignalTypedDict
    from .signaloutcome import SignalOutcome
    from .status import Status
    from .transport import Transport

__all__ = [
    "AlternateName",
    "AlternateNameTypedDict",
    "AlternateNameUnion",
    "AlternateNameUnionTypedDict",
    "Assessment",
    "AssessmentList",
    "AssessmentListTypedDict",
    "AssessmentOutcome",
    "AssessmentOutcomeRequest",
    "AssessmentOutcomeRequestTypedDict",
    "AssessmentOutcomeTypedDict",
    "AssessmentQuery",
    "AssessmentQueryTypedDict",
    "AssessmentRequest",
    "AssessmentRequestClientContext",
    "AssessmentRequestClientContextTypedDict",
    "AssessmentRequestIdentifiers",
    "AssessmentRequestIdentifiersTypedDict",
    "AssessmentRequestIssuedCredential",
    "AssessmentRequestIssuedCredentialTypedDict",
    "AssessmentRequestPolicyContext",
    "AssessmentRequestPolicyContextTypedDict",
    "AssessmentRequestTypedDict",
    "AssessmentTiming",
    "AssessmentTimingTypedDict",
    "AssessmentTypedDict",
    "AssuranceLevel",
    "AuthContext",
    "AuthContextMfa",
    "AuthContextMfaTypedDict",
    "AuthContextTypedDict",
    "AuthenticationErrorCode",
    "BadRequestErrorCode",
    "Band",
    "Breach",
    "BreachExposed",
    "BreachKind",
    "BreachSelector",
    "BreachSummary",
    "BreachSummaryTypedDict",
    "BreachTypedDict",
    "Confidence",
    "ConflictErrorCode",
    "Consistency",
    "ConsistencyTypedDict",
    "ConsistencyValue",
    "Country",
    "Email",
    "EmailTypedDict",
    "EmailUnion",
    "EmailUnionTypedDict",
    "FailureReason",
    "Flow",
    "Freshness",
    "HookPoint",
    "IPSummary",
    "IPSummaryType",
    "IPSummaryTypedDict",
    "IdentifierKind",
    "IncompleteReason",
    "IncompleteSource",
    "IncompleteSourceTypedDict",
    "Integration",
    "IntegrationHookPoint",
    "IntegrationList",
    "IntegrationListTypedDict",
    "IntegrationPlatform",
    "IntegrationRequest",
    "IntegrationRequestTypedDict",
    "IntegrationRotationRequest",
    "IntegrationRotationRequestTypedDict",
    "IntegrationTypedDict",
    "KeyRotation",
    "KeyRotationRequest",
    "KeyRotationRequestTypedDict",
    "KeyRotationTypedDict",
    "Lane",
    "LineType",
    "Location",
    "LocationTypedDict",
    "LocationUnion",
    "LocationUnionTypedDict",
    "NameCandidate",
    "NameCandidateTypedDict",
    "NameCandidateUnion",
    "NameCandidateUnionTypedDict",
    "NotFoundErrorCode",
    "Outcome",
    "PermissionDeniedErrorCode",
    "PhoneEnrichment",
    "PhoneEnrichmentFields",
    "PhoneEnrichmentFieldsTypedDict",
    "PhoneEnrichmentTypedDict",
    "Platform",
    "ProblemInvalidParam",
    "ProblemInvalidParamTypedDict",
    "RateLimitErrorCode",
    "ReasonCode",
    "ReasonIdentifier",
    "Recommendation",
    "ResponseMode",
    "Risk",
    "RiskConfidence",
    "RiskCoverage",
    "RiskCoverageTypedDict",
    "RiskDetails",
    "RiskDetailsBreachName",
    "RiskDetailsBreachNameTypedDict",
    "RiskDetailsPhoneName",
    "RiskDetailsPhoneNameTypedDict",
    "RiskDetailsTypedDict",
    "RiskReason",
    "RiskReasonTypedDict",
    "RiskSummary",
    "RiskSummaryEmail",
    "RiskSummaryEmailTypedDict",
    "RiskSummaryPhone",
    "RiskSummaryPhoneTypedDict",
    "RiskSummaryTypedDict",
    "RiskSummaryUsername",
    "RiskSummaryUsernameTypedDict",
    "RiskTypedDict",
    "Scope",
    "Security",
    "SecurityTypedDict",
    "Signal",
    "SignalOutcome",
    "SignalTypedDict",
    "SocialProfile",
    "SocialProfileTypedDict",
    "SocialProfileUnion",
    "SocialProfileUnionTypedDict",
    "Status",
    "Timezone",
    "TimezoneTypedDict",
    "TimezoneUnion",
    "TimezoneUnionTypedDict",
    "Transport",
    "Website",
    "WebsiteTypedDict",
    "WebsiteUnion",
    "WebsiteUnionTypedDict",
]

_dynamic_imports: dict[str, str] = {
    "Assessment": ".assessment",
    "AssessmentTypedDict": ".assessment",
    "AssessmentList": ".assessmentlist",
    "AssessmentListTypedDict": ".assessmentlist",
    "AssessmentOutcome": ".assessmentoutcome",
    "AssessmentOutcomeTypedDict": ".assessmentoutcome",
    "AssessmentOutcomeRequest": ".assessmentoutcomerequest",
    "AssessmentOutcomeRequestTypedDict": ".assessmentoutcomerequest",
    "AssessmentQuery": ".assessmentquery",
    "AssessmentQueryTypedDict": ".assessmentquery",
    "AssessmentRequest": ".assessmentrequest",
    "AssessmentRequestTypedDict": ".assessmentrequest",
    "AssessmentRequestClientContext": ".assessmentrequestclientcontext",
    "AssessmentRequestClientContextTypedDict": ".assessmentrequestclientcontext",
    "AssessmentRequestIdentifiers": ".assessmentrequestidentifiers",
    "AssessmentRequestIdentifiersTypedDict": ".assessmentrequestidentifiers",
    "AssessmentRequestIssuedCredential": ".assessmentrequestissuedcredential",
    "AssessmentRequestIssuedCredentialTypedDict": ".assessmentrequestissuedcredential",
    "AssessmentRequestPolicyContext": ".assessmentrequestpolicycontext",
    "AssessmentRequestPolicyContextTypedDict": ".assessmentrequestpolicycontext",
    "AssessmentTiming": ".assessmenttiming",
    "AssessmentTimingTypedDict": ".assessmenttiming",
    "AssuranceLevel": ".assurancelevel",
    "AuthContext": ".authcontext",
    "AuthContextTypedDict": ".authcontext",
    "AuthContextMfa": ".authcontextmfa",
    "AuthContextMfaTypedDict": ".authcontextmfa",
    "AuthenticationErrorCode": ".authenticationerrorcode",
    "BadRequestErrorCode": ".badrequesterrorcode",
    "Band": ".band",
    "Breach": ".breach",
    "BreachTypedDict": ".breach",
    "BreachExposed": ".breachexposed",
    "BreachKind": ".breachkind",
    "BreachSelector": ".breachselector",
    "BreachSummary": ".breachsummary",
    "BreachSummaryTypedDict": ".breachsummary",
    "Confidence": ".confidence",
    "ConflictErrorCode": ".conflicterrorcode",
    "Consistency": ".consistency",
    "ConsistencyTypedDict": ".consistency",
    "ConsistencyValue": ".consistencyvalue",
    "Country": ".country",
    "FailureReason": ".failurereason",
    "Flow": ".flow",
    "Freshness": ".freshness",
    "HookPoint": ".hookpoint",
    "IdentifierKind": ".identifierkind",
    "IncompleteReason": ".incompletereason",
    "IncompleteSource": ".incompletesource",
    "IncompleteSourceTypedDict": ".incompletesource",
    "Integration": ".integration",
    "IntegrationTypedDict": ".integration",
    "IntegrationHookPoint": ".integrationhookpoint",
    "IntegrationList": ".integrationlist",
    "IntegrationListTypedDict": ".integrationlist",
    "IntegrationPlatform": ".integrationplatform",
    "IntegrationRequest": ".integrationrequest",
    "IntegrationRequestTypedDict": ".integrationrequest",
    "IntegrationRotationRequest": ".integrationrotationrequest",
    "IntegrationRotationRequestTypedDict": ".integrationrotationrequest",
    "IPSummary": ".ipsummary",
    "IPSummaryTypedDict": ".ipsummary",
    "IPSummaryType": ".ipsummarytype",
    "KeyRotation": ".keyrotation",
    "KeyRotationTypedDict": ".keyrotation",
    "Scope": ".keyrotation",
    "KeyRotationRequest": ".keyrotationrequest",
    "KeyRotationRequestTypedDict": ".keyrotationrequest",
    "Lane": ".lane",
    "LineType": ".linetype",
    "NotFoundErrorCode": ".notfounderrorcode",
    "Outcome": ".outcome",
    "PermissionDeniedErrorCode": ".permissiondeniederrorcode",
    "PhoneEnrichment": ".phoneenrichment",
    "PhoneEnrichmentTypedDict": ".phoneenrichment",
    "AlternateName": ".phoneenrichmentfields",
    "AlternateNameTypedDict": ".phoneenrichmentfields",
    "AlternateNameUnion": ".phoneenrichmentfields",
    "AlternateNameUnionTypedDict": ".phoneenrichmentfields",
    "Email": ".phoneenrichmentfields",
    "EmailTypedDict": ".phoneenrichmentfields",
    "EmailUnion": ".phoneenrichmentfields",
    "EmailUnionTypedDict": ".phoneenrichmentfields",
    "Location": ".phoneenrichmentfields",
    "LocationTypedDict": ".phoneenrichmentfields",
    "LocationUnion": ".phoneenrichmentfields",
    "LocationUnionTypedDict": ".phoneenrichmentfields",
    "NameCandidate": ".phoneenrichmentfields",
    "NameCandidateTypedDict": ".phoneenrichmentfields",
    "NameCandidateUnion": ".phoneenrichmentfields",
    "NameCandidateUnionTypedDict": ".phoneenrichmentfields",
    "PhoneEnrichmentFields": ".phoneenrichmentfields",
    "PhoneEnrichmentFieldsTypedDict": ".phoneenrichmentfields",
    "SocialProfile": ".phoneenrichmentfields",
    "SocialProfileTypedDict": ".phoneenrichmentfields",
    "SocialProfileUnion": ".phoneenrichmentfields",
    "SocialProfileUnionTypedDict": ".phoneenrichmentfields",
    "Timezone": ".phoneenrichmentfields",
    "TimezoneTypedDict": ".phoneenrichmentfields",
    "TimezoneUnion": ".phoneenrichmentfields",
    "TimezoneUnionTypedDict": ".phoneenrichmentfields",
    "Website": ".phoneenrichmentfields",
    "WebsiteTypedDict": ".phoneenrichmentfields",
    "WebsiteUnion": ".phoneenrichmentfields",
    "WebsiteUnionTypedDict": ".phoneenrichmentfields",
    "Platform": ".platform",
    "ProblemInvalidParam": ".probleminvalidparam",
    "ProblemInvalidParamTypedDict": ".probleminvalidparam",
    "RateLimitErrorCode": ".ratelimiterrorcode",
    "ReasonCode": ".reasoncode",
    "ReasonIdentifier": ".reasonidentifier",
    "Recommendation": ".recommendation",
    "ResponseMode": ".responsemode",
    "Risk": ".risk",
    "RiskTypedDict": ".risk",
    "RiskConfidence": ".riskconfidence",
    "RiskCoverage": ".riskcoverage",
    "RiskCoverageTypedDict": ".riskcoverage",
    "RiskDetails": ".riskdetails",
    "RiskDetailsTypedDict": ".riskdetails",
    "RiskDetailsBreachName": ".riskdetailsbreachname",
    "RiskDetailsBreachNameTypedDict": ".riskdetailsbreachname",
    "RiskDetailsPhoneName": ".riskdetailsphonename",
    "RiskDetailsPhoneNameTypedDict": ".riskdetailsphonename",
    "RiskReason": ".riskreason",
    "RiskReasonTypedDict": ".riskreason",
    "RiskSummary": ".risksummary",
    "RiskSummaryTypedDict": ".risksummary",
    "RiskSummaryEmail": ".risksummaryemail",
    "RiskSummaryEmailTypedDict": ".risksummaryemail",
    "RiskSummaryPhone": ".risksummaryphone",
    "RiskSummaryPhoneTypedDict": ".risksummaryphone",
    "RiskSummaryUsername": ".risksummaryusername",
    "RiskSummaryUsernameTypedDict": ".risksummaryusername",
    "Security": ".security",
    "SecurityTypedDict": ".security",
    "Signal": ".signal",
    "SignalTypedDict": ".signal",
    "SignalOutcome": ".signaloutcome",
    "Status": ".status",
    "Transport": ".transport",
}


def __getattr__(attr_name: str) -> Any:
    return lazy_getattr(
        attr_name, package=__package__, dynamic_imports=_dynamic_imports
    )


def __dir__():
    return lazy_dir(dynamic_imports=_dynamic_imports)
