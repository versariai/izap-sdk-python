from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook_endpoint_out import WebhookEndpointOut
from ...models.webhook_endpoint_update import WebhookEndpointUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    endpoint_id: UUID,
    *,
    body: WebhookEndpointUpdate,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/webhook-endpoints/{endpoint_id}".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhookEndpointOut | None:
    if response.status_code == 200:
        response_200 = WebhookEndpointOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WebhookEndpointOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    endpoint_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointUpdate,
    business_id: str | Unset = UNSET,
) -> Response[WebhookEndpointOut]:
    """Update a webhook endpoint

     Changes an endpoint's URL, label, subscribed events or enabled state; omitted fields are left alone.
    Re-enabling an endpoint also clears the consecutive-failure streak that auto-disabled it, so a
    single later failure will not disable it again. The business is taken from the `business-id` header
    rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        endpoint_id (UUID):
        business_id (str | Unset):
        body (WebhookEndpointUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookEndpointOut]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        body=body,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointUpdate,
    business_id: str | Unset = UNSET,
) -> WebhookEndpointOut | None:
    """Update a webhook endpoint

     Changes an endpoint's URL, label, subscribed events or enabled state; omitted fields are left alone.
    Re-enabling an endpoint also clears the consecutive-failure streak that auto-disabled it, so a
    single later failure will not disable it again. The business is taken from the `business-id` header
    rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        endpoint_id (UUID):
        business_id (str | Unset):
        body (WebhookEndpointUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookEndpointOut
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    endpoint_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointUpdate,
    business_id: str | Unset = UNSET,
) -> Response[WebhookEndpointOut]:
    """Update a webhook endpoint

     Changes an endpoint's URL, label, subscribed events or enabled state; omitted fields are left alone.
    Re-enabling an endpoint also clears the consecutive-failure streak that auto-disabled it, so a
    single later failure will not disable it again. The business is taken from the `business-id` header
    rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        endpoint_id (UUID):
        business_id (str | Unset):
        body (WebhookEndpointUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookEndpointOut]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        body=body,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointUpdate,
    business_id: str | Unset = UNSET,
) -> WebhookEndpointOut | None:
    """Update a webhook endpoint

     Changes an endpoint's URL, label, subscribed events or enabled state; omitted fields are left alone.
    Re-enabling an endpoint also clears the consecutive-failure streak that auto-disabled it, so a
    single later failure will not disable it again. The business is taken from the `business-id` header
    rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        endpoint_id (UUID):
        business_id (str | Unset):
        body (WebhookEndpointUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookEndpointOut
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
