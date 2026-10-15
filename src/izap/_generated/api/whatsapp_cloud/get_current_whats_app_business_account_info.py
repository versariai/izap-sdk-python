from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.whats_app_waba_info_out import WhatsAppWabaInfoOut
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
        "url": "/api/v1/businesses/whatsapp_cloud/waba_info",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WhatsAppWabaInfoOut | None:
    if response.status_code == 200:
        response_200 = WhatsAppWabaInfoOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WhatsAppWabaInfoOut]:
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
) -> Response[WhatsAppWabaInfoOut]:
    """Read WhatsApp Business Account details

     Fetches business-verification details for the WhatsApp Business Account from Meta. The values are
    account-level, so they are the same for every number under the business. The business is taken from
    the `business-id` header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppWabaInfoOut]
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
) -> WhatsAppWabaInfoOut | None:
    """Read WhatsApp Business Account details

     Fetches business-verification details for the WhatsApp Business Account from Meta. The values are
    account-level, so they are the same for every number under the business. The business is taken from
    the `business-id` header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppWabaInfoOut
    """

    return sync_detailed(
        client=client,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppWabaInfoOut]:
    """Read WhatsApp Business Account details

     Fetches business-verification details for the WhatsApp Business Account from Meta. The values are
    account-level, so they are the same for every number under the business. The business is taken from
    the `business-id` header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppWabaInfoOut]
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
) -> WhatsAppWabaInfoOut | None:
    """Read WhatsApp Business Account details

     Fetches business-verification details for the WhatsApp Business Account from Meta. The values are
    account-level, so they are the same for every number under the business. The business is taken from
    the `business-id` header rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppWabaInfoOut
    """

    return (
        await asyncio_detailed(
            client=client,
            business_id=business_id,
        )
    ).parsed
