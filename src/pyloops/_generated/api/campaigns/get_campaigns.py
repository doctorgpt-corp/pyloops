from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.campaign_failure_response import CampaignFailureResponse
from ...models.list_campaigns_response import ListCampaignsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["perPage"] = per_page

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/campaigns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CampaignFailureResponse | ListCampaignsResponse | None:
    if response.status_code == 200:
        response_200 = ListCampaignsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CampaignFailureResponse.from_dict(response.json())

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
) -> Response[Any | CampaignFailureResponse | ListCampaignsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    per_page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[Any | CampaignFailureResponse | ListCampaignsResponse]:
    """List campaigns

     Retrieve a paginated list of campaigns.

    Args:
        per_page (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CampaignFailureResponse | ListCampaignsResponse]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    per_page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Any | CampaignFailureResponse | ListCampaignsResponse | None:
    """List campaigns

     Retrieve a paginated list of campaigns.

    Args:
        per_page (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CampaignFailureResponse | ListCampaignsResponse
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    per_page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Response[Any | CampaignFailureResponse | ListCampaignsResponse]:
    """List campaigns

     Retrieve a paginated list of campaigns.

    Args:
        per_page (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CampaignFailureResponse | ListCampaignsResponse]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    per_page: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
) -> Any | CampaignFailureResponse | ListCampaignsResponse | None:
    """List campaigns

     Retrieve a paginated list of campaigns.

    Args:
        per_page (str | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CampaignFailureResponse | ListCampaignsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            cursor=cursor,
        )
    ).parsed
