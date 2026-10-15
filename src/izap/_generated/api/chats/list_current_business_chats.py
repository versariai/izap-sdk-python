import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_list_out import ChatListOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    kind: str | Unset = "trainer",
    page: int | Unset = 1,
    page_size: int | Unset = 30,
    messages_per_chat: int | Unset = 1,
    refine_queue: None | str | Unset = UNSET,
    chatbot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    params: dict[str, Any] = {}

    params["kind"] = kind

    params["page"] = page

    params["page_size"] = page_size

    params["messages_per_chat"] = messages_per_chat

    json_refine_queue: None | str | Unset
    if isinstance(refine_queue, Unset):
        json_refine_queue = UNSET
    else:
        json_refine_queue = refine_queue
    params["refine_queue"] = json_refine_queue

    json_chatbot_id: None | str | Unset
    if isinstance(chatbot_id, Unset):
        json_chatbot_id = UNSET
    elif isinstance(chatbot_id, UUID):
        json_chatbot_id = str(chatbot_id)
    else:
        json_chatbot_id = chatbot_id
    params["chatbot_id"] = json_chatbot_id

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
        "url": "/api/v1/chats",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatListOut | None:
    if response.status_code == 200:
        response_200 = ChatListOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatListOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    kind: str | Unset = "trainer",
    page: int | Unset = 1,
    page_size: int | Unset = 30,
    messages_per_chat: int | Unset = 1,
    refine_queue: None | str | Unset = UNSET,
    chatbot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    business_id: str | Unset = UNSET,
) -> Response[ChatListOut]:
    """List a business's chats

     Returns the business's conversations with paging, and optional filters for kind and assistant. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        kind (str | Unset): Filter by Chat.kind. 'trainer' (default) returns sandbox conversations
            from the AI Trainer UI; 'real' returns customer conversations created from WhatsApp
            webhooks; 'all' returns both. The default is 'trainer' to preserve the historical behavior
            of this endpoint, which was trainer-only via a consumer-nickname heuristic. Default:
            'trainer'.
        page (int | Unset): 1-based page number for chat pagination (used by the trainer's
            infinite scroll). Default: 1.
        page_size (int | Unset): Number of chats to return per page (default 30, max 100).
            Default: 30.
        messages_per_chat (int | Unset): How many of the most-recent messages to embed per chat.
            Defaults to 1, which is enough for the list's last-message preview and ordering. Full
            conversation threads should be fetched on demand from GET /chats/{chat_id}/messages
            (paginated) rather than over-fetched here — embedding the whole thread for every chat on
            the page made this endpoint load thousands of messages per request. Default: 1.
        refine_queue (None | str | Unset): Refine trainer queue filter for kind=real. 'pending' =
            no OK review and no issues; 'reviewed' = has OK review or any issue.
        chatbot_id (None | Unset | UUID): Optional assistant ID to filter chats by (per-assistant
            trainer from dash).
        since (datetime.datetime | None | Unset): ISO-8601 timestamp. When set, only chats whose
            last activity (the same timestamp this list orders by) is strictly *newer than* `since`
            are returned — exclusive, not inclusive, so polling with `since=<last seen timestamp>`
            never returns a chat already seen. For incremental sync: pass the newest `timestamp` from
            the previous response as `since` on the next poll instead of refetching and diffing a full
            page client-side.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatListOut]
    """

    kwargs = _get_kwargs(
        kind=kind,
        page=page,
        page_size=page_size,
        messages_per_chat=messages_per_chat,
        refine_queue=refine_queue,
        chatbot_id=chatbot_id,
        since=since,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    kind: str | Unset = "trainer",
    page: int | Unset = 1,
    page_size: int | Unset = 30,
    messages_per_chat: int | Unset = 1,
    refine_queue: None | str | Unset = UNSET,
    chatbot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    business_id: str | Unset = UNSET,
) -> ChatListOut | None:
    """List a business's chats

     Returns the business's conversations with paging, and optional filters for kind and assistant. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        kind (str | Unset): Filter by Chat.kind. 'trainer' (default) returns sandbox conversations
            from the AI Trainer UI; 'real' returns customer conversations created from WhatsApp
            webhooks; 'all' returns both. The default is 'trainer' to preserve the historical behavior
            of this endpoint, which was trainer-only via a consumer-nickname heuristic. Default:
            'trainer'.
        page (int | Unset): 1-based page number for chat pagination (used by the trainer's
            infinite scroll). Default: 1.
        page_size (int | Unset): Number of chats to return per page (default 30, max 100).
            Default: 30.
        messages_per_chat (int | Unset): How many of the most-recent messages to embed per chat.
            Defaults to 1, which is enough for the list's last-message preview and ordering. Full
            conversation threads should be fetched on demand from GET /chats/{chat_id}/messages
            (paginated) rather than over-fetched here — embedding the whole thread for every chat on
            the page made this endpoint load thousands of messages per request. Default: 1.
        refine_queue (None | str | Unset): Refine trainer queue filter for kind=real. 'pending' =
            no OK review and no issues; 'reviewed' = has OK review or any issue.
        chatbot_id (None | Unset | UUID): Optional assistant ID to filter chats by (per-assistant
            trainer from dash).
        since (datetime.datetime | None | Unset): ISO-8601 timestamp. When set, only chats whose
            last activity (the same timestamp this list orders by) is strictly *newer than* `since`
            are returned — exclusive, not inclusive, so polling with `since=<last seen timestamp>`
            never returns a chat already seen. For incremental sync: pass the newest `timestamp` from
            the previous response as `since` on the next poll instead of refetching and diffing a full
            page client-side.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatListOut
    """

    return sync_detailed(
        client=client,
        kind=kind,
        page=page,
        page_size=page_size,
        messages_per_chat=messages_per_chat,
        refine_queue=refine_queue,
        chatbot_id=chatbot_id,
        since=since,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    kind: str | Unset = "trainer",
    page: int | Unset = 1,
    page_size: int | Unset = 30,
    messages_per_chat: int | Unset = 1,
    refine_queue: None | str | Unset = UNSET,
    chatbot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    business_id: str | Unset = UNSET,
) -> Response[ChatListOut]:
    """List a business's chats

     Returns the business's conversations with paging, and optional filters for kind and assistant. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        kind (str | Unset): Filter by Chat.kind. 'trainer' (default) returns sandbox conversations
            from the AI Trainer UI; 'real' returns customer conversations created from WhatsApp
            webhooks; 'all' returns both. The default is 'trainer' to preserve the historical behavior
            of this endpoint, which was trainer-only via a consumer-nickname heuristic. Default:
            'trainer'.
        page (int | Unset): 1-based page number for chat pagination (used by the trainer's
            infinite scroll). Default: 1.
        page_size (int | Unset): Number of chats to return per page (default 30, max 100).
            Default: 30.
        messages_per_chat (int | Unset): How many of the most-recent messages to embed per chat.
            Defaults to 1, which is enough for the list's last-message preview and ordering. Full
            conversation threads should be fetched on demand from GET /chats/{chat_id}/messages
            (paginated) rather than over-fetched here — embedding the whole thread for every chat on
            the page made this endpoint load thousands of messages per request. Default: 1.
        refine_queue (None | str | Unset): Refine trainer queue filter for kind=real. 'pending' =
            no OK review and no issues; 'reviewed' = has OK review or any issue.
        chatbot_id (None | Unset | UUID): Optional assistant ID to filter chats by (per-assistant
            trainer from dash).
        since (datetime.datetime | None | Unset): ISO-8601 timestamp. When set, only chats whose
            last activity (the same timestamp this list orders by) is strictly *newer than* `since`
            are returned — exclusive, not inclusive, so polling with `since=<last seen timestamp>`
            never returns a chat already seen. For incremental sync: pass the newest `timestamp` from
            the previous response as `since` on the next poll instead of refetching and diffing a full
            page client-side.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatListOut]
    """

    kwargs = _get_kwargs(
        kind=kind,
        page=page,
        page_size=page_size,
        messages_per_chat=messages_per_chat,
        refine_queue=refine_queue,
        chatbot_id=chatbot_id,
        since=since,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    kind: str | Unset = "trainer",
    page: int | Unset = 1,
    page_size: int | Unset = 30,
    messages_per_chat: int | Unset = 1,
    refine_queue: None | str | Unset = UNSET,
    chatbot_id: None | Unset | UUID = UNSET,
    since: datetime.datetime | None | Unset = UNSET,
    business_id: str | Unset = UNSET,
) -> ChatListOut | None:
    """List a business's chats

     Returns the business's conversations with paging, and optional filters for kind and assistant. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        kind (str | Unset): Filter by Chat.kind. 'trainer' (default) returns sandbox conversations
            from the AI Trainer UI; 'real' returns customer conversations created from WhatsApp
            webhooks; 'all' returns both. The default is 'trainer' to preserve the historical behavior
            of this endpoint, which was trainer-only via a consumer-nickname heuristic. Default:
            'trainer'.
        page (int | Unset): 1-based page number for chat pagination (used by the trainer's
            infinite scroll). Default: 1.
        page_size (int | Unset): Number of chats to return per page (default 30, max 100).
            Default: 30.
        messages_per_chat (int | Unset): How many of the most-recent messages to embed per chat.
            Defaults to 1, which is enough for the list's last-message preview and ordering. Full
            conversation threads should be fetched on demand from GET /chats/{chat_id}/messages
            (paginated) rather than over-fetched here — embedding the whole thread for every chat on
            the page made this endpoint load thousands of messages per request. Default: 1.
        refine_queue (None | str | Unset): Refine trainer queue filter for kind=real. 'pending' =
            no OK review and no issues; 'reviewed' = has OK review or any issue.
        chatbot_id (None | Unset | UUID): Optional assistant ID to filter chats by (per-assistant
            trainer from dash).
        since (datetime.datetime | None | Unset): ISO-8601 timestamp. When set, only chats whose
            last activity (the same timestamp this list orders by) is strictly *newer than* `since`
            are returned — exclusive, not inclusive, so polling with `since=<last seen timestamp>`
            never returns a chat already seen. For incremental sync: pass the newest `timestamp` from
            the previous response as `since` on the next poll instead of refetching and diffing a full
            page client-side.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatListOut
    """

    return (
        await asyncio_detailed(
            client=client,
            kind=kind,
            page=page,
            page_size=page_size,
            messages_per_chat=messages_per_chat,
            refine_queue=refine_queue,
            chatbot_id=chatbot_id,
            since=since,
            business_id=business_id,
        )
    ).parsed
