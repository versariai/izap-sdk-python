from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.business_library_image_list_response import BusinessLibraryImageListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/businesses/library/images",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BusinessLibraryImageListResponse | None:
    if response.status_code == 200:
        response_200 = BusinessLibraryImageListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BusinessLibraryImageListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    business_id: str | Unset = UNSET,
) -> Response[BusinessLibraryImageListResponse]:
    """List library images

     Returns the library images of the authenticated user's business, newest first, paged with `limit`
    and `offset`.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessLibraryImageListResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    business_id: str | Unset = UNSET,
) -> BusinessLibraryImageListResponse | None:
    """List library images

     Returns the library images of the authenticated user's business, newest first, paged with `limit`
    and `offset`.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessLibraryImageListResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    business_id: str | Unset = UNSET,
) -> Response[BusinessLibraryImageListResponse]:
    """List library images

     Returns the library images of the authenticated user's business, newest first, paged with `limit`
    and `offset`.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessLibraryImageListResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    business_id: str | Unset = UNSET,
) -> BusinessLibraryImageListResponse | None:
    """List library images

     Returns the library images of the authenticated user's business, newest first, paged with `limit`
    and `offset`.

    Args:
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessLibraryImageListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            business_id=business_id,
        )
    ).parsed
