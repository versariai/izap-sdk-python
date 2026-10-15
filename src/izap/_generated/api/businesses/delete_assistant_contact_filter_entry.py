from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chatbot_id: UUID,
    entry_id: UUID,
    *,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/businesses/chatbots/{chatbot_id}/contact-filter/entries/{entry_id}".format(
            chatbot_id=quote(str(chatbot_id), safe=""),
            entry_id=quote(str(entry_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chatbot_id: UUID,
    entry_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[Any]:
    """Remove a contact from an assistant's contact filter

     Removes one entry from the list it is on. Takes effect on the next inbound message.

    Args:
        chatbot_id (UUID):
        entry_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chatbot_id=chatbot_id,
        entry_id=entry_id,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    chatbot_id: UUID,
    entry_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[Any]:
    """Remove a contact from an assistant's contact filter

     Removes one entry from the list it is on. Takes effect on the next inbound message.

    Args:
        chatbot_id (UUID):
        entry_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        chatbot_id=chatbot_id,
        entry_id=entry_id,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
