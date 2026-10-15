from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_filter_out import ContactFilterOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chatbot_id: UUID,
    *,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/businesses/chatbots/{chatbot_id}/contact-filter".format(
            chatbot_id=quote(str(chatbot_id), safe=""),
        ),
    }

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
    business_id: str | Unset = UNSET,
) -> Response[ContactFilterOut]:
    """Retrieve an assistant's contact filter

     Returns which contacts may trigger the assistant: the filter mode, and the numbers on its allowlist
    and blocklist. Messages from a contact the filter excludes are still received and stored, but the
    assistant is never invoked for them — no AI reply, greeting or off-hours message is sent.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactFilterOut]
    """

    kwargs = _get_kwargs(
        chatbot_id=chatbot_id,
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
    business_id: str | Unset = UNSET,
) -> ContactFilterOut | None:
    """Retrieve an assistant's contact filter

     Returns which contacts may trigger the assistant: the filter mode, and the numbers on its allowlist
    and blocklist. Messages from a contact the filter excludes are still received and stored, but the
    assistant is never invoked for them — no AI reply, greeting or off-hours message is sent.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactFilterOut
    """

    return sync_detailed(
        chatbot_id=chatbot_id,
        client=client,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    chatbot_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[ContactFilterOut]:
    """Retrieve an assistant's contact filter

     Returns which contacts may trigger the assistant: the filter mode, and the numbers on its allowlist
    and blocklist. Messages from a contact the filter excludes are still received and stored, but the
    assistant is never invoked for them — no AI reply, greeting or off-hours message is sent.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactFilterOut]
    """

    kwargs = _get_kwargs(
        chatbot_id=chatbot_id,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chatbot_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> ContactFilterOut | None:
    """Retrieve an assistant's contact filter

     Returns which contacts may trigger the assistant: the filter mode, and the numbers on its allowlist
    and blocklist. Messages from a contact the filter excludes are still received and stored, but the
    assistant is never invoked for them — no AI reply, greeting or off-hours message is sent.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):

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
            business_id=business_id,
        )
    ).parsed
