from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_footer_body import CreateFooterBody
from ...models.footer_failure_response import FooterFailureResponse
from ...models.footer_with_variants import FooterWithVariants
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateFooterBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/footers",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | FooterFailureResponse | FooterWithVariants | None:
    if response.status_code == 201:
        response_201 = FooterWithVariants.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = FooterFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | FooterFailureResponse | FooterWithVariants]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateFooterBody | Unset = UNSET,
) -> Response[Any | FooterFailureResponse | FooterWithVariants]:
    """Create a footer

     Create a footer with one variant. The variant starts with an unpublished draft that has the company
    name, company address and unsubscribe link. Emails cannot use the footer until you publish the
    variant.

    Args:
        body (CreateFooterBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FooterFailureResponse | FooterWithVariants]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateFooterBody | Unset = UNSET,
) -> Any | FooterFailureResponse | FooterWithVariants | None:
    """Create a footer

     Create a footer with one variant. The variant starts with an unpublished draft that has the company
    name, company address and unsubscribe link. Emails cannot use the footer until you publish the
    variant.

    Args:
        body (CreateFooterBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FooterFailureResponse | FooterWithVariants
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateFooterBody | Unset = UNSET,
) -> Response[Any | FooterFailureResponse | FooterWithVariants]:
    """Create a footer

     Create a footer with one variant. The variant starts with an unpublished draft that has the company
    name, company address and unsubscribe link. Emails cannot use the footer until you publish the
    variant.

    Args:
        body (CreateFooterBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FooterFailureResponse | FooterWithVariants]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateFooterBody | Unset = UNSET,
) -> Any | FooterFailureResponse | FooterWithVariants | None:
    """Create a footer

     Create a footer with one variant. The variant starts with an unpublished draft that has the company
    name, company address and unsubscribe link. Emails cannot use the footer until you publish the
    variant.

    Args:
        body (CreateFooterBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FooterFailureResponse | FooterWithVariants
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
