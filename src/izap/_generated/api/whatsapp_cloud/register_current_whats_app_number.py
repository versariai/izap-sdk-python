from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.whats_app_cloud_register_accepted import WhatsAppCloudRegisterAccepted
from ...models.whats_app_cloud_register_request import WhatsAppCloudRegisterRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: WhatsAppCloudRegisterRequest,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/businesses/whatsapp_cloud/register",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WhatsAppCloudRegisterAccepted | None:
    if response.status_code == 202:
        response_202 = WhatsAppCloudRegisterAccepted.from_dict(response.json())

        return response_202

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WhatsAppCloudRegisterAccepted]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WhatsAppCloudRegisterRequest,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppCloudRegisterAccepted]:
    """Register a WhatsApp Cloud number

     Exchanges an Embedded Signup code and registers the WhatsApp Business Account in the background.
    Returns `202` with a `task_id`; poll the registration task until its status is `completed` or
    `failed`. The business is taken from the `business-id` header rather than the URL; the path-scoped
    form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (WhatsAppCloudRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppCloudRegisterAccepted]
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
    body: WhatsAppCloudRegisterRequest,
    business_id: str | Unset = UNSET,
) -> WhatsAppCloudRegisterAccepted | None:
    """Register a WhatsApp Cloud number

     Exchanges an Embedded Signup code and registers the WhatsApp Business Account in the background.
    Returns `202` with a `task_id`; poll the registration task until its status is `completed` or
    `failed`. The business is taken from the `business-id` header rather than the URL; the path-scoped
    form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (WhatsAppCloudRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppCloudRegisterAccepted
    """

    return sync_detailed(
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WhatsAppCloudRegisterRequest,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppCloudRegisterAccepted]:
    """Register a WhatsApp Cloud number

     Exchanges an Embedded Signup code and registers the WhatsApp Business Account in the background.
    Returns `202` with a `task_id`; poll the registration task until its status is `completed` or
    `failed`. The business is taken from the `business-id` header rather than the URL; the path-scoped
    form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (WhatsAppCloudRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppCloudRegisterAccepted]
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
    body: WhatsAppCloudRegisterRequest,
    business_id: str | Unset = UNSET,
) -> WhatsAppCloudRegisterAccepted | None:
    """Register a WhatsApp Cloud number

     Exchanges an Embedded Signup code and registers the WhatsApp Business Account in the background.
    Returns `202` with a `task_id`; poll the registration task until its status is `completed` or
    `failed`. The business is taken from the `business-id` header rather than the URL; the path-scoped
    form of this operation is deprecated.

    Args:
        business_id (str | Unset):
        body (WhatsAppCloudRegisterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppCloudRegisterAccepted
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
