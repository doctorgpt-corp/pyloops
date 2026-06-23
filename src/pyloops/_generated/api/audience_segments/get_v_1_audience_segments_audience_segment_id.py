from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audience_segment_failure_response import AudienceSegmentFailureResponse
from ...models.audience_segment_response import AudienceSegmentResponse
from ...types import Response


def _get_kwargs(
    audience_segment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audience-segments/{audience_segment_id}".format(
            audience_segment_id=quote(str(audience_segment_id), safe=""),
        ),
    }

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
    audience_segment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | AudienceSegmentFailureResponse | AudienceSegmentResponse]:
    """Get an audience segment

     Retrieve a single audience segment by ID.

    Args:
        audience_segment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AudienceSegmentFailureResponse | AudienceSegmentResponse]
    """

    kwargs = _get_kwargs(
        audience_segment_id=audience_segment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    audience_segment_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | AudienceSegmentFailureResponse | AudienceSegmentResponse | None:
    """Get an audience segment

     Retrieve a single audience segment by ID.

    Args:
        audience_segment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AudienceSegmentFailureResponse | AudienceSegmentResponse
    """

    return sync_detailed(
        audience_segment_id=audience_segment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    audience_segment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | AudienceSegmentFailureResponse | AudienceSegmentResponse]:
    """Get an audience segment

     Retrieve a single audience segment by ID.

    Args:
        audience_segment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AudienceSegmentFailureResponse | AudienceSegmentResponse]
    """

    kwargs = _get_kwargs(
        audience_segment_id=audience_segment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audience_segment_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | AudienceSegmentFailureResponse | AudienceSegmentResponse | None:
    """Get an audience segment

     Retrieve a single audience segment by ID.

    Args:
        audience_segment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AudienceSegmentFailureResponse | AudienceSegmentResponse
    """

    return (
        await asyncio_detailed(
            audience_segment_id=audience_segment_id,
            client=client,
        )
    ).parsed
