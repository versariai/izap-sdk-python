from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_read_state_out import ChatReadStateOut
from ...types import Response


def _get_kwargs(
    chat_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/chats/{chat_id}/read".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatReadStateOut | None:
    if response.status_code == 200:
        response_200 = ChatReadStateOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatReadStateOut]:
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
) -> Response[ChatReadStateOut]:
    """Mark a chat as read

     Marks the conversation read for the whole team as of now. Read state is shared between agents rather
    than tracked per agent, and the timestamp is stamped server-side.

    Args:
        chat_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatReadStateOut]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ChatReadStateOut | None:
    """Mark a chat as read

     Marks the conversation read for the whole team as of now. Read state is shared between agents rather
    than tracked per agent, and the timestamp is stamped server-side.

    Args:
        chat_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatReadStateOut
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[ChatReadStateOut]:
    """Mark a chat as read

     Marks the conversation read for the whole team as of now. Read state is shared between agents rather
    than tracked per agent, and the timestamp is stamped server-side.

    Args:
        chat_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatReadStateOut]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
) -> ChatReadStateOut | None:
    """Mark a chat as read

     Marks the conversation read for the whole team as of now. Read state is shared between agents rather
    than tracked per agent, and the timestamp is stamped server-side.

    Args:
        chat_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatReadStateOut
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
        )
    ).parsed
