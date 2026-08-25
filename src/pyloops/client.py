import json
import uuid
import warnings
from http import HTTPStatus
from typing import Any

from pyloops._generated.api.api_key import test_api_key
from pyloops._generated.api.audience_segments import (
    create_audience_segment,
    get_audience_segment,
    list_audience_segments,
)
from pyloops._generated.api.campaign_groups import (
    create_campaign_group,
    get_campaign_group,
    list_campaign_groups,
    update_campaign_group,
)
from pyloops._generated.api.campaigns import (
    create_campaign,
    get_campaign,
    list_campaigns,
    update_campaign,
)
from pyloops._generated.api.components import (
    create_component,
    get_component,
    list_components,
    update_component,
)
from pyloops._generated.api.configuration import list_dedicated_sending_ips
from pyloops._generated.api.contact_properties import (
    create_contact_property,
    list_contact_properties,
)
from pyloops._generated.api.contacts import (
    create_contact,
    delete_contact,
    find_contact,
    get_contact_suppression,
    remove_contact_suppression,
    update_contact,
)
from pyloops._generated.api.email_messages import (
    get_email_message,
    get_email_message_guardian,
    preview_email_message,
    update_email_message,
)
from pyloops._generated.api.event_patterns import (
    get_event_pattern,
    get_event_pattern_by_name,
    list_event_patterns,
)
from pyloops._generated.api.events import send_event
from pyloops._generated.api.mailing_lists import list_mailing_lists
from pyloops._generated.api.themes import (
    create_theme,
    get_theme,
    list_themes,
    update_theme,
)
from pyloops._generated.api.transactional_emails import (
    create_transactional_email,
    ensure_transactional_draft,
    get_transactional_email,
    list_published_transactional_emails,
    list_transactional_emails,
    publish_transactional_email,
    send_transactional_email,
    update_transactional_email,
)
from pyloops._generated.api.transactional_groups import (
    create_transactional_group,
    get_transactional_group,
    list_transactional_groups,
    update_transactional_group,
)
from pyloops._generated.api.uploads import complete_upload, create_upload
from pyloops._generated.api.workflow_nodes import (
    add_workflow_branch,
    create_workflow_node,
    delete_workflow_node,
    delete_workflow_node_recursively,
    get_workflow_node,
    update_workflow_node,
)
from pyloops._generated.api.workflows import (
    change_workflow_mailing_list,
    create_workflow,
    get_workflow,
    list_workflows,
    update_workflow_properties,
)
from pyloops._generated.client import AuthenticatedClient
from pyloops._generated.models import (
    AddWorkflowBranchRequest,
    AddWorkflowBranchResponse,
    AudienceSegmentFailureResponse,
    AudienceSegmentResponse,
    CampaignFailureResponse,
    CampaignResponse,
    ChangeWorkflowMailingListRequest,
    CompleteUploadResponse,
    ComponentFailureResponse,
    ComponentResponse,
    ComponentValidationFailureResponse,
    Contact,
    ContactDeleteRequest,
    ContactFailureResponse,
    ContactProperty,
    ContactPropertyCreateRequest,
    ContactPropertyCreateRequestType,
    ContactRequest,
    ContactSuccessResponse,
    ContactSuppressionRemoveResponse,
    ContactSuppressionStatusResponse,
    ContactUpdateRequest,
    CreateAudienceSegmentRequest,
    CreateAudienceSegmentRequestFilter,
    CreateCampaignRequest,
    CreateCampaignResponse,
    CreateComponentBody,
    CreateGroupRequest,
    CreateThemeBody,
    CreateTransactionalRequest,
    CreateUploadRequest,
    CreateUploadResponse,
    CreateWorkflowNodeBeforeRequest,
    CreateWorkflowNodeBeforeRequestInsertMode,
    CreateWorkflowNodeBetweenRequest,
    CreateWorkflowNodeBetweenRequestInsertMode,
    CreateWorkflowNodeTypeName,
    CreateWorkflowRequest,
    DeleteWorkflowNodeRequest,
    EmailMessageFailureResponse,
    EmailMessageGuardianResponse,
    EmailMessagePreviewRequest,
    EmailMessagePreviewRequestContactProperties,
    EmailMessagePreviewRequestDataVariables,
    EmailMessagePreviewRequestEventProperties,
    EmailMessagePreviewResponse,
    EmailMessageResponse,
    EventFailureResponse,
    EventPattern,
    EventPatternFailureResponse,
    EventSuccessResponse,
    GroupFailureResponse,
    GroupResponse,
    IdempotencyKeyFailureResponse,
    ListAudienceSegmentsResponse,
    ListCampaignsResponse,
    ListComponentsResponse,
    ListEventPatternsResponse,
    ListGroupsResponse,
    ListThemesResponse,
    ListTransactionalsResourceResponse,
    ListWorkflowsResponse,
    MailingList,
    MailingListSubscriptions,
    SimplifiedWorkflow,
    TestApiKeyResponse401,
    ThemeFailureResponse,
    ThemeResponse,
    ThemeStyles,
    TransactionalDraftResponse,
    TransactionalFailure2Response,
    TransactionalFailure3Response,
    TransactionalFailure4Response,
    TransactionalFailure5Response,
    TransactionalFailureResponse,
    TransactionalRequest,
    TransactionalRequestAttachmentsItem,
    TransactionalRequestDataVariables,
    TransactionalResource,
    TransactionalSendFailureResponse,
    TransactionalSuccessResponse,
    UpdateCampaignRequest,
    UpdateComponentBody,
    UpdateComponentResponse,
    UpdateEmailMessageRequest,
    UpdateGroupRequest,
    UpdateThemeBody,
    UpdateThemeResponse,
    UpdateTransactionalRequest,
    UpdateWorkflowNodeRequest,
    UploadFailureResponse,
    WorkflowDeletedResponse,
    WorkflowFailureResponse,
    WorkflowMailingListPreview,
    WorkflowMailingListUpdatedResponse,
    WorkflowQueuedContactDeletePreview,
    WorkflowQueuedContactPolicy,
)
from pyloops._generated.types import UNSET, Response
from pyloops.config import get_config
from pyloops.exceptions import (
    LoopsConfigurationError,
    LoopsContactExistsError,
    LoopsError,
    LoopsRateLimitError,
    LoopsUnsafeEmailError,
)
from pyloops.responses import TransactionalEmailsResponse


