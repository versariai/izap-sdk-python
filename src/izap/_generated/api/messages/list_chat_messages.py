import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_chat_messages_response_list_messages_api_v1_chats_chat_id_messages_get import (
    ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chat_id: UUID,
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    since: datetime.datetime | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    elif isinstance(since, datetime.datetime):
        json_since = since.isoformat()
    else:
        json_since = since
    params["since"] = json_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/chats/{chat_id}/messages".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet | None:
    if response.status_code == 200:
        response_200 = ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet]:
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
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    since: datetime.datetime | None | Unset = UNSET,
) -> Response[ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet]:
    """List a chat's messages

     Returns the conversation's messages newest first, with paging. Each message carries its author,
    content, timestamp and delivery status. Any chat id belonging to the conversation may be used.

    Args:
        chat_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        since (datetime.datetime | None | Unset): ISO-8601 timestamp. When set, only messages
            strictly *newer than* `since` are returned (exclusive — a message timestamped exactly at
            `since` is not repeated). Intended for incremental polling: pass the newest `timestamp`
            seen so far instead of refetching a full page and diffing client-side.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        page=page,
        page_size=page_size,
        since=since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    since: datetime.datetime | None | Unset = UNSET,
) -> ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet | None:
    """List a chat's messages

     Returns the conversation's messages newest first, with paging. Each message carries its author,
    content, timestamp and delivery status. Any chat id belonging to the conversation may be used.

    Args:
        chat_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        since (datetime.datetime | None | Unset): ISO-8601 timestamp. When set, only messages
            strictly *newer than* `since` are returned (exclusive — a message timestamped exactly at
            `since` is not repeated). Intended for incremental polling: pass the newest `timestamp`
            seen so far instead of refetching a full page and diffing client-side.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
        page=page,
        page_size=page_size,
        since=since,
    ).parsed


async def asyncio_detailed(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    since: datetime.datetime | None | Unset = UNSET,
) -> Response[ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet]:
    """List a chat's messages

     Returns the conversation's messages newest first, with paging. Each message carries its author,
    content, timestamp and delivery status. Any chat id belonging to the conversation may be used.

    Args:
        chat_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        since (datetime.datetime | None | Unset): ISO-8601 timestamp. When set, only messages
            strictly *newer than* `since` are returned (exclusive — a message timestamped exactly at
            `since` is not repeated). Intended for incremental polling: pass the newest `timestamp`
            seen so far instead of refetching a full page and diffing client-side.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        page=page,
        page_size=page_size,
        since=since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 50,
    since: datetime.datetime | None | Unset = UNSET,
) -> ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet | None:
    """List a chat's messages

     Returns the conversation's messages newest first, with paging. Each message carries its author,
    content, timestamp and delivery status. Any chat id belonging to the conversation may be used.

    Args:
        chat_id (UUID):
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 50.
        since (datetime.datetime | None | Unset): ISO-8601 timestamp. When set, only messages
            strictly *newer than* `since` are returned (exclusive — a message timestamped exactly at
            `since` is not repeated). Intended for incremental polling: pass the newest `timestamp`
            seen so far instead of refetching a full page and diffing client-side.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListChatMessagesResponseListMessagesApiV1ChatsChatIdMessagesGet
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
            page=page,
            page_size=page_size,
            since=since,
        )
    ).parsed
