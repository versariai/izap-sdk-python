from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_message_details_out import ChatMessageDetailsOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chat_id: UUID,
    message_id: UUID,
    *,
    include_replies: bool | Unset = False,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    params: dict[str, Any] = {}

    params["include_replies"] = include_replies

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/chats/{chat_id}/messages/{message_id}".format(
            chat_id=quote(str(chat_id), safe=""),
            message_id=quote(str(message_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatMessageDetailsOut | None:
    if response.status_code == 200:
        response_200 = ChatMessageDetailsOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ChatMessageDetailsOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_id: UUID,
    message_id: UUID,
    *,
    client: AuthenticatedClient,
    include_replies: bool | Unset = False,
    business_id: str | Unset = UNSET,
) -> Response[ChatMessageDetailsOut]:
    """Retrieve a message's details

     Returns one message with its delivery details, optionally including the replies generated in the
    same exchange. This operation only reads; it uses `POST` for historical reasons. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        chat_id (UUID):
        message_id (UUID):
        include_replies (bool | Unset):  Default: False.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatMessageDetailsOut]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        message_id=message_id,
        include_replies=include_replies,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: UUID,
    message_id: UUID,
    *,
    client: AuthenticatedClient,
    include_replies: bool | Unset = False,
    business_id: str | Unset = UNSET,
) -> ChatMessageDetailsOut | None:
    """Retrieve a message's details

     Returns one message with its delivery details, optionally including the replies generated in the
    same exchange. This operation only reads; it uses `POST` for historical reasons. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        chat_id (UUID):
        message_id (UUID):
        include_replies (bool | Unset):  Default: False.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatMessageDetailsOut
    """

    return sync_detailed(
        chat_id=chat_id,
        message_id=message_id,
        client=client,
        include_replies=include_replies,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    chat_id: UUID,
    message_id: UUID,
    *,
    client: AuthenticatedClient,
    include_replies: bool | Unset = False,
    business_id: str | Unset = UNSET,
) -> Response[ChatMessageDetailsOut]:
    """Retrieve a message's details

     Returns one message with its delivery details, optionally including the replies generated in the
    same exchange. This operation only reads; it uses `POST` for historical reasons. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        chat_id (UUID):
        message_id (UUID):
        include_replies (bool | Unset):  Default: False.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatMessageDetailsOut]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        message_id=message_id,
        include_replies=include_replies,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: UUID,
    message_id: UUID,
    *,
    client: AuthenticatedClient,
    include_replies: bool | Unset = False,
    business_id: str | Unset = UNSET,
) -> ChatMessageDetailsOut | None:
    """Retrieve a message's details

     Returns one message with its delivery details, optionally including the replies generated in the
    same exchange. This operation only reads; it uses `POST` for historical reasons. The business is
    taken from the `business-id` header rather than the URL; the path-scoped form of this operation is
    deprecated.

    Args:
        chat_id (UUID):
        message_id (UUID):
        include_replies (bool | Unset):  Default: False.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatMessageDetailsOut
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            message_id=message_id,
            client=client,
            include_replies=include_replies,
            business_id=business_id,
        )
    ).parsed
