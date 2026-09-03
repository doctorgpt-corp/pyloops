"""Contains all the data models used in inputs/outputs"""

from .activity_condition import ActivityCondition
from .activity_condition_action import ActivityConditionAction
from .activity_condition_target import ActivityConditionTarget
from .activity_condition_type import ActivityConditionType
from .add_to_list_trigger_workflow_mutation_node import AddToListTriggerWorkflowMutationNode
from .add_to_list_trigger_workflow_mutation_node_type_name import AddToListTriggerWorkflowMutationNodeTypeName
from .add_to_list_trigger_workflow_mutation_node_with_revision import AddToListTriggerWorkflowMutationNodeWithRevision
from .add_to_list_trigger_workflow_node import AddToListTriggerWorkflowNode
from .add_to_list_trigger_workflow_node_type_name import AddToListTriggerWorkflowNodeTypeName
from .add_workflow_branch_request import AddWorkflowBranchRequest
from .add_workflow_branch_response import AddWorkflowBranchResponse
from .audience_filter_in_request_type_0 import AudienceFilterInRequestType0
from .audience_filter_in_request_type_0_match import AudienceFilterInRequestType0Match
from .audience_filter_type_0 import AudienceFilterType0
from .audience_filter_type_0_match import AudienceFilterType0Match
from .audience_filter_workflow_mutation_node import AudienceFilterWorkflowMutationNode
from .audience_filter_workflow_mutation_node_type_name import AudienceFilterWorkflowMutationNodeTypeName
from .audience_filter_workflow_mutation_node_with_revision import AudienceFilterWorkflowMutationNodeWithRevision
from .audience_filter_workflow_node import AudienceFilterWorkflowNode
from .audience_filter_workflow_node_type_name import AudienceFilterWorkflowNodeTypeName
from .audience_segment import AudienceSegment
from .audience_segment_failure_response import AudienceSegmentFailureResponse
from .audience_segment_response import AudienceSegmentResponse
from .blank_trigger_workflow_mutation_node import BlankTriggerWorkflowMutationNode
from .blank_trigger_workflow_mutation_node_type_name import BlankTriggerWorkflowMutationNodeTypeName
from .blank_trigger_workflow_mutation_node_with_revision import BlankTriggerWorkflowMutationNodeWithRevision
from .blank_trigger_workflow_node import BlankTriggerWorkflowNode
from .blank_trigger_workflow_node_type_name import BlankTriggerWorkflowNodeTypeName
from .branch_workflow_mutation_node import BranchWorkflowMutationNode
from .branch_workflow_mutation_node_type_name import BranchWorkflowMutationNodeTypeName
from .branch_workflow_mutation_node_with_revision import BranchWorkflowMutationNodeWithRevision
from .branch_workflow_node import BranchWorkflowNode
from .branch_workflow_node_type_name import BranchWorkflowNodeTypeName
from .campaign_failure_response import CampaignFailureResponse
from .campaign_list_item import CampaignListItem
from .campaign_list_item_status import CampaignListItemStatus
from .campaign_response import CampaignResponse
from .campaign_response_status import CampaignResponseStatus
from .campaign_scheduling import CampaignScheduling
from .campaign_scheduling_method import CampaignSchedulingMethod
from .campaign_scheduling_request import CampaignSchedulingRequest
from .campaign_scheduling_request_method import CampaignSchedulingRequestMethod
from .change_workflow_mailing_list_request import ChangeWorkflowMailingListRequest
from .complete_upload_response import CompleteUploadResponse
from .component import Component
from .component_failure_response import ComponentFailureResponse
from .component_response import ComponentResponse
from .component_validation_failure_response import ComponentValidationFailureResponse
from .contact import Contact
from .contact_delete_request import ContactDeleteRequest
from .contact_delete_response import ContactDeleteResponse
from .contact_failure_response import ContactFailureResponse
from .contact_fields import ContactFields
from .contact_mailing_lists import ContactMailingLists
from .contact_opt_in_status_type_1 import ContactOptInStatusType1
from .contact_opt_in_status_type_2_type_1 import ContactOptInStatusType2Type1
from .contact_opt_in_status_type_3_type_1 import ContactOptInStatusType3Type1
from .contact_property import ContactProperty
from .contact_property_create_request import ContactPropertyCreateRequest
from .contact_property_create_request_type import ContactPropertyCreateRequestType
from .contact_property_failure_response import ContactPropertyFailureResponse
from .contact_property_success_response import ContactPropertySuccessResponse
from .contact_property_trigger_workflow_mutation_node import ContactPropertyTriggerWorkflowMutationNode
from .contact_property_trigger_workflow_mutation_node_type_name import (
    ContactPropertyTriggerWorkflowMutationNodeTypeName,
)
from .contact_property_trigger_workflow_mutation_node_with_revision import (
    ContactPropertyTriggerWorkflowMutationNodeWithRevision,
)
from .contact_property_trigger_workflow_node import ContactPropertyTriggerWorkflowNode
from .contact_property_trigger_workflow_node_type_name import ContactPropertyTriggerWorkflowNodeTypeName
from .contact_property_type import ContactPropertyType
from .contact_request import ContactRequest
from .contact_success_response import ContactSuccessResponse
from .contact_suppression_removal_quota import ContactSuppressionRemovalQuota
from .contact_suppression_remove_response import ContactSuppressionRemoveResponse
from .contact_suppression_status_response import ContactSuppressionStatusResponse
from .contact_suppression_status_response_contact import ContactSuppressionStatusResponseContact
from .contact_update_request import ContactUpdateRequest
from .create_audience_segment_request import CreateAudienceSegmentRequest
from .create_audience_segment_request_filter import CreateAudienceSegmentRequestFilter
from .create_audience_segment_request_filter_match import CreateAudienceSegmentRequestFilterMatch
from .create_campaign_request import CreateCampaignRequest
from .create_campaign_response import CreateCampaignResponse
from .create_campaign_response_status import CreateCampaignResponseStatus
from .create_component_body import CreateComponentBody
from .create_group_request import CreateGroupRequest
from .create_theme_body import CreateThemeBody
from .create_transactional_request import CreateTransactionalRequest
from .create_upload_request import CreateUploadRequest
from .create_upload_response import CreateUploadResponse
from .create_workflow_node_after_request import CreateWorkflowNodeAfterRequest
from .create_workflow_node_after_request_insert_mode import CreateWorkflowNodeAfterRequestInsertMode
from .create_workflow_node_before_request_type_0 import CreateWorkflowNodeBeforeRequestType0
from .create_workflow_node_before_request_type_1 import CreateWorkflowNodeBeforeRequestType1
from .create_workflow_node_between_request import CreateWorkflowNodeBetweenRequest
from .create_workflow_node_between_request_insert_mode import CreateWorkflowNodeBetweenRequestInsertMode
from .create_workflow_node_type_name import CreateWorkflowNodeTypeName
from .create_workflow_request import CreateWorkflowRequest
from .delete_workflow_node_request import DeleteWorkflowNodeRequest
from .delete_workflow_request import DeleteWorkflowRequest
from .email_message_failure_response import EmailMessageFailureResponse
from .email_message_guardian_response import EmailMessageGuardianResponse
from .email_message_preview_request import EmailMessagePreviewRequest
from .email_message_preview_request_contact_properties import EmailMessagePreviewRequestContactProperties
from .email_message_preview_request_data_variables import EmailMessagePreviewRequestDataVariables
from .email_message_preview_request_event_properties import EmailMessagePreviewRequestEventProperties
from .email_message_preview_response import EmailMessagePreviewResponse
from .email_message_response import EmailMessageResponse
from .email_message_response_contact_properties_fallbacks import EmailMessageResponseContactPropertiesFallbacks
from .email_message_response_data_variables_fallbacks import EmailMessageResponseDataVariablesFallbacks
from .email_message_response_email_format import EmailMessageResponseEmailFormat
from .email_message_response_event_properties_fallbacks import EmailMessageResponseEventPropertiesFallbacks
from .email_message_response_warnings_item import EmailMessageResponseWarningsItem
from .email_message_response_warnings_item_severity import EmailMessageResponseWarningsItemSeverity
from .event_failure_response import EventFailureResponse
from .event_pattern import EventPattern
from .event_pattern_failure_response import EventPatternFailureResponse
from .event_pattern_incoming_webhook_platform import EventPatternIncomingWebhookPlatform
from .event_pattern_summary import EventPatternSummary
from .event_pattern_summary_incoming_webhook_platform import EventPatternSummaryIncomingWebhookPlatform
from .event_success_response import EventSuccessResponse
from .event_trigger_workflow_mutation_node import EventTriggerWorkflowMutationNode
from .event_trigger_workflow_mutation_node_type_name import EventTriggerWorkflowMutationNodeTypeName
from .event_trigger_workflow_mutation_node_with_revision import EventTriggerWorkflowMutationNodeWithRevision
from .event_trigger_workflow_node import EventTriggerWorkflowNode
from .event_trigger_workflow_node_type_name import EventTriggerWorkflowNodeTypeName
from .exit_action_workflow_mutation_node import ExitActionWorkflowMutationNode
from .exit_action_workflow_mutation_node_type_name import ExitActionWorkflowMutationNodeTypeName
from .exit_action_workflow_mutation_node_with_revision import ExitActionWorkflowMutationNodeWithRevision
from .exit_action_workflow_node import ExitActionWorkflowNode
from .exit_action_workflow_node_type_name import ExitActionWorkflowNodeTypeName
from .experiment_branch_workflow_mutation_node import ExperimentBranchWorkflowMutationNode
from .experiment_branch_workflow_mutation_node_type_name import ExperimentBranchWorkflowMutationNodeTypeName
from .experiment_branch_workflow_mutation_node_with_revision import ExperimentBranchWorkflowMutationNodeWithRevision
from .experiment_branch_workflow_node import ExperimentBranchWorkflowNode
from .experiment_branch_workflow_node_type_name import ExperimentBranchWorkflowNodeTypeName
from .group_failure_response import GroupFailureResponse
from .group_response import GroupResponse
from .guardian_rule import GuardianRule
from .guardian_rule_items_item import GuardianRuleItemsItem
from .guardian_rule_rule import GuardianRuleRule
from .idempotency_key_failure_response import IdempotencyKeyFailureResponse
from .list_audience_segments_response import ListAudienceSegmentsResponse
from .list_campaigns_response import ListCampaignsResponse
from .list_components_response import ListComponentsResponse
from .list_event_patterns_response import ListEventPatternsResponse
from .list_event_patterns_response_pagination import ListEventPatternsResponsePagination
from .list_groups_response import ListGroupsResponse
from .list_themes_response import ListThemesResponse
from .list_transactionals_resource_response import ListTransactionalsResourceResponse
from .list_workflows_response import ListWorkflowsResponse
from .mailing_list import MailingList
from .mailing_list_subscriptions import MailingListSubscriptions
from .opt_in_condition import OptInCondition
from .opt_in_condition_status_type_1 import OptInConditionStatusType1
from .opt_in_condition_status_type_2_type_1 import OptInConditionStatusType2Type1
from .opt_in_condition_status_type_3_type_1 import OptInConditionStatusType3Type1
from .opt_in_condition_type import OptInConditionType
from .pagination import Pagination
from .property_condition import PropertyCondition
from .property_condition_operator import PropertyConditionOperator
from .property_condition_type import PropertyConditionType
from .property_condition_value_type_2 import PropertyConditionValueType2
from .reroute_node_connection_request import RerouteNodeConnectionRequest
from .send_email_action_workflow_mutation_node import SendEmailActionWorkflowMutationNode
from .send_email_action_workflow_mutation_node_type_name import SendEmailActionWorkflowMutationNodeTypeName
from .send_email_action_workflow_mutation_node_with_revision import SendEmailActionWorkflowMutationNodeWithRevision
from .send_email_action_workflow_node import SendEmailActionWorkflowNode
from .send_email_action_workflow_node_type_name import SendEmailActionWorkflowNodeTypeName
from .signup_trigger_workflow_mutation_node import SignupTriggerWorkflowMutationNode
from .signup_trigger_workflow_mutation_node_type_name import SignupTriggerWorkflowMutationNodeTypeName
from .signup_trigger_workflow_mutation_node_with_revision import SignupTriggerWorkflowMutationNodeWithRevision
from .signup_trigger_workflow_node import SignupTriggerWorkflowNode
from .signup_trigger_workflow_node_type_name import SignupTriggerWorkflowNodeTypeName
from .simplified_add_to_list_trigger_workflow_node import SimplifiedAddToListTriggerWorkflowNode
from .simplified_add_to_list_trigger_workflow_node_type_name import SimplifiedAddToListTriggerWorkflowNodeTypeName
from .simplified_audience_filter_workflow_node import SimplifiedAudienceFilterWorkflowNode
from .simplified_audience_filter_workflow_node_type_name import SimplifiedAudienceFilterWorkflowNodeTypeName
from .simplified_blank_trigger_workflow_node import SimplifiedBlankTriggerWorkflowNode
from .simplified_blank_trigger_workflow_node_type_name import SimplifiedBlankTriggerWorkflowNodeTypeName
from .simplified_branch_workflow_node import SimplifiedBranchWorkflowNode
from .simplified_branch_workflow_node_type_name import SimplifiedBranchWorkflowNodeTypeName
from .simplified_contact_property_trigger_workflow_node import SimplifiedContactPropertyTriggerWorkflowNode
from .simplified_contact_property_trigger_workflow_node_type_name import (
    SimplifiedContactPropertyTriggerWorkflowNodeTypeName,
)
from .simplified_event_trigger_workflow_node import SimplifiedEventTriggerWorkflowNode
from .simplified_event_trigger_workflow_node_type_name import SimplifiedEventTriggerWorkflowNodeTypeName
from .simplified_exit_action_workflow_node import SimplifiedExitActionWorkflowNode
from .simplified_exit_action_workflow_node_type_name import SimplifiedExitActionWorkflowNodeTypeName
from .simplified_experiment_branch_workflow_node import SimplifiedExperimentBranchWorkflowNode
from .simplified_experiment_branch_workflow_node_type_name import SimplifiedExperimentBranchWorkflowNodeTypeName
from .simplified_send_email_action_workflow_node import SimplifiedSendEmailActionWorkflowNode
from .simplified_send_email_action_workflow_node_type_name import SimplifiedSendEmailActionWorkflowNodeTypeName
from .simplified_signup_trigger_workflow_node import SimplifiedSignupTriggerWorkflowNode
from .simplified_signup_trigger_workflow_node_type_name import SimplifiedSignupTriggerWorkflowNodeTypeName
from .simplified_timer_action_workflow_node import SimplifiedTimerActionWorkflowNode
from .simplified_timer_action_workflow_node_type_name import SimplifiedTimerActionWorkflowNodeTypeName
from .simplified_variant_workflow_node import SimplifiedVariantWorkflowNode
from .simplified_variant_workflow_node_type_name import SimplifiedVariantWorkflowNodeTypeName
from .simplified_workflow import SimplifiedWorkflow
from .simplified_workflow_nodes import SimplifiedWorkflowNodes
from .simplified_workflow_status import SimplifiedWorkflowStatus
from .test_api_key_response_200 import TestApiKeyResponse200
from .test_api_key_response_401 import TestApiKeyResponse401
from .theme import Theme
from .theme_failure_response import ThemeFailureResponse
from .theme_response import ThemeResponse
from .theme_styles import ThemeStyles
from .timer_action_workflow_mutation_node import TimerActionWorkflowMutationNode
from .timer_action_workflow_mutation_node_type_name import TimerActionWorkflowMutationNodeTypeName
from .timer_action_workflow_mutation_node_with_revision import TimerActionWorkflowMutationNodeWithRevision
from .timer_action_workflow_node import TimerActionWorkflowNode
from .timer_action_workflow_node_type_name import TimerActionWorkflowNodeTypeName
from .transactional_draft_response import TransactionalDraftResponse
from .transactional_failure_2_response import TransactionalFailure2Response
from .transactional_failure_3_response import TransactionalFailure3Response
from .transactional_failure_3_response_error import TransactionalFailure3ResponseError
from .transactional_failure_4_response import TransactionalFailure4Response
from .transactional_failure_4_response_error import TransactionalFailure4ResponseError
from .transactional_failure_5_response import TransactionalFailure5Response
from .transactional_failure_5_response_error import TransactionalFailure5ResponseError
from .transactional_failure_response import TransactionalFailureResponse
from .transactional_request import TransactionalRequest
from .transactional_request_attachments_item import TransactionalRequestAttachmentsItem
from .transactional_request_data_variables import TransactionalRequestDataVariables
from .transactional_resource import TransactionalResource
from .transactional_send_failure_response import TransactionalSendFailureResponse
from .transactional_success_response import TransactionalSuccessResponse
from .update_campaign_request import UpdateCampaignRequest
from .update_component_body import UpdateComponentBody
from .update_component_response import UpdateComponentResponse
from .update_email_message_request import UpdateEmailMessageRequest
from .update_email_message_request_contact_properties_fallbacks import (
    UpdateEmailMessageRequestContactPropertiesFallbacks,
)
from .update_email_message_request_data_variables_fallbacks import UpdateEmailMessageRequestDataVariablesFallbacks
from .update_email_message_request_email_format import UpdateEmailMessageRequestEmailFormat
from .update_email_message_request_event_properties_fallbacks import UpdateEmailMessageRequestEventPropertiesFallbacks
from .update_group_request import UpdateGroupRequest
from .update_theme_body import UpdateThemeBody
from .update_theme_response import UpdateThemeResponse
from .update_transactional_request import UpdateTransactionalRequest
from .update_workflow_node_request import UpdateWorkflowNodeRequest
from .upload_failure_response import UploadFailureResponse
from .upload_limit_exceeded_failure_response import UploadLimitExceededFailureResponse
from .variant_workflow_mutation_node import VariantWorkflowMutationNode
from .variant_workflow_mutation_node_type_name import VariantWorkflowMutationNodeTypeName
from .variant_workflow_mutation_node_with_revision import VariantWorkflowMutationNodeWithRevision
from .variant_workflow_node import VariantWorkflowNode
from .variant_workflow_node_type_name import VariantWorkflowNodeTypeName
from .webhook_base_payload import WebhookBasePayload
from .webhook_contact import WebhookContact
from .webhook_contact_identity import WebhookContactIdentity
from .webhook_contact_mailing_lists import WebhookContactMailingLists
from .webhook_contact_opt_in_status_type_1 import WebhookContactOptInStatusType1
from .webhook_contact_opt_in_status_type_2_type_1 import WebhookContactOptInStatusType2Type1
from .webhook_contact_opt_in_status_type_3_type_1 import WebhookContactOptInStatusType3Type1
from .webhook_email import WebhookEmail
from .webhook_email_metric_payload import WebhookEmailMetricPayload
from .webhook_email_metric_payload_source_type import WebhookEmailMetricPayloadSourceType
from .webhook_mailing_list import WebhookMailingList
from .webhook_marketing_email_metric_payload import WebhookMarketingEmailMetricPayload
from .webhook_marketing_email_metric_payload_source_type import WebhookMarketingEmailMetricPayloadSourceType
from .webhook_testing_test_event_payload import WebhookTestingTestEventPayload
from .workflow_add_to_list_trigger_payload import WorkflowAddToListTriggerPayload
from .workflow_add_to_list_trigger_payload_type_name import WorkflowAddToListTriggerPayloadTypeName
from .workflow_audience_filter_payload import WorkflowAudienceFilterPayload
from .workflow_contact_property_comparison import WorkflowContactPropertyComparison
from .workflow_contact_property_comparison_operator import WorkflowContactPropertyComparisonOperator
from .workflow_contact_property_query import WorkflowContactPropertyQuery
from .workflow_contact_property_trigger_payload import WorkflowContactPropertyTriggerPayload
from .workflow_contact_property_trigger_payload_type_name import WorkflowContactPropertyTriggerPayloadTypeName
from .workflow_deleted_response import WorkflowDeletedResponse
from .workflow_deleted_response_status import WorkflowDeletedResponseStatus
from .workflow_event_property import WorkflowEventProperty
from .workflow_event_property_type import WorkflowEventPropertyType
from .workflow_event_trigger_payload import WorkflowEventTriggerPayload
from .workflow_event_trigger_payload_type_name import WorkflowEventTriggerPayloadTypeName
from .workflow_experiment_branch_payload import WorkflowExperimentBranchPayload
from .workflow_failure_response import WorkflowFailureResponse
from .workflow_mailing_list_preview import WorkflowMailingListPreview
from .workflow_mailing_list_preview_status import WorkflowMailingListPreviewStatus
from .workflow_mailing_list_updated_response import WorkflowMailingListUpdatedResponse
from .workflow_mailing_list_updated_response_status import WorkflowMailingListUpdatedResponseStatus
from .workflow_mutation_node_revision import WorkflowMutationNodeRevision
from .workflow_queued_contact_delete_preview import WorkflowQueuedContactDeletePreview
from .workflow_queued_contact_delete_preview_status import WorkflowQueuedContactDeletePreviewStatus
from .workflow_queued_contact_policy import WorkflowQueuedContactPolicy
from .workflow_signup_trigger_payload import WorkflowSignupTriggerPayload
from .workflow_signup_trigger_payload_type_name import WorkflowSignupTriggerPayloadTypeName
from .workflow_summary import WorkflowSummary
from .workflow_timer_action_payload import WorkflowTimerActionPayload
from .workflow_timer_unit import WorkflowTimerUnit
from .workflow_variant_payload import WorkflowVariantPayload

