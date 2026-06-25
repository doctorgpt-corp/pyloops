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
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workflows/{workflow_id}".format(
            workflow_id=quote(str(workflow_id), safe=""),
        ),
    }

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
) -> Response[Any | SimplifiedWorkflow | WorkflowFailureResponse]:
    """Get a simplified workflow

     Retrieve a workflow graph with node type names, connections, and selected display fields.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SimplifiedWorkflow | WorkflowFailureResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | SimplifiedWorkflow | WorkflowFailureResponse | None:
    """Get a simplified workflow

     Retrieve a workflow graph with node type names, connections, and selected display fields.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SimplifiedWorkflow | WorkflowFailureResponse
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | SimplifiedWorkflow | WorkflowFailureResponse]:
    """Get a simplified workflow

     Retrieve a workflow graph with node type names, connections, and selected display fields.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SimplifiedWorkflow | WorkflowFailureResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | SimplifiedWorkflow | WorkflowFailureResponse | None:
    """Get a simplified workflow

     Retrieve a workflow graph with node type names, connections, and selected display fields.

    Args:
        workflow_id (str):

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
        )
    ).parsed
