from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_message_failure_response import EmailMessageFailureResponse
from ...models.email_message_response import EmailMessageResponse
from ...types import Response


def _get_kwargs(
    email_message_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/email-messages/{email_message_id}".format(
            email_message_id=quote(str(email_message_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EmailMessageFailureResponse | EmailMessageResponse | None:
    if response.status_code == 200:
        response_200 = EmailMessageResponse.from_dict(response.json())

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
) -> Response[Any | EmailMessageFailureResponse | EmailMessageResponse]:
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
) -> Response[Any | EmailMessageFailureResponse | EmailMessageResponse]:
    """Get an email message

     Retrieve an email message, including its compiled LMX content.

    Args:
        email_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmailMessageFailureResponse | EmailMessageResponse]
    """

    kwargs = _get_kwargs(
        email_message_id=email_message_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email_message_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | EmailMessageFailureResponse | EmailMessageResponse | None:
    """Get an email message

     Retrieve an email message, including its compiled LMX content.

    Args:
        email_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmailMessageFailureResponse | EmailMessageResponse
    """

    return sync_detailed(
        email_message_id=email_message_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    email_message_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | EmailMessageFailureResponse | EmailMessageResponse]:
    """Get an email message

     Retrieve an email message, including its compiled LMX content.

    Args:
        email_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmailMessageFailureResponse | EmailMessageResponse]
    """

    kwargs = _get_kwargs(
        email_message_id=email_message_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email_message_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | EmailMessageFailureResponse | EmailMessageResponse | None:
    """Get an email message

     Retrieve an email message, including its compiled LMX content.

    Args:
        email_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmailMessageFailureResponse | EmailMessageResponse
    """

    return (
        await asyncio_detailed(
            email_message_id=email_message_id,
            client=client,
        )
    ).parsed
