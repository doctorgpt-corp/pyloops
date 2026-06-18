from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_failure_response import GroupFailureResponse
from ...models.group_response import GroupResponse
from ...types import Response


def _get_kwargs(
    campaign_group_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/campaign-groups/{campaign_group_id}".format(
            campaign_group_id=quote(str(campaign_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GroupFailureResponse | GroupResponse | None:
    if response.status_code == 200:
        response_200 = GroupResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GroupFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = GroupFailureResponse.from_dict(response.json())

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
) -> Response[Any | GroupFailureResponse | GroupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign_group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | GroupFailureResponse | GroupResponse]:
    """Get a campaign group

     Retrieve a single campaign group by ID.

    Args:
        campaign_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GroupFailureResponse | GroupResponse]
    """

    kwargs = _get_kwargs(
        campaign_group_id=campaign_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign_group_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | GroupFailureResponse | GroupResponse | None:
    """Get a campaign group

     Retrieve a single campaign group by ID.

    Args:
        campaign_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GroupFailureResponse | GroupResponse
    """

    return sync_detailed(
        campaign_group_id=campaign_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    campaign_group_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | GroupFailureResponse | GroupResponse]:
    """Get a campaign group

     Retrieve a single campaign group by ID.

    Args:
        campaign_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GroupFailureResponse | GroupResponse]
    """

    kwargs = _get_kwargs(
        campaign_group_id=campaign_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign_group_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | GroupFailureResponse | GroupResponse | None:
    """Get a campaign group

     Retrieve a single campaign group by ID.

    Args:
        campaign_group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GroupFailureResponse | GroupResponse
    """

    return (
        await asyncio_detailed(
            campaign_group_id=campaign_group_id,
            client=client,
        )
    ).parsed
