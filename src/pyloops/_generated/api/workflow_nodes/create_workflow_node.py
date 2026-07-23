from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_workflow_node_before_request import CreateWorkflowNodeBeforeRequest
from ...models.create_workflow_node_between_request import CreateWorkflowNodeBetweenRequest
from ...models.workflow_failure_response import WorkflowFailureResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    *,
    body: CreateWorkflowNodeBeforeRequest | CreateWorkflowNodeBetweenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workflows/{workflow_id}/nodes".format(
            workflow_id=quote(str(workflow_id), safe=""),
        ),
    }

    if isinstance(body, CreateWorkflowNodeBetweenRequest):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | WorkflowFailureResponse | None:
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
) -> Response[Any | WorkflowFailureResponse]:
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
    body: CreateWorkflowNodeBeforeRequest | CreateWorkflowNodeBetweenRequest,
) -> Response[Any | WorkflowFailureResponse]:
    """Create a workflow node

     Create a new default workflow node and return it with the latest workflow.

    Choose where the node goes with `insertMode`: `between` places it between an existing `fromNodeId`
    -> `toNodeId` connection, and `before` places it before `beforeNodeId`.

    New nodes start with default settings; update the node after creation to configure it. Branch nodes
    create their default paths too: `BranchNode` creates two `AudienceFilter` children, and
    `ExperimentBranchNode` creates two regular `VariantNode` children plus one control `VariantNode`.
    Public workflows can have up to 300 nodes. Generated children count toward that limit, so a normal
    create adds 1 node, `BranchNode` adds 3, and `ExperimentBranchNode` adds 4. To add a new branch or
    experiment branch, use the `POST /v1/workflows/{workflowId}/nodes/{nodeId}/add-branch` endpoint
    instead.

    Args:
        workflow_id (str):
        body (CreateWorkflowNodeBeforeRequest | CreateWorkflowNodeBetweenRequest): Create a new
            workflow node with an explicit `insertMode`. To configure the node after creation, use the
            `POST /v1/workflows/{workflowId}/nodes/{nodeId}` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowFailureResponse]
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
    body: CreateWorkflowNodeBeforeRequest | CreateWorkflowNodeBetweenRequest,
) -> Any | WorkflowFailureResponse | None:
    """Create a workflow node

     Create a new default workflow node and return it with the latest workflow.

    Choose where the node goes with `insertMode`: `between` places it between an existing `fromNodeId`
    -> `toNodeId` connection, and `before` places it before `beforeNodeId`.

    New nodes start with default settings; update the node after creation to configure it. Branch nodes
    create their default paths too: `BranchNode` creates two `AudienceFilter` children, and
    `ExperimentBranchNode` creates two regular `VariantNode` children plus one control `VariantNode`.
    Public workflows can have up to 300 nodes. Generated children count toward that limit, so a normal
    create adds 1 node, `BranchNode` adds 3, and `ExperimentBranchNode` adds 4. To add a new branch or
    experiment branch, use the `POST /v1/workflows/{workflowId}/nodes/{nodeId}/add-branch` endpoint
    instead.

    Args:
        workflow_id (str):
        body (CreateWorkflowNodeBeforeRequest | CreateWorkflowNodeBetweenRequest): Create a new
            workflow node with an explicit `insertMode`. To configure the node after creation, use the
            `POST /v1/workflows/{workflowId}/nodes/{nodeId}` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowFailureResponse
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
    body: CreateWorkflowNodeBeforeRequest | CreateWorkflowNodeBetweenRequest,
) -> Response[Any | WorkflowFailureResponse]:
    """Create a workflow node

     Create a new default workflow node and return it with the latest workflow.

    Choose where the node goes with `insertMode`: `between` places it between an existing `fromNodeId`
    -> `toNodeId` connection, and `before` places it before `beforeNodeId`.

    New nodes start with default settings; update the node after creation to configure it. Branch nodes
    create their default paths too: `BranchNode` creates two `AudienceFilter` children, and
    `ExperimentBranchNode` creates two regular `VariantNode` children plus one control `VariantNode`.
    Public workflows can have up to 300 nodes. Generated children count toward that limit, so a normal
    create adds 1 node, `BranchNode` adds 3, and `ExperimentBranchNode` adds 4. To add a new branch or
    experiment branch, use the `POST /v1/workflows/{workflowId}/nodes/{nodeId}/add-branch` endpoint
    instead.

    Args:
        workflow_id (str):
        body (CreateWorkflowNodeBeforeRequest | CreateWorkflowNodeBetweenRequest): Create a new
            workflow node with an explicit `insertMode`. To configure the node after creation, use the
            `POST /v1/workflows/{workflowId}/nodes/{nodeId}` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowFailureResponse]
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
    body: CreateWorkflowNodeBeforeRequest | CreateWorkflowNodeBetweenRequest,
) -> Any | WorkflowFailureResponse | None:
    """Create a workflow node

     Create a new default workflow node and return it with the latest workflow.

    Choose where the node goes with `insertMode`: `between` places it between an existing `fromNodeId`
    -> `toNodeId` connection, and `before` places it before `beforeNodeId`.

    New nodes start with default settings; update the node after creation to configure it. Branch nodes
    create their default paths too: `BranchNode` creates two `AudienceFilter` children, and
    `ExperimentBranchNode` creates two regular `VariantNode` children plus one control `VariantNode`.
    Public workflows can have up to 300 nodes. Generated children count toward that limit, so a normal
    create adds 1 node, `BranchNode` adds 3, and `ExperimentBranchNode` adds 4. To add a new branch or
    experiment branch, use the `POST /v1/workflows/{workflowId}/nodes/{nodeId}/add-branch` endpoint
    instead.

    Args:
        workflow_id (str):
        body (CreateWorkflowNodeBeforeRequest | CreateWorkflowNodeBetweenRequest): Create a new
            workflow node with an explicit `insertMode`. To configure the node after creation, use the
            `POST /v1/workflows/{workflowId}/nodes/{nodeId}` endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowFailureResponse
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
