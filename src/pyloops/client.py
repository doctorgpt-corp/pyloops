import json
import uuid
from http import HTTPStatus
from typing import Any

from pyloops._generated.api.api_key import get_api_key
from pyloops._generated.api.campaigns import (
    get_campaigns,
    get_campaigns_campaign_id,
    post_campaigns,
    post_campaigns_campaign_id,
)
from pyloops._generated.api.components import get_components, get_components_component_id
from pyloops._generated.api.contact_properties import (
    get_contacts_properties,
    post_contacts_properties,
)
from pyloops._generated.api.contacts import (
    delete_contacts_suppression,
    get_contacts_find,
    get_contacts_suppression,
    post_contacts_create,
    post_contacts_delete,
    put_contacts_update,
)
from pyloops._generated.api.dedicated_sending_i_ps import get_dedicated_sending_ips
from pyloops._generated.api.email_messages import (
    get_email_messages_email_message_id,
    post_email_messages_email_message_id,
)
from pyloops._generated.api.events import post_events_send
from pyloops._generated.api.mailing_lists import get_lists
from pyloops._generated.api.themes import get_themes, get_themes_theme_id
from pyloops._generated.api.transactional_emails import get_transactional, post_transactional
from pyloops._generated.client import AuthenticatedClient
from pyloops._generated.models import (
    CampaignFailureResponse,
    CampaignResponse,
    ComponentFailureResponse,
    ComponentResponse,
    Contact,
    ContactDeleteRequest,
    ContactFailureResponse,
    ContactProperty,
    ContactPropertyCreateRequest,
    ContactRequest,
    ContactRequestMailingLists,
    ContactSuccessResponse,
    ContactSuppressionRemoveResponse,
    ContactSuppressionStatusResponse,
    ContactUpdateRequest,
    ContactUpdateRequestMailingLists,
    CreateCampaignRequest,
    CreateCampaignResponse,
    EmailMessageFailureResponse,
    EmailMessageResponse,
    EventFailureResponse,
    EventRequest,
    EventRequestEventProperties,
    EventRequestMailingLists,
    EventSuccessResponse,
    GetApiKeyResponse401,
    GetDedicatedSendingIpsResponse500,
    IdempotencyKeyFailureResponse,
    ListCampaignsResponse,
    ListComponentsResponse,
    ListThemesResponse,
    MailingList,
    ThemeFailureResponse,
    ThemeResponse,
    TransactionalFailure2Response,
    TransactionalFailure3Response,
    TransactionalFailure4Response,
    TransactionalFailure5Response,
    TransactionalFailureResponse,
    TransactionalRequest,
    TransactionalRequestAttachmentsItem,
    TransactionalRequestDataVariables,
    TransactionalSuccessResponse,
    UpdateCampaignRequest,
    UpdateEmailMessageRequest,
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
        base_url: str = "https://app.loops.so/api/v1",
        safe_mode: bool | None = None,
        safe_mode_allowed_domains: tuple[str, ...] | None = None,
    ):
        """
        Initialize the Loops client.

        Args:
            api_key: API key for Loops.so. If not provided, uses configured default or LOOPS_API_KEY env var.
            base_url: Base URL for Loops API (default: https://app.loops.so/api/v1)
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
            base_url=base_url,
            token=api_key,
            prefix="Bearer",
        )

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
        response = await get_api_key.asyncio_detailed(client=self._client)
        result = self._handle_response(response)

        if isinstance(result, GetApiKeyResponse401):
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
            mailing_lists=ContactRequestMailingLists.from_dict(mailing_lists) if mailing_lists else UNSET,
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

        response = await post_contacts_create.asyncio_detailed(client=self._client, body=request)
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
            mailing_lists=ContactUpdateRequestMailingLists.from_dict(mailing_lists) if mailing_lists else UNSET,
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

        response = await put_contacts_update.asyncio_detailed(client=self._client, body=request)
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

        response = await get_contacts_find.asyncio_detailed(
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

        response = await post_contacts_delete.asyncio_detailed(client=self._client, body=body)
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
        body = ContactPropertyCreateRequest(name=name, type_=property_type)

        response = await post_contacts_properties.asyncio_detailed(client=self._client, body=body)
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
        response = await get_contacts_properties.asyncio_detailed(client=self._client)
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
        response = await get_lists.asyncio_detailed(client=self._client)
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

        # Build the request
        request = EventRequest(
            event_name=event_name,
            email=email if email else UNSET,
            user_id=user_id if user_id else UNSET,
            event_properties=EventRequestEventProperties.from_dict(event_properties) if event_properties else UNSET,
            mailing_lists=EventRequestMailingLists.from_dict(mailing_lists) if mailing_lists else UNSET,
        )

        # Set additional contact properties
        if additional_properties:
            request.additional_properties = additional_properties

        response = await post_events_send.asyncio_detailed(
            client=self._client,
            body=request,
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

        response = await post_transactional.asyncio_detailed(
            client=self._client,
            body=request,
            idempotency_key=idempotency_key,
        )
        result = self._handle_response(response)

        # Handle error responses (all return success=false + message)
        failure_types = (
            TransactionalFailureResponse,
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
        response = await get_transactional.asyncio_detailed(
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
            LoopsError: If the request fails (500)
            LoopsRateLimitError: If rate limit is exceeded
        """
        response = await get_dedicated_sending_ips.asyncio_detailed(client=self._client)
        result = self._handle_response(response)

        if isinstance(result, GetDedicatedSendingIpsResponse500):
            raise LoopsError(
                "Server error retrieving sending IPs",
                status_code=500,
                response_data=result,
            )

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
        response = await get_campaigns.asyncio_detailed(
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
        response = await get_campaigns_campaign_id.asyncio_detailed(
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
        response = await post_campaigns.asyncio_detailed(client=self._client, body=body)
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
        response = await post_campaigns_campaign_id.asyncio_detailed(
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
        response = await get_components.asyncio_detailed(
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
        response = await get_components_component_id.asyncio_detailed(
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
        response = await get_themes.asyncio_detailed(
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
        response = await get_themes_theme_id.asyncio_detailed(
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
        response = await get_email_messages_email_message_id.asyncio_detailed(
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
        response = await post_email_messages_email_message_id.asyncio_detailed(
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

        response = await get_contacts_suppression.asyncio_detailed(
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

        response = await delete_contacts_suppression.asyncio_detailed(
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
