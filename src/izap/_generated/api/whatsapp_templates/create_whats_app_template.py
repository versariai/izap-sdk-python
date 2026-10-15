from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.whats_app_template_create import WhatsAppTemplateCreate
from ...models.whats_app_template_out import WhatsAppTemplateOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: WhatsAppTemplateCreate,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/whatsapp_templates",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WhatsAppTemplateOut | None:
    if response.status_code == 201:
        response_201 = WhatsAppTemplateOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WhatsAppTemplateOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WhatsAppTemplateCreate,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppTemplateOut]:
    """Create a message template

     Creates a template as a local draft. A draft cannot be used for sending until it has been submitted
    to Meta and approved.

    Args:
        business_id (str | Unset):
        body (WhatsAppTemplateCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppTemplateOut]
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
    body: WhatsAppTemplateCreate,
    business_id: str | Unset = UNSET,
) -> WhatsAppTemplateOut | None:
    """Create a message template

     Creates a template as a local draft. A draft cannot be used for sending until it has been submitted
    to Meta and approved.

    Args:
        business_id (str | Unset):
        body (WhatsAppTemplateCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppTemplateOut
    """

    return sync_detailed(
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WhatsAppTemplateCreate,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppTemplateOut]:
    """Create a message template

     Creates a template as a local draft. A draft cannot be used for sending until it has been submitted
    to Meta and approved.

    Args:
        business_id (str | Unset):
        body (WhatsAppTemplateCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppTemplateOut]
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
    body: WhatsAppTemplateCreate,
    business_id: str | Unset = UNSET,
) -> WhatsAppTemplateOut | None:
    """Create a message template

     Creates a template as a local draft. A draft cannot be used for sending until it has been submitted
    to Meta and approved.

    Args:
        business_id (str | Unset):
        body (WhatsAppTemplateCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppTemplateOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
