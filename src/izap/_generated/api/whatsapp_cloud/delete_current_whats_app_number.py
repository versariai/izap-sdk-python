from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    number_id: str,
    *,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/businesses/whatsapp_cloud/numbers/{number_id}".format(
            number_id=quote(str(number_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    number_id: str,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[Any]:
    """Remove a number from iZap

     Disconnects a WhatsApp Cloud number from the platform: it stops reaching any assistant and its
    stored credentials are discarded. The number itself stays registered at Meta and can be connected
    again later. Conversation history is kept. The business is taken from the `business-id` header
    rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        number_id=number_id,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    number_id: str,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[Any]:
    """Remove a number from iZap

     Disconnects a WhatsApp Cloud number from the platform: it stops reaching any assistant and its
    stored credentials are discarded. The number itself stays registered at Meta and can be connected
    again later. Conversation history is kept. The business is taken from the `business-id` header
    rather than the URL; the path-scoped form of this operation is deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        number_id=number_id,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
