from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.footer_failure_response import FooterFailureResponse
from ...models.footer_variant import FooterVariant
from ...models.publish_footer_variant_body import PublishFooterVariantBody
from ...types import Response


def _get_kwargs(
    footer_id: str,
    variant_id: str,
    *,
    body: PublishFooterVariantBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/footers/{footer_id}/variants/{variant_id}/publish".format(
            footer_id=quote(str(footer_id), safe=""),
            variant_id=quote(str(variant_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | FooterFailureResponse | FooterVariant | None:
    if response.status_code == 200:
        response_200 = FooterVariant.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FooterFailureResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = FooterFailureResponse.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 409:
        response_409 = FooterFailureResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = FooterFailureResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | FooterFailureResponse | FooterVariant]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    footer_id: str,
    variant_id: str,
    *,
    client: AuthenticatedClient,
    body: PublishFooterVariantBody,
) -> Response[Any | FooterFailureResponse | FooterVariant]:
    """Publish a footer variant

     Publish the variant's draft LMX content, to replace the current published LMX content. Emails that
    use the footer will immediately use the newly published content. The draft must have
    `{system.company_name}` and `{system.company_address}` in the text, and `{system.unsubscribe_link}`
    as the URL of a link or button.

    Args:
        footer_id (str):
        variant_id (str):
        body (PublishFooterVariantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FooterFailureResponse | FooterVariant]
    """

    kwargs = _get_kwargs(
        footer_id=footer_id,
        variant_id=variant_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    footer_id: str,
    variant_id: str,
    *,
    client: AuthenticatedClient,
    body: PublishFooterVariantBody,
) -> Any | FooterFailureResponse | FooterVariant | None:
    """Publish a footer variant

     Publish the variant's draft LMX content, to replace the current published LMX content. Emails that
    use the footer will immediately use the newly published content. The draft must have
    `{system.company_name}` and `{system.company_address}` in the text, and `{system.unsubscribe_link}`
    as the URL of a link or button.

    Args:
        footer_id (str):
        variant_id (str):
        body (PublishFooterVariantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FooterFailureResponse | FooterVariant
    """

    return sync_detailed(
        footer_id=footer_id,
        variant_id=variant_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    footer_id: str,
    variant_id: str,
    *,
    client: AuthenticatedClient,
    body: PublishFooterVariantBody,
) -> Response[Any | FooterFailureResponse | FooterVariant]:
    """Publish a footer variant

     Publish the variant's draft LMX content, to replace the current published LMX content. Emails that
    use the footer will immediately use the newly published content. The draft must have
    `{system.company_name}` and `{system.company_address}` in the text, and `{system.unsubscribe_link}`
    as the URL of a link or button.

    Args:
        footer_id (str):
        variant_id (str):
        body (PublishFooterVariantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FooterFailureResponse | FooterVariant]
    """

    kwargs = _get_kwargs(
        footer_id=footer_id,
        variant_id=variant_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    footer_id: str,
    variant_id: str,
    *,
    client: AuthenticatedClient,
    body: PublishFooterVariantBody,
) -> Any | FooterFailureResponse | FooterVariant | None:
    """Publish a footer variant

     Publish the variant's draft LMX content, to replace the current published LMX content. Emails that
    use the footer will immediately use the newly published content. The draft must have
    `{system.company_name}` and `{system.company_address}` in the text, and `{system.unsubscribe_link}`
    as the URL of a link or button.

    Args:
        footer_id (str):
        variant_id (str):
        body (PublishFooterVariantBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx2.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FooterFailureResponse | FooterVariant
    """

    return (
        await asyncio_detailed(
            footer_id=footer_id,
            variant_id=variant_id,
            client=client,
            body=body,
        )
    ).parsed
