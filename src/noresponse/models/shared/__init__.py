from typing import Any, TYPE_CHECKING

from noresponse.utils.dynamic_imports import lazy_getattr, lazy_dir

if TYPE_CHECKING:
    from .account import Account, AccountTypedDict
    from .accountdecision import AccountDecision
    from .accountdecisionsbyflow import (
        AccountDecisionsByFlow,
        AccountDecisionsByFlowTypedDict,
    )
    from .accountdeleted import AccountDeleted, AccountDeletedTypedDict
    from .accountdeletedevent import AccountDeletedEvent, AccountDeletedEventTypedDict
    from .accountdeletion import AccountDeletion, AccountDeletionTypedDict
    from .accountlist import AccountList, AccountListTypedDict
    from .accountrisk import AccountRisk, AccountRiskTypedDict
    from .accountriskchanged import AccountRiskChanged, AccountRiskChangedTypedDict
    from .accountriskchangedevent import (
        AccountRiskChangedEvent,
        AccountRiskChangedEventTypedDict,
    )
    from .accountriskreason import AccountRiskReason, AccountRiskReasonTypedDict
    from .assessment import Assessment, AssessmentTypedDict
    from .assessmentdeletion import AssessmentDeletion, AssessmentDeletionTypedDict
    from .assessmentdeletionaccount import (
        AssessmentDeletionAccount,
        AssessmentDeletionAccountTypedDict,
    )
    from .assessmentdetail import AssessmentDetail, AssessmentDetailTypedDict
    from .assessmentdetailauthcontext import (
        AssessmentDetailAuthContext,
        AssessmentDetailAuthContextTypedDict,
    )
    from .assessmentdetailtiming import (
        AssessmentDetailTiming,
        AssessmentDetailTimingTypedDict,
    )
    from .assessmentexpired import AssessmentExpired, AssessmentExpiredTypedDict
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
    from .assessmentupdateddata import (
        AssessmentUpdatedData,
        AssessmentUpdatedDataTypedDict,
    )
    from .assessmentupdatedevent import (
        AssessmentUpdatedEvent,
        AssessmentUpdatedEventTypedDict,
    )
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
    from .depth import Depth
    from .endpointverification import (
        EndpointVerification,
        EndpointVerificationTypedDict,
    )
    from .endpointverificationevent import (
        EndpointVerificationEvent,
        EndpointVerificationEventTypedDict,
    )
    from .enforcement import Enforcement, EnforcementTypedDict
    from .enforcementaction import EnforcementAction
    from .enforcementprovider import EnforcementProvider
    from .enforcementrequest import EnforcementRequest, EnforcementRequestTypedDict
    from .enforcementstate import EnforcementState
    from .enforcementstatus import EnforcementStatus
    from .environment import Environment
    from .failure import Failure
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
    from .keyusagebatch import KeyUsageBatch, KeyUsageBatchTypedDict
    from .keyusagebatchrequest import (
        KeyUsageBatchRequest,
        KeyUsageBatchRequestTypedDict,
    )
    from .keyusageevent import KeyUsageEvent, KeyUsageEventTypedDict
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
    from .signingkey import SigningKey, SigningKeyTypedDict
    from .signingsecret import SigningSecret, SigningSecretTypedDict
    from .status import Status
    from .transport import Transport
    from .webhookdeliveryattempt import (
        WebhookDeliveryAttempt,
        WebhookDeliveryAttemptTypedDict,
    )
    from .webhookdeliveryattemptstatus import WebhookDeliveryAttemptStatus
    from .webhookdeliverylist import WebhookDeliveryList, WebhookDeliveryListTypedDict
    from .webhookendpoint import WebhookEndpoint, WebhookEndpointTypedDict
    from .webhookendpointcreated import (
        WebhookEndpointCreated,
        WebhookEndpointCreatedTypedDict,
    )
    from .webhookendpointdisabled import (
        WebhookEndpointDisabled,
        WebhookEndpointDisabledTypedDict,
    )
    from .webhookendpointdisabledevent import (
        WebhookEndpointDisabledEvent,
        WebhookEndpointDisabledEventTypedDict,
    )
    from .webhookendpointlist import WebhookEndpointList, WebhookEndpointListTypedDict
    from .webhookendpointrequest import (
        WebhookEndpointRequest,
        WebhookEndpointRequestTypedDict,
    )
    from .webhookendpointstate import WebhookEndpointState
    from .webhookevent import WebhookEvent, WebhookEventTypedDict
    from .webhookkeyrotation import WebhookKeyRotation, WebhookKeyRotationTypedDict
    from .webhookkeyrotationrequest import (
        WebhookKeyRotationRequest,
        WebhookKeyRotationRequestTypedDict,
    )
    from .webhookreplay import WebhookReplay, WebhookReplayTypedDict
    from .webhookreplayrequest import (
        WebhookReplayRequest,
        WebhookReplayRequestTypedDict,
    )
    from .webhooktest import WebhookTest, WebhookTestTypedDict
    from .webhooktestrequest import WebhookTestRequest, WebhookTestRequestTypedDict
    from .webhooktestrequestevent import WebhookTestRequestEvent
    from .webhookverificationresponse import (
        WebhookVerificationResponse,
        WebhookVerificationResponseTypedDict,
    )
    from .workspacedeleted import WorkspaceDeleted, WorkspaceDeletedTypedDict
    from .workspacedeletedevent import (
        WorkspaceDeletedEvent,
        WorkspaceDeletedEventTypedDict,
    )

