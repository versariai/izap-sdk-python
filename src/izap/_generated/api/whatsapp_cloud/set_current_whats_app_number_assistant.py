from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.whats_app_number_assistant_in import WhatsAppNumberAssistantIn
from ...models.whats_app_number_out import WhatsAppNumberOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    number_id: str,
    *,
    body: WhatsAppNumberAssistantIn,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/businesses/whatsapp_cloud/numbers/{number_id}/assistant".format(
            number_id=quote(str(number_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WhatsAppNumberOut | None:
    if response.status_code == 200:
        response_200 = WhatsAppNumberOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WhatsAppNumberOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    number_id: str,
    *,
    client: AuthenticatedClient,
    body: WhatsAppNumberAssistantIn,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppNumberOut]:
    """Bind an assistant to a number

     Points a connected number at one of the business's assistants. Inbound messages to that number are
    answered by the assistant bound here. The business is taken from the `business-id` header rather
    than the URL; the path-scoped form of this operation is deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):
        body (WhatsAppNumberAssistantIn): ``null`` detaches whichever assistant currently answers
            on the number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppNumberOut]
    """

    kwargs = _get_kwargs(
        number_id=number_id,
        body=body,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    number_id: str,
    *,
    client: AuthenticatedClient,
    body: WhatsAppNumberAssistantIn,
    business_id: str | Unset = UNSET,
) -> WhatsAppNumberOut | None:
    """Bind an assistant to a number

     Points a connected number at one of the business's assistants. Inbound messages to that number are
    answered by the assistant bound here. The business is taken from the `business-id` header rather
    than the URL; the path-scoped form of this operation is deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):
        body (WhatsAppNumberAssistantIn): ``null`` detaches whichever assistant currently answers
            on the number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppNumberOut
    """

    return sync_detailed(
        number_id=number_id,
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    number_id: str,
    *,
    client: AuthenticatedClient,
    body: WhatsAppNumberAssistantIn,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppNumberOut]:
    """Bind an assistant to a number

     Points a connected number at one of the business's assistants. Inbound messages to that number are
    answered by the assistant bound here. The business is taken from the `business-id` header rather
    than the URL; the path-scoped form of this operation is deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):
        body (WhatsAppNumberAssistantIn): ``null`` detaches whichever assistant currently answers
            on the number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppNumberOut]
    """

    kwargs = _get_kwargs(
        number_id=number_id,
        body=body,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    number_id: str,
    *,
    client: AuthenticatedClient,
    body: WhatsAppNumberAssistantIn,
    business_id: str | Unset = UNSET,
) -> WhatsAppNumberOut | None:
    """Bind an assistant to a number

     Points a connected number at one of the business's assistants. Inbound messages to that number are
    answered by the assistant bound here. The business is taken from the `business-id` header rather
    than the URL; the path-scoped form of this operation is deprecated.

    Args:
        number_id (str):
        business_id (str | Unset):
        body (WhatsAppNumberAssistantIn): ``null`` detaches whichever assistant currently answers
            on the number.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppNumberOut
    """

    return (
        await asyncio_detailed(
            number_id=number_id,
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
