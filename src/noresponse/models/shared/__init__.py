from typing import Any, TYPE_CHECKING

from noresponse.utils.dynamic_imports import lazy_getattr, lazy_dir

if TYPE_CHECKING:
    from .account import Account, AccountTypedDict
    from .accountbinding import AccountBinding, AccountBindingTypedDict
    from .accountbindingactor import AccountBindingActor, AccountBindingActorTypedDict
    from .accountbindingrequest import (
        AccountBindingRequest,
        AccountBindingRequestTypedDict,
    )
    from .accountdecision import AccountDecision
    from .accountdecisionsbyflow import (
        AccountDecisionsByFlow,
        AccountDecisionsByFlowTypedDict,
    )
    from .accountdecisionsnapshot import (
        AccountDecisionSnapshot,
        AccountDecisionSnapshotTypedDict,
    )
    from .accountdeleted import AccountDeleted, AccountDeletedTypedDict
    from .accountdeletedevent import AccountDeletedEvent, AccountDeletedEventTypedDict
    from .accountdeletion import AccountDeletion, AccountDeletionTypedDict
    from .accountexport import AccountExport, AccountExportTypedDict, Exclusion
    from .accountlist import AccountList, AccountListTypedDict
    from .accountoutcome import AccountOutcome, AccountOutcomeTypedDict
    from .accountoutcomeactor import AccountOutcomeActor, AccountOutcomeActorTypedDict
    from .accountoutcomepage import AccountOutcomePage, AccountOutcomePageTypedDict
    from .accountoutcomerequest import (
        AccountOutcomeRequest,
        AccountOutcomeRequestTypedDict,
    )
    from .accountrisk import AccountRisk, AccountRiskTypedDict
    from .accountriskchanged import AccountRiskChanged, AccountRiskChangedTypedDict
    from .accountriskchangedevent import (
        AccountRiskChangedEvent,
        AccountRiskChangedEventTypedDict,
    )
    from .accountriskreason import AccountRiskReason, AccountRiskReasonTypedDict
    from .admission import Admission
    from .agreement import Agreement
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
    from .assessmentrevision import AssessmentRevision, AssessmentRevisionTypedDict
    from .assessmentsearchpage import (
        AssessmentSearchPage,
        AssessmentSearchPageTypedDict,
    )
    from .assessmentsearchrequest import (
        AssessmentSearchRequest,
        AssessmentSearchRequestTypedDict,
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
    from .attributeagreement import AttributeAgreement, AttributeAgreementTypedDict
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
    from .credentialassociation import (
        CredentialAssociation,
        CredentialAssociationTypedDict,
    )
    from .credentialassociationactor import (
        CredentialAssociationActor,
        CredentialAssociationActorTypedDict,
    )
    from .credentialassociationretiredby import (
        CredentialAssociationRetiredBy,
        CredentialAssociationRetiredByTypedDict,
    )
    from .credentialpage import CredentialPage, CredentialPageTypedDict
    from .credentialrequest import CredentialRequest, CredentialRequestTypedDict
    from .decision import Decision
    from .decisionreceipt import DecisionReceipt, DecisionReceiptTypedDict
    from .defaultdepth import DefaultDepth
    from .depth import Depth
    from .direction import Direction
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
    from .exportassessmentoutcome import (
        ExportAssessmentOutcome,
        ExportAssessmentOutcomeTypedDict,
    )
    from .failure import Failure
    from .failurereason import FailureReason
    from .flow import Flow
    from .flowchange import FlowChange, FlowChangeTypedDict
    from .flowsettings import FlowSettings, FlowSettingsTypedDict
    from .footprint import Footprint, FootprintTypedDict
    from .footprintcoherence import FootprintCoherence, FootprintCoherenceTypedDict
    from .footprintfamily import FootprintFamily
    from .footprinttimeline import FootprintTimeline, FootprintTimelineTypedDict
    from .freshness import Freshness
    from .hookpoint import HookPoint
    from .identifier import Identifier
    from .identifierkind import IdentifierKind
    from .impact import Impact
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
    from .key import Key, KeyScope, KeyTypedDict
    from .keyenvironment import KeyEnvironment
    from .keylist import KeyList, KeyListTypedDict
    from .keyrequest import KeyRequest, KeyRequestScope, KeyRequestTypedDict
    from .keyrotation import KeyRotation, KeyRotationScope, KeyRotationTypedDict
    from .keyrotationrequest import KeyRotationRequest, KeyRotationRequestTypedDict
    from .keystatus import KeyStatus
    from .keyusagebatch import KeyUsageBatch, KeyUsageBatchTypedDict
    from .keyusagebatchrequest import (
        KeyUsageBatchRequest,
        KeyUsageBatchRequestTypedDict,
    )
    from .keyusageevent import KeyUsageEvent, KeyUsageEventTypedDict
    from .lane import Lane
    from .linetype import LineType
    from .listentry import ListEntry, ListEntryTypedDict
    from .listentryaction import ListEntryAction
    from .listentrykind import ListEntryKind
    from .listentrylist import ListEntryList, ListEntryListTypedDict
    from .listentryrequest import ListEntryRequest, ListEntryRequestTypedDict
    from .notfounderrorcode import NotFoundErrorCode
    from .onexpiry import OnExpiry
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
    from .requestdiagnostic import RequestDiagnostic, RequestDiagnosticTypedDict
    from .requestdiagnosticpage import (
        RequestDiagnosticPage,
        RequestDiagnosticPageTypedDict,
    )
    from .responsemode import ResponseMode
    from .risk import Risk, RiskTypedDict
    from .riskconfidence import RiskConfidence
    from .riskcoverage import RiskCoverage, RiskCoverageTypedDict
    from .riskdetails import RiskDetails, RiskDetailsTypedDict
    from .riskdetailsbreachname import (
        RiskDetailsBreachName,
        RiskDetailsBreachNameTypedDict,
    )
    from .riskdetailsevent import RiskDetailsEvent, RiskDetailsEventTypedDict
    from .riskdetailseventkind import RiskDetailsEventKind
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
    from .sentidentifiers import SentIdentifiers, SentIdentifiersTypedDict
    from .settings import Settings, SettingsTypedDict
    from .settingsflows import SettingsFlows, SettingsFlowsTypedDict
    from .settingsrequest import SettingsRequest, SettingsRequestTypedDict
    from .settingsrequestflows import (
        SettingsRequestFlows,
        SettingsRequestFlowsTypedDict,
    )
    from .signal import Signal, SignalTypedDict
    from .signaloutcome import SignalOutcome
    from .signingkey import SigningKey, SigningKeyTypedDict
    from .signingsecret import SigningSecret, SigningSecretTypedDict
    from .sourceid import SourceID
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
    "AccountBinding",
    "AccountBindingActor",
    "AccountBindingActorTypedDict",
    "AccountBindingRequest",
    "AccountBindingRequestTypedDict",
    "AccountBindingTypedDict",
    "AccountDecision",
    "AccountDecisionSnapshot",
    "AccountDecisionSnapshotTypedDict",
    "AccountDecisionsByFlow",
    "AccountDecisionsByFlowTypedDict",
    "AccountDeleted",
    "AccountDeletedEvent",
    "AccountDeletedEventTypedDict",
    "AccountDeletedTypedDict",
    "AccountDeletion",
    "AccountDeletionTypedDict",
    "AccountExport",
    "AccountExportTypedDict",
    "AccountList",
    "AccountListTypedDict",
    "AccountOutcome",
    "AccountOutcomeActor",
    "AccountOutcomeActorTypedDict",
    "AccountOutcomePage",
    "AccountOutcomePageTypedDict",
    "AccountOutcomeRequest",
    "AccountOutcomeRequestTypedDict",
    "AccountOutcomeTypedDict",
    "AccountRisk",
    "AccountRiskChanged",
    "AccountRiskChangedEvent",
    "AccountRiskChangedEventTypedDict",
    "AccountRiskChangedTypedDict",
    "AccountRiskReason",
    "AccountRiskReasonTypedDict",
    "AccountRiskTypedDict",
    "AccountTypedDict",
    "Admission",
    "Agreement",
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
    "AssessmentRevision",
    "AssessmentRevisionTypedDict",
    "AssessmentSearchPage",
    "AssessmentSearchPageTypedDict",
    "AssessmentSearchRequest",
    "AssessmentSearchRequestTypedDict",
    "AssessmentTypedDict",
    "AssessmentUpdatedData",
    "AssessmentUpdatedDataTypedDict",
    "AssessmentUpdatedEvent",
    "AssessmentUpdatedEventTypedDict",
    "AssuranceLevel",
    "AttributeAgreement",
    "AttributeAgreementTypedDict",
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
    "CredentialAssociation",
    "CredentialAssociationActor",
    "CredentialAssociationActorTypedDict",
    "CredentialAssociationRetiredBy",
    "CredentialAssociationRetiredByTypedDict",
    "CredentialAssociationTypedDict",
    "CredentialPage",
    "CredentialPageTypedDict",
    "CredentialRequest",
    "CredentialRequestTypedDict",
    "Decision",
    "DecisionReceipt",
    "DecisionReceiptTypedDict",
    "DefaultDepth",
    "Depth",
    "Direction",
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
    "Exclusion",
    "ExportAssessmentOutcome",
    "ExportAssessmentOutcomeTypedDict",
    "Failure",
    "FailureReason",
    "Flow",
    "FlowChange",
    "FlowChangeTypedDict",
    "FlowSettings",
    "FlowSettingsTypedDict",
    "Footprint",
    "FootprintCoherence",
    "FootprintCoherenceTypedDict",
    "FootprintFamily",
    "FootprintTimeline",
    "FootprintTimelineTypedDict",
    "FootprintTypedDict",
    "Freshness",
    "HookPoint",
    "IPSummary",
    "IPSummaryType",
    "IPSummaryTypedDict",
    "Identifier",
    "IdentifierKind",
    "Impact",
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
    "Key",
    "KeyEnvironment",
    "KeyList",
    "KeyListTypedDict",
    "KeyRequest",
    "KeyRequestScope",
    "KeyRequestTypedDict",
    "KeyRotation",
    "KeyRotationRequest",
    "KeyRotationRequestTypedDict",
    "KeyRotationScope",
    "KeyRotationTypedDict",
    "KeyScope",
    "KeyStatus",
    "KeyTypedDict",
    "KeyUsageBatch",
    "KeyUsageBatchRequest",
    "KeyUsageBatchRequestTypedDict",
    "KeyUsageBatchTypedDict",
    "KeyUsageEvent",
    "KeyUsageEventTypedDict",
    "Lane",
    "LineType",
    "ListEntry",
    "ListEntryAction",
    "ListEntryKind",
    "ListEntryList",
    "ListEntryListTypedDict",
    "ListEntryRequest",
    "ListEntryRequestTypedDict",
    "ListEntryTypedDict",
    "Location",
    "LocationTypedDict",
    "LocationUnion",
    "LocationUnionTypedDict",
    "NameCandidate",
    "NameCandidateTypedDict",
    "NameCandidateUnion",
    "NameCandidateUnionTypedDict",
    "NotFoundErrorCode",
    "OnExpiry",
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
    "RequestDiagnostic",
    "RequestDiagnosticPage",
    "RequestDiagnosticPageTypedDict",
    "RequestDiagnosticTypedDict",
    "ResponseMode",
    "Risk",
    "RiskConfidence",
    "RiskCoverage",
    "RiskCoverageTypedDict",
    "RiskDetails",
    "RiskDetailsBreachName",
    "RiskDetailsBreachNameTypedDict",
    "RiskDetailsEvent",
    "RiskDetailsEventKind",
    "RiskDetailsEventTypedDict",
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
    "Security",
    "SecurityTypedDict",
    "SentIdentifiers",
    "SentIdentifiersTypedDict",
    "Settings",
    "SettingsFlows",
    "SettingsFlowsTypedDict",
    "SettingsRequest",
    "SettingsRequestFlows",
    "SettingsRequestFlowsTypedDict",
    "SettingsRequestTypedDict",
    "SettingsTypedDict",
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
    "SourceID",
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
    "AccountBinding": ".accountbinding",
    "AccountBindingTypedDict": ".accountbinding",
    "AccountBindingActor": ".accountbindingactor",
    "AccountBindingActorTypedDict": ".accountbindingactor",
    "AccountBindingRequest": ".accountbindingrequest",
    "AccountBindingRequestTypedDict": ".accountbindingrequest",
    "AccountDecision": ".accountdecision",
    "AccountDecisionsByFlow": ".accountdecisionsbyflow",
    "AccountDecisionsByFlowTypedDict": ".accountdecisionsbyflow",
    "AccountDecisionSnapshot": ".accountdecisionsnapshot",
    "AccountDecisionSnapshotTypedDict": ".accountdecisionsnapshot",
    "AccountDeleted": ".accountdeleted",
    "AccountDeletedTypedDict": ".accountdeleted",
    "AccountDeletedEvent": ".accountdeletedevent",
    "AccountDeletedEventTypedDict": ".accountdeletedevent",
    "AccountDeletion": ".accountdeletion",
    "AccountDeletionTypedDict": ".accountdeletion",
    "AccountExport": ".accountexport",
    "AccountExportTypedDict": ".accountexport",
    "Exclusion": ".accountexport",
    "AccountList": ".accountlist",
    "AccountListTypedDict": ".accountlist",
    "AccountOutcome": ".accountoutcome",
    "AccountOutcomeTypedDict": ".accountoutcome",
    "AccountOutcomeActor": ".accountoutcomeactor",
    "AccountOutcomeActorTypedDict": ".accountoutcomeactor",
    "AccountOutcomePage": ".accountoutcomepage",
    "AccountOutcomePageTypedDict": ".accountoutcomepage",
    "AccountOutcomeRequest": ".accountoutcomerequest",
    "AccountOutcomeRequestTypedDict": ".accountoutcomerequest",
    "AccountRisk": ".accountrisk",
    "AccountRiskTypedDict": ".accountrisk",
    "AccountRiskChanged": ".accountriskchanged",
    "AccountRiskChangedTypedDict": ".accountriskchanged",
    "AccountRiskChangedEvent": ".accountriskchangedevent",
    "AccountRiskChangedEventTypedDict": ".accountriskchangedevent",
    "AccountRiskReason": ".accountriskreason",
    "AccountRiskReasonTypedDict": ".accountriskreason",
    "Admission": ".admission",
    "Agreement": ".agreement",
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
    "AssessmentRevision": ".assessmentrevision",
    "AssessmentRevisionTypedDict": ".assessmentrevision",
    "AssessmentSearchPage": ".assessmentsearchpage",
    "AssessmentSearchPageTypedDict": ".assessmentsearchpage",
    "AssessmentSearchRequest": ".assessmentsearchrequest",
    "AssessmentSearchRequestTypedDict": ".assessmentsearchrequest",
    "AssessmentUpdatedData": ".assessmentupdateddata",
    "AssessmentUpdatedDataTypedDict": ".assessmentupdateddata",
    "AssessmentUpdatedEvent": ".assessmentupdatedevent",
    "AssessmentUpdatedEventTypedDict": ".assessmentupdatedevent",
    "AssuranceLevel": ".assurancelevel",
    "AttributeAgreement": ".attributeagreement",
    "AttributeAgreementTypedDict": ".attributeagreement",
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
    "CredentialAssociation": ".credentialassociation",
    "CredentialAssociationTypedDict": ".credentialassociation",
    "CredentialAssociationActor": ".credentialassociationactor",
    "CredentialAssociationActorTypedDict": ".credentialassociationactor",
    "CredentialAssociationRetiredBy": ".credentialassociationretiredby",
    "CredentialAssociationRetiredByTypedDict": ".credentialassociationretiredby",
    "CredentialPage": ".credentialpage",
    "CredentialPageTypedDict": ".credentialpage",
    "CredentialRequest": ".credentialrequest",
    "CredentialRequestTypedDict": ".credentialrequest",
    "Decision": ".decision",
    "DecisionReceipt": ".decisionreceipt",
    "DecisionReceiptTypedDict": ".decisionreceipt",
    "DefaultDepth": ".defaultdepth",
    "Depth": ".depth",
    "Direction": ".direction",
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
    "ExportAssessmentOutcome": ".exportassessmentoutcome",
    "ExportAssessmentOutcomeTypedDict": ".exportassessmentoutcome",
    "Failure": ".failure",
    "FailureReason": ".failurereason",
    "Flow": ".flow",
    "FlowChange": ".flowchange",
    "FlowChangeTypedDict": ".flowchange",
    "FlowSettings": ".flowsettings",
    "FlowSettingsTypedDict": ".flowsettings",
    "Footprint": ".footprint",
    "FootprintTypedDict": ".footprint",
    "FootprintCoherence": ".footprintcoherence",
    "FootprintCoherenceTypedDict": ".footprintcoherence",
    "FootprintFamily": ".footprintfamily",
    "FootprintTimeline": ".footprinttimeline",
    "FootprintTimelineTypedDict": ".footprinttimeline",
    "Freshness": ".freshness",
    "HookPoint": ".hookpoint",
    "Identifier": ".identifier",
    "IdentifierKind": ".identifierkind",
    "Impact": ".impact",
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
    "Key": ".key",
    "KeyScope": ".key",
    "KeyTypedDict": ".key",
    "KeyEnvironment": ".keyenvironment",
    "KeyList": ".keylist",
    "KeyListTypedDict": ".keylist",
    "KeyRequest": ".keyrequest",
    "KeyRequestScope": ".keyrequest",
    "KeyRequestTypedDict": ".keyrequest",
    "KeyRotation": ".keyrotation",
    "KeyRotationScope": ".keyrotation",
    "KeyRotationTypedDict": ".keyrotation",
    "KeyRotationRequest": ".keyrotationrequest",
    "KeyRotationRequestTypedDict": ".keyrotationrequest",
    "KeyStatus": ".keystatus",
    "KeyUsageBatch": ".keyusagebatch",
    "KeyUsageBatchTypedDict": ".keyusagebatch",
    "KeyUsageBatchRequest": ".keyusagebatchrequest",
    "KeyUsageBatchRequestTypedDict": ".keyusagebatchrequest",
    "KeyUsageEvent": ".keyusageevent",
    "KeyUsageEventTypedDict": ".keyusageevent",
    "Lane": ".lane",
    "LineType": ".linetype",
    "ListEntry": ".listentry",
    "ListEntryTypedDict": ".listentry",
    "ListEntryAction": ".listentryaction",
    "ListEntryKind": ".listentrykind",
    "ListEntryList": ".listentrylist",
    "ListEntryListTypedDict": ".listentrylist",
    "ListEntryRequest": ".listentryrequest",
    "ListEntryRequestTypedDict": ".listentryrequest",
    "NotFoundErrorCode": ".notfounderrorcode",
    "OnExpiry": ".onexpiry",
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
    "RequestDiagnostic": ".requestdiagnostic",
    "RequestDiagnosticTypedDict": ".requestdiagnostic",
    "RequestDiagnosticPage": ".requestdiagnosticpage",
    "RequestDiagnosticPageTypedDict": ".requestdiagnosticpage",
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
    "RiskDetailsEvent": ".riskdetailsevent",
    "RiskDetailsEventTypedDict": ".riskdetailsevent",
    "RiskDetailsEventKind": ".riskdetailseventkind",
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
    "SentIdentifiers": ".sentidentifiers",
    "SentIdentifiersTypedDict": ".sentidentifiers",
    "Settings": ".settings",
    "SettingsTypedDict": ".settings",
    "SettingsFlows": ".settingsflows",
    "SettingsFlowsTypedDict": ".settingsflows",
    "SettingsRequest": ".settingsrequest",
    "SettingsRequestTypedDict": ".settingsrequest",
    "SettingsRequestFlows": ".settingsrequestflows",
    "SettingsRequestFlowsTypedDict": ".settingsrequestflows",
    "Signal": ".signal",
    "SignalTypedDict": ".signal",
    "SignalOutcome": ".signaloutcome",
    "SigningKey": ".signingkey",
    "SigningKeyTypedDict": ".signingkey",
    "SigningSecret": ".signingsecret",
    "SigningSecretTypedDict": ".signingsecret",
    "SourceID": ".sourceid",
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
