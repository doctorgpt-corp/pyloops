from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_message_failure_response import EmailMessageFailureResponse
from ...models.email_message_guardian_response import EmailMessageGuardianResponse
from ...types import Response


def _get_kwargs(
    email_message_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/email-messages/{email_message_id}/guardian".format(
            email_message_id=quote(str(email_message_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EmailMessageFailureResponse | EmailMessageGuardianResponse | None:
    if response.status_code == 200:
        response_200 = EmailMessageGuardianResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = EmailMessageFailureResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EmailMessageFailureResponse | EmailMessageGuardianResponse]:
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
) -> Response[Any | EmailMessageFailureResponse | EmailMessageGuardianResponse]:
    """Run Guardian checks on an email message

     Validate an email message's content against Guardian rules and return any errors and warnings.
    Errors must be resolved before the email can be published, warnings are advisory.

    Args:
        email_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmailMessageFailureResponse | EmailMessageGuardianResponse]
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
) -> Any | EmailMessageFailureResponse | EmailMessageGuardianResponse | None:
    """Run Guardian checks on an email message

     Validate an email message's content against Guardian rules and return any errors and warnings.
    Errors must be resolved before the email can be published, warnings are advisory.

    Args:
        email_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmailMessageFailureResponse | EmailMessageGuardianResponse
    """

    return sync_detailed(
        email_message_id=email_message_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    email_message_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | EmailMessageFailureResponse | EmailMessageGuardianResponse]:
    """Run Guardian checks on an email message

     Validate an email message's content against Guardian rules and return any errors and warnings.
    Errors must be resolved before the email can be published, warnings are advisory.

    Args:
        email_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmailMessageFailureResponse | EmailMessageGuardianResponse]
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
) -> Any | EmailMessageFailureResponse | EmailMessageGuardianResponse | None:
    """Run Guardian checks on an email message

     Validate an email message's content against Guardian rules and return any errors and warnings.
    Errors must be resolved before the email can be published, warnings are advisory.

    Args:
        email_message_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmailMessageFailureResponse | EmailMessageGuardianResponse
    """

    return (
        await asyncio_detailed(
            email_message_id=email_message_id,
            client=client,
        )
    ).parsed
