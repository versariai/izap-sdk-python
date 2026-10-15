from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.template_list_response import TemplateListResponse
from ...models.template_status import TemplateStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: None | TemplateStatus | Unset = UNSET,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, str):
        json_status = status
    else:
        json_status = status
    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/whatsapp_templates",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TemplateListResponse | None:
    if response.status_code == 200:
        response_200 = TemplateListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TemplateListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: None | TemplateStatus | Unset = UNSET,
    business_id: str | Unset = UNSET,
) -> Response[TemplateListResponse]:
    """List message templates

     Returns the business's WhatsApp message templates, optionally filtered by review status.

    Args:
        status (None | TemplateStatus | Unset):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplateListResponse]
    """

    kwargs = _get_kwargs(
        status=status,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: None | TemplateStatus | Unset = UNSET,
    business_id: str | Unset = UNSET,
) -> TemplateListResponse | None:
    """List message templates

     Returns the business's WhatsApp message templates, optionally filtered by review status.

    Args:
        status (None | TemplateStatus | Unset):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplateListResponse
    """

    return sync_detailed(
        client=client,
        status=status,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: None | TemplateStatus | Unset = UNSET,
    business_id: str | Unset = UNSET,
) -> Response[TemplateListResponse]:
    """List message templates

     Returns the business's WhatsApp message templates, optionally filtered by review status.

    Args:
        status (None | TemplateStatus | Unset):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplateListResponse]
    """

    kwargs = _get_kwargs(
        status=status,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: None | TemplateStatus | Unset = UNSET,
    business_id: str | Unset = UNSET,
) -> TemplateListResponse | None:
    """List message templates

     Returns the business's WhatsApp message templates, optionally filtered by review status.

    Args:
        status (None | TemplateStatus | Unset):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplateListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            business_id=business_id,
        )
    ).parsed
