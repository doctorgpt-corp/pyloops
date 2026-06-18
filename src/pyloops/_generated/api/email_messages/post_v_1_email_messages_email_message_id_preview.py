from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_message_failure_response import EmailMessageFailureResponse
from ...models.email_message_preview_request import EmailMessagePreviewRequest
from ...models.email_message_preview_response import EmailMessagePreviewResponse
from ...types import Response


def _get_kwargs(
    email_message_id: str,
    *,
    body: EmailMessagePreviewRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/email-messages/{email_message_id}/preview".format(
            email_message_id=quote(str(email_message_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EmailMessageFailureResponse | EmailMessagePreviewResponse | None:
    if response.status_code == 200:
        response_200 = EmailMessagePreviewResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EmailMessageFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = EmailMessageFailureResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EmailMessageFailureResponse | EmailMessagePreviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    email_message_id: str,
    *,
    client: AuthenticatedClient,
    body: EmailMessagePreviewRequest,
) -> Response[Any | EmailMessageFailureResponse | EmailMessagePreviewResponse]:
    """Send a preview of an email message

     Send a test preview of an email message to one or more addresses. The accepted variable fields
    depend on the parent's type - campaign previews accept `contactProperties`, workflow previews accept
    `contactProperties` and `eventProperties`, and transactional previews accept `dataVariables`.
    Supplying a field the parent cannot reference is rejected with 400.

    Args:
        email_message_id (str):
        body (EmailMessagePreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmailMessageFailureResponse | EmailMessagePreviewResponse]
    """

    kwargs = _get_kwargs(
        email_message_id=email_message_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email_message_id: str,
    *,
    client: AuthenticatedClient,
    body: EmailMessagePreviewRequest,
) -> Any | EmailMessageFailureResponse | EmailMessagePreviewResponse | None:
    """Send a preview of an email message

     Send a test preview of an email message to one or more addresses. The accepted variable fields
    depend on the parent's type - campaign previews accept `contactProperties`, workflow previews accept
    `contactProperties` and `eventProperties`, and transactional previews accept `dataVariables`.
    Supplying a field the parent cannot reference is rejected with 400.

    Args:
        email_message_id (str):
        body (EmailMessagePreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmailMessageFailureResponse | EmailMessagePreviewResponse
    """

    return sync_detailed(
        email_message_id=email_message_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    email_message_id: str,
    *,
    client: AuthenticatedClient,
    body: EmailMessagePreviewRequest,
) -> Response[Any | EmailMessageFailureResponse | EmailMessagePreviewResponse]:
    """Send a preview of an email message

     Send a test preview of an email message to one or more addresses. The accepted variable fields
    depend on the parent's type - campaign previews accept `contactProperties`, workflow previews accept
    `contactProperties` and `eventProperties`, and transactional previews accept `dataVariables`.
    Supplying a field the parent cannot reference is rejected with 400.

    Args:
        email_message_id (str):
        body (EmailMessagePreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmailMessageFailureResponse | EmailMessagePreviewResponse]
    """

    kwargs = _get_kwargs(
        email_message_id=email_message_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email_message_id: str,
    *,
    client: AuthenticatedClient,
    body: EmailMessagePreviewRequest,
) -> Any | EmailMessageFailureResponse | EmailMessagePreviewResponse | None:
    """Send a preview of an email message

     Send a test preview of an email message to one or more addresses. The accepted variable fields
    depend on the parent's type - campaign previews accept `contactProperties`, workflow previews accept
    `contactProperties` and `eventProperties`, and transactional previews accept `dataVariables`.
    Supplying a field the parent cannot reference is rejected with 400.

    Args:
        email_message_id (str):
        body (EmailMessagePreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmailMessageFailureResponse | EmailMessagePreviewResponse
    """

    return (
        await asyncio_detailed(
            email_message_id=email_message_id,
            client=client,
            body=body,
        )
    ).parsed
