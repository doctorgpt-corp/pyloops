from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_to_list_trigger_workflow_mutation_node_with_revision import (
    AddToListTriggerWorkflowMutationNodeWithRevision,
)
from ...models.audience_filter_workflow_mutation_node_with_revision import (
    AudienceFilterWorkflowMutationNodeWithRevision,
)
from ...models.contact_property_trigger_workflow_mutation_node_with_revision import (
    ContactPropertyTriggerWorkflowMutationNodeWithRevision,
)
from ...models.event_trigger_workflow_mutation_node_with_revision import EventTriggerWorkflowMutationNodeWithRevision
from ...models.experiment_branch_workflow_mutation_node_with_revision import (
    ExperimentBranchWorkflowMutationNodeWithRevision,
)
from ...models.signup_trigger_workflow_mutation_node_with_revision import SignupTriggerWorkflowMutationNodeWithRevision
from ...models.timer_action_workflow_mutation_node_with_revision import TimerActionWorkflowMutationNodeWithRevision
from ...models.update_workflow_node_request import UpdateWorkflowNodeRequest
from ...models.variant_workflow_mutation_node_with_revision import VariantWorkflowMutationNodeWithRevision
from ...models.workflow_failure_response import WorkflowFailureResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    node_id: str,
    *,
    body: UpdateWorkflowNodeRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workflows/{workflow_id}/nodes/{node_id}".format(
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
) -> (
    AddToListTriggerWorkflowMutationNodeWithRevision
    | AudienceFilterWorkflowMutationNodeWithRevision
    | ContactPropertyTriggerWorkflowMutationNodeWithRevision
    | EventTriggerWorkflowMutationNodeWithRevision
    | ExperimentBranchWorkflowMutationNodeWithRevision
    | SignupTriggerWorkflowMutationNodeWithRevision
    | TimerActionWorkflowMutationNodeWithRevision
    | VariantWorkflowMutationNodeWithRevision
    | Any
    | WorkflowFailureResponse
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            AddToListTriggerWorkflowMutationNodeWithRevision
            | AudienceFilterWorkflowMutationNodeWithRevision
            | ContactPropertyTriggerWorkflowMutationNodeWithRevision
            | EventTriggerWorkflowMutationNodeWithRevision
            | ExperimentBranchWorkflowMutationNodeWithRevision
            | SignupTriggerWorkflowMutationNodeWithRevision
            | TimerActionWorkflowMutationNodeWithRevision
            | VariantWorkflowMutationNodeWithRevision
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_response_type_0 = (
                    SignupTriggerWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_update_workflow_node_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_response_type_1 = (
                    EventTriggerWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_update_workflow_node_response_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_response_type_2 = (
                    ContactPropertyTriggerWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_update_workflow_node_response_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_response_type_3 = (
                    AddToListTriggerWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_update_workflow_node_response_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_response_type_4 = (
                    AudienceFilterWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_update_workflow_node_response_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_response_type_5 = (
                    TimerActionWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_update_workflow_node_response_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_response_type_6 = (
                    ExperimentBranchWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_update_workflow_node_response_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_update_workflow_node_response_type_7 = VariantWorkflowMutationNodeWithRevision.from_dict(
                data
            )

            return componentsschemas_update_workflow_node_response_type_7

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

    if response.status_code == 501:
        response_501 = WorkflowFailureResponse.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddToListTriggerWorkflowMutationNodeWithRevision
    | AudienceFilterWorkflowMutationNodeWithRevision
    | ContactPropertyTriggerWorkflowMutationNodeWithRevision
    | EventTriggerWorkflowMutationNodeWithRevision
    | ExperimentBranchWorkflowMutationNodeWithRevision
    | SignupTriggerWorkflowMutationNodeWithRevision
    | TimerActionWorkflowMutationNodeWithRevision
    | VariantWorkflowMutationNodeWithRevision
    | Any
    | WorkflowFailureResponse
]:
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
    body: UpdateWorkflowNodeRequest,
) -> Response[
    AddToListTriggerWorkflowMutationNodeWithRevision
    | AudienceFilterWorkflowMutationNodeWithRevision
    | ContactPropertyTriggerWorkflowMutationNodeWithRevision
    | EventTriggerWorkflowMutationNodeWithRevision
    | ExperimentBranchWorkflowMutationNodeWithRevision
    | SignupTriggerWorkflowMutationNodeWithRevision
    | TimerActionWorkflowMutationNodeWithRevision
    | VariantWorkflowMutationNodeWithRevision
    | Any
    | WorkflowFailureResponse
]:
    """Update a workflow node

     Update workflow-node-owned fields for a single node. Shared resources such as email messages and
    audience segments should be updated through their own APIs.

    Args:
        workflow_id (str):
        node_id (str):
        body (UpdateWorkflowNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddToListTriggerWorkflowMutationNodeWithRevision | AudienceFilterWorkflowMutationNodeWithRevision | ContactPropertyTriggerWorkflowMutationNodeWithRevision | EventTriggerWorkflowMutationNodeWithRevision | ExperimentBranchWorkflowMutationNodeWithRevision | SignupTriggerWorkflowMutationNodeWithRevision | TimerActionWorkflowMutationNodeWithRevision | VariantWorkflowMutationNodeWithRevision | Any | WorkflowFailureResponse]
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
    body: UpdateWorkflowNodeRequest,
) -> (
    AddToListTriggerWorkflowMutationNodeWithRevision
    | AudienceFilterWorkflowMutationNodeWithRevision
    | ContactPropertyTriggerWorkflowMutationNodeWithRevision
    | EventTriggerWorkflowMutationNodeWithRevision
    | ExperimentBranchWorkflowMutationNodeWithRevision
    | SignupTriggerWorkflowMutationNodeWithRevision
    | TimerActionWorkflowMutationNodeWithRevision
    | VariantWorkflowMutationNodeWithRevision
    | Any
    | WorkflowFailureResponse
    | None
):
    """Update a workflow node

     Update workflow-node-owned fields for a single node. Shared resources such as email messages and
    audience segments should be updated through their own APIs.

    Args:
        workflow_id (str):
        node_id (str):
        body (UpdateWorkflowNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddToListTriggerWorkflowMutationNodeWithRevision | AudienceFilterWorkflowMutationNodeWithRevision | ContactPropertyTriggerWorkflowMutationNodeWithRevision | EventTriggerWorkflowMutationNodeWithRevision | ExperimentBranchWorkflowMutationNodeWithRevision | SignupTriggerWorkflowMutationNodeWithRevision | TimerActionWorkflowMutationNodeWithRevision | VariantWorkflowMutationNodeWithRevision | Any | WorkflowFailureResponse
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
    body: UpdateWorkflowNodeRequest,
) -> Response[
    AddToListTriggerWorkflowMutationNodeWithRevision
    | AudienceFilterWorkflowMutationNodeWithRevision
    | ContactPropertyTriggerWorkflowMutationNodeWithRevision
    | EventTriggerWorkflowMutationNodeWithRevision
    | ExperimentBranchWorkflowMutationNodeWithRevision
    | SignupTriggerWorkflowMutationNodeWithRevision
    | TimerActionWorkflowMutationNodeWithRevision
    | VariantWorkflowMutationNodeWithRevision
    | Any
    | WorkflowFailureResponse
]:
    """Update a workflow node

     Update workflow-node-owned fields for a single node. Shared resources such as email messages and
    audience segments should be updated through their own APIs.

    Args:
        workflow_id (str):
        node_id (str):
        body (UpdateWorkflowNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddToListTriggerWorkflowMutationNodeWithRevision | AudienceFilterWorkflowMutationNodeWithRevision | ContactPropertyTriggerWorkflowMutationNodeWithRevision | EventTriggerWorkflowMutationNodeWithRevision | ExperimentBranchWorkflowMutationNodeWithRevision | SignupTriggerWorkflowMutationNodeWithRevision | TimerActionWorkflowMutationNodeWithRevision | VariantWorkflowMutationNodeWithRevision | Any | WorkflowFailureResponse]
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
    body: UpdateWorkflowNodeRequest,
) -> (
    AddToListTriggerWorkflowMutationNodeWithRevision
    | AudienceFilterWorkflowMutationNodeWithRevision
    | ContactPropertyTriggerWorkflowMutationNodeWithRevision
    | EventTriggerWorkflowMutationNodeWithRevision
    | ExperimentBranchWorkflowMutationNodeWithRevision
    | SignupTriggerWorkflowMutationNodeWithRevision
    | TimerActionWorkflowMutationNodeWithRevision
    | VariantWorkflowMutationNodeWithRevision
    | Any
    | WorkflowFailureResponse
    | None
):
    """Update a workflow node

     Update workflow-node-owned fields for a single node. Shared resources such as email messages and
    audience segments should be updated through their own APIs.

    Args:
        workflow_id (str):
        node_id (str):
        body (UpdateWorkflowNodeRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddToListTriggerWorkflowMutationNodeWithRevision | AudienceFilterWorkflowMutationNodeWithRevision | ContactPropertyTriggerWorkflowMutationNodeWithRevision | EventTriggerWorkflowMutationNodeWithRevision | ExperimentBranchWorkflowMutationNodeWithRevision | SignupTriggerWorkflowMutationNodeWithRevision | TimerActionWorkflowMutationNodeWithRevision | VariantWorkflowMutationNodeWithRevision | Any | WorkflowFailureResponse
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            node_id=node_id,
            client=client,
            body=body,
        )
    ).parsed
