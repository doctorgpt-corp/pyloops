from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dedicated-sending-ips",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[str] | None:
    if response.status_code == 200:
        response_200 = cast(list[str], response.json())

        return response_200

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[str]]:
    """List dedicated sending IP addresses

     Retrieve a list of Loops' dedicated sending IP addresses.

    This endpoint is provided for the rare instances where you may need to whitelist our sending IPs.
    Please note that this list is subject to change and will not include shared IPs used for sending
    mail.

    Unless you are sure you need this and are comfortable watching for changes, we strongly recommend
    you _do not_ whitelist these IPs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[str]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | list[str] | None:
    """List dedicated sending IP addresses

     Retrieve a list of Loops' dedicated sending IP addresses.

    This endpoint is provided for the rare instances where you may need to whitelist our sending IPs.
    Please note that this list is subject to change and will not include shared IPs used for sending
    mail.

    Unless you are sure you need this and are comfortable watching for changes, we strongly recommend
    you _do not_ whitelist these IPs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[str]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[str]]:
    """List dedicated sending IP addresses

     Retrieve a list of Loops' dedicated sending IP addresses.

    This endpoint is provided for the rare instances where you may need to whitelist our sending IPs.
    Please note that this list is subject to change and will not include shared IPs used for sending
    mail.

    Unless you are sure you need this and are comfortable watching for changes, we strongly recommend
    you _do not_ whitelist these IPs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[str]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | list[str] | None:
    """List dedicated sending IP addresses

     Retrieve a list of Loops' dedicated sending IP addresses.

    This endpoint is provided for the rare instances where you may need to whitelist our sending IPs.
    Please note that this list is subject to change and will not include shared IPs used for sending
    mail.

    Unless you are sure you need this and are comfortable watching for changes, we strongly recommend
    you _do not_ whitelist these IPs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[str]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
