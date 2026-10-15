from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_catalog_request import SendCatalogRequest
from ...models.send_catalog_response import SendCatalogResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SendCatalogRequest,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/businesses/whatsapp_cloud/send_catalog",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SendCatalogResponse | None:
    if response.status_code == 200:
        response_200 = SendCatalogResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SendCatalogResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SendCatalogRequest,
    business_id: str | Unset = UNSET,
) -> Response[SendCatalogResponse]:
    """Send the product catalog

     Sends an interactive catalog message to a WhatsApp recipient. The catalog is the one linked to the
    business's WhatsApp Business Account in Meta's Commerce Manager. The business is taken from the
    `business-id` header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (SendCatalogRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendCatalogResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SendCatalogRequest,
    business_id: str | Unset = UNSET,
) -> SendCatalogResponse | None:
    """Send the product catalog

     Sends an interactive catalog message to a WhatsApp recipient. The catalog is the one linked to the
    business's WhatsApp Business Account in Meta's Commerce Manager. The business is taken from the
    `business-id` header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (SendCatalogRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendCatalogResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SendCatalogRequest,
    business_id: str | Unset = UNSET,
) -> Response[SendCatalogResponse]:
    """Send the product catalog

     Sends an interactive catalog message to a WhatsApp recipient. The catalog is the one linked to the
    business's WhatsApp Business Account in Meta's Commerce Manager. The business is taken from the
    `business-id` header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (SendCatalogRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendCatalogResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SendCatalogRequest,
    business_id: str | Unset = UNSET,
) -> SendCatalogResponse | None:
    """Send the product catalog

     Sends an interactive catalog message to a WhatsApp recipient. The catalog is the one linked to the
    business's WhatsApp Business Account in Meta's Commerce Manager. The business is taken from the
    `business-id` header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (SendCatalogRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendCatalogResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
