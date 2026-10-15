from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_filter_mode_in import ContactFilterModeIn
from ...models.contact_filter_out import ContactFilterOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chatbot_id: UUID,
    *,
    body: ContactFilterModeIn,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/businesses/chatbots/{chatbot_id}/contact-filter".format(
            chatbot_id=quote(str(chatbot_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ContactFilterOut | None:
    if response.status_code == 200:
        response_200 = ContactFilterOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ContactFilterOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chatbot_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ContactFilterModeIn,
    business_id: str | Unset = UNSET,
) -> Response[ContactFilterOut]:
    """Set an assistant's contact filter mode

     Chooses who may trigger the assistant: `off` (everyone), `allowlist` (only the numbers on the
    allowlist) or `blocklist` (everyone except the numbers on the blocklist). Takes effect on the next
    inbound message. Both lists are kept when the mode changes; an empty allowlist silences the
    assistant for every contact.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):
        body (ContactFilterModeIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactFilterOut]
    """

    kwargs = _get_kwargs(
        chatbot_id=chatbot_id,
        body=body,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chatbot_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ContactFilterModeIn,
    business_id: str | Unset = UNSET,
) -> ContactFilterOut | None:
    """Set an assistant's contact filter mode

     Chooses who may trigger the assistant: `off` (everyone), `allowlist` (only the numbers on the
    allowlist) or `blocklist` (everyone except the numbers on the blocklist). Takes effect on the next
    inbound message. Both lists are kept when the mode changes; an empty allowlist silences the
    assistant for every contact.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):
        body (ContactFilterModeIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactFilterOut
    """

    return sync_detailed(
        chatbot_id=chatbot_id,
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    chatbot_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ContactFilterModeIn,
    business_id: str | Unset = UNSET,
) -> Response[ContactFilterOut]:
    """Set an assistant's contact filter mode

     Chooses who may trigger the assistant: `off` (everyone), `allowlist` (only the numbers on the
    allowlist) or `blocklist` (everyone except the numbers on the blocklist). Takes effect on the next
    inbound message. Both lists are kept when the mode changes; an empty allowlist silences the
    assistant for every contact.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):
        body (ContactFilterModeIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactFilterOut]
    """

    kwargs = _get_kwargs(
        chatbot_id=chatbot_id,
        body=body,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chatbot_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ContactFilterModeIn,
    business_id: str | Unset = UNSET,
) -> ContactFilterOut | None:
    """Set an assistant's contact filter mode

     Chooses who may trigger the assistant: `off` (everyone), `allowlist` (only the numbers on the
    allowlist) or `blocklist` (everyone except the numbers on the blocklist). Takes effect on the next
    inbound message. Both lists are kept when the mode changes; an empty allowlist silences the
    assistant for every contact.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):
        body (ContactFilterModeIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactFilterOut
    """

    return (
        await asyncio_detailed(
            chatbot_id=chatbot_id,
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