__all__ = [
    "Account",
    "AccountDecision",
    "AccountDecisionsByFlow",
    "AccountDecisionsByFlowTypedDict",
    "AccountDeleted",
    "AccountDeletedEvent",
    "AccountDeletedEventTypedDict",
    "AccountDeletedTypedDict",
    "AccountDeletion",
    "AccountDeletionTypedDict",
    "AccountList",
    "AccountListTypedDict",
    "AccountRisk",
    "AccountRiskChanged",
    "AccountRiskChangedEvent",
    "AccountRiskChangedEventTypedDict",
    "AccountRiskChangedTypedDict",
    "AccountRiskReason",
    "AccountRiskReasonTypedDict",
    "AccountRiskTypedDict",
    "AccountTypedDict",
    "AlternateName",
    "AlternateNameTypedDict",
    "AlternateNameUnion",
    "AlternateNameUnionTypedDict",
    "Assessment",
    "AssessmentDeletion",
    "AssessmentDeletionAccount",
    "AssessmentDeletionAccountTypedDict",
    "AssessmentDeletionTypedDict",
    "AssessmentDetail",
    "AssessmentDetailAuthContext",
    "AssessmentDetailAuthContextTypedDict",
    "AssessmentDetailTiming",
    "AssessmentDetailTimingTypedDict",
    "AssessmentDetailTypedDict",
    "AssessmentExpired",
    "AssessmentExpiredTypedDict",
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
    "AssessmentTypedDict",
    "AssessmentUpdatedData",
    "AssessmentUpdatedDataTypedDict",
    "AssessmentUpdatedEvent",
    "AssessmentUpdatedEventTypedDict",
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
    "Depth",
    "Email",
    "EmailTypedDict",
    "EmailUnion",
    "EmailUnionTypedDict",
    "EndpointVerification",
    "EndpointVerificationEvent",
    "EndpointVerificationEventTypedDict",
    "EndpointVerificationTypedDict",
    "Enforcement",
    "EnforcementAction",
    "EnforcementProvider",
    "EnforcementRequest",
    "EnforcementRequestTypedDict",
    "EnforcementState",
    "EnforcementStatus",
    "EnforcementTypedDict",
    "Environment",
    "Failure",
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
    "KeyUsageBatch",
    "KeyUsageBatchRequest",
    "KeyUsageBatchRequestTypedDict",
    "KeyUsageBatchTypedDict",
    "KeyUsageEvent",
    "KeyUsageEventTypedDict",
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
    "SigningKey",
    "SigningKeyTypedDict",
    "SigningSecret",
    "SigningSecretTypedDict",
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
    "WebhookDeliveryAttempt",
    "WebhookDeliveryAttemptStatus",
    "WebhookDeliveryAttemptTypedDict",
    "WebhookDeliveryList",
    "WebhookDeliveryListTypedDict",
    "WebhookEndpoint",
    "WebhookEndpointCreated",
    "WebhookEndpointCreatedTypedDict",
    "WebhookEndpointDisabled",
    "WebhookEndpointDisabledEvent",
    "WebhookEndpointDisabledEventTypedDict",
    "WebhookEndpointDisabledTypedDict",
    "WebhookEndpointList",
    "WebhookEndpointListTypedDict",
    "WebhookEndpointRequest",
    "WebhookEndpointRequestTypedDict",
    "WebhookEndpointState",
    "WebhookEndpointTypedDict",
    "WebhookEvent",
    "WebhookEventTypedDict",
    "WebhookKeyRotation",
    "WebhookKeyRotationRequest",
    "WebhookKeyRotationRequestTypedDict",
    "WebhookKeyRotationTypedDict",
    "WebhookReplay",
    "WebhookReplayRequest",
    "WebhookReplayRequestTypedDict",
    "WebhookReplayTypedDict",
    "WebhookTest",
    "WebhookTestRequest",
    "WebhookTestRequestEvent",
    "WebhookTestRequestTypedDict",
    "WebhookTestTypedDict",
    "WebhookVerificationResponse",
    "WebhookVerificationResponseTypedDict",
    "Website",
    "WebsiteTypedDict",
    "WebsiteUnion",
    "WebsiteUnionTypedDict",
    "WorkspaceDeleted",
    "WorkspaceDeletedEvent",
    "WorkspaceDeletedEventTypedDict",
    "WorkspaceDeletedTypedDict",
]

