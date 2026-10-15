from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_out import ChatOut
from ...models.create_chat_in import CreateChatIn
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateChatIn,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/chats",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatOut | None:
    if response.status_code == 200:
        response_200 = ChatOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateChatIn,
    business_id: str | Unset = UNSET,
) -> Response[ChatOut]:
    """Create a sandbox chat

     Creates a trainer sandbox conversation for the business named in the `business-id` header. Sandbox
    chats exercise an assistant without messaging a real customer, and a business with no connected
    WhatsApp number may keep only a limited number of them.

    Args:
        business_id (str | Unset):
        body (CreateChatIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatOut]
    """

    kwargs = _get_kwargs(
        body=body,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateChatIn,
    business_id: str | Unset = UNSET,
) -> ChatOut | None:
    """Create a sandbox chat

     Creates a trainer sandbox conversation for the business named in the `business-id` header. Sandbox
    chats exercise an assistant without messaging a real customer, and a business with no connected
    WhatsApp number may keep only a limited number of them.

    Args:
        business_id (str | Unset):
        body (CreateChatIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatOut
    """

    return sync_detailed(
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateChatIn,
    business_id: str | Unset = UNSET,
) -> Response[ChatOut]:
    """Create a sandbox chat

     Creates a trainer sandbox conversation for the business named in the `business-id` header. Sandbox
    chats exercise an assistant without messaging a real customer, and a business with no connected
    WhatsApp number may keep only a limited number of them.

    Args:
        business_id (str | Unset):
        body (CreateChatIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatOut]
    """

    kwargs = _get_kwargs(
        body=body,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateChatIn,
    business_id: str | Unset = UNSET,
) -> ChatOut | None:
    """Create a sandbox chat

     Creates a trainer sandbox conversation for the business named in the `business-id` header. Sandbox
    chats exercise an assistant without messaging a real customer, and a business with no connected
    WhatsApp number may keep only a limited number of them.

    Args:
        business_id (str | Unset):
        body (CreateChatIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
