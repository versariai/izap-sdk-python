from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_status_in import ChatStatusIn
from ...models.chat_status_out import ChatStatusOut
from ...types import Response


def _get_kwargs(
    chat_id: UUID,
    *,
    body: ChatStatusIn,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/chats/{chat_id}/status".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatStatusOut | None:
    if response.status_code == 200:
        response_200 = ChatStatusOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatStatusOut]:
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
    body: ChatStatusIn,
) -> Response[ChatStatusOut]:
    """Set a chat's status

     Sets the conversation's status — the value the inbox filters on. The status is held against the
    business/customer pair, so it survives a conversation being closed and reopened.

    Args:
        chat_id (UUID):
        body (ChatStatusIn): The conversation's CRM status, as shown by the inbox status filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatStatusOut]
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
    body: ChatStatusIn,
) -> ChatStatusOut | None:
    """Set a chat's status

     Sets the conversation's status — the value the inbox filters on. The status is held against the
    business/customer pair, so it survives a conversation being closed and reopened.

    Args:
        chat_id (UUID):
        body (ChatStatusIn): The conversation's CRM status, as shown by the inbox status filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatStatusOut
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
    body: ChatStatusIn,
) -> Response[ChatStatusOut]:
    """Set a chat's status

     Sets the conversation's status — the value the inbox filters on. The status is held against the
    business/customer pair, so it survives a conversation being closed and reopened.

    Args:
        chat_id (UUID):
        body (ChatStatusIn): The conversation's CRM status, as shown by the inbox status filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatStatusOut]
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
    body: ChatStatusIn,
) -> ChatStatusOut | None:
    """Set a chat's status

     Sets the conversation's status — the value the inbox filters on. The status is held against the
    business/customer pair, so it survives a conversation being closed and reopened.

    Args:
        chat_id (UUID):
        body (ChatStatusIn): The conversation's CRM status, as shown by the inbox status filter.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatStatusOut
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
            body=body,
        )
    ).parsed
