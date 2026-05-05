from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.component_failure_response import ComponentFailureResponse
from ...models.component_response import ComponentResponse
from ...types import Response


def _get_kwargs(
    component_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/components/{component_id}".format(
            component_id=quote(str(component_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComponentFailureResponse | ComponentResponse | None:
    if response.status_code == 200:
        response_200 = ComponentResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ComponentFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = ComponentFailureResponse.from_dict(response.json())

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
) -> Response[Any | ComponentFailureResponse | ComponentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    component_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ComponentFailureResponse | ComponentResponse]:
    """Get a component

     Retrieve a single component by ID.

    Args:
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComponentFailureResponse | ComponentResponse]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    component_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ComponentFailureResponse | ComponentResponse | None:
    """Get a component

     Retrieve a single component by ID.

    Args:
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComponentFailureResponse | ComponentResponse
    """

    return sync_detailed(
        component_id=component_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    component_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ComponentFailureResponse | ComponentResponse]:
    """Get a component

     Retrieve a single component by ID.

    Args:
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComponentFailureResponse | ComponentResponse]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    component_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ComponentFailureResponse | ComponentResponse | None:
    """Get a component

     Retrieve a single component by ID.

    Args:
        component_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComponentFailureResponse | ComponentResponse
    """

    return (
        await asyncio_detailed(
            component_id=component_id,
            client=client,
        )
    ).parsed
