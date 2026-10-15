from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.whats_app_cloud_register_task_status import WhatsAppCloudRegisterTaskStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    task_id: UUID,
    *,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/businesses/whatsapp_cloud/register/tasks/{task_id}".format(
            task_id=quote(str(task_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WhatsAppCloudRegisterTaskStatus | None:
    if response.status_code == 200:
        response_200 = WhatsAppCloudRegisterTaskStatus.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WhatsAppCloudRegisterTaskStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppCloudRegisterTaskStatus]:
    """Check a number registration task

     Returns the progress of an asynchronous number registration. Read-only and safe to poll. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        task_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppCloudRegisterTaskStatus]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> WhatsAppCloudRegisterTaskStatus | None:
    """Check a number registration task

     Returns the progress of an asynchronous number registration. Read-only and safe to poll. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        task_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppCloudRegisterTaskStatus
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    task_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[WhatsAppCloudRegisterTaskStatus]:
    """Check a number registration task

     Returns the progress of an asynchronous number registration. Read-only and safe to poll. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        task_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WhatsAppCloudRegisterTaskStatus]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: UUID,
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> WhatsAppCloudRegisterTaskStatus | None:
    """Check a number registration task

     Returns the progress of an asynchronous number registration. Read-only and safe to poll. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        task_id (UUID):
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WhatsAppCloudRegisterTaskStatus
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            business_id=business_id,
        )
    ).parsed