class LoopsClient:
    """
    High-level client wrapper for Loops.so API.

    This client provides a more convenient interface than the low-level API,
    with better error handling and simpler method signatures.

    Example:
        >>> import pyloops
        >>> pyloops.configure(api_key="your_api_key")
        >>> client = pyloops.get_client()
        >>> await client.upsert_contact(email="user@example.com", first_name="John")
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = "https://app.loops.so/api",
        safe_mode: bool | None = None,
        safe_mode_allowed_domains: tuple[str, ...] | None = None,
    ):
        """
        Initialize the Loops client.

        Args:
            api_key: API key for Loops.so. If not provided, uses configured default or LOOPS_API_KEY env var.
            base_url: Base URL for Loops API (default: https://app.loops.so/api). As of the
                Loops API v1.14.x update the ``/v1`` version segment is part of each endpoint
                path, so the base URL must NOT include it. A trailing ``/v1`` is stripped
                automatically (with a DeprecationWarning) for backwards compatibility.
            safe_mode: If True, only allow emails to domains in safe_mode_allowed_domains.
                Useful for local development to prevent accidentally emailing real users.
                If None, falls back to the value set via configure().
            safe_mode_allowed_domains: Tuple of allowed email domains when safe_mode is enabled
                (e.g. ("@test.com", "@example.com")). Each entry should start with "@".
                If None, falls back to the value set via configure().

        Raises:
            LoopsConfigurationError: If no API key is available
        """
        # Get API key from parameter, config, or env var
        config = get_config()
        if api_key is None:
            api_key = config["api_key"]
            if config["base_url"]:
                base_url = config["base_url"]

        if safe_mode is None:
            safe_mode = config["safe_mode"]
        self._safe_mode = safe_mode

        if safe_mode_allowed_domains is None:
            safe_mode_allowed_domains = config["safe_mode_allowed_domains"]
        self._safe_mode_allowed_domains = safe_mode_allowed_domains

        if not api_key:
            raise LoopsConfigurationError(
                "API key not configured. Set LOOPS_API_KEY env var or call pyloops.configure(api_key='...')"
            )

        self._client = AuthenticatedClient(
            base_url=self._normalize_base_url(base_url),
            token=api_key,
            prefix="Bearer",
        )

    @staticmethod
    def _normalize_base_url(base_url: str) -> str:
        """Normalize the base URL for the Loops API.

        As of the Loops API v1.14.x update, the ``/v1`` version segment is part of
        every endpoint path (e.g. ``/v1/api-key``) rather than the base URL. Older
        pyloops versions defaulted the base URL to ``https://app.loops.so/api/v1``,
        so a base URL that still ends in ``/v1`` would produce doubled paths like
        ``/api/v1/v1/api-key``.

        To keep upgrades smooth, any trailing ``/v1`` (and trailing slashes) is
        stripped here, with a ``DeprecationWarning`` so callers know to drop it.
        """
        normalized = base_url.rstrip("/")
        if normalized.endswith("/v1"):
            warnings.warn(
                "base_url ending in '/v1' is deprecated: the Loops API version segment "
                "is now part of each endpoint path. Drop the trailing '/v1' from your "
                "base_url (e.g. use 'https://app.loops.so/api'). It is being stripped "
                "automatically for now.",
                DeprecationWarning,
                stacklevel=3,
            )
            normalized = normalized[: -len("/v1")]
        return normalized

    def _handle_response(self, response: Response[Any]) -> Any:
        """
        Check for rate limiting and return parsed response.

        Args:
            response: Response object from API call

        Returns:
            Parsed response data

        Raises:
            LoopsRateLimitError: If rate limit is exceeded (HTTP 429)
        """
        if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
            limit = int(response.headers.get("x-ratelimit-limit", 0))
            remaining = int(response.headers.get("x-ratelimit-remaining", 0))
            raise LoopsRateLimitError(limit=limit, remaining=remaining)
        return response.parsed

    def _validate_email(self, email: str | None) -> None:
        """Validate email domain against the allowlist when safe mode is enabled."""
        if not self._safe_mode or not email:
            return
        if not self._safe_mode_allowed_domains:
            raise LoopsConfigurationError(
                "safe_mode is enabled but no safe_mode_allowed_domains configured. "
                "Set allowed domains via configure(safe_mode_allowed_domains=('@test.com',)) "
                "or pass them to LoopsClient()."
            )
        email_lower = email.lower()
        if not any(email_lower.endswith(domain) for domain in self._safe_mode_allowed_domains):
            raise LoopsUnsafeEmailError(email, self._safe_mode_allowed_domains)

    async def health(self) -> bool:
        """
        Validate the API key.

        Returns:
            True if API key is valid

        Raises:
            LoopsError: If API key is invalid or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await test_api_key.asyncio_detailed(client=self._client)
        result = self._handle_response(response)

        if isinstance(result, TestApiKeyResponse401):
            raise LoopsError("Invalid API key", status_code=401, response_data=result)

        if result is None:
            raise LoopsError("Failed to validate API key", status_code=None)

        return True

    async def create_contact(
        self,
        email: str,
        user_id: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        source: str | None = None,
        subscribed: bool | None = None,
        user_group: str | None = None,
        mailing_lists: dict[str, bool] | None = None,
        **custom_properties: bool | float | str,
    ) -> ContactSuccessResponse:
        """
        Create a new contact.

        This endpoint will return a 409 Conflict error if a matching contact already exists.
        If you want to "update or create" contacts, use upsert_contact() instead.

        Args:
            email: Contact email address (required)
            user_id: Custom user ID
            first_name: First name
            last_name: Last name
            source: Custom source value to replace the default "API"
            subscribed: Subscription status. Note: API defaults to true if not provided.
            user_group: User group
            mailing_lists: Dictionary of mailing list IDs to subscription status
            **custom_properties: Additional custom contact properties

        Returns:
            ContactSuccessResponse on success

        Raises:
            LoopsContactExistsError: If a contact with this email already exists (409)
            LoopsError: If the request fails (400)
            LoopsRateLimitError: If rate limit is exceeded
        """
        self._validate_email(email)

        # Build the request
        request = ContactRequest(
            email=email,
            first_name=first_name if first_name else UNSET,
            last_name=last_name if last_name else UNSET,
            subscribed=subscribed if subscribed is not None else UNSET,
            user_group=user_group if user_group else UNSET,
            user_id=user_id if user_id else UNSET,
            mailing_lists=MailingListSubscriptions.from_dict(mailing_lists) if mailing_lists else UNSET,
        )

        # NOTE: `source` is not specified in the specification
        if source:
            if custom_properties:
                custom_properties["source"] = source
            else:
                custom_properties = {"source": source}

        # Add custom properties
        if custom_properties:
            request.additional_properties = custom_properties

        response = await create_contact.asyncio_detailed(client=self._client, body=request)
        result = self._handle_response(response)

        if isinstance(result, ContactFailureResponse):
            # Handle 409 Conflict (contact already exists)
            if response.status_code == 409:
                raise LoopsContactExistsError(getattr(result, "message", "A contact with this email already exists"))
            # Handle other errors (400, etc.)
            raise LoopsError(
                f"Failed to create contact: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, ContactSuccessResponse):
            return result

        raise LoopsError("Failed to create contact", status_code=None, response_data=result)

    async def upsert_contact(
        self,
        email: str | None = None,
        user_id: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        source: str | None = None,
        subscribed: bool | None = None,
        user_group: str | None = None,
        mailing_lists: dict[str, bool] | None = None,
        **custom_properties: bool | float | str,
    ) -> ContactSuccessResponse:
        """
        Create or update a contact (upsert operation).

        Note: This endpoint creates a contact if one doesn't exist. To update a contact's
        email address, the contact must have a userId. If both email and userId are provided,
        the system will look for a contact with either value and update accordingly.

        Args:
            email: Contact email address
            user_id: Custom user ID
            first_name: First name
            last_name: Last name
            source: Custom source value to replace the default "API"
            subscribed: Subscription status. WARNING: Setting subscribed=True will re-subscribe
                previously unsubscribed contacts. Leave as None unless you specifically want to
                change subscription status.
            user_group: User group
            mailing_lists: Dictionary of mailing list IDs to subscription status
            **custom_properties: Additional custom contact properties

        Returns:
            ContactSuccessResponse on success

        Raises:
            LoopsError: If the request fails
        """
        if not email and not user_id:
            raise LoopsError("Either email or user_id must be provided")

        self._validate_email(email)

        # Build the request
        request = ContactUpdateRequest(
            email=email if email else UNSET,
            user_id=user_id if user_id else UNSET,
            first_name=first_name if first_name else UNSET,
            last_name=last_name if last_name else UNSET,
            subscribed=subscribed if subscribed is not None else UNSET,
            user_group=user_group if user_group else UNSET,
            mailing_lists=MailingListSubscriptions.from_dict(mailing_lists) if mailing_lists else UNSET,
        )

        # Add source to custom properties if provided (not in generated model yet)
        if source:
            if custom_properties:
                custom_properties["source"] = source
            else:
                custom_properties = {"source": source}

        # Add custom properties
        if custom_properties:
            request.additional_properties = custom_properties

        response = await update_contact.asyncio_detailed(client=self._client, body=request)
        result = self._handle_response(response)

        if isinstance(result, ContactFailureResponse):
            raise LoopsError(
                f"Failed to upsert contact: {getattr(result, 'message', 'Unknown error')}",
                status_code=400,
                response_data=result,
            )

        if isinstance(result, ContactSuccessResponse):
            return result

        raise LoopsError("Failed to upsert contact", status_code=None, response_data=result)

    async def find_contact(
        self,
        email: str | None = None,
        user_id: str | None = None,
    ) -> list[Contact] | None:
        """
        Find a contact by email or user_id.

        Args:
            email: Contact email address
            user_id: Custom user ID

        Returns:
            List of Contact objects if found, None otherwise

        Raises:
            LoopsError: If the request fails
        """
        if not email and not user_id:
            raise LoopsError("Either email or user_id must be provided")

        self._validate_email(email)

        response = await find_contact.asyncio_detailed(
            client=self._client,
            email=email if email else UNSET,
            user_id=user_id if user_id else UNSET,
        )
        result = self._handle_response(response)

        if isinstance(result, ContactFailureResponse):
            # Contact not found is not an error, return None
            if getattr(result, "success", None) is False:
                return None
            raise LoopsError(
                f"Failed to find contact: {getattr(result, 'message', 'Unknown error')}",
                status_code=400,
                response_data=result,
            )

        if isinstance(result, list):
            return result

        return None

    async def delete_contact(
        self,
        email: str | None = None,
        user_id: str | None = None,
    ) -> bool:
        """
        Delete a contact by email or user_id.

        Args:
            email: Contact email address
            user_id: Custom user ID

        Returns:
            True if deleted successfully, False if not found

        Raises:
            LoopsError: If the request fails
        """
        if not email and not user_id:
            raise LoopsError("Either email or user_id must be provided")

        self._validate_email(email)

        # ContactDeleteRequest requires both fields, use empty string for the unused one
        body = ContactDeleteRequest(
            email=email if email else "",
            user_id=user_id if user_id else "",
        )

        response = await delete_contact.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)

        if isinstance(result, ContactFailureResponse):
            # Not found is not an error
            if getattr(result, "success", None) is False:
                return False
            raise LoopsError(
                f"Failed to delete contact: {getattr(result, 'message', 'Unknown error')}",
                status_code=400,
                response_data=result,
            )

        if isinstance(result, ContactSuccessResponse):
            return True

        return False

    async def create_contact_property(
        self,
        name: str,
        property_type: str,
    ) -> dict[str, Any]:
        """
        Create a new custom contact property.

        Args:
            name: Property name
            property_type: Property type (e.g., "string", "number", "boolean")

        Returns:
            Response data as dictionary

        Raises:
            LoopsError: If the request fails
        """
        body = ContactPropertyCreateRequest(name=name, type_=ContactPropertyCreateRequestType(property_type))

        response = await create_contact_property.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)

        if result is None:
            raise LoopsError("Failed to create contact property", status_code=None)

        if hasattr(result, "to_dict"):
            return result.to_dict()

        return {}

    async def list_contact_properties(self) -> list[ContactProperty]:
        """
        List all contact properties.

        Returns:
            List of ContactProperty objects

        Raises:
            LoopsError: If the request fails
        """
        response = await list_contact_properties.asyncio_detailed(client=self._client)
        result = self._handle_response(response)

        if result is None:
            raise LoopsError("Failed to list contact properties", status_code=None)

        if isinstance(result, list):
            return result

        return []

    async def list_mailing_lists(self) -> list[MailingList]:
        """
        List all mailing lists.

        Returns:
            List of MailingList objects

        Raises:
            LoopsError: If the request fails
        """
        response = await list_mailing_lists.asyncio_detailed(client=self._client)
        result = self._handle_response(response)

        if result is None:
            raise LoopsError("Failed to list mailing lists", status_code=None)

        if isinstance(result, list):
            return result

        return []

    async def send_event(
        self,
        event_name: str,
        email: str | None = None,
        user_id: str | None = None,
        event_properties: dict[str, Any] | None = None,
        mailing_lists: dict[str, bool] | None = None,
        idempotency_key: str | None = None,
        **additional_properties: bool | float | str,
    ) -> EventSuccessResponse:
        """
        Send an event to trigger emails in Loops.

        Args:
            event_name: Name of the event
            email: Contact email address
            user_id: Custom user ID
            event_properties: Event properties dictionary
            mailing_lists: Dictionary of mailing list IDs to subscription status
            idempotency_key: Optional idempotency key (auto-generated if not provided)
            **additional_properties: Contact properties to update (e.g., firstName="John", customField=123)

        Returns:
            EventSuccessResponse on success

        Raises:
            LoopsError: If the request fails
        """
        if not email and not user_id:
            raise LoopsError("Either email or user_id must be provided")

        self._validate_email(email)

        # Auto-generate idempotency key if not provided
        if idempotency_key is None:
            idempotency_key = str(uuid.uuid4())

        # The events endpoint has an untyped request schema in the spec, so the
        # generated client sends the body dict as-is. Keys must be camelCase, and
        # contact properties are merged in at the top level (as with the old model).
        body: dict[str, Any] = {"eventName": event_name}
        if email:
            body["email"] = email
        if user_id:
            body["userId"] = user_id
        if event_properties:
            body["eventProperties"] = event_properties
        if mailing_lists:
            body["mailingLists"] = mailing_lists
        if additional_properties:
            body.update(additional_properties)

        response = await send_event.asyncio_detailed(
            client=self._client,
            body=body,
            idempotency_key=idempotency_key,
        )
        result = self._handle_response(response)

        if isinstance(result, EventFailureResponse):
            raise LoopsError(
                f"Failed to send event: {getattr(result, 'message', 'Unknown error')}",
                status_code=400,
                response_data=result,
            )

        if isinstance(result, IdempotencyKeyFailureResponse):
            raise LoopsError(
                f"Idempotency key conflict: {getattr(result, 'message', 'Duplicate request')}",
                status_code=409,
                response_data=result,
            )

        if isinstance(result, EventSuccessResponse):
            return result

        raise LoopsError("Failed to send event", status_code=None, response_data=result)

    async def send_transactional_email(
        self,
        transactional_id: str,
        email: str,
        data_variables: dict[str, Any] | None = None,
        attachments: list[dict[str, Any]] | None = None,
        add_to_audience: bool | None = None,
        idempotency_key: str | None = None,
    ) -> TransactionalSuccessResponse:
        """
        Send a transactional email to a contact.

        Args:
            transactional_id: ID of the transactional email template
            email: Recipient email address
            data_variables: Object containing data as defined by data variables in the template.
                Values can be string or number.
            attachments: List of file objects sent along with the email. Email us to enable
                attachments on your account before using them with the API.
            add_to_audience: If true, a contact will be created in your audience using the email
                value (if a matching contact doesn't already exist). Default: false
            idempotency_key: Optional idempotency key (up to 100 characters) to avoid duplicate
                requests. We recommend using V4 UUIDs. Auto-generated if not provided.

        Returns:
            TransactionalSuccessResponse on success

        Raises:
            LoopsError: If the request fails (400, 404) or idempotency key conflict (409)
            LoopsRateLimitError: If rate limit is exceeded
        """
        self._validate_email(email)

        # Auto-generate idempotency key if not provided
        if idempotency_key is None:
            idempotency_key = str(uuid.uuid4())

        # Build the request
        request = TransactionalRequest(
            transactional_id=transactional_id,
            email=email,
            add_to_audience=add_to_audience if add_to_audience is not None else UNSET,
            data_variables=TransactionalRequestDataVariables.from_dict(data_variables) if data_variables else UNSET,
            attachments=[TransactionalRequestAttachmentsItem.from_dict(att) for att in attachments]
            if attachments
            else UNSET,
        )

        response = await send_transactional_email.asyncio_detailed(
            client=self._client,
            body=request,
            idempotency_key=idempotency_key,
        )
        result = self._handle_response(response)

        # Handle error responses (all return success=false + message)
        failure_types = (
            TransactionalSendFailureResponse,
            TransactionalFailure2Response,
            TransactionalFailure3Response,
            TransactionalFailure4Response,
            TransactionalFailure5Response,
        )
        if isinstance(result, failure_types):
            error_msg = getattr(result, "message", "Unknown error")
            # 404 means transactional email not found
            if response.status_code == 404:
                raise LoopsError(
                    f"Transactional email not found: {error_msg}",
                    status_code=404,
                    response_data=result,
                )
            # Other 400 errors
            raise LoopsError(
                f"Failed to send transactional email: {error_msg}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, IdempotencyKeyFailureResponse):
            raise LoopsError(
                f"Idempotency key conflict: {getattr(result, 'message', 'Duplicate request')}",
                status_code=409,
                response_data=result,
            )

        if isinstance(result, TransactionalSuccessResponse):
            return result

        raise LoopsError("Failed to send transactional email", status_code=None, response_data=result)

    async def list_transactional_emails(
        self,
        per_page: int | None = None,
        cursor: str | None = None,
    ) -> TransactionalEmailsResponse:
        """
        Retrieve a list of your transactional emails.

        Args:
            per_page: How many results to return per request (10-50). Default: 20
            cursor: Pagination cursor for a specific page of results

        Returns:
            TransactionalEmailsResponse containing:
                - pagination: Pagination info with nextCursor, totalResults, etc.
                - data: List of TransactionalEmail objects

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_published_transactional_emails.asyncio_detailed(
            client=self._client,
            per_page=str(per_page) if per_page is not None else UNSET,
            cursor=cursor if cursor else UNSET,
        )
        result = self._handle_response(response)

        # The generated endpoint returns Any, so we parse manually using custom models
        if response.status_code == 200:
            try:
                data = json.loads(response.content)
                return TransactionalEmailsResponse.from_dict(data)
            except (json.JSONDecodeError, AttributeError, KeyError) as e:
                raise LoopsError(f"Failed to parse transactional emails response: {e}", status_code=200)

        raise LoopsError("Failed to list transactional emails", status_code=response.status_code, response_data=result)

    async def list_sending_ips(self) -> list[str]:
        """
        Retrieve a list of Loops' dedicated sending IP addresses.

        Returns:
            List of IP address strings

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_dedicated_sending_ips.asyncio_detailed(client=self._client)
        result = self._handle_response(response)

        if isinstance(result, list):
            return result

        raise LoopsError("Failed to list sending IPs", status_code=None, response_data=result)

    # ------------------------------------------------------------------
    # Campaigns
    # ------------------------------------------------------------------

    async def list_campaigns(
        self,
        per_page: int | None = None,
        cursor: str | None = None,
    ) -> ListCampaignsResponse:
        """
        Retrieve a paginated list of campaigns.

        Args:
            per_page: Results per page (10-50). Default: 20
            cursor: Pagination cursor

        Returns:
            ListCampaignsResponse with pagination and data

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_campaigns.asyncio_detailed(
            client=self._client,
            per_page=str(per_page) if per_page is not None else UNSET,
            cursor=cursor if cursor else UNSET,
        )
        result = self._handle_response(response)

        if isinstance(result, CampaignFailureResponse):
            raise LoopsError(
                f"Failed to list campaigns: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, ListCampaignsResponse):
            return result

        raise LoopsError("Failed to list campaigns", status_code=None, response_data=result)

    async def get_campaign(self, campaign_id: str) -> CampaignResponse:
        """
        Retrieve a single campaign by ID.

        Args:
            campaign_id: The campaign ID

        Returns:
            CampaignResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_campaign.asyncio_detailed(
            campaign_id=campaign_id,
            client=self._client,
        )
        result = self._handle_response(response)

        if isinstance(result, CampaignFailureResponse):
            raise LoopsError(
                f"Failed to get campaign: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, CampaignResponse):
            return result

        raise LoopsError("Failed to get campaign", status_code=None, response_data=result)

    async def create_campaign(self, name: str) -> CreateCampaignResponse:
        """
        Create a new campaign.

        Args:
            name: Campaign name

        Returns:
            CreateCampaignResponse with campaign_id and linked email_message_id

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = CreateCampaignRequest(name=name)
        response = await create_campaign.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)

        if isinstance(result, CampaignFailureResponse):
            raise LoopsError(
                f"Failed to create campaign: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, CreateCampaignResponse):
            return result

        raise LoopsError("Failed to create campaign", status_code=None, response_data=result)

    async def update_campaign(self, campaign_id: str, name: str) -> CampaignResponse:
        """
        Update a campaign's name.

        Args:
            campaign_id: The campaign ID
            name: New campaign name

        Returns:
            CampaignResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = UpdateCampaignRequest(name=name)
        response = await update_campaign.asyncio_detailed(
            campaign_id=campaign_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)

        if isinstance(result, CampaignFailureResponse):
            raise LoopsError(
                f"Failed to update campaign: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, CampaignResponse):
            return result

        raise LoopsError("Failed to update campaign", status_code=None, response_data=result)

    # ------------------------------------------------------------------
    # Components
    # ------------------------------------------------------------------

    async def list_components(
        self,
        per_page: int | None = None,
        cursor: str | None = None,
    ) -> ListComponentsResponse:
        """
        Retrieve a paginated list of components.

        Args:
            per_page: Results per page (10-50). Default: 20
            cursor: Pagination cursor

        Returns:
            ListComponentsResponse with pagination and data

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_components.asyncio_detailed(
            client=self._client,
            per_page=str(per_page) if per_page is not None else UNSET,
            cursor=cursor if cursor else UNSET,
        )
        result = self._handle_response(response)

        if isinstance(result, ComponentFailureResponse):
            raise LoopsError(
                f"Failed to list components: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, ListComponentsResponse):
            return result

        raise LoopsError("Failed to list components", status_code=None, response_data=result)

    async def get_component(self, component_id: str) -> ComponentResponse:
        """
        Retrieve a single component by ID.

        Args:
            component_id: The component ID

        Returns:
            ComponentResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_component.asyncio_detailed(
            component_id=component_id,
            client=self._client,
        )
        result = self._handle_response(response)

        if isinstance(result, ComponentFailureResponse):
            raise LoopsError(
                f"Failed to get component: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, ComponentResponse):
            return result

        raise LoopsError("Failed to get component", status_code=None, response_data=result)

    async def create_component(self, name: str, lmx: str) -> ComponentResponse:
        """Create a new component.

        Args:
            name: Component name
            lmx: Component body as LMX (Loops markup)

        Returns:
            ComponentResponse

        Raises:
            LoopsError: If the request fails (e.g. invalid LMX)
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = CreateComponentBody(name=name, lmx=lmx)
        response = await create_component.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=ComponentResponse,
            failure=ComponentFailureResponse,
            action="create component",
        )

    async def update_component(
        self,
        component_id: str,
        name: str | None = None,
        lmx: str | None = None,
    ) -> UpdateComponentResponse:
        """Update a component's name and/or body.

        Args:
            component_id: The component ID
            name: New component name
            lmx: New component body as LMX. Changing the body updates every email
                that uses the component; the count is returned as
                ``affectedEmailCount``.

        Returns:
            UpdateComponentResponse (includes ``affected_email_count``)

        Raises:
            LoopsError: If not found (404), the LMX is invalid, or the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = UpdateComponentBody(
            name=name if name is not None else UNSET,
            lmx=lmx if lmx is not None else UNSET,
        )
        response = await update_component.asyncio_detailed(
            component_id=component_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=UpdateComponentResponse,
            failure=(ComponentFailureResponse, ComponentValidationFailureResponse),
            action="update component",
        )

    # ------------------------------------------------------------------
    # Themes
    # ------------------------------------------------------------------

    async def list_themes(
        self,
        per_page: int | None = None,
        cursor: str | None = None,
    ) -> ListThemesResponse:
        """
        Retrieve a paginated list of themes.

        Args:
            per_page: Results per page (10-50). Default: 20
            cursor: Pagination cursor

        Returns:
            ListThemesResponse with pagination and data

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_themes.asyncio_detailed(
            client=self._client,
            per_page=str(per_page) if per_page is not None else UNSET,
            cursor=cursor if cursor else UNSET,
        )
        result = self._handle_response(response)

        if isinstance(result, ThemeFailureResponse):
            raise LoopsError(
                f"Failed to list themes: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, ListThemesResponse):
            return result

        raise LoopsError("Failed to list themes", status_code=None, response_data=result)

    async def get_theme(self, theme_id: str) -> ThemeResponse:
        """
        Retrieve a single theme by ID.

        Args:
            theme_id: The theme ID

        Returns:
            ThemeResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_theme.asyncio_detailed(
            theme_id=theme_id,
            client=self._client,
        )
        result = self._handle_response(response)

        if isinstance(result, ThemeFailureResponse):
            raise LoopsError(
                f"Failed to get theme: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, ThemeResponse):
            return result

        raise LoopsError("Failed to get theme", status_code=None, response_data=result)

    async def create_theme(self, name: str, styles: dict[str, Any] | None = None) -> ThemeResponse:
        """Create a new theme.

        Args:
            name: Theme name
            styles: Optional dictionary of styling preferences mirroring the LMX
                ``<Style />`` attributes (e.g. ``{"bodyColor": "#ffffff",
                "textBaseFontSize": "16px"}``). See the Loops docs for the full
                list of supported keys.

        Returns:
            ThemeResponse

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = CreateThemeBody(
            name=name,
            styles=ThemeStyles.from_dict(styles) if styles else UNSET,
        )
        response = await create_theme.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=ThemeResponse,
            failure=ThemeFailureResponse,
            action="create theme",
        )

    async def update_theme(
        self,
        theme_id: str,
        name: str | None = None,
        styles: dict[str, Any] | None = None,
    ) -> UpdateThemeResponse:
        """Update a theme's name and/or styles.

        Args:
            theme_id: The theme ID
            name: New theme name
            styles: New dictionary of styling preferences (see ``create_theme``).
                Changing styles updates every email using the theme; the count is
                returned as ``affectedEmailCount``.

        Returns:
            UpdateThemeResponse (includes ``affected_email_count``)

        Raises:
            LoopsError: If not found (404) or the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = UpdateThemeBody(
            name=name if name is not None else UNSET,
            styles=ThemeStyles.from_dict(styles) if styles else UNSET,
        )
        response = await update_theme.asyncio_detailed(
            theme_id=theme_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=UpdateThemeResponse,
            failure=ThemeFailureResponse,
            action="update theme",
        )

    # ------------------------------------------------------------------
    # Email Messages
    # ------------------------------------------------------------------

    async def get_email_message(self, email_message_id: str) -> EmailMessageResponse:
        """
        Retrieve an email message by ID.

        Args:
            email_message_id: The email message ID

        Returns:
            EmailMessageResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_email_message.asyncio_detailed(
            email_message_id=email_message_id,
            client=self._client,
        )
        result = self._handle_response(response)

        if isinstance(result, EmailMessageFailureResponse):
            raise LoopsError(
                f"Failed to get email message: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, EmailMessageResponse):
            return result

        raise LoopsError("Failed to get email message", status_code=None, response_data=result)

    async def update_email_message(
        self,
        email_message_id: str,
        subject: str | None = None,
        preview_text: str | None = None,
        from_name: str | None = None,
        from_email: str | None = None,
        reply_to_email: str | None = None,
        lmx: str | None = None,
        expected_revision_id: str | None = None,
    ) -> EmailMessageResponse:
        """
        Update an email message.

        Args:
            email_message_id: The email message ID
            subject: Email subject line
            preview_text: Preview text shown in inbox
            from_name: Sender display name
            from_email: Sender username (without @ or domain; team domain is appended)
            reply_to_email: Reply-to email address (must be empty or a valid email)
            lmx: Email body as LMX with styles embedded in a <Style /> tag
            expected_revision_id: Optimistic concurrency token (raises 409 if out of sync)

        Returns:
            EmailMessageResponse

        Raises:
            LoopsError: If the request fails or revision conflict (409)
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = UpdateEmailMessageRequest(
            subject=subject if subject is not None else UNSET,
            preview_text=preview_text if preview_text is not None else UNSET,
            from_name=from_name if from_name is not None else UNSET,
            from_email=from_email if from_email is not None else UNSET,
            reply_to_email=reply_to_email if reply_to_email is not None else UNSET,
            lmx=lmx if lmx is not None else UNSET,
            expected_revision_id=expected_revision_id if expected_revision_id is not None else UNSET,
        )
        response = await update_email_message.asyncio_detailed(
            email_message_id=email_message_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)

        if isinstance(result, EmailMessageFailureResponse):
            raise LoopsError(
                f"Failed to update email message: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, EmailMessageResponse):
            return result

        raise LoopsError("Failed to update email message", status_code=None, response_data=result)

    async def get_email_message_guardian(self, email_message_id: str) -> EmailMessageGuardianResponse:
        """Run Guardian content checks against a saved email message.

        Guardian runs the same validation the Loops editor performs (missing or
        invalid hrefs, unsupported contact/event properties, malformed buttons,
        missing required data variables, and so on).

        Note: Guardian does not support MJML email messages.

        Args:
            email_message_id: The email message ID to check

        Returns:
            EmailMessageGuardianResponse with ``errors`` and ``warnings`` lists

        Raises:
            LoopsError: If not found (404) or the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_email_message_guardian.asyncio_detailed(
            email_message_id=email_message_id,
            client=self._client,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=EmailMessageGuardianResponse,
            failure=EmailMessageFailureResponse,
            action="get email message guardian checks",
        )

    # ------------------------------------------------------------------
    # Contact Suppression
    # ------------------------------------------------------------------

    async def get_contact_suppression(
        self,
        email: str | None = None,
        user_id: str | None = None,
    ) -> ContactSuppressionStatusResponse:
        """
        Get the suppression status of a contact.

        Args:
            email: Contact email address
            user_id: Custom user ID

        Returns:
            ContactSuppressionStatusResponse with is_suppressed flag and removal quota

        Raises:
            LoopsError: If neither email nor user_id is provided, or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        if not email and not user_id:
            raise LoopsError("Either email or user_id must be provided")

        response = await get_contact_suppression.asyncio_detailed(
            client=self._client,
            email=email if email else UNSET,
            user_id=user_id if user_id else UNSET,
        )
        result = self._handle_response(response)

        if isinstance(result, ContactFailureResponse):
            raise LoopsError(
                f"Failed to get suppression status: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, ContactSuppressionStatusResponse):
            return result

        raise LoopsError("Failed to get suppression status", status_code=None, response_data=result)

    async def remove_contact_suppression(
        self,
        email: str | None = None,
        user_id: str | None = None,
    ) -> ContactSuppressionRemoveResponse:
        """
        Remove a contact from the suppression list.

        Args:
            email: Contact email address
            user_id: Custom user ID

        Returns:
            ContactSuppressionRemoveResponse with success flag and remaining removal quota

        Raises:
            LoopsError: If neither email nor user_id is provided, or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        if not email and not user_id:
            raise LoopsError("Either email or user_id must be provided")

        response = await remove_contact_suppression.asyncio_detailed(
            client=self._client,
            email=email if email else UNSET,
            user_id=user_id if user_id else UNSET,
        )
        result = self._handle_response(response)

        if isinstance(result, ContactFailureResponse):
            raise LoopsError(
                f"Failed to remove suppression: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )

        if isinstance(result, ContactSuppressionRemoveResponse):
            return result

        raise LoopsError("Failed to remove suppression", status_code=None, response_data=result)

    # ------------------------------------------------------------------
    # Shared result helper (used by the endpoint families below)
    # ------------------------------------------------------------------

    def _unwrap(
        self,
        result: Any,
        response: Response[Any],
        *,
        success: type | tuple[type, ...],
        failure: type | tuple[type, ...],
        action: str,
    ) -> Any:
        """Return the parsed *result* or raise a ``LoopsError``.

        Mirrors the success/failure handling used by the older wrapper methods:
        failure models raise with their ``message``; the expected success type is
        returned; anything else raises a generic error.
        """
        if isinstance(result, failure):
            raise LoopsError(
                f"Failed to {action}: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )
        if isinstance(result, success):
            return result
        raise LoopsError(f"Failed to {action}", status_code=None, response_data=result)

    def _unwrap_raw(
        self,
        result: Any,
        response: Response[Any],
        *,
        failure: type | tuple[type, ...],
        action: str,
    ) -> Any:
        """Return the raw JSON body for endpoints whose success payload is untyped.

        Some Loops endpoints (e.g. the workflow node reads/writes) expose an
        unstructured success schema, so ``openapi-python-client`` does not emit a
        parse branch for the 2xx response and ``response.parsed`` is ``None``.
        For those we decode ``response.content`` directly and return the parsed
        JSON, mirroring how ``list_transactional_emails`` handles its response.
        """
        if isinstance(result, failure):
            raise LoopsError(
                f"Failed to {action}: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )
        if 200 <= response.status_code < 300:
            try:
                return json.loads(response.content)
            except (json.JSONDecodeError, ValueError) as exc:
                raise LoopsError(f"Failed to parse {action} response: {exc}", status_code=response.status_code)
        raise LoopsError(f"Failed to {action}", status_code=response.status_code, response_data=result)

    # ------------------------------------------------------------------
    # Transactional email templates (1.14.x)
    # ------------------------------------------------------------------

    async def list_transactional_templates(
        self,
        per_page: int | None = None,
        cursor: str | None = None,
    ) -> ListTransactionalsResourceResponse:
        """Retrieve a paginated list of transactional email templates.

        Args:
            per_page: Results per page (10-50). Default: 20
            cursor: Pagination cursor

        Returns:
            ListTransactionalsResourceResponse with pagination and data

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_transactional_emails.asyncio_detailed(
            client=self._client,
            per_page=str(per_page) if per_page is not None else UNSET,
            cursor=cursor if cursor else UNSET,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=ListTransactionalsResourceResponse,
            failure=TransactionalFailureResponse,
            action="list transactional templates",
        )

    async def get_transactional_template(self, transactional_id: str) -> TransactionalResource:
        """Retrieve a single transactional email template by ID.

        Args:
            transactional_id: The transactional email template ID

        Returns:
            TransactionalResource

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_transactional_email.asyncio_detailed(
            transactional_id=transactional_id,
            client=self._client,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=TransactionalResource,
            failure=TransactionalFailureResponse,
            action="get transactional template",
        )

    async def create_transactional_template(
        self,
        name: str,
        transactional_group_id: str | None = None,
    ) -> TransactionalDraftResponse:
        """Create a new (draft) transactional email template.

        Args:
            name: Template name
            transactional_group_id: Optional transactional group to add the template to

        Returns:
            TransactionalDraftResponse

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = CreateTransactionalRequest(
            name=name,
            transactional_group_id=transactional_group_id if transactional_group_id else UNSET,
        )
        response = await create_transactional_email.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=TransactionalDraftResponse,
            failure=TransactionalFailureResponse,
            action="create transactional template",
        )

    async def update_transactional_template(
        self,
        transactional_id: str,
        name: str | None = None,
        transactional_group_id: str | None = None,
    ) -> TransactionalResource:
        """Update a transactional email template.

        Args:
            transactional_id: The transactional email template ID
            name: New template name
            transactional_group_id: New transactional group ID

        Returns:
            TransactionalResource

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = UpdateTransactionalRequest(
            name=name if name is not None else UNSET,
            transactional_group_id=transactional_group_id if transactional_group_id is not None else UNSET,
        )
        response = await update_transactional_email.asyncio_detailed(
            transactional_id=transactional_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=TransactionalResource,
            failure=TransactionalFailureResponse,
            action="update transactional template",
        )

    async def draft_transactional_template(self, transactional_id: str) -> TransactionalDraftResponse:
        """Create/refresh the draft of a transactional email template.

        Args:
            transactional_id: The transactional email template ID

        Returns:
            TransactionalDraftResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await ensure_transactional_draft.asyncio_detailed(
            transactional_id=transactional_id,
            client=self._client,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=TransactionalDraftResponse,
            failure=TransactionalFailureResponse,
            action="draft transactional template",
        )

    async def publish_transactional_template(self, transactional_id: str) -> TransactionalResource:
        """Publish a transactional email template.

        Args:
            transactional_id: The transactional email template ID

        Returns:
            TransactionalResource

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await publish_transactional_email.asyncio_detailed(
            transactional_id=transactional_id,
            client=self._client,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=TransactionalResource,
            failure=TransactionalFailureResponse,
            action="publish transactional template",
        )

    # ------------------------------------------------------------------
    # Uploads (1.14.x)
    # ------------------------------------------------------------------

    async def create_upload(self, content_type: str, content_length: int) -> CreateUploadResponse:
        """Create a pre-signed upload for an asset.

        Args:
            content_type: MIME type of the file to upload (e.g. "image/png")
            content_length: Size of the file in bytes

        Returns:
            CreateUploadResponse with the signed upload URL and upload ID

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = CreateUploadRequest(content_type=content_type, content_length=content_length)
        response = await create_upload.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=CreateUploadResponse,
            failure=UploadFailureResponse,
            action="create upload",
        )

    async def complete_upload(self, upload_id: str) -> CompleteUploadResponse:
        """Mark a previously created upload as complete.

        Args:
            upload_id: The upload ID returned by create_upload()

        Returns:
            CompleteUploadResponse

        Raises:
            LoopsError: If the request fails or the upload limit is exceeded
            LoopsRateLimitError: If rate limit is exceeded
        """
        # Note: the upload-limit-exceeded response uses HTTP 429, which
        # _handle_response already surfaces as LoopsRateLimitError before we get
        # here — so UploadLimitExceededFailureResponse is handled as a rate limit.
        response = await complete_upload.asyncio_detailed(email_asset_id=upload_id, client=self._client)
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=CompleteUploadResponse,
            failure=UploadFailureResponse,
            action="complete upload",
        )

    # ------------------------------------------------------------------
    # Workflows (1.14.x)
    # ------------------------------------------------------------------

    async def list_workflows(
        self,
        per_page: int | None = None,
        cursor: str | None = None,
    ) -> ListWorkflowsResponse:
        """Retrieve a paginated list of workflows.

        Args:
            per_page: Results per page (10-50). Default: 20
            cursor: Pagination cursor

        Returns:
            ListWorkflowsResponse with pagination and data

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_workflows.asyncio_detailed(
            client=self._client,
            per_page=str(per_page) if per_page is not None else UNSET,
            cursor=cursor if cursor else UNSET,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=ListWorkflowsResponse,
            failure=WorkflowFailureResponse,
            action="list workflows",
        )

    async def get_workflow(self, workflow_id: str) -> SimplifiedWorkflow:
        """Retrieve a single workflow by ID.

        Args:
            workflow_id: The workflow ID

        Returns:
            SimplifiedWorkflow

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_workflow.asyncio_detailed(workflow_id=workflow_id, client=self._client)
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=SimplifiedWorkflow,
            failure=WorkflowFailureResponse,
            action="get workflow",
        )

    async def get_workflow_node(self, workflow_id: str, node_id: str) -> dict[str, Any]:
        """Retrieve a single node within a workflow.

        Args:
            workflow_id: The workflow ID
            node_id: The node ID

        Returns:
            The workflow node as a dictionary. Node payloads are polymorphic
            (the shape depends on ``typeName``), so the raw JSON body is
            returned rather than a single typed model.

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_workflow_node.asyncio_detailed(
            workflow_id=workflow_id,
            node_id=node_id,
            client=self._client,
        )
        result = self._handle_response(response)
        return self._unwrap_raw(
            result,
            response,
            failure=WorkflowFailureResponse,
            action="get workflow node",
        )

    async def create_workflow(
        self,
        name: str,
        description: str | None = None,
        mailing_list_id: str | None = None,
    ) -> SimplifiedWorkflow:
        """Create a new (draft) workflow.

        The workflow is created with a blank trigger and an exit node; use the
        workflow node methods to build out its graph.

        Args:
            name: Workflow name
            description: Optional workflow description
            mailing_list_id: Optional mailing list to associate with the workflow

        Returns:
            SimplifiedWorkflow

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = CreateWorkflowRequest(
            name=name,
            description=description if description is not None else UNSET,
            mailing_list_id=mailing_list_id if mailing_list_id is not None else UNSET,
        )
        response = await create_workflow.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=SimplifiedWorkflow,
            failure=WorkflowFailureResponse,
            action="create workflow",
        )

    async def update_workflow(
        self,
        workflow_id: str,
        expected_revision_id: str | None,
        name: str | None = None,
        description: str | None = None,
    ) -> SimplifiedWorkflow:
        """Update a workflow's name and/or description.

        Args:
            workflow_id: The workflow ID
            expected_revision_id: Optimistic concurrency token. Pass the latest
                ``workflow_revision_id`` (or ``None`` for pre-revision workflows);
                a stale value raises a 409 conflict.
            name: New workflow name
            description: New workflow description

        Returns:
            SimplifiedWorkflow

        Raises:
            LoopsError: If not found (404) or a revision conflict occurs (409)
            LoopsRateLimitError: If rate limit is exceeded
        """
        # This endpoint's request schema is untyped in the spec, so the generated
        # client sends the body dict as-is (no model). Keys must be camelCase.
        body: dict[str, Any] = {"expectedRevisionId": expected_revision_id}
        if name is not None:
            body["name"] = name
        if description is not None:
            body["description"] = description
        response = await update_workflow_properties.asyncio_detailed(
            workflow_id=workflow_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=SimplifiedWorkflow,
            failure=WorkflowFailureResponse,
            action="update workflow",
        )

    async def change_workflow_mailing_list(
        self,
        workflow_id: str,
        expected_revision_id: str | None,
        mailing_list_id: str | None,
        dry_run: bool | None = None,
        queued_contact_policy: str | None = None,
    ) -> WorkflowMailingListUpdatedResponse | WorkflowMailingListPreview:
        """Change (or clear) the mailing list associated with a workflow.

        Args:
            workflow_id: The workflow ID
            expected_revision_id: Optimistic concurrency token (see ``update_workflow``)
            mailing_list_id: The mailing list to associate, or ``None`` to clear it
            dry_run: If True, validate the change without applying it. The response
                is a ``WorkflowMailingListPreview`` describing what would happen.
            queued_contact_policy: How to handle contacts currently queued in the
                workflow: ``"fail"`` (default) or ``"discard"``.

        Returns:
            WorkflowMailingListUpdatedResponse when applied, or
            WorkflowMailingListPreview for a dry run / when queued contacts are found.

        Raises:
            LoopsError: If not found (404) or a revision conflict occurs (409)
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = ChangeWorkflowMailingListRequest(
            expected_revision_id=expected_revision_id,
            mailing_list_id=mailing_list_id,
            dry_run=dry_run if dry_run is not None else UNSET,
            queued_contact_policy=WorkflowQueuedContactPolicy(queued_contact_policy)
            if queued_contact_policy is not None
            else UNSET,
        )
        response = await change_workflow_mailing_list.asyncio_detailed(
            workflow_id=workflow_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=(WorkflowMailingListUpdatedResponse, WorkflowMailingListPreview),
            failure=WorkflowFailureResponse,
            action="change workflow mailing list",
        )

    # ------------------------------------------------------------------
    # Workflow nodes (1.21.x)
    # ------------------------------------------------------------------

    async def create_workflow_node(
        self,
        workflow_id: str,
        node_type_name: str,
        expected_revision_id: str | None,
        from_node_id: str | None = None,
        to_node_id: str | None = None,
        before_node_id: str | None = None,
    ) -> dict[str, Any]:
        """Add a node to a workflow.

        Nodes are inserted either *between* an existing edge (pass ``from_node_id``
        and ``to_node_id``) or *before* an existing node (pass ``before_node_id``).
        New nodes are created with default settings; call ``update_workflow_node``
        afterwards to configure them.

        Args:
            workflow_id: The workflow ID
            node_type_name: The node type to create, one of ``AudienceFilter``,
                ``BranchNode``, ``ExperimentBranchNode``, ``TimerAction``,
                ``SendEmailAction`` or ``VariantNode`` (triggers and exit nodes
                cannot be created).
            expected_revision_id: Optimistic concurrency token (see ``update_workflow``)
            from_node_id: Source node of the edge to insert into (``between`` mode)
            to_node_id: Target node of the edge to insert into (``between`` mode)
            before_node_id: Node to insert before (``before`` mode)

        Returns:
            The API response as a dictionary containing the created ``node`` and the
            updated ``workflow``.

        Raises:
            LoopsError: If the arguments are inconsistent, the workflow/node is not
                found (404), or a revision conflict occurs (409)
            LoopsRateLimitError: If rate limit is exceeded
        """
        node_type = CreateWorkflowNodeTypeName(node_type_name)
        body: CreateWorkflowNodeBeforeRequest | CreateWorkflowNodeBetweenRequest
        if before_node_id is not None:
            if from_node_id is not None or to_node_id is not None:
                raise LoopsError("Pass before_node_id for 'before' inserts or from/to_node_id for 'between', not both")
            body = CreateWorkflowNodeBeforeRequest(
                expected_revision_id=expected_revision_id,
                insert_mode=CreateWorkflowNodeBeforeRequestInsertMode.BEFORE,
                node_type_name=node_type,
                before_node_id=before_node_id,
            )
        elif from_node_id is not None and to_node_id is not None:
            body = CreateWorkflowNodeBetweenRequest(
                expected_revision_id=expected_revision_id,
                insert_mode=CreateWorkflowNodeBetweenRequestInsertMode.BETWEEN,
                node_type_name=node_type,
                from_node_id=from_node_id,
                to_node_id=to_node_id,
            )
        else:
            raise LoopsError(
                "Provide either before_node_id ('before' insert) or both from_node_id and to_node_id ('between' insert)"
            )
        response = await create_workflow_node.asyncio_detailed(
            workflow_id=workflow_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap_raw(
            result,
            response,
            failure=WorkflowFailureResponse,
            action="create workflow node",
        )

    async def update_workflow_node(
        self,
        workflow_id: str,
        node_id: str,
        expected_revision_id: str | None,
        payload: dict[str, Any],
    ) -> Any:
        """Update the settings of a workflow node.

        Args:
            workflow_id: The workflow ID
            node_id: The node ID
            expected_revision_id: Optimistic concurrency token (see ``update_workflow``)
            payload: The node-type-specific settings as a dictionary. The accepted
                keys depend on the node's type (e.g. ``{"amount": 2, "unit": "d"}``
                for a TimerAction, ``{"emailMessageId": "...", "subject": "..."}`` for
                a SendEmailAction). See the Loops docs for each node type's payload.

        Returns:
            The updated node (one of the workflow mutation node models).

        Raises:
            LoopsError: If not found (404), a revision conflict occurs (409), or the
                node type does not support updates (501)
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = UpdateWorkflowNodeRequest.from_dict({"expectedRevisionId": expected_revision_id, "payload": payload})
        response = await update_workflow_node.asyncio_detailed(
            workflow_id=workflow_id,
            node_id=node_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        if isinstance(result, WorkflowFailureResponse):
            raise LoopsError(
                f"Failed to update workflow node: {getattr(result, 'message', 'Unknown error')}",
                status_code=response.status_code,
                response_data=result,
            )
        if result is None:
            raise LoopsError("Failed to update workflow node", status_code=response.status_code)
        return result

    async def add_workflow_branch(
        self,
        workflow_id: str,
        node_id: str,
        expected_revision_id: str | None,
    ) -> AddWorkflowBranchResponse:
        """Add a branch to a BranchNode or ExperimentBranchNode.

        The new branch is created unconfigured; call ``update_workflow_node`` on the
        returned child to configure it.

        Args:
            workflow_id: The workflow ID
            node_id: The BranchNode or ExperimentBranchNode ID
            expected_revision_id: Optimistic concurrency token (see ``update_workflow``)

        Returns:
            AddWorkflowBranchResponse with the created ``node`` and updated ``workflow``

        Raises:
            LoopsError: If not found (404) or a revision conflict occurs (409)
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = AddWorkflowBranchRequest(expected_revision_id=expected_revision_id)
        response = await add_workflow_branch.asyncio_detailed(
            workflow_id=workflow_id,
            node_id=node_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=AddWorkflowBranchResponse,
            failure=WorkflowFailureResponse,
            action="add workflow branch",
        )

    async def delete_workflow_node(
        self,
        workflow_id: str,
        node_id: str,
        expected_revision_id: str | None,
        dry_run: bool | None = None,
        queued_contact_policy: str | None = None,
        recursive: bool = False,
    ) -> WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview:
        """Delete a node from a workflow.

        Args:
            workflow_id: The workflow ID
            node_id: The node ID to delete
            expected_revision_id: Optimistic concurrency token (see ``update_workflow``)
            dry_run: If True, report what would be deleted without applying it.
            queued_contact_policy: How to handle contacts currently queued at the
                node: ``"fail"`` (default) or ``"discard"``.
            recursive: If True, also delete the node's entire downstream subtree;
                otherwise only the single node is removed and its edge re-linked.

        Returns:
            WorkflowDeletedResponse when applied, or WorkflowQueuedContactDeletePreview
            for a dry run / when queued contacts are found.

        Raises:
            LoopsError: If not found (404) or a revision conflict occurs (409)
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = DeleteWorkflowNodeRequest(
            expected_revision_id=expected_revision_id,
            dry_run=dry_run if dry_run is not None else UNSET,
            queued_contact_policy=WorkflowQueuedContactPolicy(queued_contact_policy)
            if queued_contact_policy is not None
            else UNSET,
        )
        endpoint = delete_workflow_node_recursively if recursive else delete_workflow_node
        response = await endpoint.asyncio_detailed(
            workflow_id=workflow_id,
            node_id=node_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=(WorkflowDeletedResponse, WorkflowQueuedContactDeletePreview),
            failure=WorkflowFailureResponse,
            action="delete workflow node",
        )

    # ------------------------------------------------------------------
    # Event patterns (1.21.x)
    # ------------------------------------------------------------------

    async def list_event_patterns(
        self,
        per_page: int | None = None,
        cursor: str | None = None,
    ) -> ListEventPatternsResponse:
        """Retrieve a paginated list of event patterns.

        Event patterns are the triggerable event types available for workflow
        automation (custom events or events from integrated webhook platforms).

        Args:
            per_page: Results per page (10-50). Default: 20
            cursor: Pagination cursor

        Returns:
            ListEventPatternsResponse with pagination and data

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_event_patterns.asyncio_detailed(
            client=self._client,
            per_page=str(per_page) if per_page is not None else UNSET,
            cursor=cursor if cursor else UNSET,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=ListEventPatternsResponse,
            failure=EventPatternFailureResponse,
            action="list event patterns",
        )

    async def get_event_pattern(self, event_pattern_id: str) -> EventPattern:
        """Retrieve a single event pattern by ID.

        Args:
            event_pattern_id: The event pattern ID

        Returns:
            EventPattern (includes ``event_properties``)

        Raises:
            LoopsError: If not found (404) or the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_event_pattern.asyncio_detailed(
            event_pattern_id=event_pattern_id,
            client=self._client,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=EventPattern,
            failure=EventPatternFailureResponse,
            action="get event pattern",
        )

    async def get_event_pattern_by_name(self, event_name: str) -> EventPattern:
        """Retrieve a single event pattern by its event name.

        Args:
            event_name: The event name (case-sensitive)

        Returns:
            EventPattern (includes ``event_properties``)

        Raises:
            LoopsError: If not found (404) or the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_event_pattern_by_name.asyncio_detailed(
            event_name=event_name,
            client=self._client,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=EventPattern,
            failure=EventPatternFailureResponse,
            action="get event pattern by name",
        )

    # ------------------------------------------------------------------
    # Audience segments (1.14.x)
    # ------------------------------------------------------------------

    async def list_audience_segments(
        self,
        per_page: int | None = None,
        cursor: str | None = None,
    ) -> ListAudienceSegmentsResponse:
        """Retrieve a paginated list of audience segments.

        Args:
            per_page: Results per page (10-50). Default: 20
            cursor: Pagination cursor

        Returns:
            ListAudienceSegmentsResponse with pagination and data

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_audience_segments.asyncio_detailed(
            client=self._client,
            per_page=str(per_page) if per_page is not None else UNSET,
            cursor=cursor if cursor else UNSET,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=ListAudienceSegmentsResponse,
            failure=AudienceSegmentFailureResponse,
            action="list audience segments",
        )

    async def get_audience_segment(self, audience_segment_id: str) -> AudienceSegmentResponse:
        """Retrieve a single audience segment by ID.

        Args:
            audience_segment_id: The audience segment ID

        Returns:
            AudienceSegmentResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_audience_segment.asyncio_detailed(
            audience_segment_id=audience_segment_id,
            client=self._client,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=AudienceSegmentResponse,
            failure=AudienceSegmentFailureResponse,
            action="get audience segment",
        )

    async def create_audience_segment(
        self,
        name: str,
        filter: dict[str, Any],
        description: str | None = None,
    ) -> AudienceSegmentResponse:
        """Create a new audience segment.

        Args:
            name: Segment name (must be unique within the team)
            filter: The segment's condition tree as a dictionary, e.g.
                ``{"match": "all", "conditions": [{"type": "property", "key": "plan",
                "operator": "equals", "value": "pro"}]}``. ``match`` is ``"all"`` or
                ``"any"``; each condition is a ``property``, ``optIn`` or ``activity``
                condition (see the Loops docs for the full grammar).
            description: Optional segment description

        Returns:
            AudienceSegmentResponse

        Raises:
            LoopsError: If the request fails (e.g. duplicate name, invalid filter)
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = CreateAudienceSegmentRequest(
            name=name,
            filter_=CreateAudienceSegmentRequestFilter.from_dict(filter),
            description=description if description is not None else UNSET,
        )
        response = await create_audience_segment.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=AudienceSegmentResponse,
            failure=AudienceSegmentFailureResponse,
            action="create audience segment",
        )

    # ------------------------------------------------------------------
    # Campaign groups (1.14.x)
    # ------------------------------------------------------------------

    async def list_campaign_groups(
        self,
        per_page: int | None = None,
        cursor: str | None = None,
    ) -> ListGroupsResponse:
        """Retrieve a paginated list of campaign groups.

        Args:
            per_page: Results per page (10-50). Default: 20
            cursor: Pagination cursor

        Returns:
            ListGroupsResponse with pagination and data

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_campaign_groups.asyncio_detailed(
            client=self._client,
            per_page=str(per_page) if per_page is not None else UNSET,
            cursor=cursor if cursor else UNSET,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=ListGroupsResponse,
            failure=GroupFailureResponse,
            action="list campaign groups",
        )

    async def get_campaign_group(self, campaign_group_id: str) -> GroupResponse:
        """Retrieve a single campaign group by ID.

        Args:
            campaign_group_id: The campaign group ID

        Returns:
            GroupResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_campaign_group.asyncio_detailed(
            campaign_group_id=campaign_group_id,
            client=self._client,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=GroupResponse,
            failure=GroupFailureResponse,
            action="get campaign group",
        )

    async def create_campaign_group(self, name: str, description: str | None = None) -> GroupResponse:
        """Create a new campaign group.

        Args:
            name: Group name
            description: Optional group description

        Returns:
            GroupResponse

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = CreateGroupRequest(name=name, description=description if description else UNSET)
        response = await create_campaign_group.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=GroupResponse,
            failure=GroupFailureResponse,
            action="create campaign group",
        )

    async def update_campaign_group(
        self,
        campaign_group_id: str,
        name: str | None = None,
        description: str | None = None,
    ) -> GroupResponse:
        """Update a campaign group.

        Args:
            campaign_group_id: The campaign group ID
            name: New group name
            description: New group description

        Returns:
            GroupResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = UpdateGroupRequest(
            name=name if name is not None else UNSET,
            description=description if description is not None else UNSET,
        )
        response = await update_campaign_group.asyncio_detailed(
            campaign_group_id=campaign_group_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=GroupResponse,
            failure=GroupFailureResponse,
            action="update campaign group",
        )

    # ------------------------------------------------------------------
    # Transactional groups (1.14.x)
    # ------------------------------------------------------------------

    async def list_transactional_groups(
        self,
        per_page: int | None = None,
        cursor: str | None = None,
    ) -> ListGroupsResponse:
        """Retrieve a paginated list of transactional groups.

        Args:
            per_page: Results per page (10-50). Default: 20
            cursor: Pagination cursor

        Returns:
            ListGroupsResponse with pagination and data

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await list_transactional_groups.asyncio_detailed(
            client=self._client,
            per_page=str(per_page) if per_page is not None else UNSET,
            cursor=cursor if cursor else UNSET,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=ListGroupsResponse,
            failure=GroupFailureResponse,
            action="list transactional groups",
        )

    async def get_transactional_group(self, transactional_group_id: str) -> GroupResponse:
        """Retrieve a single transactional group by ID.

        Args:
            transactional_group_id: The transactional group ID

        Returns:
            GroupResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_transactional_group.asyncio_detailed(
            transactional_group_id=transactional_group_id,
            client=self._client,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=GroupResponse,
            failure=GroupFailureResponse,
            action="get transactional group",
        )

    async def create_transactional_group(self, name: str, description: str | None = None) -> GroupResponse:
        """Create a new transactional group.

        Args:
            name: Group name
            description: Optional group description

        Returns:
            GroupResponse

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = CreateGroupRequest(name=name, description=description if description else UNSET)
        response = await create_transactional_group.asyncio_detailed(client=self._client, body=body)
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=GroupResponse,
            failure=GroupFailureResponse,
            action="create transactional group",
        )

    async def update_transactional_group(
        self,
        transactional_group_id: str,
        name: str | None = None,
        description: str | None = None,
    ) -> GroupResponse:
        """Update a transactional group.

        Args:
            transactional_group_id: The transactional group ID
            name: New group name
            description: New group description

        Returns:
            GroupResponse

        Raises:
            LoopsError: If not found (404) or request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        body = UpdateGroupRequest(
            name=name if name is not None else UNSET,
            description=description if description is not None else UNSET,
        )
        response = await update_transactional_group.asyncio_detailed(
            transactional_group_id=transactional_group_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=GroupResponse,
            failure=GroupFailureResponse,
            action="update transactional group",
        )

    # ------------------------------------------------------------------
    # Email message preview (1.14.x)
    # ------------------------------------------------------------------

    async def preview_email_message(
        self,
        email_message_id: str,
        emails: list[str],
        contact_properties: dict[str, Any] | None = None,
        event_properties: dict[str, Any] | None = None,
        data_variables: dict[str, Any] | None = None,
    ) -> EmailMessagePreviewResponse:
        """Send a preview of an email message to one or more addresses.

        Args:
            email_message_id: The email message ID to preview
            emails: List of recipient email addresses for the preview
            contact_properties: Optional contact property values for rendering
            event_properties: Optional event property values for rendering
            data_variables: Optional data variable values for rendering

        Returns:
            EmailMessagePreviewResponse

        Raises:
            LoopsError: If the request fails
            LoopsRateLimitError: If rate limit is exceeded
        """
        for email in emails:
            self._validate_email(email)

        body = EmailMessagePreviewRequest(
            emails=emails,
            contact_properties=EmailMessagePreviewRequestContactProperties.from_dict(contact_properties)
            if contact_properties
            else UNSET,
            event_properties=EmailMessagePreviewRequestEventProperties.from_dict(event_properties)
            if event_properties
            else UNSET,
            data_variables=EmailMessagePreviewRequestDataVariables.from_dict(data_variables)
            if data_variables
            else UNSET,
        )
        response = await preview_email_message.asyncio_detailed(
            email_message_id=email_message_id,
            client=self._client,
            body=body,
        )
        result = self._handle_response(response)
        return self._unwrap(
            result,
            response,
            success=EmailMessagePreviewResponse,
            failure=EmailMessageFailureResponse,
            action="preview email message",
        )


# Module-level singleton
_client: LoopsClient | None = None


def get_client() -> LoopsClient:
    """
    Get or create singleton Loops client instance using configured settings.

    Returns:
        LoopsClient instance

    Raises:
        LoopsConfigurationError: If API key is not configured

    Example:
        >>> import pyloops
        >>> pyloops.configure(api_key="your_api_key")
        >>> client = pyloops.get_client()
        >>> await client.upsert_contact(email="user@example.com")
    """
    global _client
    if _client is None:
        _client = LoopsClient()
    return _client


def reset_client() -> None:
    """Reset the singleton client so the next ``get_client()`` creates a fresh instance.

    Useful after calling ``configure()`` with new settings, or in test
    teardown to prevent state leaking between tests.
    """
    global _client
    _client = None
