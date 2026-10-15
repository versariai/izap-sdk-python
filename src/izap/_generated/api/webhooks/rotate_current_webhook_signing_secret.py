from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.webhook_endpoint_created import WebhookEndpointCreated
from ...types import UNSET, Response, Unset


def _get_kwargs(
    endpoint_id: UUID,
    *,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/webhook-endpoints/{endpoint_id}/rotate-secret".format(
            endpoint_id=quote(str(endpoint_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhookEndpointCreated | None:
    if response.status_code == 200:
        response_200 = WebhookEndpointCreated.from_dict(response.json())

        return response_200

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
    endpoint_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[WebhookEndpointCreated]:
    """Rotate an endpoint's signing secret

     Issues a new signing secret and returns it. **The previous secret stops verifying immediately** and
    there is no overlap window, so deploy the new one to your receiver before rotating. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        endpoint_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookEndpointCreated]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
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
    business_id: str | Unset = UNSET,
) -> WebhookEndpointCreated | None:
    """Rotate an endpoint's signing secret

     Issues a new signing secret and returns it. **The previous secret stops verifying immediately** and
    there is no overlap window, so deploy the new one to your receiver before rotating. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        endpoint_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookEndpointCreated
    """

    return sync_detailed(
        endpoint_id=endpoint_id,
        client=client,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    endpoint_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[WebhookEndpointCreated]:
    """Rotate an endpoint's signing secret

     Issues a new signing secret and returns it. **The previous secret stops verifying immediately** and
    there is no overlap window, so deploy the new one to your receiver before rotating. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        endpoint_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookEndpointCreated]
    """

    kwargs = _get_kwargs(
        endpoint_id=endpoint_id,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> WebhookEndpointCreated | None:
    """Rotate an endpoint's signing secret

     Issues a new signing secret and returns it. **The previous secret stops verifying immediately** and
    there is no overlap window, so deploy the new one to your receiver before rotating. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        endpoint_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookEndpointCreated
    """

    return (
        await asyncio_detailed(
            endpoint_id=endpoint_id,
            client=client,
            business_id=business_id,
        )
    ).parsed
