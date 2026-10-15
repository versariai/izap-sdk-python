from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook_endpoint_out import WebhookEndpointOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/webhook-endpoints",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> list[WebhookEndpointOut] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WebhookEndpointOut.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[list[WebhookEndpointOut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[list[WebhookEndpointOut]]:
    """List webhook endpoints

     Returns the webhook endpoints registered for the business, newest first. Signing secrets are never
    included — a secret is readable only in the response that creates or rotates it. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[WebhookEndpointOut]]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> list[WebhookEndpointOut] | None:
    """List webhook endpoints

     Returns the webhook endpoints registered for the business, newest first. Signing secrets are never
    included — a secret is readable only in the response that creates or rotates it. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[WebhookEndpointOut]
    """

    return sync_detailed(
        client=client,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[list[WebhookEndpointOut]]:
    """List webhook endpoints

     Returns the webhook endpoints registered for the business, newest first. Signing secrets are never
    included — a secret is readable only in the response that creates or rotates it. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[WebhookEndpointOut]]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> list[WebhookEndpointOut] | None:
    """List webhook endpoints

     Returns the webhook endpoints registered for the business, newest first. Signing secrets are never
    included — a secret is readable only in the response that creates or rotates it. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[WebhookEndpointOut]
    """

    return (
        await asyncio_detailed(
            client=client,
            business_id=business_id,
        )
    ).parsed
