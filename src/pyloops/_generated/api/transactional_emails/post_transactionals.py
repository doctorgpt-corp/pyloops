from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_transactional_request import CreateTransactionalRequest
from ...models.transactional_failure_response import TransactionalFailureResponse
from ...models.transactional_resource import TransactionalResource
from ...types import Response


def _get_kwargs(
    *,
    body: CreateTransactionalRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/transactionals",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TransactionalFailureResponse | TransactionalResource | None:
    if response.status_code == 201:
        response_201 = TransactionalResource.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = TransactionalFailureResponse.from_dict(response.json())

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
) -> Response[Any | TransactionalFailureResponse | TransactionalResource]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionalRequest,
) -> Response[Any | TransactionalFailureResponse | TransactionalResource]:
    """Create a transactional

     Create a new transactional. An empty draft email message is created automatically and its
    `draftEmailMessageId` is returned. Use the `/email-messages/{emailMessageId}` endpoint to set
    subject, sender, preview text, and LMX content, then call
    `/transactionals/{transactionalId}/publish` to publish.

    Args:
        body (CreateTransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionalFailureResponse | TransactionalResource]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionalRequest,
) -> Any | TransactionalFailureResponse | TransactionalResource | None:
    """Create a transactional

     Create a new transactional. An empty draft email message is created automatically and its
    `draftEmailMessageId` is returned. Use the `/email-messages/{emailMessageId}` endpoint to set
    subject, sender, preview text, and LMX content, then call
    `/transactionals/{transactionalId}/publish` to publish.

    Args:
        body (CreateTransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionalFailureResponse | TransactionalResource
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionalRequest,
) -> Response[Any | TransactionalFailureResponse | TransactionalResource]:
    """Create a transactional

     Create a new transactional. An empty draft email message is created automatically and its
    `draftEmailMessageId` is returned. Use the `/email-messages/{emailMessageId}` endpoint to set
    subject, sender, preview text, and LMX content, then call
    `/transactionals/{transactionalId}/publish` to publish.

    Args:
        body (CreateTransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TransactionalFailureResponse | TransactionalResource]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateTransactionalRequest,
) -> Any | TransactionalFailureResponse | TransactionalResource | None:
    """Create a transactional

     Create a new transactional. An empty draft email message is created automatically and its
    `draftEmailMessageId` is returned. Use the `/email-messages/{emailMessageId}` endpoint to set
    subject, sender, preview text, and LMX content, then call
    `/transactionals/{transactionalId}/publish` to publish.

    Args:
        body (CreateTransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TransactionalFailureResponse | TransactionalResource
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
