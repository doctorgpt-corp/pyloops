from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_pattern_failure_response import EventPatternFailureResponse
from ...models.list_event_patterns_response import ListEventPatternsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["perPage"] = per_page

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/event-patterns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EventPatternFailureResponse | ListEventPatternsResponse | None:
    if response.status_code == 200:
        response_200 = ListEventPatternsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EventPatternFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EventPatternFailureResponse | ListEventPatternsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    per_page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[Any | EventPatternFailureResponse | ListEventPatternsResponse]:
    """List event patterns

     Retrieve a paginated list of event patterns available to workflow event trigger nodes.

    Args:
        per_page (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EventPatternFailureResponse | ListEventPatternsResponse]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    per_page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Any | EventPatternFailureResponse | ListEventPatternsResponse | None:
    """List event patterns

     Retrieve a paginated list of event patterns available to workflow event trigger nodes.

    Args:
        per_page (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EventPatternFailureResponse | ListEventPatternsResponse
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    per_page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[Any | EventPatternFailureResponse | ListEventPatternsResponse]:
    """List event patterns

     Retrieve a paginated list of event patterns available to workflow event trigger nodes.

    Args:
        per_page (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EventPatternFailureResponse | ListEventPatternsResponse]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    per_page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Any | EventPatternFailureResponse | ListEventPatternsResponse | None:
    """List event patterns

     Retrieve a paginated list of event patterns available to workflow event trigger nodes.

    Args:
        per_page (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EventPatternFailureResponse | ListEventPatternsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            cursor=cursor,
        )
    ).parsed
