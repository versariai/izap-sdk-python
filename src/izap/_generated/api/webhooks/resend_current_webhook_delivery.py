from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resend_current_webhook_delivery_response_resend_delivery_api_v1_webhook_endpoints_deliveries_delivery_id_resend_post import (
    ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    delivery_id: UUID,
    *,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/webhook-endpoints/deliveries/{delivery_id}/resend".format(
            delivery_id=quote(str(delivery_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost | None:
    if response.status_code == 202:
        response_202 = ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost.from_dict(
            response.json()
        )

        return response_202

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    delivery_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost]:
    """Resend a delivery

     Queues a past delivery to be sent again. The stored request body is replayed byte for byte, so the
    original signature still verifies. Responds `202` once queued; the send itself happens in the
    background. The business is taken from the `business-id` header rather than the URL; the path-scoped
    form of this operation is deprecated.

    Args:
        delivery_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost]
    """

    kwargs = _get_kwargs(
        delivery_id=delivery_id,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    delivery_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost | None:
    """Resend a delivery

     Queues a past delivery to be sent again. The stored request body is replayed byte for byte, so the
    original signature still verifies. Responds `202` once queued; the send itself happens in the
    background. The business is taken from the `business-id` header rather than the URL; the path-scoped
    form of this operation is deprecated.

    Args:
        delivery_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost
    """

    return sync_detailed(
        delivery_id=delivery_id,
        client=client,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    delivery_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost]:
    """Resend a delivery

     Queues a past delivery to be sent again. The stored request body is replayed byte for byte, so the
    original signature still verifies. Responds `202` once queued; the send itself happens in the
    background. The business is taken from the `business-id` header rather than the URL; the path-scoped
    form of this operation is deprecated.

    Args:
        delivery_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost]
    """

    kwargs = _get_kwargs(
        delivery_id=delivery_id,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    delivery_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost | None:
    """Resend a delivery

     Queues a past delivery to be sent again. The stored request body is replayed byte for byte, so the
    original signature still verifies. Responds `202` once queued; the send itself happens in the
    background. The business is taken from the `business-id` header rather than the URL; the path-scoped
    form of this operation is deprecated.

    Args:
        delivery_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResendCurrentWebhookDeliveryResponseResendDeliveryApiV1WebhookEndpointsDeliveriesDeliveryIdResendPost
    """

    return (
        await asyncio_detailed(
            delivery_id=delivery_id,
            client=client,
            business_id=business_id,
        )
    ).parsed
