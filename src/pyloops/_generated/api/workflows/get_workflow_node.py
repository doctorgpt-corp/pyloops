from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_to_list_trigger_workflow_node import AddToListTriggerWorkflowNode
from ...models.audience_filter_workflow_node import AudienceFilterWorkflowNode
from ...models.blank_trigger_workflow_node import BlankTriggerWorkflowNode
from ...models.branch_workflow_node import BranchWorkflowNode
from ...models.contact_property_trigger_workflow_node import ContactPropertyTriggerWorkflowNode
from ...models.event_trigger_workflow_node import EventTriggerWorkflowNode
from ...models.exit_action_workflow_node import ExitActionWorkflowNode
from ...models.experiment_branch_workflow_node import ExperimentBranchWorkflowNode
from ...models.send_email_action_workflow_node import SendEmailActionWorkflowNode
from ...models.signup_trigger_workflow_node import SignupTriggerWorkflowNode
from ...models.timer_action_workflow_node import TimerActionWorkflowNode
from ...models.variant_workflow_node import VariantWorkflowNode
from ...models.workflow_failure_response import WorkflowFailureResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    node_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workflows/{workflow_id}/nodes/{node_id}".format(
            workflow_id=quote(str(workflow_id), safe=""),
            node_id=quote(str(node_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddToListTriggerWorkflowNode
    | AudienceFilterWorkflowNode
    | BlankTriggerWorkflowNode
    | BranchWorkflowNode
    | ContactPropertyTriggerWorkflowNode
    | EventTriggerWorkflowNode
    | ExitActionWorkflowNode
    | ExperimentBranchWorkflowNode
    | SendEmailActionWorkflowNode
    | SignupTriggerWorkflowNode
    | TimerActionWorkflowNode
    | VariantWorkflowNode
    | Any
    | WorkflowFailureResponse
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            AddToListTriggerWorkflowNode
            | AudienceFilterWorkflowNode
            | BlankTriggerWorkflowNode
            | BranchWorkflowNode
            | ContactPropertyTriggerWorkflowNode
            | EventTriggerWorkflowNode
            | ExitActionWorkflowNode
            | ExperimentBranchWorkflowNode
            | SendEmailActionWorkflowNode
            | SignupTriggerWorkflowNode
            | TimerActionWorkflowNode
            | VariantWorkflowNode
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_0 = SignupTriggerWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_1 = EventTriggerWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_2 = ContactPropertyTriggerWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_3 = AddToListTriggerWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_4 = BlankTriggerWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_5 = AudienceFilterWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_6 = TimerActionWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_7 = SendEmailActionWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_8 = ExitActionWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_9 = BranchWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_node_type_10 = ExperimentBranchWorkflowNode.from_dict(data)

                return componentsschemas_workflow_node_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_workflow_node_type_11 = VariantWorkflowNode.from_dict(data)

            return componentsschemas_workflow_node_type_11

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AddToListTriggerWorkflowNode
    | AudienceFilterWorkflowNode
    | BlankTriggerWorkflowNode
    | BranchWorkflowNode
    | ContactPropertyTriggerWorkflowNode
    | EventTriggerWorkflowNode
    | ExitActionWorkflowNode
    | ExperimentBranchWorkflowNode
    | SendEmailActionWorkflowNode
    | SignupTriggerWorkflowNode
    | TimerActionWorkflowNode
    | VariantWorkflowNode
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
) -> Response[
    AddToListTriggerWorkflowNode
    | AudienceFilterWorkflowNode
    | BlankTriggerWorkflowNode
    | BranchWorkflowNode
    | ContactPropertyTriggerWorkflowNode
    | EventTriggerWorkflowNode
    | ExitActionWorkflowNode
    | ExperimentBranchWorkflowNode
    | SendEmailActionWorkflowNode
    | SignupTriggerWorkflowNode
    | TimerActionWorkflowNode
    | VariantWorkflowNode
    | Any
    | WorkflowFailureResponse
]:
    """Get workflow node details

     Retrieve detailed data for a single workflow node.

    Args:
        workflow_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddToListTriggerWorkflowNode | AudienceFilterWorkflowNode | BlankTriggerWorkflowNode | BranchWorkflowNode | ContactPropertyTriggerWorkflowNode | EventTriggerWorkflowNode | ExitActionWorkflowNode | ExperimentBranchWorkflowNode | SendEmailActionWorkflowNode | SignupTriggerWorkflowNode | TimerActionWorkflowNode | VariantWorkflowNode | Any | WorkflowFailureResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        node_id=node_id,
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
) -> (
    AddToListTriggerWorkflowNode
    | AudienceFilterWorkflowNode
    | BlankTriggerWorkflowNode
    | BranchWorkflowNode
    | ContactPropertyTriggerWorkflowNode
    | EventTriggerWorkflowNode
    | ExitActionWorkflowNode
    | ExperimentBranchWorkflowNode
    | SendEmailActionWorkflowNode
    | SignupTriggerWorkflowNode
    | TimerActionWorkflowNode
    | VariantWorkflowNode
    | Any
    | WorkflowFailureResponse
    | None
):
    """Get workflow node details

     Retrieve detailed data for a single workflow node.

    Args:
        workflow_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddToListTriggerWorkflowNode | AudienceFilterWorkflowNode | BlankTriggerWorkflowNode | BranchWorkflowNode | ContactPropertyTriggerWorkflowNode | EventTriggerWorkflowNode | ExitActionWorkflowNode | ExperimentBranchWorkflowNode | SendEmailActionWorkflowNode | SignupTriggerWorkflowNode | TimerActionWorkflowNode | VariantWorkflowNode | Any | WorkflowFailureResponse
    """

    return sync_detailed(
        workflow_id=workflow_id,
        node_id=node_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[
    AddToListTriggerWorkflowNode
    | AudienceFilterWorkflowNode
    | BlankTriggerWorkflowNode
    | BranchWorkflowNode
    | ContactPropertyTriggerWorkflowNode
    | EventTriggerWorkflowNode
    | ExitActionWorkflowNode
    | ExperimentBranchWorkflowNode
    | SendEmailActionWorkflowNode
    | SignupTriggerWorkflowNode
    | TimerActionWorkflowNode
    | VariantWorkflowNode
    | Any
    | WorkflowFailureResponse
]:
    """Get workflow node details

     Retrieve detailed data for a single workflow node.

    Args:
        workflow_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddToListTriggerWorkflowNode | AudienceFilterWorkflowNode | BlankTriggerWorkflowNode | BranchWorkflowNode | ContactPropertyTriggerWorkflowNode | EventTriggerWorkflowNode | ExitActionWorkflowNode | ExperimentBranchWorkflowNode | SendEmailActionWorkflowNode | SignupTriggerWorkflowNode | TimerActionWorkflowNode | VariantWorkflowNode | Any | WorkflowFailureResponse]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        node_id=node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    node_id: str,
    *,
    client: AuthenticatedClient,
) -> (
    AddToListTriggerWorkflowNode
    | AudienceFilterWorkflowNode
    | BlankTriggerWorkflowNode
    | BranchWorkflowNode
    | ContactPropertyTriggerWorkflowNode
    | EventTriggerWorkflowNode
    | ExitActionWorkflowNode
    | ExperimentBranchWorkflowNode
    | SendEmailActionWorkflowNode
    | SignupTriggerWorkflowNode
    | TimerActionWorkflowNode
    | VariantWorkflowNode
    | Any
    | WorkflowFailureResponse
    | None
):
    """Get workflow node details

     Retrieve detailed data for a single workflow node.

    Args:
        workflow_id (str):
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddToListTriggerWorkflowNode | AudienceFilterWorkflowNode | BlankTriggerWorkflowNode | BranchWorkflowNode | ContactPropertyTriggerWorkflowNode | EventTriggerWorkflowNode | ExitActionWorkflowNode | ExperimentBranchWorkflowNode | SendEmailActionWorkflowNode | SignupTriggerWorkflowNode | TimerActionWorkflowNode | VariantWorkflowNode | Any | WorkflowFailureResponse
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            node_id=node_id,
            client=client,
        )
    ).parsed
