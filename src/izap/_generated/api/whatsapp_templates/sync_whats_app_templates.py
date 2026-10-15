from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.template_sync_response import TemplateSyncResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/whatsapp_templates/sync",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TemplateSyncResponse | None:
    if response.status_code == 200:
        response_200 = TemplateSyncResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TemplateSyncResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[TemplateSyncResponse]:
    """Sync template status from Meta

     Pulls the current review status of the business's templates from Meta and updates the stored copies,
    so templates approved or rejected on Meta's side become visible here.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplateSyncResponse]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> TemplateSyncResponse | None:
    """Sync template status from Meta

     Pulls the current review status of the business's templates from Meta and updates the stored copies,
    so templates approved or rejected on Meta's side become visible here.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplateSyncResponse
    """

    return sync_detailed(
        client=client,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[TemplateSyncResponse]:
    """Sync template status from Meta

     Pulls the current review status of the business's templates from Meta and updates the stored copies,
    so templates approved or rejected on Meta's side become visible here.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TemplateSyncResponse]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> TemplateSyncResponse | None:
    """Sync template status from Meta

     Pulls the current review status of the business's templates from Meta and updates the stored copies,
    so templates approved or rejected on Meta's side become visible here.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TemplateSyncResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            business_id=business_id,
        )
    ).parsed
