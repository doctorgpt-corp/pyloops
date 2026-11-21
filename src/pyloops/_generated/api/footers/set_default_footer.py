from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.footer_failure_response import FooterFailureResponse
from ...models.set_default_footer_body import SetDefaultFooterBody
from ...models.set_default_footer_response import SetDefaultFooterResponse
from ...types import Response


def _get_kwargs(
    footer_id: str,
    *,
    body: SetDefaultFooterBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/footers/{footer_id}/set-default".format(
            footer_id=quote(str(footer_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | FooterFailureResponse | SetDefaultFooterResponse | None:
    if response.status_code == 200:
        response_200 = SetDefaultFooterResponse.from_dict(response.json())

        return response_200

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
        response_409 = FooterFailureResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | FooterFailureResponse | SetDefaultFooterResponse]:
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
    body: SetDefaultFooterBody,
) -> Response[Any | FooterFailureResponse | SetDefaultFooterResponse]:
    """Set the default footer

     Make a published footer the team's default footer. New campaign and workflow emails use the default
    footer. `existingEmails` picks which existing emails switch to it. With `none`, only new emails use
    it.

    Args:
        footer_id (str):
        body (SetDefaultFooterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FooterFailureResponse | SetDefaultFooterResponse]
    """

    kwargs = _get_kwargs(
        footer_id=footer_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    footer_id: str,
    *,
    client: AuthenticatedClient,
    body: SetDefaultFooterBody,
) -> Any | FooterFailureResponse | SetDefaultFooterResponse | None:
    """Set the default footer

     Make a published footer the team's default footer. New campaign and workflow emails use the default
    footer. `existingEmails` picks which existing emails switch to it. With `none`, only new emails use
    it.

    Args:
        footer_id (str):
        body (SetDefaultFooterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FooterFailureResponse | SetDefaultFooterResponse
    """

    return sync_detailed(
        footer_id=footer_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    footer_id: str,
    *,
    client: AuthenticatedClient,
    body: SetDefaultFooterBody,
) -> Response[Any | FooterFailureResponse | SetDefaultFooterResponse]:
    """Set the default footer

     Make a published footer the team's default footer. New campaign and workflow emails use the default
    footer. `existingEmails` picks which existing emails switch to it. With `none`, only new emails use
    it.

    Args:
        footer_id (str):
        body (SetDefaultFooterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FooterFailureResponse | SetDefaultFooterResponse]
    """

    kwargs = _get_kwargs(
        footer_id=footer_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    footer_id: str,
    *,
    client: AuthenticatedClient,
    body: SetDefaultFooterBody,
) -> Any | FooterFailureResponse | SetDefaultFooterResponse | None:
    """Set the default footer

     Make a published footer the team's default footer. New campaign and workflow emails use the default
    footer. `existingEmails` picks which existing emails switch to it. With `none`, only new emails use
    it.

    Args:
        footer_id (str):
        body (SetDefaultFooterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FooterFailureResponse | SetDefaultFooterResponse
    """

    return (
        await asyncio_detailed(
            footer_id=footer_id,
            client=client,
            body=body,
        )
    ).parsed
