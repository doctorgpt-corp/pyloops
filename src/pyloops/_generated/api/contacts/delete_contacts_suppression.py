from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_failure_response import ContactFailureResponse
from ...models.contact_suppression_remove_response import ContactSuppressionRemoveResponse
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
        "method": "delete",
        "url": "/contacts/suppression",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ContactFailureResponse | ContactSuppressionRemoveResponse | None:
    if response.status_code == 200:
        response_200 = ContactSuppressionRemoveResponse.from_dict(response.json())

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
) -> Response[Any | ContactFailureResponse | ContactSuppressionRemoveResponse]:
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
) -> Response[Any | ContactFailureResponse | ContactSuppressionRemoveResponse]:
    """Remove a contact from suppression list

     Remove a suppressed contact from the suppression list by `email` or `userId`. Include only one query
    parameter.

    Args:
        email (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContactFailureResponse | ContactSuppressionRemoveResponse]
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
) -> Any | ContactFailureResponse | ContactSuppressionRemoveResponse | None:
    """Remove a contact from suppression list

     Remove a suppressed contact from the suppression list by `email` or `userId`. Include only one query
    parameter.

    Args:
        email (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContactFailureResponse | ContactSuppressionRemoveResponse
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
) -> Response[Any | ContactFailureResponse | ContactSuppressionRemoveResponse]:
    """Remove a contact from suppression list

     Remove a suppressed contact from the suppression list by `email` or `userId`. Include only one query
    parameter.

    Args:
        email (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ContactFailureResponse | ContactSuppressionRemoveResponse]
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
) -> Any | ContactFailureResponse | ContactSuppressionRemoveResponse | None:
    """Remove a contact from suppression list

     Remove a suppressed contact from the suppression list by `email` or `userId`. Include only one query
    parameter.

    Args:
        email (str | Unset):
        user_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ContactFailureResponse | ContactSuppressionRemoveResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            email=email,
            user_id=user_id,
        )
    ).parsed
