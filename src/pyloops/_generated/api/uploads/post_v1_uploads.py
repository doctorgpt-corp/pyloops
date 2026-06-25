from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_upload_request import CreateUploadRequest
from ...models.create_upload_response import CreateUploadResponse
from ...models.upload_failure_response import UploadFailureResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateUploadRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/uploads",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateUploadResponse | UploadFailureResponse | None:
    if response.status_code == 200:
        response_200 = CreateUploadResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UploadFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 413:
        response_413 = UploadFailureResponse.from_dict(response.json())

        return response_413

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CreateUploadResponse | UploadFailureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUploadRequest,
) -> Response[Any | CreateUploadResponse | UploadFailureResponse]:
    """Create an upload

     Request a pre-signed URL to upload an image asset. Upload the file with an HTTP `PUT` to the
    returned `presignedUrl` (sending the same `Content-Type` and `Content-Length`), then call
    `/uploads/{id}/complete` to finalize the asset.

    Args:
        body (CreateUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateUploadResponse | UploadFailureResponse]
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
    body: CreateUploadRequest,
) -> Any | CreateUploadResponse | UploadFailureResponse | None:
    """Create an upload

     Request a pre-signed URL to upload an image asset. Upload the file with an HTTP `PUT` to the
    returned `presignedUrl` (sending the same `Content-Type` and `Content-Length`), then call
    `/uploads/{id}/complete` to finalize the asset.

    Args:
        body (CreateUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateUploadResponse | UploadFailureResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUploadRequest,
) -> Response[Any | CreateUploadResponse | UploadFailureResponse]:
    """Create an upload

     Request a pre-signed URL to upload an image asset. Upload the file with an HTTP `PUT` to the
    returned `presignedUrl` (sending the same `Content-Type` and `Content-Length`), then call
    `/uploads/{id}/complete` to finalize the asset.

    Args:
        body (CreateUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateUploadResponse | UploadFailureResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateUploadRequest,
) -> Any | CreateUploadResponse | UploadFailureResponse | None:
    """Create an upload

     Request a pre-signed URL to upload an image asset. Upload the file with an HTTP `PUT` to the
    returned `presignedUrl` (sending the same `Content-Type` and `Content-Length`), then call
    `/uploads/{id}/complete` to finalize the asset.

    Args:
        body (CreateUploadRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateUploadResponse | UploadFailureResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
