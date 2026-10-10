from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachments_not_enabled import AttachmentsNotEnabled
from ...models.email_not_sendable import EmailNotSendable
from ...models.general_error import GeneralError
from ...models.idempotency_key_failure_response import IdempotencyKeyFailureResponse
from ...models.invalid_data_variables import InvalidDataVariables
from ...models.invalid_request_or_email import InvalidRequestOrEmail
from ...models.transactional_request import TransactionalRequest
from ...models.transactional_success_response import TransactionalSuccessResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TransactionalRequest,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/transactional",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AttachmentsNotEnabled
    | EmailNotSendable
    | GeneralError
    | InvalidDataVariables
    | InvalidRequestOrEmail
    | IdempotencyKeyFailureResponse
    | InvalidRequestOrEmail
    | TransactionalSuccessResponse
    | None
):
    if response.status_code == 200:
        response_200 = TransactionalSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(
            data: object,
        ) -> AttachmentsNotEnabled | EmailNotSendable | GeneralError | InvalidDataVariables | InvalidRequestOrEmail:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_0 = GeneralError.from_dict(data)

                return response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_1 = AttachmentsNotEnabled.from_dict(data)

                return response_400_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_2 = InvalidRequestOrEmail.from_dict(data)

                return response_400_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_3 = EmailNotSendable.from_dict(data)

                return response_400_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_4 = InvalidDataVariables.from_dict(data)

            return response_400_type_4

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = InvalidRequestOrEmail.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 409:
        response_409 = IdempotencyKeyFailureResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AttachmentsNotEnabled
    | EmailNotSendable
    | GeneralError
    | InvalidDataVariables
    | InvalidRequestOrEmail
    | IdempotencyKeyFailureResponse
    | InvalidRequestOrEmail
    | TransactionalSuccessResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TransactionalRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    Any
    | AttachmentsNotEnabled
    | EmailNotSendable
    | GeneralError
    | InvalidDataVariables
    | InvalidRequestOrEmail
    | IdempotencyKeyFailureResponse
    | InvalidRequestOrEmail
    | TransactionalSuccessResponse
]:
    """Send a transactional email

     Send a transactional email to a contact.<br>Please [email us](mailto:help@loops.so) to enable
    attachments on your account before using them with the API.

    To set dynamic Subject, From, Reply to, CC, BCC email header fields, add data variables to those
    fields in the editor, then include data for each variable in the API request. Read our transactional
    email guide for more details.

    Args:
        idempotency_key (str | Unset):
        body (TransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentsNotEnabled | EmailNotSendable | GeneralError | InvalidDataVariables | InvalidRequestOrEmail | IdempotencyKeyFailureResponse | InvalidRequestOrEmail | TransactionalSuccessResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: TransactionalRequest,
    idempotency_key: str | Unset = UNSET,
) -> (
    Any
    | AttachmentsNotEnabled
    | EmailNotSendable
    | GeneralError
    | InvalidDataVariables
    | InvalidRequestOrEmail
    | IdempotencyKeyFailureResponse
    | InvalidRequestOrEmail
    | TransactionalSuccessResponse
    | None
):
    """Send a transactional email

     Send a transactional email to a contact.<br>Please [email us](mailto:help@loops.so) to enable
    attachments on your account before using them with the API.

    To set dynamic Subject, From, Reply to, CC, BCC email header fields, add data variables to those
    fields in the editor, then include data for each variable in the API request. Read our transactional
    email guide for more details.

    Args:
        idempotency_key (str | Unset):
        body (TransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentsNotEnabled | EmailNotSendable | GeneralError | InvalidDataVariables | InvalidRequestOrEmail | IdempotencyKeyFailureResponse | InvalidRequestOrEmail | TransactionalSuccessResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TransactionalRequest,
    idempotency_key: str | Unset = UNSET,
) -> Response[
    Any
    | AttachmentsNotEnabled
    | EmailNotSendable
    | GeneralError
    | InvalidDataVariables
    | InvalidRequestOrEmail
    | IdempotencyKeyFailureResponse
    | InvalidRequestOrEmail
    | TransactionalSuccessResponse
]:
    """Send a transactional email

     Send a transactional email to a contact.<br>Please [email us](mailto:help@loops.so) to enable
    attachments on your account before using them with the API.

    To set dynamic Subject, From, Reply to, CC, BCC email header fields, add data variables to those
    fields in the editor, then include data for each variable in the API request. Read our transactional
    email guide for more details.

    Args:
        idempotency_key (str | Unset):
        body (TransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AttachmentsNotEnabled | EmailNotSendable | GeneralError | InvalidDataVariables | InvalidRequestOrEmail | IdempotencyKeyFailureResponse | InvalidRequestOrEmail | TransactionalSuccessResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TransactionalRequest,
    idempotency_key: str | Unset = UNSET,
) -> (
    Any
    | AttachmentsNotEnabled
    | EmailNotSendable
    | GeneralError
    | InvalidDataVariables
    | InvalidRequestOrEmail
    | IdempotencyKeyFailureResponse
    | InvalidRequestOrEmail
    | TransactionalSuccessResponse
    | None
):
    """Send a transactional email

     Send a transactional email to a contact.<br>Please [email us](mailto:help@loops.so) to enable
    attachments on your account before using them with the API.

    To set dynamic Subject, From, Reply to, CC, BCC email header fields, add data variables to those
    fields in the editor, then include data for each variable in the API request. Read our transactional
    email guide for more details.

    Args:
        idempotency_key (str | Unset):
        body (TransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AttachmentsNotEnabled | EmailNotSendable | GeneralError | InvalidDataVariables | InvalidRequestOrEmail | IdempotencyKeyFailureResponse | InvalidRequestOrEmail | TransactionalSuccessResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
