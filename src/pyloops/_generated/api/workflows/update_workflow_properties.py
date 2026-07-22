from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.simplified_workflow import SimplifiedWorkflow
from ...models.workflow_failure_response import WorkflowFailureResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    *,
    body: Any,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workflows/{workflow_id}".format(
            workflow_id=quote(str(workflow_id), safe=""),
        ),
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | SimplifiedWorkflow | WorkflowFailureResponse | None:
    if response.status_code == 200:
        response_200 = SimplifiedWorkflow.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = WorkflowFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = WorkflowFailureResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 409:
        response_409 = WorkflowFailureResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | SimplifiedWorkflow | WorkflowFailureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Response[Any | SimplifiedWorkflow | WorkflowFailureResponse]:
    """Update a workflow

     Update a workflow's display properties. At least one property must be provided. To change the
    workflow's mailing list, use the `/v1/workflows/{workflowId}/mailing-list` endpoint instead.

    Args:
        workflow_id (str):
        body (Any): At least one property must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SimplifiedWorkflow | WorkflowFailureResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Any | SimplifiedWorkflow | WorkflowFailureResponse | None:
    """Update a workflow

     Update a workflow's display properties. At least one property must be provided. To change the
    workflow's mailing list, use the `/v1/workflows/{workflowId}/mailing-list` endpoint instead.

    Args:
        workflow_id (str):
        body (Any): At least one property must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SimplifiedWorkflow | WorkflowFailureResponse
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Response[Any | SimplifiedWorkflow | WorkflowFailureResponse]:
    """Update a workflow

     Update a workflow's display properties. At least one property must be provided. To change the
    workflow's mailing list, use the `/v1/workflows/{workflowId}/mailing-list` endpoint instead.

    Args:
        workflow_id (str):
        body (Any): At least one property must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SimplifiedWorkflow | WorkflowFailureResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Any | SimplifiedWorkflow | WorkflowFailureResponse | None:
    """Update a workflow

     Update a workflow's display properties. At least one property must be provided. To change the
    workflow's mailing list, use the `/v1/workflows/{workflowId}/mailing-list` endpoint instead.

    Args:
        workflow_id (str):
        body (Any): At least one property must be provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SimplifiedWorkflow | WorkflowFailureResponse
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
