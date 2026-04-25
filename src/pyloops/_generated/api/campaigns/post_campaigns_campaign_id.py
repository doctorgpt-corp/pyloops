from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.campaign_failure_response import CampaignFailureResponse
from ...models.campaign_response import CampaignResponse
from ...models.update_campaign_request import UpdateCampaignRequest
from ...types import Response


def _get_kwargs(
    campaign_id: str,
    *,
    body: UpdateCampaignRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/campaigns/{campaign_id}".format(
            campaign_id=quote(str(campaign_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CampaignFailureResponse | CampaignResponse | None:
    if response.status_code == 200:
        response_200 = CampaignResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CampaignFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = CampaignFailureResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 409:
        response_409 = CampaignFailureResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CampaignFailureResponse | CampaignResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCampaignRequest,
) -> Response[Any | CampaignFailureResponse | CampaignResponse]:
    """Update a campaign

     Update a draft campaign's name. Campaigns can only be updated while in draft status.

    Args:
        campaign_id (str):
        body (UpdateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CampaignFailureResponse | CampaignResponse]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCampaignRequest,
) -> Any | CampaignFailureResponse | CampaignResponse | None:
    """Update a campaign

     Update a draft campaign's name. Campaigns can only be updated while in draft status.

    Args:
        campaign_id (str):
        body (UpdateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CampaignFailureResponse | CampaignResponse
    """

    return sync_detailed(
        campaign_id=campaign_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCampaignRequest,
) -> Response[Any | CampaignFailureResponse | CampaignResponse]:
    """Update a campaign

     Update a draft campaign's name. Campaigns can only be updated while in draft status.

    Args:
        campaign_id (str):
        body (UpdateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CampaignFailureResponse | CampaignResponse]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCampaignRequest,
) -> Any | CampaignFailureResponse | CampaignResponse | None:
    """Update a campaign

     Update a draft campaign's name. Campaigns can only be updated while in draft status.

    Args:
        campaign_id (str):
        body (UpdateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CampaignFailureResponse | CampaignResponse
    """

    return (
        await asyncio_detailed(
            campaign_id=campaign_id,
            client=client,
            body=body,
        )
    ).parsed
