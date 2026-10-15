from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_transmissions_out import ListTransmissionsOut
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    params: dict[str, Any] = {}

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/transmissions",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListTransmissionsOut | None:
    if response.status_code == 200:
        response_200 = ListTransmissionsOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListTransmissionsOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    business_id: str | Unset = UNSET,
) -> Response[ListTransmissionsOut]:
    """List transmissions

     Returns the business's bulk sends, newest first. Archived rows are omitted unless `status=archived`
    is passed. Optionally filter by any other status.

    Args:
        status (None | str | Unset):
        limit (int | Unset):  Default: 50.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTransmissionsOut]
    """

    kwargs = _get_kwargs(
        status=status,
        limit=limit,
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    business_id: str | Unset = UNSET,
) -> ListTransmissionsOut | None:
    """List transmissions

     Returns the business's bulk sends, newest first. Archived rows are omitted unless `status=archived`
    is passed. Optionally filter by any other status.

    Args:
        status (None | str | Unset):
        limit (int | Unset):  Default: 50.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTransmissionsOut
    """

    return sync_detailed(
        client=client,
        status=status,
        limit=limit,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    business_id: str | Unset = UNSET,
) -> Response[ListTransmissionsOut]:
    """List transmissions

     Returns the business's bulk sends, newest first. Archived rows are omitted unless `status=archived`
    is passed. Optionally filter by any other status.

    Args:
        status (None | str | Unset):
        limit (int | Unset):  Default: 50.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTransmissionsOut]
    """

    kwargs = _get_kwargs(
        status=status,
        limit=limit,
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: None | str | Unset = UNSET,
    limit: int | Unset = 50,
    business_id: str | Unset = UNSET,
) -> ListTransmissionsOut | None:
    """List transmissions

     Returns the business's bulk sends, newest first. Archived rows are omitted unless `status=archived`
    is passed. Optionally filter by any other status.

    Args:
        status (None | str | Unset):
        limit (int | Unset):  Default: 50.
        business_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTransmissionsOut
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            limit=limit,
            business_id=business_id,
        )
    ).parsed
