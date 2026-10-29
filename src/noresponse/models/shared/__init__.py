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
    from .accountdecisionlist import AccountDecisionList, AccountDecisionListTypedDict
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
    from .accountdirectorypage import (
        AccountDirectoryPage,
        AccountDirectoryPageTypedDict,
    )
    from .accountdirectorypageitem import (
        AccountDirectoryPageItem,
        AccountDirectoryPageItemTypedDict,
    )
    from .accountdirectorysearchrequest import (
        AccountDirectorySearchRequest,
        AccountDirectorySearchRequestTypedDict,
    )
    from .accountenforcementlist import (
        AccountEnforcementList,
        AccountEnforcementListTypedDict,
    )
    from .accountexport import AccountExport, AccountExportTypedDict, Exclusion
    from .accountlist import AccountList, AccountListTypedDict
    from .accountoutcome import AccountOutcome, AccountOutcomeTypedDict
    from .accountoutcomeactor import AccountOutcomeActor, AccountOutcomeActorTypedDict
    from .accountoutcomeactortype import AccountOutcomeActorType
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
    from .action import Action
    from .admission import Admission
    from .aggregatebucket import AggregateBucket, AggregateBucketTypedDict
    from .aggregatedimension import AggregateDimension
    from .aggregategroup import AggregateGroup, AggregateGroupTypedDict
    from .aggregategrouplistmatch import AggregateGroupListMatch
    from .aggregatelateflip import AggregateLateFlip, AggregateLateFlipTypedDict
    from .aggregatescorecount import AggregateScoreCount, AggregateScoreCountTypedDict
    from .aggregatescoreoutcome import (
        AggregateScoreOutcome,
        AggregateScoreOutcomeTypedDict,
    )
    from .agreement import Agreement
    from .answerrevision import AnswerRevision
    from .assessment import Assessment, AssessmentTypedDict
    from .assessmentaggregate import (
        AssessmentAggregate,
        AssessmentAggregateMetric,
        AssessmentAggregateTypedDict,
    )
    from .assessmentaggregatecoverage import (
        AssessmentAggregateCoverage,
        AssessmentAggregateCoverageTypedDict,
    )
    from .assessmentaggregaterequest import (
        AssessmentAggregateRequest,
        AssessmentAggregateRequestMetric,
        AssessmentAggregateRequestTypedDict,
    )
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
    from .assessmentsearchitem import (
        AssessmentSearchItem,
        AssessmentSearchItemTypedDict,
    )
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
    from .auditevent import (
        Actor,
        ActorTypedDict,
        AuditEvent,
        AuditEventTypedDict,
        UnknownActor,
    )
    from .auditeventevent import AuditEventEvent, AuditEventEventTypedDict
    from .auditeventlist import AuditEventList, AuditEventListTypedDict
    from .auditeventtarget import AuditEventTarget, AuditEventTargetTypedDict
    from .auditeventtargettype import AuditEventTargetType
    from .auditsettings import AuditSettings, AuditSettingsTypedDict
    from .auditsettingsenvironment import AuditSettingsEnvironment
    from .auditsettingsrequest import (
        AuditSettingsRequest,
        AuditSettingsRequestTypedDict,
    )
    from .auditstream import AuditStream, AuditStreamTypedDict
    from .auditstreamlist import AuditStreamList, AuditStreamListTypedDict
    from .auditstreamreplayrequest import (
        AuditStreamReplayRequest,
        AuditStreamReplayRequestTypedDict,
    )
    from .auditstreamrequest import AuditStreamRequest, AuditStreamRequestTypedDict
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
    from .bucket import Bucket
    from .conclusion import Conclusion
    from .confidence import Confidence
    from .conflicterrorcode import ConflictErrorCode
    from .consistency import Consistency, ConsistencyTypedDict
    from .consistencyvalue import ConsistencyValue
    from .consolelookups import ConsoleLookups, ConsoleLookupsTypedDict
    from .cost import Cost, CostTypedDict
    from .country import Country
    from .coverage import Coverage, CoverageTypedDict
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
    from .customerexport import CustomerExport, CustomerExportTypedDict
    from .customerexportactionrequest import (
        CustomerExportActionRequest,
        CustomerExportActionRequestTypedDict,
    )
    from .customerexportchunk import CustomerExportChunk, CustomerExportChunkTypedDict
    from .customerexportlist import CustomerExportList, CustomerExportListTypedDict
    from .customerexportrequest import (
        CustomerExportRequest,
        CustomerExportRequestTypedDict,
    )
    from .customerexportrequestfilter import (
        CustomerExportRequestFilter,
        CustomerExportRequestFilterTypedDict,
    )
    from .customerexportrequestfilteroutcome import CustomerExportRequestFilterOutcome
    from .customerexportrequestkind import CustomerExportRequestKind
    from .customerexportstatus import CustomerExportStatus
    from .decision import Decision
    from .decisionreceipt import DecisionReceipt, DecisionReceiptTypedDict
    from .delay import Delay
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
    from .enforcements import Enforcements, EnforcementsTypedDict
    from .enforcementstate import EnforcementState
    from .enforcementstatus import EnforcementStatus
    from .environment import Environment
    from .erasurereceipt import ErasureReceipt, ErasureReceiptTypedDict
    from .erasurereceiptkind import ErasureReceiptKind
    from .erasurereceipttarget import (
        ErasureReceiptTarget,
        ErasureReceiptTargetTypedDict,
    )
    from .erasurereceipttargetname import ErasureReceiptTargetName
    from .erasurereceipttargetstatus import ErasureReceiptTargetStatus
    from .export import Export, ExportTypedDict
    from .exportassessmentoutcome import (
        ExportAssessmentOutcome,
        ExportAssessmentOutcomeTypedDict,
    )
    from .failure import Failure
    from .failurereason import FailureReason
    from .filter_ import Filter, FilterTypedDict
    from .flow import Flow
    from .flowchange import FlowChange, FlowChangeTypedDict
    from .flowsettings import FlowSettings, FlowSettingsTypedDict
    from .footprint import Footprint, FootprintTypedDict
    from .footprintcoherence import FootprintCoherence, FootprintCoherenceTypedDict
    from .footprintfamily import FootprintFamily
    from .footprinttimeline import FootprintTimeline, FootprintTimelineTypedDict
    from .freshness import Freshness
    from .from_ import From
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
    from .invite import Invite, InviteDeniedAction, InviteEnvironment, InviteTypedDict
    from .invitelist import InviteList, InviteListTypedDict
    from .inviterequest import (
        InviteRequest,
        InviteRequestDeniedAction,
        InviteRequestEnvironment,
        InviteRequestTypedDict,
    )
    from .inviteresendrequest import InviteResendRequest, InviteResendRequestTypedDict
    from .ipsummary import IPSummary, IPSummaryTypedDict
    from .ipsummarytype import IPSummaryType
    from .key import Key, KeyScope, KeyTypedDict
    from .keyactor import KeyActor, KeyActorTypedDict
    from .keyenvironment import KeyEnvironment
    from .keykind import KeyKind
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
    from .listbulkrequest import ListBulkRequest, ListBulkRequestTypedDict
    from .listchange import ListChange, ListChangeTypedDict
    from .listchangestate import ListChangeState
    from .listentry import ListEntry, ListEntryTypedDict
    from .listentryaction import ListEntryAction
    from .listentrykind import ListEntryKind
    from .listentrylist import ListEntryList, ListEntryListTypedDict
    from .listentryrequest import ListEntryRequest, ListEntryRequestTypedDict
    from .listimpact import ListImpact, ListImpactTypedDict
    from .listimpactkind import ListImpactKind
    from .listimpacttransition import (
        ListImpactTransition,
        ListImpactTransitionTypedDict,
    )
    from .listimpacttransitionfrom import ListImpactTransitionFrom
    from .listmatch import ListMatch
    from .listpreviewrequest import ListPreviewRequest, ListPreviewRequestTypedDict
    from .member import Member, MemberDeniedAction, MemberEnvironment, MemberTypedDict
    from .memberlist import MemberList, MemberListTypedDict
    from .memberstatus import MemberStatus
    from .memberupdaterequest import (
        MemberUpdateRequest,
        MemberUpdateRequestDeniedAction,
        MemberUpdateRequestEnvironment,
        MemberUpdateRequestTypedDict,
    )
    from .metric import Metric
    from .notfounderrorcode import NotFoundErrorCode
    from .onexpiry import OnExpiry
    from .operationalaggregate import (
        OperationalAggregate,
        OperationalAggregateTypedDict,
    )
    from .operationalaggregatebucket import (
        OperationalAggregateBucket,
        OperationalAggregateBucketTypedDict,
    )
    from .operationalaggregatequeue import (
        OperationalAggregateQueue,
        OperationalAggregateQueueTypedDict,
    )
    from .operationalaggregatetotals import (
        OperationalAggregateTotals,
        OperationalAggregateTotalsTypedDict,
    )
    from .outcome import Outcome
    from .outcomes import Outcomes, OutcomesTypedDict
    from .outcomesbyoutcome import OutcomesByOutcome, OutcomesByOutcomeTypedDict
    from .ownertype import OwnerType
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
    from .policyevaluation import PolicyEvaluation, PolicyEvaluationTypedDict
    from .policyevaluationcancelrequest import (
        PolicyEvaluationCancelRequest,
        PolicyEvaluationCancelRequestTypedDict,
    )
    from .policyevaluationlist import (
        PolicyEvaluationList,
        PolicyEvaluationListTypedDict,
    )
    from .policyevaluationpublishrequest import (
        PolicyEvaluationPublishRequest,
        PolicyEvaluationPublishRequestTypedDict,
    )
    from .policyevaluationrequest import (
        PolicyEvaluationRequest,
        PolicyEvaluationRequestTypedDict,
    )
    from .policyevaluationrequestcosts import (
        PolicyEvaluationRequestCosts,
        PolicyEvaluationRequestCostsTypedDict,
    )
    from .policyevaluationrequestlimits import (
        PolicyEvaluationRequestLimits,
        PolicyEvaluationRequestLimitsTypedDict,
    )
    from .policyevaluationresult import (
        PolicyEvaluationResult,
        PolicyEvaluationResultTypedDict,
    )
    from .policyevaluationstatus import PolicyEvaluationStatus
    from .policyhistory import PolicyHistory, PolicyHistoryTypedDict
    from .policyhistoryitem import PolicyHistoryItem, PolicyHistoryItemTypedDict
    from .policypreview import PolicyPreview, PolicyPreviewTypedDict
    from .policypreviewcoverage import (
        PolicyPreviewCoverage,
        PolicyPreviewCoverageTypedDict,
    )
    from .policypreviewrequest import (
        PolicyPreviewRequest,
        PolicyPreviewRequestTypedDict,
    )
    from .policypreviewrequestflows import (
        PolicyPreviewRequestFlows,
        PolicyPreviewRequestFlowsTypedDict,
    )
    from .policypreviewrequestflowsaccountcreation import (
        PolicyPreviewRequestFlowsAccountCreation,
        PolicyPreviewRequestFlowsAccountCreationTypedDict,
    )
    from .policypreviewrequestflowslogin import (
        PolicyPreviewRequestFlowsLogin,
        PolicyPreviewRequestFlowsLoginTypedDict,
    )
    from .policypreviewrequestflowspurchase import (
        PolicyPreviewRequestFlowsPurchase,
        PolicyPreviewRequestFlowsPurchaseTypedDict,
    )
    from .policypreviewtransition import (
        PolicyPreviewTransition,
        PolicyPreviewTransitionTypedDict,
    )
    from .policyrestorerequest import (
        PolicyRestoreRequest,
        PolicyRestoreRequestTypedDict,
    )
    from .population import Population
    from .priority import Priority
    from .probleminvalidparam import ProblemInvalidParam, ProblemInvalidParamTypedDict
    from .publication import Publication, PublicationTypedDict
    from .ratelimiterrorcode import RateLimitErrorCode
    from .reasoncode import ReasonCode
    from .reasonidentifier import ReasonIdentifier
    from .recommendation import Recommendation
    from .report import Report, ReportScope, ReportScopeTypedDict, ReportTypedDict
    from .requestaggregaterequest import (
        RequestAggregateRequest,
        RequestAggregateRequestTypedDict,
    )
    from .requestaggregaterequestbucket import RequestAggregateRequestBucket
    from .requestdiagnostic import RequestDiagnostic, RequestDiagnosticTypedDict
    from .requestdiagnosticpage import (
        RequestDiagnosticPage,
        RequestDiagnosticPageTypedDict,
    )
    from .resolution import Resolution, ResolutionTypedDict
    from .responsemode import ResponseMode
    from .resultstatus import ResultStatus
    from .review import Review, ReviewTypedDict
    from .reviewcomment import ReviewComment, ReviewCommentTypedDict
    from .reviewcommentlist import ReviewCommentList, ReviewCommentListTypedDict
    from .reviewcommentrequest import (
        ReviewCommentRequest,
        ReviewCommentRequestTypedDict,
    )
    from .reviewcreaterequest import ReviewCreateRequest, ReviewCreateRequestTypedDict
    from .reviewlist import ReviewList, ReviewListTypedDict
    from .reviewresolutionlist import (
        ReviewResolutionList,
        ReviewResolutionListTypedDict,
    )
    from .reviewresolverequest import (
        ReviewResolveRequest,
        ReviewResolveRequestTypedDict,
    )
    from .reviews import Reviews, ReviewsTypedDict
    from .reviewsconclusions import ReviewsConclusions, ReviewsConclusionsTypedDict
    from .reviewstatus import ReviewStatus
    from .reviewsubject import ReviewSubject, ReviewSubjectTypedDict
    from .reviewsubjectchange import ReviewSubjectChange, ReviewSubjectChangeTypedDict
    from .reviewsubjectkind import ReviewSubjectKind
    from .reviewsubjectlist import ReviewSubjectList, ReviewSubjectListTypedDict
    from .reviewsubjectrequest import (
        ReviewSubjectRequest,
        ReviewSubjectRequestTypedDict,
    )
    from .reviewupdaterequest import ReviewUpdateRequest, ReviewUpdateRequestTypedDict
    from .reviewupdaterequeststatus import ReviewUpdateRequestStatus
    from .reviewview import ReviewView, ReviewViewTypedDict
    from .reviewviewdeleterequest import (
        ReviewViewDeleteRequest,
        ReviewViewDeleteRequestTypedDict,
    )
    from .reviewviewlist import ReviewViewList, ReviewViewListTypedDict
    from .reviewviewrequest import ReviewViewRequest, ReviewViewRequestTypedDict
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
    from .role import Role
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
    from .source import Source
    from .sourceid import SourceID
    from .status import Status
    from .thresholds import Thresholds, ThresholdsTypedDict
    from .transport import Transport
    from .usage import Usage, UsageTypedDict
    from .usagecount import UsageCount, UsageCountTypedDict
    from .usagecountdepth import UsageCountDepth
    from .usagecountflow import UsageCountFlow
    from .useractor import UserActor, UserActorTypedDict
    from .webhookaggregaterequest import (
        WebhookAggregateRequest,
        WebhookAggregateRequestTypedDict,
    )
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
    from .workspaceoperationssummary import (
        WorkspaceOperationsSummary,
        WorkspaceOperationsSummaryTypedDict,
    )
    from .workspaceoperationssummaryrequest import (
        WorkspaceOperationsSummaryRequest,
        WorkspaceOperationsSummaryRequestTypedDict,
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
    "AccountDecisionList",
    "AccountDecisionListTypedDict",
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
    "AccountDirectoryPage",
    "AccountDirectoryPageItem",
    "AccountDirectoryPageItemTypedDict",
    "AccountDirectoryPageTypedDict",
    "AccountDirectorySearchRequest",
    "AccountDirectorySearchRequestTypedDict",
    "AccountEnforcementList",
    "AccountEnforcementListTypedDict",
    "AccountExport",
    "AccountExportTypedDict",
    "AccountList",
    "AccountListTypedDict",
    "AccountOutcome",
    "AccountOutcomeActor",
    "AccountOutcomeActorType",
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
    "Action",
    "Actor",
    "ActorTypedDict",
    "Admission",
    "AggregateBucket",
    "AggregateBucketTypedDict",
    "AggregateDimension",
    "AggregateGroup",
    "AggregateGroupListMatch",
    "AggregateGroupTypedDict",
    "AggregateLateFlip",
    "AggregateLateFlipTypedDict",
    "AggregateScoreCount",
    "AggregateScoreCountTypedDict",
    "AggregateScoreOutcome",
    "AggregateScoreOutcomeTypedDict",
    "Agreement",
    "AlternateName",
    "AlternateNameTypedDict",
    "AlternateNameUnion",
    "AlternateNameUnionTypedDict",
    "AnswerRevision",
    "Assessment",
    "AssessmentAggregate",
    "AssessmentAggregateCoverage",
    "AssessmentAggregateCoverageTypedDict",
    "AssessmentAggregateMetric",
    "AssessmentAggregateRequest",
    "AssessmentAggregateRequestMetric",
    "AssessmentAggregateRequestTypedDict",
    "AssessmentAggregateTypedDict",
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
    "AssessmentSearchItem",
    "AssessmentSearchItemTypedDict",
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
    "AuditEvent",
    "AuditEventEvent",
    "AuditEventEventTypedDict",
    "AuditEventList",
    "AuditEventListTypedDict",
    "AuditEventTarget",
    "AuditEventTargetType",
    "AuditEventTargetTypedDict",
    "AuditEventTypedDict",
    "AuditSettings",
    "AuditSettingsEnvironment",
    "AuditSettingsRequest",
    "AuditSettingsRequestTypedDict",
    "AuditSettingsTypedDict",
    "AuditStream",
    "AuditStreamList",
    "AuditStreamListTypedDict",
    "AuditStreamReplayRequest",
    "AuditStreamReplayRequestTypedDict",
    "AuditStreamRequest",
    "AuditStreamRequestTypedDict",
    "AuditStreamTypedDict",
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
    "Bucket",
    "Conclusion",
    "Confidence",
    "ConflictErrorCode",
    "Consistency",
    "ConsistencyTypedDict",
    "ConsistencyValue",
    "ConsoleLookups",
    "ConsoleLookupsTypedDict",
    "Cost",
    "CostTypedDict",
    "Country",
    "Coverage",
    "CoverageTypedDict",
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
    "CustomerExport",
    "CustomerExportActionRequest",
    "CustomerExportActionRequestTypedDict",
    "CustomerExportChunk",
    "CustomerExportChunkTypedDict",
    "CustomerExportList",
    "CustomerExportListTypedDict",
    "CustomerExportRequest",
    "CustomerExportRequestFilter",
    "CustomerExportRequestFilterOutcome",
    "CustomerExportRequestFilterTypedDict",
    "CustomerExportRequestKind",
    "CustomerExportRequestTypedDict",
    "CustomerExportStatus",
    "CustomerExportTypedDict",
    "Decision",
    "DecisionReceipt",
    "DecisionReceiptTypedDict",
    "Delay",
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
    "Enforcements",
    "EnforcementsTypedDict",
    "Environment",
    "ErasureReceipt",
    "ErasureReceiptKind",
    "ErasureReceiptTarget",
    "ErasureReceiptTargetName",
    "ErasureReceiptTargetStatus",
    "ErasureReceiptTargetTypedDict",
    "ErasureReceiptTypedDict",
    "Exclusion",
    "Export",
    "ExportAssessmentOutcome",
    "ExportAssessmentOutcomeTypedDict",
    "ExportTypedDict",
    "Failure",
    "FailureReason",
    "Filter",
    "FilterTypedDict",
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
    "From",
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
    "Invite",
    "InviteDeniedAction",
    "InviteEnvironment",
    "InviteList",
    "InviteListTypedDict",
    "InviteRequest",
    "InviteRequestDeniedAction",
    "InviteRequestEnvironment",
    "InviteRequestTypedDict",
    "InviteResendRequest",
    "InviteResendRequestTypedDict",
    "InviteTypedDict",
    "Key",
    "KeyActor",
    "KeyActorTypedDict",
    "KeyEnvironment",
    "KeyKind",
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
    "ListBulkRequest",
    "ListBulkRequestTypedDict",
    "ListChange",
    "ListChangeState",
    "ListChangeTypedDict",
    "ListEntry",
    "ListEntryAction",
    "ListEntryKind",
    "ListEntryList",
    "ListEntryListTypedDict",
    "ListEntryRequest",
    "ListEntryRequestTypedDict",
    "ListEntryTypedDict",
    "ListImpact",
    "ListImpactKind",
    "ListImpactTransition",
    "ListImpactTransitionFrom",
    "ListImpactTransitionTypedDict",
    "ListImpactTypedDict",
    "ListMatch",
    "ListPreviewRequest",
    "ListPreviewRequestTypedDict",
    "Location",
    "LocationTypedDict",
    "LocationUnion",
    "LocationUnionTypedDict",
    "Member",
    "MemberDeniedAction",
    "MemberEnvironment",
    "MemberList",
    "MemberListTypedDict",
    "MemberStatus",
    "MemberTypedDict",
    "MemberUpdateRequest",
    "MemberUpdateRequestDeniedAction",
    "MemberUpdateRequestEnvironment",
    "MemberUpdateRequestTypedDict",
    "Metric",
    "NameCandidate",
    "NameCandidateTypedDict",
    "NameCandidateUnion",
    "NameCandidateUnionTypedDict",
    "NotFoundErrorCode",
    "OnExpiry",
    "OperationalAggregate",
    "OperationalAggregateBucket",
    "OperationalAggregateBucketTypedDict",
    "OperationalAggregateQueue",
    "OperationalAggregateQueueTypedDict",
    "OperationalAggregateTotals",
    "OperationalAggregateTotalsTypedDict",
    "OperationalAggregateTypedDict",
    "Outcome",
    "Outcomes",
    "OutcomesByOutcome",
    "OutcomesByOutcomeTypedDict",
    "OutcomesTypedDict",
    "OwnerType",
    "PermissionDeniedErrorCode",
    "PhoneEnrichment",
    "PhoneEnrichmentFields",
    "PhoneEnrichmentFieldsTypedDict",
    "PhoneEnrichmentTypedDict",
    "Platform",
    "PolicyEvaluation",
    "PolicyEvaluationCancelRequest",
    "PolicyEvaluationCancelRequestTypedDict",
    "PolicyEvaluationList",
    "PolicyEvaluationListTypedDict",
    "PolicyEvaluationPublishRequest",
    "PolicyEvaluationPublishRequestTypedDict",
    "PolicyEvaluationRequest",
    "PolicyEvaluationRequestCosts",
    "PolicyEvaluationRequestCostsTypedDict",
    "PolicyEvaluationRequestLimits",
    "PolicyEvaluationRequestLimitsTypedDict",
    "PolicyEvaluationRequestTypedDict",
    "PolicyEvaluationResult",
    "PolicyEvaluationResultTypedDict",
    "PolicyEvaluationStatus",
    "PolicyEvaluationTypedDict",
    "PolicyHistory",
    "PolicyHistoryItem",
    "PolicyHistoryItemTypedDict",
    "PolicyHistoryTypedDict",
    "PolicyPreview",
    "PolicyPreviewCoverage",
    "PolicyPreviewCoverageTypedDict",
    "PolicyPreviewRequest",
    "PolicyPreviewRequestFlows",
    "PolicyPreviewRequestFlowsAccountCreation",
    "PolicyPreviewRequestFlowsAccountCreationTypedDict",
    "PolicyPreviewRequestFlowsLogin",
    "PolicyPreviewRequestFlowsLoginTypedDict",
    "PolicyPreviewRequestFlowsPurchase",
    "PolicyPreviewRequestFlowsPurchaseTypedDict",
    "PolicyPreviewRequestFlowsTypedDict",
    "PolicyPreviewRequestTypedDict",
    "PolicyPreviewTransition",
    "PolicyPreviewTransitionTypedDict",
    "PolicyPreviewTypedDict",
    "PolicyRestoreRequest",
    "PolicyRestoreRequestTypedDict",
    "Population",
    "Priority",
    "ProblemInvalidParam",
    "ProblemInvalidParamTypedDict",
    "Publication",
    "PublicationTypedDict",
    "RateLimitErrorCode",
    "ReasonCode",
    "ReasonIdentifier",
    "Recommendation",
    "Report",
    "ReportScope",
    "ReportScopeTypedDict",
    "ReportTypedDict",
    "RequestAggregateRequest",
    "RequestAggregateRequestBucket",
    "RequestAggregateRequestTypedDict",
    "RequestDiagnostic",
    "RequestDiagnosticPage",
    "RequestDiagnosticPageTypedDict",
    "RequestDiagnosticTypedDict",
    "Resolution",
    "ResolutionTypedDict",
    "ResponseMode",
    "ResultStatus",
    "Review",
    "ReviewComment",
    "ReviewCommentList",
    "ReviewCommentListTypedDict",
    "ReviewCommentRequest",
    "ReviewCommentRequestTypedDict",
    "ReviewCommentTypedDict",
    "ReviewCreateRequest",
    "ReviewCreateRequestTypedDict",
    "ReviewList",
    "ReviewListTypedDict",
    "ReviewResolutionList",
    "ReviewResolutionListTypedDict",
    "ReviewResolveRequest",
    "ReviewResolveRequestTypedDict",
    "ReviewStatus",
    "ReviewSubject",
    "ReviewSubjectChange",
    "ReviewSubjectChangeTypedDict",
    "ReviewSubjectKind",
    "ReviewSubjectList",
    "ReviewSubjectListTypedDict",
    "ReviewSubjectRequest",
    "ReviewSubjectRequestTypedDict",
    "ReviewSubjectTypedDict",
    "ReviewTypedDict",
    "ReviewUpdateRequest",
    "ReviewUpdateRequestStatus",
    "ReviewUpdateRequestTypedDict",
    "ReviewView",
    "ReviewViewDeleteRequest",
    "ReviewViewDeleteRequestTypedDict",
    "ReviewViewList",
    "ReviewViewListTypedDict",
    "ReviewViewRequest",
    "ReviewViewRequestTypedDict",
    "ReviewViewTypedDict",
    "Reviews",
    "ReviewsConclusions",
    "ReviewsConclusionsTypedDict",
    "ReviewsTypedDict",
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
    "Role",
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
    "Source",
    "SourceID",
    "Status",
    "Thresholds",
    "ThresholdsTypedDict",
    "Timezone",
    "TimezoneTypedDict",
    "TimezoneUnion",
    "TimezoneUnionTypedDict",
    "Transport",
    "UnknownActor",
    "Usage",
    "UsageCount",
    "UsageCountDepth",
    "UsageCountFlow",
    "UsageCountTypedDict",
    "UsageTypedDict",
    "UserActor",
    "UserActorTypedDict",
    "WebhookAggregateRequest",
    "WebhookAggregateRequestTypedDict",
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
    "WorkspaceOperationsSummary",
    "WorkspaceOperationsSummaryRequest",
    "WorkspaceOperationsSummaryRequestTypedDict",
    "WorkspaceOperationsSummaryTypedDict",
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
    "AccountDecisionList": ".accountdecisionlist",
    "AccountDecisionListTypedDict": ".accountdecisionlist",
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
    "AccountDirectoryPage": ".accountdirectorypage",
    "AccountDirectoryPageTypedDict": ".accountdirectorypage",
    "AccountDirectoryPageItem": ".accountdirectorypageitem",
    "AccountDirectoryPageItemTypedDict": ".accountdirectorypageitem",
    "AccountDirectorySearchRequest": ".accountdirectorysearchrequest",
    "AccountDirectorySearchRequestTypedDict": ".accountdirectorysearchrequest",
    "AccountEnforcementList": ".accountenforcementlist",
    "AccountEnforcementListTypedDict": ".accountenforcementlist",
    "AccountExport": ".accountexport",
    "AccountExportTypedDict": ".accountexport",
    "Exclusion": ".accountexport",
    "AccountList": ".accountlist",
    "AccountListTypedDict": ".accountlist",
    "AccountOutcome": ".accountoutcome",
    "AccountOutcomeTypedDict": ".accountoutcome",
    "AccountOutcomeActor": ".accountoutcomeactor",
    "AccountOutcomeActorTypedDict": ".accountoutcomeactor",
    "AccountOutcomeActorType": ".accountoutcomeactortype",
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
    "Action": ".action",
    "Admission": ".admission",
    "AggregateBucket": ".aggregatebucket",
    "AggregateBucketTypedDict": ".aggregatebucket",
    "AggregateDimension": ".aggregatedimension",
    "AggregateGroup": ".aggregategroup",
    "AggregateGroupTypedDict": ".aggregategroup",
    "AggregateGroupListMatch": ".aggregategrouplistmatch",
    "AggregateLateFlip": ".aggregatelateflip",
    "AggregateLateFlipTypedDict": ".aggregatelateflip",
    "AggregateScoreCount": ".aggregatescorecount",
    "AggregateScoreCountTypedDict": ".aggregatescorecount",
    "AggregateScoreOutcome": ".aggregatescoreoutcome",
    "AggregateScoreOutcomeTypedDict": ".aggregatescoreoutcome",
    "Agreement": ".agreement",
    "AnswerRevision": ".answerrevision",
    "Assessment": ".assessment",
    "AssessmentTypedDict": ".assessment",
    "AssessmentAggregate": ".assessmentaggregate",
    "AssessmentAggregateMetric": ".assessmentaggregate",
    "AssessmentAggregateTypedDict": ".assessmentaggregate",
    "AssessmentAggregateCoverage": ".assessmentaggregatecoverage",
    "AssessmentAggregateCoverageTypedDict": ".assessmentaggregatecoverage",
    "AssessmentAggregateRequest": ".assessmentaggregaterequest",
    "AssessmentAggregateRequestMetric": ".assessmentaggregaterequest",
    "AssessmentAggregateRequestTypedDict": ".assessmentaggregaterequest",
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
    "AssessmentSearchItem": ".assessmentsearchitem",
    "AssessmentSearchItemTypedDict": ".assessmentsearchitem",
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
    "Actor": ".auditevent",
    "ActorTypedDict": ".auditevent",
    "AuditEvent": ".auditevent",
    "AuditEventTypedDict": ".auditevent",
    "UnknownActor": ".auditevent",
    "AuditEventEvent": ".auditeventevent",
    "AuditEventEventTypedDict": ".auditeventevent",
    "AuditEventList": ".auditeventlist",
    "AuditEventListTypedDict": ".auditeventlist",
    "AuditEventTarget": ".auditeventtarget",
    "AuditEventTargetTypedDict": ".auditeventtarget",
    "AuditEventTargetType": ".auditeventtargettype",
    "AuditSettings": ".auditsettings",
    "AuditSettingsTypedDict": ".auditsettings",
    "AuditSettingsEnvironment": ".auditsettingsenvironment",
    "AuditSettingsRequest": ".auditsettingsrequest",
    "AuditSettingsRequestTypedDict": ".auditsettingsrequest",
    "AuditStream": ".auditstream",
    "AuditStreamTypedDict": ".auditstream",
    "AuditStreamList": ".auditstreamlist",
    "AuditStreamListTypedDict": ".auditstreamlist",
    "AuditStreamReplayRequest": ".auditstreamreplayrequest",
    "AuditStreamReplayRequestTypedDict": ".auditstreamreplayrequest",
    "AuditStreamRequest": ".auditstreamrequest",
    "AuditStreamRequestTypedDict": ".auditstreamrequest",
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
    "Bucket": ".bucket",
    "Conclusion": ".conclusion",
    "Confidence": ".confidence",
    "ConflictErrorCode": ".conflicterrorcode",
    "Consistency": ".consistency",
    "ConsistencyTypedDict": ".consistency",
    "ConsistencyValue": ".consistencyvalue",
    "ConsoleLookups": ".consolelookups",
    "ConsoleLookupsTypedDict": ".consolelookups",
    "Cost": ".cost",
    "CostTypedDict": ".cost",
    "Country": ".country",
    "Coverage": ".coverage",
    "CoverageTypedDict": ".coverage",
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
    "CustomerExport": ".customerexport",
    "CustomerExportTypedDict": ".customerexport",
    "CustomerExportActionRequest": ".customerexportactionrequest",
    "CustomerExportActionRequestTypedDict": ".customerexportactionrequest",
    "CustomerExportChunk": ".customerexportchunk",
    "CustomerExportChunkTypedDict": ".customerexportchunk",
    "CustomerExportList": ".customerexportlist",
    "CustomerExportListTypedDict": ".customerexportlist",
    "CustomerExportRequest": ".customerexportrequest",
    "CustomerExportRequestTypedDict": ".customerexportrequest",
    "CustomerExportRequestFilter": ".customerexportrequestfilter",
    "CustomerExportRequestFilterTypedDict": ".customerexportrequestfilter",
    "CustomerExportRequestFilterOutcome": ".customerexportrequestfilteroutcome",
    "CustomerExportRequestKind": ".customerexportrequestkind",
    "CustomerExportStatus": ".customerexportstatus",
    "Decision": ".decision",
    "DecisionReceipt": ".decisionreceipt",
    "DecisionReceiptTypedDict": ".decisionreceipt",
    "Delay": ".delay",
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
    "Enforcements": ".enforcements",
    "EnforcementsTypedDict": ".enforcements",
    "EnforcementState": ".enforcementstate",
    "EnforcementStatus": ".enforcementstatus",
    "Environment": ".environment",
    "ErasureReceipt": ".erasurereceipt",
    "ErasureReceiptTypedDict": ".erasurereceipt",
    "ErasureReceiptKind": ".erasurereceiptkind",
    "ErasureReceiptTarget": ".erasurereceipttarget",
    "ErasureReceiptTargetTypedDict": ".erasurereceipttarget",
    "ErasureReceiptTargetName": ".erasurereceipttargetname",
    "ErasureReceiptTargetStatus": ".erasurereceipttargetstatus",
    "Export": ".export",
    "ExportTypedDict": ".export",
    "ExportAssessmentOutcome": ".exportassessmentoutcome",
    "ExportAssessmentOutcomeTypedDict": ".exportassessmentoutcome",
    "Failure": ".failure",
    "FailureReason": ".failurereason",
    "Filter": ".filter_",
    "FilterTypedDict": ".filter_",
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
    "From": ".from_",
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
    "Invite": ".invite",
    "InviteDeniedAction": ".invite",
    "InviteEnvironment": ".invite",
    "InviteTypedDict": ".invite",
    "InviteList": ".invitelist",
    "InviteListTypedDict": ".invitelist",
    "InviteRequest": ".inviterequest",
    "InviteRequestDeniedAction": ".inviterequest",
    "InviteRequestEnvironment": ".inviterequest",
    "InviteRequestTypedDict": ".inviterequest",
    "InviteResendRequest": ".inviteresendrequest",
    "InviteResendRequestTypedDict": ".inviteresendrequest",
    "IPSummary": ".ipsummary",
    "IPSummaryTypedDict": ".ipsummary",
    "IPSummaryType": ".ipsummarytype",
    "Key": ".key",
    "KeyScope": ".key",
    "KeyTypedDict": ".key",
    "KeyActor": ".keyactor",
    "KeyActorTypedDict": ".keyactor",
    "KeyEnvironment": ".keyenvironment",
    "KeyKind": ".keykind",
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
    "ListBulkRequest": ".listbulkrequest",
    "ListBulkRequestTypedDict": ".listbulkrequest",
    "ListChange": ".listchange",
    "ListChangeTypedDict": ".listchange",
    "ListChangeState": ".listchangestate",
    "ListEntry": ".listentry",
    "ListEntryTypedDict": ".listentry",
    "ListEntryAction": ".listentryaction",
    "ListEntryKind": ".listentrykind",
    "ListEntryList": ".listentrylist",
    "ListEntryListTypedDict": ".listentrylist",
    "ListEntryRequest": ".listentryrequest",
    "ListEntryRequestTypedDict": ".listentryrequest",
    "ListImpact": ".listimpact",
    "ListImpactTypedDict": ".listimpact",
    "ListImpactKind": ".listimpactkind",
    "ListImpactTransition": ".listimpacttransition",
    "ListImpactTransitionTypedDict": ".listimpacttransition",
    "ListImpactTransitionFrom": ".listimpacttransitionfrom",
    "ListMatch": ".listmatch",
    "ListPreviewRequest": ".listpreviewrequest",
    "ListPreviewRequestTypedDict": ".listpreviewrequest",
    "Member": ".member",
    "MemberDeniedAction": ".member",
    "MemberEnvironment": ".member",
    "MemberTypedDict": ".member",
    "MemberList": ".memberlist",
    "MemberListTypedDict": ".memberlist",
    "MemberStatus": ".memberstatus",
    "MemberUpdateRequest": ".memberupdaterequest",
    "MemberUpdateRequestDeniedAction": ".memberupdaterequest",
    "MemberUpdateRequestEnvironment": ".memberupdaterequest",
    "MemberUpdateRequestTypedDict": ".memberupdaterequest",
    "Metric": ".metric",
    "NotFoundErrorCode": ".notfounderrorcode",
    "OnExpiry": ".onexpiry",
    "OperationalAggregate": ".operationalaggregate",
    "OperationalAggregateTypedDict": ".operationalaggregate",
    "OperationalAggregateBucket": ".operationalaggregatebucket",
    "OperationalAggregateBucketTypedDict": ".operationalaggregatebucket",
    "OperationalAggregateQueue": ".operationalaggregatequeue",
    "OperationalAggregateQueueTypedDict": ".operationalaggregatequeue",
    "OperationalAggregateTotals": ".operationalaggregatetotals",
    "OperationalAggregateTotalsTypedDict": ".operationalaggregatetotals",
    "Outcome": ".outcome",
    "Outcomes": ".outcomes",
    "OutcomesTypedDict": ".outcomes",
    "OutcomesByOutcome": ".outcomesbyoutcome",
    "OutcomesByOutcomeTypedDict": ".outcomesbyoutcome",
    "OwnerType": ".ownertype",
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
    "PolicyEvaluation": ".policyevaluation",
    "PolicyEvaluationTypedDict": ".policyevaluation",
    "PolicyEvaluationCancelRequest": ".policyevaluationcancelrequest",
    "PolicyEvaluationCancelRequestTypedDict": ".policyevaluationcancelrequest",
    "PolicyEvaluationList": ".policyevaluationlist",
    "PolicyEvaluationListTypedDict": ".policyevaluationlist",
    "PolicyEvaluationPublishRequest": ".policyevaluationpublishrequest",
    "PolicyEvaluationPublishRequestTypedDict": ".policyevaluationpublishrequest",
    "PolicyEvaluationRequest": ".policyevaluationrequest",
    "PolicyEvaluationRequestTypedDict": ".policyevaluationrequest",
    "PolicyEvaluationRequestCosts": ".policyevaluationrequestcosts",
    "PolicyEvaluationRequestCostsTypedDict": ".policyevaluationrequestcosts",
    "PolicyEvaluationRequestLimits": ".policyevaluationrequestlimits",
    "PolicyEvaluationRequestLimitsTypedDict": ".policyevaluationrequestlimits",
    "PolicyEvaluationResult": ".policyevaluationresult",
    "PolicyEvaluationResultTypedDict": ".policyevaluationresult",
    "PolicyEvaluationStatus": ".policyevaluationstatus",
    "PolicyHistory": ".policyhistory",
    "PolicyHistoryTypedDict": ".policyhistory",
    "PolicyHistoryItem": ".policyhistoryitem",
    "PolicyHistoryItemTypedDict": ".policyhistoryitem",
    "PolicyPreview": ".policypreview",
    "PolicyPreviewTypedDict": ".policypreview",
    "PolicyPreviewCoverage": ".policypreviewcoverage",
    "PolicyPreviewCoverageTypedDict": ".policypreviewcoverage",
    "PolicyPreviewRequest": ".policypreviewrequest",
    "PolicyPreviewRequestTypedDict": ".policypreviewrequest",
    "PolicyPreviewRequestFlows": ".policypreviewrequestflows",
    "PolicyPreviewRequestFlowsTypedDict": ".policypreviewrequestflows",
    "PolicyPreviewRequestFlowsAccountCreation": ".policypreviewrequestflowsaccountcreation",
    "PolicyPreviewRequestFlowsAccountCreationTypedDict": ".policypreviewrequestflowsaccountcreation",
    "PolicyPreviewRequestFlowsLogin": ".policypreviewrequestflowslogin",
    "PolicyPreviewRequestFlowsLoginTypedDict": ".policypreviewrequestflowslogin",
    "PolicyPreviewRequestFlowsPurchase": ".policypreviewrequestflowspurchase",
    "PolicyPreviewRequestFlowsPurchaseTypedDict": ".policypreviewrequestflowspurchase",
    "PolicyPreviewTransition": ".policypreviewtransition",
    "PolicyPreviewTransitionTypedDict": ".policypreviewtransition",
    "PolicyRestoreRequest": ".policyrestorerequest",
    "PolicyRestoreRequestTypedDict": ".policyrestorerequest",
    "Population": ".population",
    "Priority": ".priority",
    "ProblemInvalidParam": ".probleminvalidparam",
    "ProblemInvalidParamTypedDict": ".probleminvalidparam",
    "Publication": ".publication",
    "PublicationTypedDict": ".publication",
    "RateLimitErrorCode": ".ratelimiterrorcode",
    "ReasonCode": ".reasoncode",
    "ReasonIdentifier": ".reasonidentifier",
    "Recommendation": ".recommendation",
    "Report": ".report",
    "ReportScope": ".report",
    "ReportScopeTypedDict": ".report",
    "ReportTypedDict": ".report",
    "RequestAggregateRequest": ".requestaggregaterequest",
    "RequestAggregateRequestTypedDict": ".requestaggregaterequest",
    "RequestAggregateRequestBucket": ".requestaggregaterequestbucket",
    "RequestDiagnostic": ".requestdiagnostic",
    "RequestDiagnosticTypedDict": ".requestdiagnostic",
    "RequestDiagnosticPage": ".requestdiagnosticpage",
    "RequestDiagnosticPageTypedDict": ".requestdiagnosticpage",
    "Resolution": ".resolution",
    "ResolutionTypedDict": ".resolution",
    "ResponseMode": ".responsemode",
    "ResultStatus": ".resultstatus",
    "Review": ".review",
    "ReviewTypedDict": ".review",
    "ReviewComment": ".reviewcomment",
    "ReviewCommentTypedDict": ".reviewcomment",
    "ReviewCommentList": ".reviewcommentlist",
    "ReviewCommentListTypedDict": ".reviewcommentlist",
    "ReviewCommentRequest": ".reviewcommentrequest",
    "ReviewCommentRequestTypedDict": ".reviewcommentrequest",
    "ReviewCreateRequest": ".reviewcreaterequest",
    "ReviewCreateRequestTypedDict": ".reviewcreaterequest",
    "ReviewList": ".reviewlist",
    "ReviewListTypedDict": ".reviewlist",
    "ReviewResolutionList": ".reviewresolutionlist",
    "ReviewResolutionListTypedDict": ".reviewresolutionlist",
    "ReviewResolveRequest": ".reviewresolverequest",
    "ReviewResolveRequestTypedDict": ".reviewresolverequest",
    "Reviews": ".reviews",
    "ReviewsTypedDict": ".reviews",
    "ReviewsConclusions": ".reviewsconclusions",
    "ReviewsConclusionsTypedDict": ".reviewsconclusions",
    "ReviewStatus": ".reviewstatus",
    "ReviewSubject": ".reviewsubject",
    "ReviewSubjectTypedDict": ".reviewsubject",
    "ReviewSubjectChange": ".reviewsubjectchange",
    "ReviewSubjectChangeTypedDict": ".reviewsubjectchange",
    "ReviewSubjectKind": ".reviewsubjectkind",
    "ReviewSubjectList": ".reviewsubjectlist",
    "ReviewSubjectListTypedDict": ".reviewsubjectlist",
    "ReviewSubjectRequest": ".reviewsubjectrequest",
    "ReviewSubjectRequestTypedDict": ".reviewsubjectrequest",
    "ReviewUpdateRequest": ".reviewupdaterequest",
    "ReviewUpdateRequestTypedDict": ".reviewupdaterequest",
    "ReviewUpdateRequestStatus": ".reviewupdaterequeststatus",
    "ReviewView": ".reviewview",
    "ReviewViewTypedDict": ".reviewview",
    "ReviewViewDeleteRequest": ".reviewviewdeleterequest",
    "ReviewViewDeleteRequestTypedDict": ".reviewviewdeleterequest",
    "ReviewViewList": ".reviewviewlist",
    "ReviewViewListTypedDict": ".reviewviewlist",
    "ReviewViewRequest": ".reviewviewrequest",
    "ReviewViewRequestTypedDict": ".reviewviewrequest",
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
    "Role": ".role",
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
    "Source": ".source",
    "SourceID": ".sourceid",
    "Status": ".status",
    "Thresholds": ".thresholds",
    "ThresholdsTypedDict": ".thresholds",
    "Transport": ".transport",
    "Usage": ".usage",
    "UsageTypedDict": ".usage",
    "UsageCount": ".usagecount",
    "UsageCountTypedDict": ".usagecount",
    "UsageCountDepth": ".usagecountdepth",
    "UsageCountFlow": ".usagecountflow",
    "UserActor": ".useractor",
    "UserActorTypedDict": ".useractor",
    "WebhookAggregateRequest": ".webhookaggregaterequest",
    "WebhookAggregateRequestTypedDict": ".webhookaggregaterequest",
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
    "WorkspaceOperationsSummary": ".workspaceoperationssummary",
    "WorkspaceOperationsSummaryTypedDict": ".workspaceoperationssummary",
    "WorkspaceOperationsSummaryRequest": ".workspaceoperationssummaryrequest",
    "WorkspaceOperationsSummaryRequestTypedDict": ".workspaceoperationssummaryrequest",
}


def __getattr__(attr_name: str) -> Any:
    return lazy_getattr(
        attr_name, package=__package__, dynamic_imports=_dynamic_imports
    )


def __dir__():
    return lazy_dir(dynamic_imports=_dynamic_imports)
