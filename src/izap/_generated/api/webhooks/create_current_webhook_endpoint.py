from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook_endpoint_create import WebhookEndpointCreate
from ...models.webhook_endpoint_created import WebhookEndpointCreated
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: WebhookEndpointCreate,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/webhook-endpoints",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhookEndpointCreated | None:
    if response.status_code == 201:
        response_201 = WebhookEndpointCreated.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WebhookEndpointCreated]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointCreate,
    business_id: str | Unset = UNSET,
) -> Response[WebhookEndpointCreated]:
    """Register a webhook endpoint

     Registers a URL to receive signed event deliveries and returns it along with its signing secret.
    **The secret is shown exactly once** — store it now; afterwards you can only rotate it. The URL must
    be a publicly resolvable HTTPS address, and every entry in `subscribed_events` must be a known event
    type. Requires a plan that includes event webhooks. The business is taken from the `business-id`
    header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (WebhookEndpointCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookEndpointCreated]
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
    body: WebhookEndpointCreate,
    business_id: str | Unset = UNSET,
) -> WebhookEndpointCreated | None:
    """Register a webhook endpoint

     Registers a URL to receive signed event deliveries and returns it along with its signing secret.
    **The secret is shown exactly once** — store it now; afterwards you can only rotate it. The URL must
    be a publicly resolvable HTTPS address, and every entry in `subscribed_events` must be a known event
    type. Requires a plan that includes event webhooks. The business is taken from the `business-id`
    header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (WebhookEndpointCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookEndpointCreated
    """

    return sync_detailed(
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookEndpointCreate,
    business_id: str | Unset = UNSET,
) -> Response[WebhookEndpointCreated]:
    """Register a webhook endpoint

     Registers a URL to receive signed event deliveries and returns it along with its signing secret.
    **The secret is shown exactly once** — store it now; afterwards you can only rotate it. The URL must
    be a publicly resolvable HTTPS address, and every entry in `subscribed_events` must be a known event
    type. Requires a plan that includes event webhooks. The business is taken from the `business-id`
    header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (WebhookEndpointCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookEndpointCreated]
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
    body: WebhookEndpointCreate,
    business_id: str | Unset = UNSET,
) -> WebhookEndpointCreated | None:
    """Register a webhook endpoint

     Registers a URL to receive signed event deliveries and returns it along with its signing secret.
    **The secret is shown exactly once** — store it now; afterwards you can only rotate it. The URL must
    be a publicly resolvable HTTPS address, and every entry in `subscribed_events` must be a known event
    type. Requires a plan that includes event webhooks. The business is taken from the `business-id`
    header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (WebhookEndpointCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookEndpointCreated
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
