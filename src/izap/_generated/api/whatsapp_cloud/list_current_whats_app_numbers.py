from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.whats_app_numbers_out import WhatsAppNumbersOut
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
        "url": "/api/v1/businesses/whatsapp_cloud/numbers",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WhatsAppNumbersOut | None:
    if response.status_code == 200:
        response_200 = WhatsAppNumbersOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WhatsAppNumbersOut]:
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
) -> Response[WhatsAppNumbersOut]:
    """List WhatsApp Cloud numbers

     Returns the WhatsApp Cloud numbers connected to the business, along with the assistant bound to
    each. The business is taken from the `business-id` header rather than the URL; the path-scoped form
    of this operation is deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppNumbersOut]
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
) -> WhatsAppNumbersOut | None:
    """List WhatsApp Cloud numbers

     Returns the WhatsApp Cloud numbers connected to the business, along with the assistant bound to
    each. The business is taken from the `business-id` header rather than the URL; the path-scoped form
    of this operation is deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppNumbersOut
    """

    return sync_detailed(
        client=client,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppNumbersOut]:
    """List WhatsApp Cloud numbers

     Returns the WhatsApp Cloud numbers connected to the business, along with the assistant bound to
    each. The business is taken from the `business-id` header rather than the URL; the path-scoped form
    of this operation is deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppNumbersOut]
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
) -> WhatsAppNumbersOut | None:
    """List WhatsApp Cloud numbers

     Returns the WhatsApp Cloud numbers connected to the business, along with the assistant bound to
    each. The business is taken from the `business-id` header rather than the URL; the path-scoped form
    of this operation is deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppNumbersOut
    """

    return (
        await asyncio_detailed(
            client=client,
            business_id=business_id,
        )
    ).parsed
