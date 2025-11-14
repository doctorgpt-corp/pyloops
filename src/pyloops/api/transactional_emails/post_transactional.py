from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.idempotency_key_failure_response import IdempotencyKeyFailureResponse
from ...models.transactional_failure_2_response import TransactionalFailure2Response
from ...models.transactional_failure_3_response import TransactionalFailure3Response
from ...models.transactional_failure_4_response import TransactionalFailure4Response
from ...models.transactional_failure_5_response import TransactionalFailure5Response
from ...models.transactional_failure_response import TransactionalFailureResponse
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
        "url": "/transactional",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | IdempotencyKeyFailureResponse
    | TransactionalFailure2Response
    | TransactionalFailure3Response
    | TransactionalFailure4Response
    | TransactionalFailure5Response
    | TransactionalFailureResponse
    | TransactionalFailure3Response
    | TransactionalSuccessResponse
    | None
):
    if response.status_code == 200:
        response_200 = TransactionalSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:

        def _parse_response_400(
            data: object,
        ) -> (
            TransactionalFailure2Response
            | TransactionalFailure3Response
            | TransactionalFailure4Response
            | TransactionalFailure5Response
            | TransactionalFailureResponse
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_0 = TransactionalFailureResponse.from_dict(data)

                return response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_1 = TransactionalFailure2Response.from_dict(data)

                return response_400_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_2 = TransactionalFailure3Response.from_dict(data)

                return response_400_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_3 = TransactionalFailure4Response.from_dict(data)

                return response_400_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_4 = TransactionalFailure5Response.from_dict(data)

            return response_400_type_4

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = TransactionalFailure3Response.from_dict(response.json())

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
    | IdempotencyKeyFailureResponse
    | TransactionalFailure2Response
    | TransactionalFailure3Response
    | TransactionalFailure4Response
    | TransactionalFailure5Response
    | TransactionalFailureResponse
    | TransactionalFailure3Response
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
    | IdempotencyKeyFailureResponse
    | TransactionalFailure2Response
    | TransactionalFailure3Response
    | TransactionalFailure4Response
    | TransactionalFailure5Response
    | TransactionalFailureResponse
    | TransactionalFailure3Response
    | TransactionalSuccessResponse
]:
    """Send a transactional email

     Send a transactional email to a contact.<br>Please [email us](mailto:help@loops.so) to enable
    attachments on your account before using them with the API.

    Args:
        idempotency_key (str | Unset):
        body (TransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IdempotencyKeyFailureResponse | TransactionalFailure2Response | TransactionalFailure3Response | TransactionalFailure4Response | TransactionalFailure5Response | TransactionalFailureResponse | TransactionalFailure3Response | TransactionalSuccessResponse]
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
    | IdempotencyKeyFailureResponse
    | TransactionalFailure2Response
    | TransactionalFailure3Response
    | TransactionalFailure4Response
    | TransactionalFailure5Response
    | TransactionalFailureResponse
    | TransactionalFailure3Response
    | TransactionalSuccessResponse
    | None
):
    """Send a transactional email

     Send a transactional email to a contact.<br>Please [email us](mailto:help@loops.so) to enable
    attachments on your account before using them with the API.

    Args:
        idempotency_key (str | Unset):
        body (TransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IdempotencyKeyFailureResponse | TransactionalFailure2Response | TransactionalFailure3Response | TransactionalFailure4Response | TransactionalFailure5Response | TransactionalFailureResponse | TransactionalFailure3Response | TransactionalSuccessResponse
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
    | IdempotencyKeyFailureResponse
    | TransactionalFailure2Response
    | TransactionalFailure3Response
    | TransactionalFailure4Response
    | TransactionalFailure5Response
    | TransactionalFailureResponse
    | TransactionalFailure3Response
    | TransactionalSuccessResponse
]:
    """Send a transactional email

     Send a transactional email to a contact.<br>Please [email us](mailto:help@loops.so) to enable
    attachments on your account before using them with the API.

    Args:
        idempotency_key (str | Unset):
        body (TransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IdempotencyKeyFailureResponse | TransactionalFailure2Response | TransactionalFailure3Response | TransactionalFailure4Response | TransactionalFailure5Response | TransactionalFailureResponse | TransactionalFailure3Response | TransactionalSuccessResponse]
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
    | IdempotencyKeyFailureResponse
    | TransactionalFailure2Response
    | TransactionalFailure3Response
    | TransactionalFailure4Response
    | TransactionalFailure5Response
    | TransactionalFailureResponse
    | TransactionalFailure3Response
    | TransactionalSuccessResponse
    | None
):
    """Send a transactional email

     Send a transactional email to a contact.<br>Please [email us](mailto:help@loops.so) to enable
    attachments on your account before using them with the API.

    Args:
        idempotency_key (str | Unset):
        body (TransactionalRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IdempotencyKeyFailureResponse | TransactionalFailure2Response | TransactionalFailure3Response | TransactionalFailure4Response | TransactionalFailure5Response | TransactionalFailureResponse | TransactionalFailure3Response | TransactionalSuccessResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
