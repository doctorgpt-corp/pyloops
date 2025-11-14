from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_property import ContactProperty
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    list_: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["list"] = list_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/contacts/properties",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[ContactProperty] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ContactProperty.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list[ContactProperty]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    list_: str | Unset = UNSET,
) -> Response[Any | list[ContactProperty]]:
    r"""Get a list of contact properties

     Retrieve a list of your account's contact properties.<br>Use the `list` parameter to query \"all\"
    or \"custom\" properties.

    Args:
        list_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ContactProperty]]
    """

    kwargs = _get_kwargs(
        list_=list_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    list_: str | Unset = UNSET,
) -> Any | list[ContactProperty] | None:
    r"""Get a list of contact properties

     Retrieve a list of your account's contact properties.<br>Use the `list` parameter to query \"all\"
    or \"custom\" properties.

    Args:
        list_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ContactProperty]
    """

    return sync_detailed(
        client=client,
        list_=list_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    list_: str | Unset = UNSET,
) -> Response[Any | list[ContactProperty]]:
    r"""Get a list of contact properties

     Retrieve a list of your account's contact properties.<br>Use the `list` parameter to query \"all\"
    or \"custom\" properties.

    Args:
        list_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ContactProperty]]
    """

    kwargs = _get_kwargs(
        list_=list_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    list_: str | Unset = UNSET,
) -> Any | list[ContactProperty] | None:
    r"""Get a list of contact properties

     Retrieve a list of your account's contact properties.<br>Use the `list` parameter to query \"all\"
    or \"custom\" properties.

    Args:
        list_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ContactProperty]
    """

    return (
        await asyncio_detailed(
            client=client,
            list_=list_,
        )
    ).parsed
