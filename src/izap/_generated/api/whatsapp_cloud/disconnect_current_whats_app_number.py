from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.whats_app_number_disconnect_in import WhatsAppNumberDisconnectIn
from ...models.whats_app_number_disconnect_out import WhatsAppNumberDisconnectOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    number_id: str,
    *,
    body: None | Unset | WhatsAppNumberDisconnectIn = UNSET,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/businesses/whatsapp_cloud/numbers/{number_id}/disconnect".format(
            number_id=quote(str(number_id), safe=""),
        ),
    }

    if isinstance(body, WhatsAppNumberDisconnectIn):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WhatsAppNumberDisconnectOut | None:
    if response.status_code == 200:
        response_200 = WhatsAppNumberDisconnectOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WhatsAppNumberDisconnectOut]:
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
    body: None | Unset | WhatsAppNumberDisconnectIn = UNSET,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppNumberDisconnectOut]:
    """Revoke iZap's access to a number at Meta

     Revokes iZap's access to the number at Meta and removes it from the platform. Unlike
    `deleteCurrentWhatsAppNumber`, which only disconnects the number from iZap, this also unsubscribes
    from the WhatsApp Business Account's webhooks at Meta and optionally deregisters the number from
    Cloud API entirely (`deregister`). Reconnecting requires a full Embedded Signup run. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):
        body (None | Unset | WhatsAppNumberDisconnectIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppNumberDisconnectOut]
    """

    kwargs = _get_kwargs(
        number_id=number_id,
        body=body,
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
    body: None | Unset | WhatsAppNumberDisconnectIn = UNSET,
    business_id: str | Unset = UNSET,
) -> WhatsAppNumberDisconnectOut | None:
    """Revoke iZap's access to a number at Meta

     Revokes iZap's access to the number at Meta and removes it from the platform. Unlike
    `deleteCurrentWhatsAppNumber`, which only disconnects the number from iZap, this also unsubscribes
    from the WhatsApp Business Account's webhooks at Meta and optionally deregisters the number from
    Cloud API entirely (`deregister`). Reconnecting requires a full Embedded Signup run. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):
        body (None | Unset | WhatsAppNumberDisconnectIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppNumberDisconnectOut
    """

    return sync_detailed(
        number_id=number_id,
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    number_id: str,
    *,
    client: AuthenticatedClient,
    body: None | Unset | WhatsAppNumberDisconnectIn = UNSET,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppNumberDisconnectOut]:
    """Revoke iZap's access to a number at Meta

     Revokes iZap's access to the number at Meta and removes it from the platform. Unlike
    `deleteCurrentWhatsAppNumber`, which only disconnects the number from iZap, this also unsubscribes
    from the WhatsApp Business Account's webhooks at Meta and optionally deregisters the number from
    Cloud API entirely (`deregister`). Reconnecting requires a full Embedded Signup run. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):
        body (None | Unset | WhatsAppNumberDisconnectIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppNumberDisconnectOut]
    """

    kwargs = _get_kwargs(
        number_id=number_id,
        body=body,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    number_id: str,
    *,
    client: AuthenticatedClient,
    body: None | Unset | WhatsAppNumberDisconnectIn = UNSET,
    business_id: str | Unset = UNSET,
) -> WhatsAppNumberDisconnectOut | None:
    """Revoke iZap's access to a number at Meta

     Revokes iZap's access to the number at Meta and removes it from the platform. Unlike
    `deleteCurrentWhatsAppNumber`, which only disconnects the number from iZap, this also unsubscribes
    from the WhatsApp Business Account's webhooks at Meta and optionally deregisters the number from
    Cloud API entirely (`deregister`). Reconnecting requires a full Embedded Signup run. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):
        body (None | Unset | WhatsAppNumberDisconnectIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppNumberDisconnectOut
    """

    return (
        await asyncio_detailed(
            number_id=number_id,
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
