from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_workflow_branch_request import AddWorkflowBranchRequest
from ...models.add_workflow_branch_response import AddWorkflowBranchResponse
from ...models.workflow_failure_response import WorkflowFailureResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    node_id: str,
    *,
    body: AddWorkflowBranchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workflows/{workflow_id}/nodes/{node_id}/add-branch".format(
            workflow_id=quote(str(workflow_id), safe=""),
            node_id=quote(str(node_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddWorkflowBranchResponse | Any | WorkflowFailureResponse | None:
    if response.status_code == 200:
        response_200 = AddWorkflowBranchResponse.from_dict(response.json())

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
) -> Response[AddWorkflowBranchResponse | Any | WorkflowFailureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
    body: AddWorkflowBranchRequest,
) -> Response[AddWorkflowBranchResponse | Any | WorkflowFailureResponse]:
    """Add a branch

     Add a branch and a child node under an existing Branch or Experiment node. Returns the created child
    node plus the latest workflow.

    - Adding a branch to a `BranchNode` creates one `AudienceFilter` child node.
    - Adding a branch to an `ExperimentBranchNode` creates one `VariantNode` child node.

    This endpoint does not accept node configuration fields; update the child node with `POST
    /v1/workflows/{workflowId}/nodes/{nodeId}` after creation. Public workflows are limited to 300
    nodes, and this endpoint adds 1 node.

    Args:
        workflow_id (str):
        node_id (str):
        body (AddWorkflowBranchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddWorkflowBranchResponse | Any | WorkflowFailureResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        node_id=node_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
    body: AddWorkflowBranchRequest,
) -> AddWorkflowBranchResponse | Any | WorkflowFailureResponse | None:
    """Add a branch

     Add a branch and a child node under an existing Branch or Experiment node. Returns the created child
    node plus the latest workflow.

    - Adding a branch to a `BranchNode` creates one `AudienceFilter` child node.
    - Adding a branch to an `ExperimentBranchNode` creates one `VariantNode` child node.

    This endpoint does not accept node configuration fields; update the child node with `POST
    /v1/workflows/{workflowId}/nodes/{nodeId}` after creation. Public workflows are limited to 300
    nodes, and this endpoint adds 1 node.

    Args:
        workflow_id (str):
        node_id (str):
        body (AddWorkflowBranchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddWorkflowBranchResponse | Any | WorkflowFailureResponse
    """

    return sync_detailed(
        workflow_id=workflow_id,
        node_id=node_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
    body: AddWorkflowBranchRequest,
) -> Response[AddWorkflowBranchResponse | Any | WorkflowFailureResponse]:
    """Add a branch

     Add a branch and a child node under an existing Branch or Experiment node. Returns the created child
    node plus the latest workflow.

    - Adding a branch to a `BranchNode` creates one `AudienceFilter` child node.
    - Adding a branch to an `ExperimentBranchNode` creates one `VariantNode` child node.

    This endpoint does not accept node configuration fields; update the child node with `POST
    /v1/workflows/{workflowId}/nodes/{nodeId}` after creation. Public workflows are limited to 300
    nodes, and this endpoint adds 1 node.

    Args:
        workflow_id (str):
        node_id (str):
        body (AddWorkflowBranchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddWorkflowBranchResponse | Any | WorkflowFailureResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        node_id=node_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
    body: AddWorkflowBranchRequest,
) -> AddWorkflowBranchResponse | Any | WorkflowFailureResponse | None:
    """Add a branch

     Add a branch and a child node under an existing Branch or Experiment node. Returns the created child
    node plus the latest workflow.

    - Adding a branch to a `BranchNode` creates one `AudienceFilter` child node.
    - Adding a branch to an `ExperimentBranchNode` creates one `VariantNode` child node.

    This endpoint does not accept node configuration fields; update the child node with `POST
    /v1/workflows/{workflowId}/nodes/{nodeId}` after creation. Public workflows are limited to 300
    nodes, and this endpoint adds 1 node.

    Args:
        workflow_id (str):
        node_id (str):
        body (AddWorkflowBranchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddWorkflowBranchResponse | Any | WorkflowFailureResponse
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            node_id=node_id,
            client=client,
            body=body,
        )
    ).parsed
