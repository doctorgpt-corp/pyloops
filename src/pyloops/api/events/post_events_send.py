from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_failure_response import EventFailureResponse
from ...models.event_request import EventRequest
from ...models.event_success_response import EventSuccessResponse
from ...models.idempotency_key_failure_response import IdempotencyKeyFailureResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: EventRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/events/send",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EventFailureResponse | EventSuccessResponse | IdempotencyKeyFailureResponse | None:
    if response.status_code == 200:
        response_200 = EventSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EventFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 409:
        response_409 = IdempotencyKeyFailureResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EventFailureResponse | EventSuccessResponse | IdempotencyKeyFailureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EventRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any | EventFailureResponse | EventSuccessResponse | IdempotencyKeyFailureResponse]:
    """Send an event

     Send events to trigger emails in Loops.

    Args:
        idempotency_key (str | Unset):
        body (EventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EventFailureResponse | EventSuccessResponse | IdempotencyKeyFailureResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: EventRequest,
    idempotency_key: str | Unset = UNSET,
) -> Any | EventFailureResponse | EventSuccessResponse | IdempotencyKeyFailureResponse | None:
    """Send an event

     Send events to trigger emails in Loops.

    Args:
        idempotency_key (str | Unset):
        body (EventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EventFailureResponse | EventSuccessResponse | IdempotencyKeyFailureResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EventRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any | EventFailureResponse | EventSuccessResponse | IdempotencyKeyFailureResponse]:
    """Send an event

     Send events to trigger emails in Loops.

    Args:
        idempotency_key (str | Unset):
        body (EventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EventFailureResponse | EventSuccessResponse | IdempotencyKeyFailureResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EventRequest,
    idempotency_key: str | Unset = UNSET,
) -> Any | EventFailureResponse | EventSuccessResponse | IdempotencyKeyFailureResponse | None:
    """Send an event

     Send events to trigger emails in Loops.

    Args:
        idempotency_key (str | Unset):
        body (EventRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EventFailureResponse | EventSuccessResponse | IdempotencyKeyFailureResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
