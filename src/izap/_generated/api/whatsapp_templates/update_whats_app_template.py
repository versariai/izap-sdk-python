from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.whats_app_template_out import WhatsAppTemplateOut
from ...models.whats_app_template_update import WhatsAppTemplateUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    template_id: UUID,
    *,
    body: WhatsAppTemplateUpdate,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/whatsapp_templates/{template_id}".format(
            template_id=quote(str(template_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WhatsAppTemplateOut | None:
    if response.status_code == 200:
        response_200 = WhatsAppTemplateOut.from_dict(response.json())

        return response_200

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
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WhatsAppTemplateUpdate,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppTemplateOut]:
    """Update a message template

     Updates a template. Its content can only be changed while the template is still a local draft or has
    been rejected — an approved template has to be replaced by a new one.

    Args:
        template_id (UUID):
        business_id (str | Unset):
        body (WhatsAppTemplateUpdate): Partial update. Approved templates can only be edited while
            in DRAFT/REJECTED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppTemplateOut]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        body=body,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WhatsAppTemplateUpdate,
    business_id: str | Unset = UNSET,
) -> WhatsAppTemplateOut | None:
    """Update a message template

     Updates a template. Its content can only be changed while the template is still a local draft or has
    been rejected — an approved template has to be replaced by a new one.

    Args:
        template_id (UUID):
        business_id (str | Unset):
        body (WhatsAppTemplateUpdate): Partial update. Approved templates can only be edited while
            in DRAFT/REJECTED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppTemplateOut
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WhatsAppTemplateUpdate,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppTemplateOut]:
    """Update a message template

     Updates a template. Its content can only be changed while the template is still a local draft or has
    been rejected — an approved template has to be replaced by a new one.

    Args:
        template_id (UUID):
        business_id (str | Unset):
        body (WhatsAppTemplateUpdate): Partial update. Approved templates can only be edited while
            in DRAFT/REJECTED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppTemplateOut]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
        body=body,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: UUID,
    *,
    client: AuthenticatedClient,
    body: WhatsAppTemplateUpdate,
    business_id: str | Unset = UNSET,
) -> WhatsAppTemplateOut | None:
    """Update a message template

     Updates a template. Its content can only be changed while the template is still a local draft or has
    been rejected — an approved template has to be replaced by a new one.

    Args:
        template_id (UUID):
        business_id (str | Unset):
        body (WhatsAppTemplateUpdate): Partial update. Approved templates can only be edited while
            in DRAFT/REJECTED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppTemplateOut
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
