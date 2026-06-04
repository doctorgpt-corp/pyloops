from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.transactional_failure_response import TransactionalFailureResponse
from ...models.transactional_response import TransactionalResponse
from ...types import Response


def _get_kwargs(
    transactional_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transactional-emails/{transactional_id}".format(
            transactional_id=quote(str(transactional_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TransactionalFailureResponse | TransactionalResponse | None:
    if response.status_code == 200:
        response_200 = TransactionalResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = TransactionalFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = TransactionalFailureResponse.from_dict(response.json())

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
) -> Response[Any | TransactionalFailureResponse | TransactionalResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transactional_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | TransactionalFailureResponse | TransactionalResponse]:
    """Get a transactional email

     Retrieve a single transactional by ID.

    Args:
        transactional_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionalFailureResponse | TransactionalResponse]
    """

    kwargs = _get_kwargs(
        transactional_id=transactional_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transactional_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | TransactionalFailureResponse | TransactionalResponse | None:
    """Get a transactional email

     Retrieve a single transactional by ID.

    Args:
        transactional_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionalFailureResponse | TransactionalResponse
    """

    return sync_detailed(
        transactional_id=transactional_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    transactional_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | TransactionalFailureResponse | TransactionalResponse]:
    """Get a transactional email

     Retrieve a single transactional by ID.

    Args:
        transactional_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionalFailureResponse | TransactionalResponse]
    """

    kwargs = _get_kwargs(
        transactional_id=transactional_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transactional_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | TransactionalFailureResponse | TransactionalResponse | None:
    """Get a transactional email

     Retrieve a single transactional by ID.

    Args:
        transactional_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionalFailureResponse | TransactionalResponse
    """

    return (
        await asyncio_detailed(
            transactional_id=transactional_id,
            client=client,
        )
    ).parsed
