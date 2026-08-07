from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audience_segment_failure_response import AudienceSegmentFailureResponse
from ...models.audience_segment_response import AudienceSegmentResponse
from ...models.create_audience_segment_request import CreateAudienceSegmentRequest
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAudienceSegmentRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/audience-segments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AudienceSegmentFailureResponse | AudienceSegmentResponse | None:
    if response.status_code == 200:
        response_200 = AudienceSegmentResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AudienceSegmentFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = AudienceSegmentFailureResponse.from_dict(response.json())

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
) -> Response[Any | AudienceSegmentFailureResponse | AudienceSegmentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateAudienceSegmentRequest,
) -> Response[Any | AudienceSegmentFailureResponse | AudienceSegmentResponse]:
    """Create an audience segment

     Create a new audience segment.

    Args:
        body (CreateAudienceSegmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AudienceSegmentFailureResponse | AudienceSegmentResponse]
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
    body: CreateAudienceSegmentRequest,
) -> Any | AudienceSegmentFailureResponse | AudienceSegmentResponse | None:
    """Create an audience segment

     Create a new audience segment.

    Args:
        body (CreateAudienceSegmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AudienceSegmentFailureResponse | AudienceSegmentResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateAudienceSegmentRequest,
) -> Response[Any | AudienceSegmentFailureResponse | AudienceSegmentResponse]:
    """Create an audience segment

     Create a new audience segment.

    Args:
        body (CreateAudienceSegmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AudienceSegmentFailureResponse | AudienceSegmentResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateAudienceSegmentRequest,
) -> Any | AudienceSegmentFailureResponse | AudienceSegmentResponse | None:
    """Create an audience segment

     Create a new audience segment.

    Args:
        body (CreateAudienceSegmentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AudienceSegmentFailureResponse | AudienceSegmentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
