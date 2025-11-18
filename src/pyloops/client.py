import json
import uuid
from http import HTTPStatus
from typing import Any

from pyloops._generated.api.api_key import get_api_key
from pyloops._generated.api.contact_properties import (
    get_contacts_properties,
    post_contacts_properties,
)
from pyloops._generated.api.contacts import (
    get_contacts_find,
    post_contacts_create,
    post_contacts_delete,
    put_contacts_update,
)
from pyloops._generated.api.dedicated_sending_i_ps import get_dedicated_sending_ips
from pyloops._generated.api.events import post_events_send
from pyloops._generated.api.mailing_lists import get_lists
from pyloops._generated.api.transactional_emails import get_transactional, post_transactional
from pyloops._generated.client import AuthenticatedClient
from pyloops._generated.models import (
    Contact,
    ContactDeleteRequest,
    ContactFailureResponse,
    ContactProperty,
    ContactPropertyCreateRequest,
    ContactRequest,
    ContactRequestMailingLists,
    ContactSuccessResponse,
    ContactUpdateRequest,
    ContactUpdateRequestMailingLists,
    EventFailureResponse,
    EventRequest,
    EventRequestEventProperties,
    EventRequestMailingLists,
    EventSuccessResponse,
    GetApiKeyResponse401,
    GetDedicatedSendingIpsResponse500,
    IdempotencyKeyFailureResponse,
    MailingList,
    TransactionalFailure2Response,
    TransactionalFailure3Response,
    TransactionalFailure4Response,
    TransactionalFailure5Response,
    TransactionalFailureResponse,
    TransactionalRequest,
    TransactionalRequestAttachmentsItem,
    TransactionalRequestDataVariables,
    TransactionalSuccessResponse,
)
from pyloops._generated.types import UNSET, Response
from pyloops.config import get_config
from pyloops.exceptions import (
    LoopsConfigurationError,
    LoopsContactExistsError,
    LoopsError,
    LoopsRateLimitError,
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
    ):
        """
        Initialize the Loops client.

        Args:
            api_key: API key for Loops.so. If not provided, uses configured default or LOOPS_API_KEY env var.
            base_url: Base URL for Loops API (default: https://app.loops.so/api/v1)

        Raises:
            LoopsConfigurationError: If no API key is available
        """
        # Get API key from parameter, config, or env var
        if api_key is None:
            config = get_config()
            api_key = config["api_key"]
            if config["base_url"]:
                base_url = config["base_url"]

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
