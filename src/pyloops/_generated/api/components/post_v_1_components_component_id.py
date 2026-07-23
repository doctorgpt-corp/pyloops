from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.component_failure_response import ComponentFailureResponse
from ...models.component_validation_failure_response import ComponentValidationFailureResponse
from ...models.update_component_body import UpdateComponentBody
from ...models.update_component_response import UpdateComponentResponse
from ...types import Response


def _get_kwargs(
    component_id: str,
    *,
    body: UpdateComponentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/components/{component_id}".format(
            component_id=quote(str(component_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ComponentFailureResponse | ComponentValidationFailureResponse | UpdateComponentResponse | None:
    if response.status_code == 200:
        response_200 = UpdateComponentResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ComponentFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = ComponentFailureResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 413:
        response_413 = ComponentFailureResponse.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = ComponentValidationFailureResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ComponentFailureResponse | ComponentValidationFailureResponse | UpdateComponentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateComponentBody,
) -> Response[Any | ComponentFailureResponse | ComponentValidationFailureResponse | UpdateComponentResponse]:
    """Update a component

     Update a component's name and/or body. When the `lmx` body changes, the update cascades to every
    email using this component, and `affectedEmailCount` reports how many were affected. A change that
    would introduce a dynamic variable an email using the component cannot use is rejected.

    Args:
        component_id (str):
        body (UpdateComponentBody): At least one of `name` or `lmx` must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComponentFailureResponse | ComponentValidationFailureResponse | UpdateComponentResponse]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateComponentBody,
) -> Any | ComponentFailureResponse | ComponentValidationFailureResponse | UpdateComponentResponse | None:
    """Update a component

     Update a component's name and/or body. When the `lmx` body changes, the update cascades to every
    email using this component, and `affectedEmailCount` reports how many were affected. A change that
    would introduce a dynamic variable an email using the component cannot use is rejected.

    Args:
        component_id (str):
        body (UpdateComponentBody): At least one of `name` or `lmx` must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComponentFailureResponse | ComponentValidationFailureResponse | UpdateComponentResponse
    """

    return sync_detailed(
        component_id=component_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateComponentBody,
) -> Response[Any | ComponentFailureResponse | ComponentValidationFailureResponse | UpdateComponentResponse]:
    """Update a component

     Update a component's name and/or body. When the `lmx` body changes, the update cascades to every
    email using this component, and `affectedEmailCount` reports how many were affected. A change that
    would introduce a dynamic variable an email using the component cannot use is rejected.

    Args:
        component_id (str):
        body (UpdateComponentBody): At least one of `name` or `lmx` must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ComponentFailureResponse | ComponentValidationFailureResponse | UpdateComponentResponse]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    component_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateComponentBody,
) -> Any | ComponentFailureResponse | ComponentValidationFailureResponse | UpdateComponentResponse | None:
    """Update a component

     Update a component's name and/or body. When the `lmx` body changes, the update cascades to every
    email using this component, and `affectedEmailCount` reports how many were affected. A change that
    would introduce a dynamic variable an email using the component cannot use is rejected.

    Args:
        component_id (str):
        body (UpdateComponentBody): At least one of `name` or `lmx` must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ComponentFailureResponse | ComponentValidationFailureResponse | UpdateComponentResponse
    """

    return (
        await asyncio_detailed(
            component_id=component_id,
            client=client,
            body=body,
        )
    ).parsed
