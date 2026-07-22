from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.change_workflow_mailing_list_request import ChangeWorkflowMailingListRequest
from ...models.workflow_failure_response import WorkflowFailureResponse
from ...models.workflow_mailing_list_preview import WorkflowMailingListPreview
from ...models.workflow_mailing_list_updated_response import WorkflowMailingListUpdatedResponse
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    *,
    body: ChangeWorkflowMailingListRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workflows/{workflow_id}/mailing-list".format(
            workflow_id=quote(str(workflow_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | WorkflowFailureResponse | WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_change_workflow_mailing_list_response_type_0 = WorkflowMailingListPreview.from_dict(
                    data
                )

                return componentsschemas_change_workflow_mailing_list_response_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_change_workflow_mailing_list_response_type_1 = (
                WorkflowMailingListUpdatedResponse.from_dict(data)
            )

            return componentsschemas_change_workflow_mailing_list_response_type_1

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
) -> Response[Any | WorkflowFailureResponse | WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse]:
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
    body: ChangeWorkflowMailingListRequest,
) -> Response[Any | WorkflowFailureResponse | WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse]:
    r"""Change workflow mailing list

     Dry run or apply a workflow mailing list change. If queued contacts would be removed from the
    workflow due to the change of mailing list, Loops returns with `\"status\": \"queuedContactsFound\"`
    instead of applying the change. Retry with `queuedContactPolicy: \"discard\"` to apply the change
    and discard those contacts.

    Args:
        workflow_id (str):
        body (ChangeWorkflowMailingListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowFailureResponse | WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse]
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
    body: ChangeWorkflowMailingListRequest,
) -> Any | WorkflowFailureResponse | WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse | None:
    r"""Change workflow mailing list

     Dry run or apply a workflow mailing list change. If queued contacts would be removed from the
    workflow due to the change of mailing list, Loops returns with `\"status\": \"queuedContactsFound\"`
    instead of applying the change. Retry with `queuedContactPolicy: \"discard\"` to apply the change
    and discard those contacts.

    Args:
        workflow_id (str):
        body (ChangeWorkflowMailingListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowFailureResponse | WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse
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
    body: ChangeWorkflowMailingListRequest,
) -> Response[Any | WorkflowFailureResponse | WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse]:
    r"""Change workflow mailing list

     Dry run or apply a workflow mailing list change. If queued contacts would be removed from the
    workflow due to the change of mailing list, Loops returns with `\"status\": \"queuedContactsFound\"`
    instead of applying the change. Retry with `queuedContactPolicy: \"discard\"` to apply the change
    and discard those contacts.

    Args:
        workflow_id (str):
        body (ChangeWorkflowMailingListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | WorkflowFailureResponse | WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse]
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
    body: ChangeWorkflowMailingListRequest,
) -> Any | WorkflowFailureResponse | WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse | None:
    r"""Change workflow mailing list

     Dry run or apply a workflow mailing list change. If queued contacts would be removed from the
    workflow due to the change of mailing list, Loops returns with `\"status\": \"queuedContactsFound\"`
    instead of applying the change. Retry with `queuedContactPolicy: \"discard\"` to apply the change
    and discard those contacts.

    Args:
        workflow_id (str):
        body (ChangeWorkflowMailingListRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | WorkflowFailureResponse | WorkflowMailingListPreview | WorkflowMailingListUpdatedResponse
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