_dynamic_imports: dict[str, str] = {
    "Account": ".account",
    "AccountTypedDict": ".account",
    "AccountDecision": ".accountdecision",
    "AccountDecisionsByFlow": ".accountdecisionsbyflow",
    "AccountDecisionsByFlowTypedDict": ".accountdecisionsbyflow",
    "AccountDeleted": ".accountdeleted",
    "AccountDeletedTypedDict": ".accountdeleted",
    "AccountDeletedEvent": ".accountdeletedevent",
    "AccountDeletedEventTypedDict": ".accountdeletedevent",
    "AccountDeletion": ".accountdeletion",
    "AccountDeletionTypedDict": ".accountdeletion",
    "AccountList": ".accountlist",
    "AccountListTypedDict": ".accountlist",
    "AccountRisk": ".accountrisk",
    "AccountRiskTypedDict": ".accountrisk",
    "AccountRiskChanged": ".accountriskchanged",
    "AccountRiskChangedTypedDict": ".accountriskchanged",
    "AccountRiskChangedEvent": ".accountriskchangedevent",
    "AccountRiskChangedEventTypedDict": ".accountriskchangedevent",
    "AccountRiskReason": ".accountriskreason",
    "AccountRiskReasonTypedDict": ".accountriskreason",
    "Assessment": ".assessment",
    "AssessmentTypedDict": ".assessment",
    "AssessmentDeletion": ".assessmentdeletion",
    "AssessmentDeletionTypedDict": ".assessmentdeletion",
    "AssessmentDeletionAccount": ".assessmentdeletionaccount",
    "AssessmentDeletionAccountTypedDict": ".assessmentdeletionaccount",
    "AssessmentDetail": ".assessmentdetail",
    "AssessmentDetailTypedDict": ".assessmentdetail",
    "AssessmentDetailAuthContext": ".assessmentdetailauthcontext",
    "AssessmentDetailAuthContextTypedDict": ".assessmentdetailauthcontext",
    "AssessmentDetailTiming": ".assessmentdetailtiming",
    "AssessmentDetailTimingTypedDict": ".assessmentdetailtiming",
    "AssessmentExpired": ".assessmentexpired",
    "AssessmentExpiredTypedDict": ".assessmentexpired",
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
    "AssessmentUpdatedData": ".assessmentupdateddata",
    "AssessmentUpdatedDataTypedDict": ".assessmentupdateddata",
    "AssessmentUpdatedEvent": ".assessmentupdatedevent",
    "AssessmentUpdatedEventTypedDict": ".assessmentupdatedevent",
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
    "Depth": ".depth",
    "EndpointVerification": ".endpointverification",
    "EndpointVerificationTypedDict": ".endpointverification",
    "EndpointVerificationEvent": ".endpointverificationevent",
    "EndpointVerificationEventTypedDict": ".endpointverificationevent",
    "Enforcement": ".enforcement",
    "EnforcementTypedDict": ".enforcement",
    "EnforcementAction": ".enforcementaction",
    "EnforcementProvider": ".enforcementprovider",
    "EnforcementRequest": ".enforcementrequest",
    "EnforcementRequestTypedDict": ".enforcementrequest",
    "EnforcementState": ".enforcementstate",
    "EnforcementStatus": ".enforcementstatus",
    "Environment": ".environment",
    "Failure": ".failure",
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
    "KeyUsageBatch": ".keyusagebatch",
    "KeyUsageBatchTypedDict": ".keyusagebatch",
    "KeyUsageBatchRequest": ".keyusagebatchrequest",
    "KeyUsageBatchRequestTypedDict": ".keyusagebatchrequest",
    "KeyUsageEvent": ".keyusageevent",
    "KeyUsageEventTypedDict": ".keyusageevent",
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
    "SigningKey": ".signingkey",
    "SigningKeyTypedDict": ".signingkey",
    "SigningSecret": ".signingsecret",
    "SigningSecretTypedDict": ".signingsecret",
    "Status": ".status",
    "Transport": ".transport",
    "WebhookDeliveryAttempt": ".webhookdeliveryattempt",
    "WebhookDeliveryAttemptTypedDict": ".webhookdeliveryattempt",
    "WebhookDeliveryAttemptStatus": ".webhookdeliveryattemptstatus",
    "WebhookDeliveryList": ".webhookdeliverylist",
    "WebhookDeliveryListTypedDict": ".webhookdeliverylist",
    "WebhookEndpoint": ".webhookendpoint",
    "WebhookEndpointTypedDict": ".webhookendpoint",
    "WebhookEndpointCreated": ".webhookendpointcreated",
    "WebhookEndpointCreatedTypedDict": ".webhookendpointcreated",
    "WebhookEndpointDisabled": ".webhookendpointdisabled",
    "WebhookEndpointDisabledTypedDict": ".webhookendpointdisabled",
    "WebhookEndpointDisabledEvent": ".webhookendpointdisabledevent",
    "WebhookEndpointDisabledEventTypedDict": ".webhookendpointdisabledevent",
    "WebhookEndpointList": ".webhookendpointlist",
    "WebhookEndpointListTypedDict": ".webhookendpointlist",
    "WebhookEndpointRequest": ".webhookendpointrequest",
    "WebhookEndpointRequestTypedDict": ".webhookendpointrequest",
    "WebhookEndpointState": ".webhookendpointstate",
    "WebhookEvent": ".webhookevent",
    "WebhookEventTypedDict": ".webhookevent",
    "WebhookKeyRotation": ".webhookkeyrotation",
    "WebhookKeyRotationTypedDict": ".webhookkeyrotation",
    "WebhookKeyRotationRequest": ".webhookkeyrotationrequest",
    "WebhookKeyRotationRequestTypedDict": ".webhookkeyrotationrequest",
    "WebhookReplay": ".webhookreplay",
    "WebhookReplayTypedDict": ".webhookreplay",
    "WebhookReplayRequest": ".webhookreplayrequest",
    "WebhookReplayRequestTypedDict": ".webhookreplayrequest",
    "WebhookTest": ".webhooktest",
    "WebhookTestTypedDict": ".webhooktest",
    "WebhookTestRequest": ".webhooktestrequest",
    "WebhookTestRequestTypedDict": ".webhooktestrequest",
    "WebhookTestRequestEvent": ".webhooktestrequestevent",
    "WebhookVerificationResponse": ".webhookverificationresponse",
    "WebhookVerificationResponseTypedDict": ".webhookverificationresponse",
    "WorkspaceDeleted": ".workspacedeleted",
    "WorkspaceDeletedTypedDict": ".workspacedeleted",
    "WorkspaceDeletedEvent": ".workspacedeletedevent",
    "WorkspaceDeletedEventTypedDict": ".workspacedeletedevent",
}


def __getattr__(attr_name: str) -> Any:
    return lazy_getattr(
        attr_name, package=__package__, dynamic_imports=_dynamic_imports
    )


def __dir__():
    return lazy_dir(dynamic_imports=_dynamic_imports)
