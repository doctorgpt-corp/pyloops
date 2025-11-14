from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_delete_request import ContactDeleteRequest
from ...models.contact_delete_response import ContactDeleteResponse
from ...models.contact_failure_response import ContactFailureResponse
from ...types import Response


def _get_kwargs(
    *,
    body: ContactDeleteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/contacts/delete",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ContactDeleteResponse | ContactFailureResponse | None:
    if response.status_code == 200:
        response_200 = ContactDeleteResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ContactFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ContactFailureResponse.from_dict(response.json())

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
) -> Response[Any | ContactDeleteResponse | ContactFailureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ContactDeleteRequest,
) -> Response[Any | ContactDeleteResponse | ContactFailureResponse]:
    """Delete a contact

     Delete a contact by `email` or `userId`.

    Args:
        body (ContactDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContactDeleteResponse | ContactFailureResponse]
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
    body: ContactDeleteRequest,
) -> Any | ContactDeleteResponse | ContactFailureResponse | None:
    """Delete a contact

     Delete a contact by `email` or `userId`.

    Args:
        body (ContactDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContactDeleteResponse | ContactFailureResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ContactDeleteRequest,
) -> Response[Any | ContactDeleteResponse | ContactFailureResponse]:
    """Delete a contact

     Delete a contact by `email` or `userId`.

    Args:
        body (ContactDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContactDeleteResponse | ContactFailureResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ContactDeleteRequest,
) -> Any | ContactDeleteResponse | ContactFailureResponse | None:
    """Delete a contact

     Delete a contact by `email` or `userId`.

    Args:
        body (ContactDeleteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContactDeleteResponse | ContactFailureResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
