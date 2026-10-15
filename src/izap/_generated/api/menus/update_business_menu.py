from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.menu_update_in import MenuUpdateIn
from ...models.menus_out import MenusOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    menu_id: str,
    *,
    body: MenuUpdateIn,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/businesses/menus/{menu_id}".format(
            menu_id=quote(str(menu_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MenusOut | None:
    if response.status_code == 200:
        response_200 = MenusOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MenusOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    menu_id: str,
    *,
    client: AuthenticatedClient,
    body: MenuUpdateIn,
    business_id: str | Unset = UNSET,
) -> Response[MenusOut]:
    """Update a menu

     Replaces the contents of an existing menu.

    Args:
        menu_id (str):
        business_id (str | Unset):
        body (MenuUpdateIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MenusOut]
    """

    kwargs = _get_kwargs(
        menu_id=menu_id,
        body=body,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    menu_id: str,
    *,
    client: AuthenticatedClient,
    body: MenuUpdateIn,
    business_id: str | Unset = UNSET,
) -> MenusOut | None:
    """Update a menu

     Replaces the contents of an existing menu.

    Args:
        menu_id (str):
        business_id (str | Unset):
        body (MenuUpdateIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MenusOut
    """

    return sync_detailed(
        menu_id=menu_id,
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    menu_id: str,
    *,
    client: AuthenticatedClient,
    body: MenuUpdateIn,
    business_id: str | Unset = UNSET,
) -> Response[MenusOut]:
    """Update a menu

     Replaces the contents of an existing menu.

    Args:
        menu_id (str):
        business_id (str | Unset):
        body (MenuUpdateIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MenusOut]
    """

    kwargs = _get_kwargs(
        menu_id=menu_id,
        body=body,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    menu_id: str,
    *,
    client: AuthenticatedClient,
    body: MenuUpdateIn,
    business_id: str | Unset = UNSET,
) -> MenusOut | None:
    """Update a menu

     Replaces the contents of an existing menu.

    Args:
        menu_id (str):
        business_id (str | Unset):
        body (MenuUpdateIn):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MenusOut
    """

    return (
        await asyncio_detailed(
            menu_id=menu_id,
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
