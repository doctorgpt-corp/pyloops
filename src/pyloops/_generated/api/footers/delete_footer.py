from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.footer_delete_failure_response import FooterDeleteFailureResponse
from ...models.footer_failure_response import FooterFailureResponse
from ...types import Response


def _get_kwargs(
    footer_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/footers/{footer_id}".format(
            footer_id=quote(str(footer_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | FooterDeleteFailureResponse | FooterFailureResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = FooterFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = FooterFailureResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 409:
        response_409 = FooterDeleteFailureResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | FooterDeleteFailureResponse | FooterFailureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    footer_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | FooterDeleteFailureResponse | FooterFailureResponse]:
    """Delete a footer

     Delete a footer and its variants. You cannot delete the team's default footer or a footer that
    emails use.

    Args:
        footer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FooterDeleteFailureResponse | FooterFailureResponse]
    """

    kwargs = _get_kwargs(
        footer_id=footer_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    footer_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | FooterDeleteFailureResponse | FooterFailureResponse | None:
    """Delete a footer

     Delete a footer and its variants. You cannot delete the team's default footer or a footer that
    emails use.

    Args:
        footer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FooterDeleteFailureResponse | FooterFailureResponse
    """

    return sync_detailed(
        footer_id=footer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    footer_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | FooterDeleteFailureResponse | FooterFailureResponse]:
    """Delete a footer

     Delete a footer and its variants. You cannot delete the team's default footer or a footer that
    emails use.

    Args:
        footer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FooterDeleteFailureResponse | FooterFailureResponse]
    """

    kwargs = _get_kwargs(
        footer_id=footer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    footer_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | FooterDeleteFailureResponse | FooterFailureResponse | None:
    """Delete a footer

     Delete a footer and its variants. You cannot delete the team's default footer or a footer that
    emails use.

    Args:
        footer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FooterDeleteFailureResponse | FooterFailureResponse
    """

    return (
        await asyncio_detailed(
            footer_id=footer_id,
            client=client,
        )
    ).parsed
