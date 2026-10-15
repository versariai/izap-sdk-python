from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.whats_app_phone_live_out import WhatsAppPhoneLiveOut
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
        "method": "get",
        "url": "/api/v1/businesses/whatsapp_cloud/numbers/{number_id}/live".format(
            number_id=quote(str(number_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WhatsAppPhoneLiveOut | None:
    if response.status_code == 200:
        response_200 = WhatsAppPhoneLiveOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WhatsAppPhoneLiveOut]:
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
) -> Response[WhatsAppPhoneLiveOut]:
    """Read a number's live status at Meta

     Fetches the number's current quality rating, verification state and status directly from Meta. Read-
    only. The business is taken from the `business-id` header rather than the URL; the path-scoped form
    of this operation is deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppPhoneLiveOut]
    """

    kwargs = _get_kwargs(
        number_id=number_id,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    number_id: str,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> WhatsAppPhoneLiveOut | None:
    """Read a number's live status at Meta

     Fetches the number's current quality rating, verification state and status directly from Meta. Read-
    only. The business is taken from the `business-id` header rather than the URL; the path-scoped form
    of this operation is deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppPhoneLiveOut
    """

    return sync_detailed(
        number_id=number_id,
        client=client,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    number_id: str,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppPhoneLiveOut]:
    """Read a number's live status at Meta

     Fetches the number's current quality rating, verification state and status directly from Meta. Read-
    only. The business is taken from the `business-id` header rather than the URL; the path-scoped form
    of this operation is deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppPhoneLiveOut]
    """

    kwargs = _get_kwargs(
        number_id=number_id,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    number_id: str,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> WhatsAppPhoneLiveOut | None:
    """Read a number's live status at Meta

     Fetches the number's current quality rating, verification state and status directly from Meta. Read-
    only. The business is taken from the `business-id` header rather than the URL; the path-scoped form
    of this operation is deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppPhoneLiveOut
    """

    return (
        await asyncio_detailed(
            number_id=number_id,
            client=client,
            business_id=business_id,
        )
    ).parsed