__all__ = (
    "ActivityCondition",
    "ActivityConditionAction",
    "ActivityConditionTarget",
    "ActivityConditionType",
    "AddToListTriggerWorkflowMutationNode",
    "AddToListTriggerWorkflowMutationNodeTypeName",
    "AddToListTriggerWorkflowMutationNodeWithRevision",
    "AddToListTriggerWorkflowNode",
    "AddToListTriggerWorkflowNodeTypeName",
    "AddWorkflowBranchRequest",
    "AddWorkflowBranchResponse",
    "AudienceFilterInRequestType0",
    "AudienceFilterInRequestType0Match",
    "AudienceFilterType0",
    "AudienceFilterType0Match",
    "AudienceFilterWorkflowMutationNode",
    "AudienceFilterWorkflowMutationNodeTypeName",
    "AudienceFilterWorkflowMutationNodeWithRevision",
    "AudienceFilterWorkflowNode",
    "AudienceFilterWorkflowNodeTypeName",
    "AudienceSegment",
    "AudienceSegmentFailureResponse",
    "AudienceSegmentResponse",
    "BlankTriggerWorkflowMutationNode",
    "BlankTriggerWorkflowMutationNodeTypeName",
    "BlankTriggerWorkflowMutationNodeWithRevision",
    "BlankTriggerWorkflowNode",
    "BlankTriggerWorkflowNodeTypeName",
    "BranchWorkflowMutationNode",
    "BranchWorkflowMutationNodeTypeName",
    "BranchWorkflowMutationNodeWithRevision",
    "BranchWorkflowNode",
    "BranchWorkflowNodeTypeName",
    "CampaignFailureResponse",
    "CampaignListItem",
    "CampaignListItemStatus",
    "CampaignResponse",
    "CampaignResponseStatus",
    "CampaignScheduling",
    "CampaignSchedulingMethod",
    "CampaignSchedulingRequest",
    "CampaignSchedulingRequestMethod",
    "ChangeWorkflowMailingListRequest",
    "CompleteUploadResponse",
    "Component",
    "ComponentFailureResponse",
    "ComponentResponse",
    "ComponentValidationFailureResponse",
    "Contact",
    "ContactDeleteRequest",
    "ContactDeleteResponse",
    "ContactFailureResponse",
    "ContactFields",
    "ContactMailingLists",
    "ContactOptInStatusType1",
    "ContactOptInStatusType2Type1",
    "ContactOptInStatusType3Type1",
    "ContactProperty",
    "ContactPropertyCreateRequest",
    "ContactPropertyCreateRequestType",
    "ContactPropertyFailureResponse",
    "ContactPropertySuccessResponse",
    "ContactPropertyTriggerWorkflowMutationNode",
    "ContactPropertyTriggerWorkflowMutationNodeTypeName",
    "ContactPropertyTriggerWorkflowMutationNodeWithRevision",
    "ContactPropertyTriggerWorkflowNode",
    "ContactPropertyTriggerWorkflowNodeTypeName",
    "ContactPropertyType",
    "ContactRequest",
    "ContactSuccessResponse",
    "ContactSuppressionRemovalQuota",
    "ContactSuppressionRemoveResponse",
    "ContactSuppressionStatusResponse",
    "ContactSuppressionStatusResponseContact",
    "ContactUpdateRequest",
    "CreateAudienceSegmentRequest",
    "CreateAudienceSegmentRequestFilter",
    "CreateAudienceSegmentRequestFilterMatch",
    "CreateCampaignRequest",
    "CreateCampaignResponse",
    "CreateCampaignResponseStatus",
    "CreateComponentBody",
    "CreateGroupRequest",
    "CreateThemeBody",
    "CreateTransactionalRequest",
    "CreateUploadRequest",
    "CreateUploadResponse",
    "CreateWorkflowNodeAfterRequest",
    "CreateWorkflowNodeAfterRequestInsertMode",
    "CreateWorkflowNodeBeforeRequestType0",
    "CreateWorkflowNodeBeforeRequestType1",
    "CreateWorkflowNodeBetweenRequest",
    "CreateWorkflowNodeBetweenRequestInsertMode",
    "CreateWorkflowNodeTypeName",
    "CreateWorkflowRequest",
    "DeleteWorkflowNodeRequest",
    "DeleteWorkflowRequest",
    "EmailMessageFailureResponse",
    "EmailMessageGuardianResponse",
    "EmailMessagePreviewRequest",
    "EmailMessagePreviewRequestContactProperties",
    "EmailMessagePreviewRequestDataVariables",
    "EmailMessagePreviewRequestEventProperties",
    "EmailMessagePreviewResponse",
    "EmailMessageResponse",
    "EmailMessageResponseContactPropertiesFallbacks",
    "EmailMessageResponseDataVariablesFallbacks",
    "EmailMessageResponseEmailFormat",
    "EmailMessageResponseEventPropertiesFallbacks",
    "EmailMessageResponseWarningsItem",
    "EmailMessageResponseWarningsItemSeverity",
    "EventFailureResponse",
    "EventPattern",
    "EventPatternFailureResponse",
    "EventPatternIncomingWebhookPlatform",
    "EventPatternSummary",
    "EventPatternSummaryIncomingWebhookPlatform",
    "EventSuccessResponse",
    "EventTriggerWorkflowMutationNode",
    "EventTriggerWorkflowMutationNodeTypeName",
    "EventTriggerWorkflowMutationNodeWithRevision",
    "EventTriggerWorkflowNode",
    "EventTriggerWorkflowNodeTypeName",
    "ExitActionWorkflowMutationNode",
    "ExitActionWorkflowMutationNodeTypeName",
    "ExitActionWorkflowMutationNodeWithRevision",
    "ExitActionWorkflowNode",
    "ExitActionWorkflowNodeTypeName",
    "ExperimentBranchWorkflowMutationNode",
    "ExperimentBranchWorkflowMutationNodeTypeName",
    "ExperimentBranchWorkflowMutationNodeWithRevision",
    "ExperimentBranchWorkflowNode",
    "ExperimentBranchWorkflowNodeTypeName",
    "GroupFailureResponse",
    "GroupResponse",
    "GuardianRule",
    "GuardianRuleItemsItem",
    "GuardianRuleRule",
    "IdempotencyKeyFailureResponse",
    "ListAudienceSegmentsResponse",
    "ListCampaignsResponse",
    "ListComponentsResponse",
    "ListEventPatternsResponse",
    "ListEventPatternsResponsePagination",
    "ListGroupsResponse",
    "ListThemesResponse",
    "ListTransactionalsResourceResponse",
    "ListWorkflowsResponse",
    "MailingList",
    "MailingListSubscriptions",
    "OptInCondition",
    "OptInConditionStatusType1",
    "OptInConditionStatusType2Type1",
    "OptInConditionStatusType3Type1",
    "OptInConditionType",
    "Pagination",
    "PropertyCondition",
    "PropertyConditionOperator",
    "PropertyConditionType",
    "PropertyConditionValueType2",
    "RerouteNodeConnectionRequest",
    "SendEmailActionWorkflowMutationNode",
    "SendEmailActionWorkflowMutationNodeTypeName",
    "SendEmailActionWorkflowMutationNodeWithRevision",
    "SendEmailActionWorkflowNode",
    "SendEmailActionWorkflowNodeTypeName",
    "SignupTriggerWorkflowMutationNode",
    "SignupTriggerWorkflowMutationNodeTypeName",
    "SignupTriggerWorkflowMutationNodeWithRevision",
    "SignupTriggerWorkflowNode",
    "SignupTriggerWorkflowNodeTypeName",
    "SimplifiedAddToListTriggerWorkflowNode",
    "SimplifiedAddToListTriggerWorkflowNodeTypeName",
    "SimplifiedAudienceFilterWorkflowNode",
    "SimplifiedAudienceFilterWorkflowNodeTypeName",
    "SimplifiedBlankTriggerWorkflowNode",
    "SimplifiedBlankTriggerWorkflowNodeTypeName",
    "SimplifiedBranchWorkflowNode",
    "SimplifiedBranchWorkflowNodeTypeName",
    "SimplifiedContactPropertyTriggerWorkflowNode",
    "SimplifiedContactPropertyTriggerWorkflowNodeTypeName",
    "SimplifiedEventTriggerWorkflowNode",
    "SimplifiedEventTriggerWorkflowNodeTypeName",
    "SimplifiedExitActionWorkflowNode",
    "SimplifiedExitActionWorkflowNodeTypeName",
    "SimplifiedExperimentBranchWorkflowNode",
    "SimplifiedExperimentBranchWorkflowNodeTypeName",
    "SimplifiedSendEmailActionWorkflowNode",
    "SimplifiedSendEmailActionWorkflowNodeTypeName",
    "SimplifiedSignupTriggerWorkflowNode",
    "SimplifiedSignupTriggerWorkflowNodeTypeName",
    "SimplifiedTimerActionWorkflowNode",
    "SimplifiedTimerActionWorkflowNodeTypeName",
    "SimplifiedVariantWorkflowNode",
    "SimplifiedVariantWorkflowNodeTypeName",
    "SimplifiedWorkflow",
    "SimplifiedWorkflowNodes",
    "SimplifiedWorkflowStatus",
    "TestApiKeyResponse200",
    "TestApiKeyResponse401",
    "Theme",
    "ThemeFailureResponse",
    "ThemeResponse",
    "ThemeStyles",
    "TimerActionWorkflowMutationNode",
    "TimerActionWorkflowMutationNodeTypeName",
    "TimerActionWorkflowMutationNodeWithRevision",
    "TimerActionWorkflowNode",
    "TimerActionWorkflowNodeTypeName",
    "TransactionalDraftResponse",
    "TransactionalFailure2Response",
    "TransactionalFailure3Response",
    "TransactionalFailure3ResponseError",
    "TransactionalFailure4Response",
    "TransactionalFailure4ResponseError",
    "TransactionalFailure5Response",
    "TransactionalFailure5ResponseError",
    "TransactionalFailureResponse",
    "TransactionalRequest",
    "TransactionalRequestAttachmentsItem",
    "TransactionalRequestDataVariables",
    "TransactionalResource",
    "TransactionalSendFailureResponse",
    "TransactionalSuccessResponse",
    "UpdateCampaignRequest",
    "UpdateComponentBody",
    "UpdateComponentResponse",
    "UpdateEmailMessageRequest",
    "UpdateEmailMessageRequestContactPropertiesFallbacks",
    "UpdateEmailMessageRequestDataVariablesFallbacks",
    "UpdateEmailMessageRequestEmailFormat",
    "UpdateEmailMessageRequestEventPropertiesFallbacks",
    "UpdateGroupRequest",
    "UpdateThemeBody",
    "UpdateThemeResponse",
    "UpdateTransactionalRequest",
    "UpdateWorkflowNodeRequest",
    "UploadFailureResponse",
    "UploadLimitExceededFailureResponse",
    "VariantWorkflowMutationNode",
    "VariantWorkflowMutationNodeTypeName",
    "VariantWorkflowMutationNodeWithRevision",
    "VariantWorkflowNode",
    "VariantWorkflowNodeTypeName",
    "WebhookBasePayload",
    "WebhookContact",
    "WebhookContactIdentity",
    "WebhookContactMailingLists",
    "WebhookContactOptInStatusType1",
    "WebhookContactOptInStatusType2Type1",
    "WebhookContactOptInStatusType3Type1",
    "WebhookEmail",
    "WebhookEmailMetricPayload",
    "WebhookEmailMetricPayloadSourceType",
    "WebhookMailingList",
    "WebhookMarketingEmailMetricPayload",
    "WebhookMarketingEmailMetricPayloadSourceType",
    "WebhookTestingTestEventPayload",
    "WorkflowAddToListTriggerPayload",
    "WorkflowAddToListTriggerPayloadTypeName",
    "WorkflowAudienceFilterPayload",
    "WorkflowContactPropertyComparison",
    "WorkflowContactPropertyComparisonOperator",
    "WorkflowContactPropertyQuery",
    "WorkflowContactPropertyTriggerPayload",
    "WorkflowContactPropertyTriggerPayloadTypeName",
    "WorkflowDeletedResponse",
    "WorkflowDeletedResponseStatus",
    "WorkflowEventProperty",
    "WorkflowEventPropertyType",
    "WorkflowEventTriggerPayload",
    "WorkflowEventTriggerPayloadTypeName",
    "WorkflowExperimentBranchPayload",
    "WorkflowFailureResponse",
    "WorkflowMailingListPreview",
    "WorkflowMailingListPreviewStatus",
    "WorkflowMailingListUpdatedResponse",
    "WorkflowMailingListUpdatedResponseStatus",
    "WorkflowMutationNodeRevision",
    "WorkflowQueuedContactDeletePreview",
    "WorkflowQueuedContactDeletePreviewStatus",
    "WorkflowQueuedContactPolicy",
    "WorkflowSignupTriggerPayload",
    "WorkflowSignupTriggerPayloadTypeName",
    "WorkflowSummary",
    "WorkflowTimerActionPayload",
    "WorkflowTimerUnit",
    "WorkflowVariantPayload",
)
