from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_upload_response import CompleteUploadResponse
from ...models.upload_failure_response import UploadFailureResponse
from ...models.upload_limit_exceeded_failure_response import UploadLimitExceededFailureResponse
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/uploads/{id}/complete".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CompleteUploadResponse | UploadFailureResponse | UploadLimitExceededFailureResponse | None:
    if response.status_code == 200:
        response_200 = CompleteUploadResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UploadFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = UploadFailureResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 429:
        response_429 = UploadLimitExceededFailureResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CompleteUploadResponse | UploadFailureResponse | UploadLimitExceededFailureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CompleteUploadResponse | UploadFailureResponse | UploadLimitExceededFailureResponse]:
    """Complete an upload

     Finalize an asset after the file has been uploaded to the pre-signed URL. Returns the public URL of
    the uploaded asset.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteUploadResponse | UploadFailureResponse | UploadLimitExceededFailureResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Any | CompleteUploadResponse | UploadFailureResponse | UploadLimitExceededFailureResponse | None:
    """Complete an upload

     Finalize an asset after the file has been uploaded to the pre-signed URL. Returns the public URL of
    the uploaded asset.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteUploadResponse | UploadFailureResponse | UploadLimitExceededFailureResponse
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CompleteUploadResponse | UploadFailureResponse | UploadLimitExceededFailureResponse]:
    """Complete an upload

     Finalize an asset after the file has been uploaded to the pre-signed URL. Returns the public URL of
    the uploaded asset.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompleteUploadResponse | UploadFailureResponse | UploadLimitExceededFailureResponse]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Any | CompleteUploadResponse | UploadFailureResponse | UploadLimitExceededFailureResponse | None:
    """Complete an upload

     Finalize an asset after the file has been uploaded to the pre-signed URL. Returns the public URL of
    the uploaded asset.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompleteUploadResponse | UploadFailureResponse | UploadLimitExceededFailureResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
