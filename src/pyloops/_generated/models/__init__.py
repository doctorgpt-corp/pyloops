"""Contains all the data models used in inputs/outputs"""

from .campaign_failure_response import CampaignFailureResponse
from .campaign_list_item import CampaignListItem
from .campaign_response import CampaignResponse
from .complete_upload_response import CompleteUploadResponse
from .component import Component
from .component_failure_response import ComponentFailureResponse
from .component_response import ComponentResponse
from .contact import Contact
from .contact_delete_request import ContactDeleteRequest
from .contact_delete_response import ContactDeleteResponse
from .contact_failure_response import ContactFailureResponse
from .contact_mailing_lists import ContactMailingLists
from .contact_opt_in_status_type_1 import ContactOptInStatusType1
from .contact_opt_in_status_type_2_type_1 import ContactOptInStatusType2Type1
from .contact_opt_in_status_type_3_type_1 import ContactOptInStatusType3Type1
from .contact_property import ContactProperty
from .contact_property_create_request import ContactPropertyCreateRequest
from .contact_property_failure_response import ContactPropertyFailureResponse
from .contact_property_success_response import ContactPropertySuccessResponse
from .contact_request import ContactRequest
from .contact_request_mailing_lists import ContactRequestMailingLists
from .contact_success_response import ContactSuccessResponse
from .contact_suppression_removal_quota import ContactSuppressionRemovalQuota
from .contact_suppression_remove_response import ContactSuppressionRemoveResponse
from .contact_suppression_status_response import ContactSuppressionStatusResponse
from .contact_suppression_status_response_contact import ContactSuppressionStatusResponseContact
from .contact_update_request import ContactUpdateRequest
from .contact_update_request_mailing_lists import ContactUpdateRequestMailingLists
from .create_campaign_request import CreateCampaignRequest
from .create_campaign_response import CreateCampaignResponse
from .create_transactional_request import CreateTransactionalRequest
from .create_upload_request import CreateUploadRequest
from .create_upload_response import CreateUploadResponse
from .email_message_failure_response import EmailMessageFailureResponse
from .email_message_response import EmailMessageResponse
from .email_message_response_warnings_item import EmailMessageResponseWarningsItem
from .email_message_response_warnings_item_severity import EmailMessageResponseWarningsItemSeverity
from .event_failure_response import EventFailureResponse
from .event_request import EventRequest
from .event_request_event_properties import EventRequestEventProperties
from .event_request_mailing_lists import EventRequestMailingLists
from .event_success_response import EventSuccessResponse
from .get_v1_api_key_response_200 import GetV1ApiKeyResponse200
from .get_v1_api_key_response_401 import GetV1ApiKeyResponse401
from .get_v1_dedicated_sending_ips_response_500 import GetV1DedicatedSendingIpsResponse500
from .idempotency_key_failure_response import IdempotencyKeyFailureResponse
from .list_campaigns_response import ListCampaignsResponse
from .list_campaigns_response_pagination import ListCampaignsResponsePagination
from .list_components_response import ListComponentsResponse
from .list_components_response_pagination import ListComponentsResponsePagination
from .list_themes_response import ListThemesResponse
from .list_themes_response_pagination import ListThemesResponsePagination
from .list_transactionals_resource_response import ListTransactionalsResourceResponse
from .list_transactionals_resource_response_pagination import ListTransactionalsResourceResponsePagination
from .mailing_list import MailingList
from .theme import Theme
from .theme_failure_response import ThemeFailureResponse
from .theme_response import ThemeResponse
from .theme_styles import ThemeStyles
from .transactional_draft_response import TransactionalDraftResponse
from .transactional_email_resource import TransactionalEmailResource
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
from .transactional_response import TransactionalResponse
from .transactional_send_failure_response import TransactionalSendFailureResponse
from .transactional_success_response import TransactionalSuccessResponse
from .update_campaign_request import UpdateCampaignRequest
from .update_email_message_request import UpdateEmailMessageRequest
from .update_transactional_request import UpdateTransactionalRequest
from .upload_failure_response import UploadFailureResponse
from .upload_limit_exceeded_failure_response import UploadLimitExceededFailureResponse

__all__ = (
    "CampaignFailureResponse",
    "CampaignListItem",
    "CampaignResponse",
    "CompleteUploadResponse",
    "Component",
    "ComponentFailureResponse",
    "ComponentResponse",
    "Contact",
    "ContactDeleteRequest",
    "ContactDeleteResponse",
    "ContactFailureResponse",
    "ContactMailingLists",
    "ContactOptInStatusType1",
    "ContactOptInStatusType2Type1",
    "ContactOptInStatusType3Type1",
    "ContactProperty",
    "ContactPropertyCreateRequest",
    "ContactPropertyFailureResponse",
    "ContactPropertySuccessResponse",
    "ContactRequest",
    "ContactRequestMailingLists",
    "ContactSuccessResponse",
    "ContactSuppressionRemovalQuota",
    "ContactSuppressionRemoveResponse",
    "ContactSuppressionStatusResponse",
    "ContactSuppressionStatusResponseContact",
    "ContactUpdateRequest",
    "ContactUpdateRequestMailingLists",
    "CreateCampaignRequest",
    "CreateCampaignResponse",
    "CreateTransactionalRequest",
    "CreateUploadRequest",
    "CreateUploadResponse",
    "EmailMessageFailureResponse",
    "EmailMessageResponse",
    "EmailMessageResponseWarningsItem",
    "EmailMessageResponseWarningsItemSeverity",
    "EventFailureResponse",
    "EventRequest",
    "EventRequestEventProperties",
    "EventRequestMailingLists",
    "EventSuccessResponse",
    "GetV1ApiKeyResponse200",
    "GetV1ApiKeyResponse401",
    "GetV1DedicatedSendingIpsResponse500",
    "IdempotencyKeyFailureResponse",
    "ListCampaignsResponse",
    "ListCampaignsResponsePagination",
    "ListComponentsResponse",
    "ListComponentsResponsePagination",
    "ListThemesResponse",
    "ListThemesResponsePagination",
    "ListTransactionalsResourceResponse",
    "ListTransactionalsResourceResponsePagination",
    "MailingList",
    "Theme",
    "ThemeFailureResponse",
    "ThemeResponse",
    "ThemeStyles",
    "TransactionalDraftResponse",
    "TransactionalEmailResource",
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
    "TransactionalResponse",
    "TransactionalSendFailureResponse",
    "TransactionalSuccessResponse",
    "UpdateCampaignRequest",
    "UpdateEmailMessageRequest",
    "UpdateTransactionalRequest",
    "UploadFailureResponse",
    "UploadLimitExceededFailureResponse",
)
