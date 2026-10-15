from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_template_send_request import ChatTemplateSendRequest
from ...models.send_chat_template_message_out import SendChatTemplateMessageOut
from ...types import Response


def _get_kwargs(
    chat_id: UUID,
    *,
    body: ChatTemplateSendRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/chats/{chat_id}/messages/template".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SendChatTemplateMessageOut | None:
    if response.status_code == 200:
        response_200 = SendChatTemplateMessageOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SendChatTemplateMessageOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ChatTemplateSendRequest,
) -> Response[SendChatTemplateMessageOut]:
    """Send a template message to a chat

     Sends an approved WhatsApp template into the conversation. This is the only way to reach a customer
    outside the 24-hour customer-service window. A rendered copy is stored so agents see what was sent.

    Args:
        chat_id (UUID):
        body (ChatTemplateSendRequest): Send an approved template into an existing live-chat
            conversation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendChatTemplateMessageOut]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ChatTemplateSendRequest,
) -> SendChatTemplateMessageOut | None:
    """Send a template message to a chat

     Sends an approved WhatsApp template into the conversation. This is the only way to reach a customer
    outside the 24-hour customer-service window. A rendered copy is stored so agents see what was sent.

    Args:
        chat_id (UUID):
        body (ChatTemplateSendRequest): Send an approved template into an existing live-chat
            conversation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendChatTemplateMessageOut
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ChatTemplateSendRequest,
) -> Response[SendChatTemplateMessageOut]:
    """Send a template message to a chat

     Sends an approved WhatsApp template into the conversation. This is the only way to reach a customer
    outside the 24-hour customer-service window. A rendered copy is stored so agents see what was sent.

    Args:
        chat_id (UUID):
        body (ChatTemplateSendRequest): Send an approved template into an existing live-chat
            conversation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SendChatTemplateMessageOut]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    body: ChatTemplateSendRequest,
) -> SendChatTemplateMessageOut | None:
    """Send a template message to a chat

     Sends an approved WhatsApp template into the conversation. This is the only way to reach a customer
    outside the 24-hour customer-service window. A rendered copy is stored so agents see what was sent.

    Args:
        chat_id (UUID):
        body (ChatTemplateSendRequest): Send an approved template into an existing live-chat
            conversation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SendChatTemplateMessageOut
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
            body=body,
        )
    ).parsed
