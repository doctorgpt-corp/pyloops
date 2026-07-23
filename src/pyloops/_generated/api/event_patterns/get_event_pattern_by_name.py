from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_pattern import EventPattern
from ...models.event_pattern_failure_response import EventPatternFailureResponse
from ...types import Response


def _get_kwargs(
    event_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/event-patterns/by-name/{event_name}".format(
            event_name=quote(str(event_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EventPattern | EventPatternFailureResponse | None:
    if response.status_code == 200:
        response_200 = EventPattern.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EventPatternFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = EventPatternFailureResponse.from_dict(response.json())

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
) -> Response[Any | EventPattern | EventPatternFailureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | EventPattern | EventPatternFailureResponse]:
    """Get an event pattern by name

     Retrieve event pattern details by event name for a workflow event trigger. Event names are case-
    sensitive, so `PaymentReceived` and `paymentReceived` are different events.

    Args:
        event_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EventPattern | EventPatternFailureResponse]
    """

    kwargs = _get_kwargs(
        event_name=event_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_name: str,
    *,
    client: AuthenticatedClient,
) -> Any | EventPattern | EventPatternFailureResponse | None:
    """Get an event pattern by name

     Retrieve event pattern details by event name for a workflow event trigger. Event names are case-
    sensitive, so `PaymentReceived` and `paymentReceived` are different events.

    Args:
        event_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EventPattern | EventPatternFailureResponse
    """

    return sync_detailed(
        event_name=event_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | EventPattern | EventPatternFailureResponse]:
    """Get an event pattern by name

     Retrieve event pattern details by event name for a workflow event trigger. Event names are case-
    sensitive, so `PaymentReceived` and `paymentReceived` are different events.

    Args:
        event_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EventPattern | EventPatternFailureResponse]
    """

    kwargs = _get_kwargs(
        event_name=event_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_name: str,
    *,
    client: AuthenticatedClient,
) -> Any | EventPattern | EventPatternFailureResponse | None:
    """Get an event pattern by name

     Retrieve event pattern details by event name for a workflow event trigger. Event names are case-
    sensitive, so `PaymentReceived` and `paymentReceived` are different events.

    Args:
        event_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EventPattern | EventPatternFailureResponse
    """

    return (
        await asyncio_detailed(
            event_name=event_name,
            client=client,
        )
    ).parsed
