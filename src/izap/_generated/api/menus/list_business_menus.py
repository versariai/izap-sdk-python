from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.business_menu_out import BusinessMenuOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/businesses/menus",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BusinessMenuOut | None:
    if response.status_code == 200:
        response_200 = BusinessMenuOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BusinessMenuOut]:
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
) -> Response[BusinessMenuOut]:
    """List the business menus

     Returns the product catalog menus published by the business named in the `business-id` header.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessMenuOut]
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
) -> BusinessMenuOut | None:
    """List the business menus

     Returns the product catalog menus published by the business named in the `business-id` header.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessMenuOut
    """

    return sync_detailed(
        client=client,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    business_id: str | Unset = UNSET,
) -> Response[BusinessMenuOut]:
    """List the business menus

     Returns the product catalog menus published by the business named in the `business-id` header.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessMenuOut]
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
) -> BusinessMenuOut | None:
    """List the business menus

     Returns the product catalog menus published by the business named in the `business-id` header.

    Args:
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessMenuOut
    """

    return (
        await asyncio_detailed(
            client=client,
            business_id=business_id,
        )
    ).parsed
