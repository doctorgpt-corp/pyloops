from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_workflow_node_request import DeleteWorkflowNodeRequest
from ...models.workflow_deleted_response import WorkflowDeletedResponse
from ...models.workflow_failure_response import WorkflowFailureResponse
from ...models.workflow_queued_contact_delete_preview import WorkflowQueuedContactDeletePreview
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    node_id: str,
    *,
    body: DeleteWorkflowNodeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/workflows/{workflow_id}/nodes/{node_id}/recursive".format(
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
) -> Any | WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview | WorkflowFailureResponse | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_delete_workflow_node_response_type_0 = WorkflowQueuedContactDeletePreview.from_dict(
                    data
                )

                return componentsschemas_delete_workflow_node_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_delete_workflow_node_response_type_1 = WorkflowDeletedResponse.from_dict(data)

            return componentsschemas_delete_workflow_node_response_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[Any | WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview | WorkflowFailureResponse]:
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
    body: DeleteWorkflowNodeRequest,
) -> Response[Any | WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview | WorkflowFailureResponse]:
    r"""Delete workflow nodes recursively

     Delete a node and its downstream subtree. If contacts are queued at any node that would be deleted,
    Loops returns with `\"status\": \"queuedContactsFound\"` instead of deleting. Retry with
    `queuedContactPolicy: \"discard\"` to delete the nodes and discard those queued contacts. Confirmed
    deletion responses include the simplified workflow after the nodes are removed.

    Args:
        workflow_id (str):
        node_id (str):
        body (DeleteWorkflowNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview | WorkflowFailureResponse]
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
    body: DeleteWorkflowNodeRequest,
) -> Any | WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview | WorkflowFailureResponse | None:
    r"""Delete workflow nodes recursively

     Delete a node and its downstream subtree. If contacts are queued at any node that would be deleted,
    Loops returns with `\"status\": \"queuedContactsFound\"` instead of deleting. Retry with
    `queuedContactPolicy: \"discard\"` to delete the nodes and discard those queued contacts. Confirmed
    deletion responses include the simplified workflow after the nodes are removed.

    Args:
        workflow_id (str):
        node_id (str):
        body (DeleteWorkflowNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview | WorkflowFailureResponse
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
    body: DeleteWorkflowNodeRequest,
) -> Response[Any | WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview | WorkflowFailureResponse]:
    r"""Delete workflow nodes recursively

     Delete a node and its downstream subtree. If contacts are queued at any node that would be deleted,
    Loops returns with `\"status\": \"queuedContactsFound\"` instead of deleting. Retry with
    `queuedContactPolicy: \"discard\"` to delete the nodes and discard those queued contacts. Confirmed
    deletion responses include the simplified workflow after the nodes are removed.

    Args:
        workflow_id (str):
        node_id (str):
        body (DeleteWorkflowNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview | WorkflowFailureResponse]
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
    body: DeleteWorkflowNodeRequest,
) -> Any | WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview | WorkflowFailureResponse | None:
    r"""Delete workflow nodes recursively

     Delete a node and its downstream subtree. If contacts are queued at any node that would be deleted,
    Loops returns with `\"status\": \"queuedContactsFound\"` instead of deleting. Retry with
    `queuedContactPolicy: \"discard\"` to delete the nodes and discard those queued contacts. Confirmed
    deletion responses include the simplified workflow after the nodes are removed.

    Args:
        workflow_id (str):
        node_id (str):
        body (DeleteWorkflowNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowDeletedResponse | WorkflowQueuedContactDeletePreview | WorkflowFailureResponse
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            node_id=node_id,
            client=client,
            body=body,
        )
    ).parsed
