from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.theme_failure_response import ThemeFailureResponse
from ...models.update_theme_body import UpdateThemeBody
from ...models.update_theme_response import UpdateThemeResponse
from ...types import Response


def _get_kwargs(
    theme_id: str,
    *,
    body: UpdateThemeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/themes/{theme_id}".format(
            theme_id=quote(str(theme_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ThemeFailureResponse | UpdateThemeResponse | None:
    if response.status_code == 200:
        response_200 = UpdateThemeResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ThemeFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = ThemeFailureResponse.from_dict(response.json())

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
) -> Response[Any | ThemeFailureResponse | UpdateThemeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    theme_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateThemeBody,
) -> Response[Any | ThemeFailureResponse | UpdateThemeResponse]:
    """Update a theme

     Update a theme's name and/or styles. When `styles` change, the update cascades to every email using
    this theme, and `affectedEmailCount` in the response reports how many emails were affected. Manual
    style edits made on individual emails are preserved: the cascade only changes properties an email
    has not overridden. A per-email override is removed only when it becomes identical to the theme's
    new value, after which that email follows the theme for that property.

    Args:
        theme_id (str):
        body (UpdateThemeBody): At least one of `name` or `styles` must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ThemeFailureResponse | UpdateThemeResponse]
    """

    kwargs = _get_kwargs(
        theme_id=theme_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    theme_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateThemeBody,
) -> Any | ThemeFailureResponse | UpdateThemeResponse | None:
    """Update a theme

     Update a theme's name and/or styles. When `styles` change, the update cascades to every email using
    this theme, and `affectedEmailCount` in the response reports how many emails were affected. Manual
    style edits made on individual emails are preserved: the cascade only changes properties an email
    has not overridden. A per-email override is removed only when it becomes identical to the theme's
    new value, after which that email follows the theme for that property.

    Args:
        theme_id (str):
        body (UpdateThemeBody): At least one of `name` or `styles` must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ThemeFailureResponse | UpdateThemeResponse
    """

    return sync_detailed(
        theme_id=theme_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    theme_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateThemeBody,
) -> Response[Any | ThemeFailureResponse | UpdateThemeResponse]:
    """Update a theme

     Update a theme's name and/or styles. When `styles` change, the update cascades to every email using
    this theme, and `affectedEmailCount` in the response reports how many emails were affected. Manual
    style edits made on individual emails are preserved: the cascade only changes properties an email
    has not overridden. A per-email override is removed only when it becomes identical to the theme's
    new value, after which that email follows the theme for that property.

    Args:
        theme_id (str):
        body (UpdateThemeBody): At least one of `name` or `styles` must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ThemeFailureResponse | UpdateThemeResponse]
    """

    kwargs = _get_kwargs(
        theme_id=theme_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    theme_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateThemeBody,
) -> Any | ThemeFailureResponse | UpdateThemeResponse | None:
    """Update a theme

     Update a theme's name and/or styles. When `styles` change, the update cascades to every email using
    this theme, and `affectedEmailCount` in the response reports how many emails were affected. Manual
    style edits made on individual emails are preserved: the cascade only changes properties an email
    has not overridden. A per-email override is removed only when it becomes identical to the theme's
    new value, after which that email follows the theme for that property.

    Args:
        theme_id (str):
        body (UpdateThemeBody): At least one of `name` or `styles` must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ThemeFailureResponse | UpdateThemeResponse
    """

    return (
        await asyncio_detailed(
            theme_id=theme_id,
            client=client,
            body=body,
        )
    ).parsed
