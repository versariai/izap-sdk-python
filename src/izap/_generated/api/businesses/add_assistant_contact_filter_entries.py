from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_filter_entries_added_out import ContactFilterEntriesAddedOut
from ...models.contact_filter_entries_in import ContactFilterEntriesIn
from ...types import UNSET, Response, Unset


def _get_kwargs(
    chatbot_id: UUID,
    *,
    body: ContactFilterEntriesIn,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/businesses/chatbots/{chatbot_id}/contact-filter/entries".format(
            chatbot_id=quote(str(chatbot_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContactFilterEntriesAddedOut | None:
    if response.status_code == 200:
        response_200 = ContactFilterEntriesAddedOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ContactFilterEntriesAddedOut]:
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
    body: ContactFilterEntriesIn,
    business_id: str | Unset = UNSET,
) -> Response[ContactFilterEntriesAddedOut]:
    """Add contacts to an assistant's contact filter

     Adds up to 500 phone numbers to the allowlist or blocklist in one call. Numbers are stored in
    canonical E.164 form, so different spellings of one number are one entry. Adding a number that is
    already listed is not an error; the response reports it separately, along with any input that is not
    a usable phone number.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):
        body (ContactFilterEntriesIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactFilterEntriesAddedOut]
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
    body: ContactFilterEntriesIn,
    business_id: str | Unset = UNSET,
) -> ContactFilterEntriesAddedOut | None:
    """Add contacts to an assistant's contact filter

     Adds up to 500 phone numbers to the allowlist or blocklist in one call. Numbers are stored in
    canonical E.164 form, so different spellings of one number are one entry. Adding a number that is
    already listed is not an error; the response reports it separately, along with any input that is not
    a usable phone number.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):
        body (ContactFilterEntriesIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactFilterEntriesAddedOut
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
    body: ContactFilterEntriesIn,
    business_id: str | Unset = UNSET,
) -> Response[ContactFilterEntriesAddedOut]:
    """Add contacts to an assistant's contact filter

     Adds up to 500 phone numbers to the allowlist or blocklist in one call. Numbers are stored in
    canonical E.164 form, so different spellings of one number are one entry. Adding a number that is
    already listed is not an error; the response reports it separately, along with any input that is not
    a usable phone number.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):
        body (ContactFilterEntriesIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactFilterEntriesAddedOut]
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
    body: ContactFilterEntriesIn,
    business_id: str | Unset = UNSET,
) -> ContactFilterEntriesAddedOut | None:
    """Add contacts to an assistant's contact filter

     Adds up to 500 phone numbers to the allowlist or blocklist in one call. Numbers are stored in
    canonical E.164 form, so different spellings of one number are one entry. Adding a number that is
    already listed is not an error; the response reports it separately, along with any input that is not
    a usable phone number.

    Args:
        chatbot_id (UUID):
        business_id (str | Unset):
        body (ContactFilterEntriesIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactFilterEntriesAddedOut
    """

    return (
        await asyncio_detailed(
            chatbot_id=chatbot_id,
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
