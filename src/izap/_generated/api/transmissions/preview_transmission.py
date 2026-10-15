from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_transmission_preview_in import CreateTransmissionPreviewIn
from ...models.transmission_preview_out import TransmissionPreviewOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateTransmissionPreviewIn,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/transmissions/preview",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TransmissionPreviewOut | None:
    if response.status_code == 200:
        response_200 = TransmissionPreviewOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TransmissionPreviewOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTransmissionPreviewIn,
    business_id: str | Unset = UNSET,
) -> Response[TransmissionPreviewOut]:
    """Preview a transmission

     Validates the recipient list and template and stores the result as a draft, without sending
    anything. Review the draft, then confirm it to dispatch.

    Args:
        business_id (str | Unset):
        body (CreateTransmissionPreviewIn): Validate CSV recipients against a template and create
            a DRAFT transmission.

            No messages are sent. ``recipients`` are parsed CSV rows (header -> value); each
            row must contain ``phone_column`` and the columns that fill the template's
            variables. Confirm the returned draft id with ``confirm_transmission`` to send.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransmissionPreviewOut]
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
    body: CreateTransmissionPreviewIn,
    business_id: str | Unset = UNSET,
) -> TransmissionPreviewOut | None:
    """Preview a transmission

     Validates the recipient list and template and stores the result as a draft, without sending
    anything. Review the draft, then confirm it to dispatch.

    Args:
        business_id (str | Unset):
        body (CreateTransmissionPreviewIn): Validate CSV recipients against a template and create
            a DRAFT transmission.

            No messages are sent. ``recipients`` are parsed CSV rows (header -> value); each
            row must contain ``phone_column`` and the columns that fill the template's
            variables. Confirm the returned draft id with ``confirm_transmission`` to send.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransmissionPreviewOut
    """

    return sync_detailed(
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTransmissionPreviewIn,
    business_id: str | Unset = UNSET,
) -> Response[TransmissionPreviewOut]:
    """Preview a transmission

     Validates the recipient list and template and stores the result as a draft, without sending
    anything. Review the draft, then confirm it to dispatch.

    Args:
        business_id (str | Unset):
        body (CreateTransmissionPreviewIn): Validate CSV recipients against a template and create
            a DRAFT transmission.

            No messages are sent. ``recipients`` are parsed CSV rows (header -> value); each
            row must contain ``phone_column`` and the columns that fill the template's
            variables. Confirm the returned draft id with ``confirm_transmission`` to send.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransmissionPreviewOut]
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
    body: CreateTransmissionPreviewIn,
    business_id: str | Unset = UNSET,
) -> TransmissionPreviewOut | None:
    """Preview a transmission

     Validates the recipient list and template and stores the result as a draft, without sending
    anything. Review the draft, then confirm it to dispatch.

    Args:
        business_id (str | Unset):
        body (CreateTransmissionPreviewIn): Validate CSV recipients against a template and create
            a DRAFT transmission.

            No messages are sent. ``recipients`` are parsed CSV rows (header -> value); each
            row must contain ``phone_column`` and the columns that fill the template's
            variables. Confirm the returned draft id with ``confirm_transmission`` to send.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransmissionPreviewOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
