from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact import Contact
from ...models.contact_failure_response import ContactFailureResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    email: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["email"] = email

    params["userId"] = user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts/find",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ContactFailureResponse | list[Contact] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Contact.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ContactFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ContactFailureResponse | list[Contact]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[Any | ContactFailureResponse | list[Contact]]:
    """Find a contact

     Search for a contact by `email` or `userId`. Only one parameter is allowed.

    Args:
        email (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContactFailureResponse | list[Contact]]
    """

    kwargs = _get_kwargs(
        email=email,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Any | ContactFailureResponse | list[Contact] | None:
    """Find a contact

     Search for a contact by `email` or `userId`. Only one parameter is allowed.

    Args:
        email (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContactFailureResponse | list[Contact]
    """

    return sync_detailed(
        client=client,
        email=email,
        user_id=user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Response[Any | ContactFailureResponse | list[Contact]]:
    """Find a contact

     Search for a contact by `email` or `userId`. Only one parameter is allowed.

    Args:
        email (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContactFailureResponse | list[Contact]]
    """

    kwargs = _get_kwargs(
        email=email,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    email: str | Unset = UNSET,
    user_id: str | Unset = UNSET,
) -> Any | ContactFailureResponse | list[Contact] | None:
    """Find a contact

     Search for a contact by `email` or `userId`. Only one parameter is allowed.

    Args:
        email (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContactFailureResponse | list[Contact]
    """

    return (
        await asyncio_detailed(
            client=client,
            email=email,
            user_id=user_id,
        )
    ).parsed
