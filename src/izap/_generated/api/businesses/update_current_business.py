from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.business_out import BusinessOut
from ...models.business_update_request import BusinessUpdateRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BusinessUpdateRequest,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/businesses/current",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BusinessOut | None:
    if response.status_code == 200:
        response_200 = BusinessOut.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BusinessOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BusinessUpdateRequest,
    business_id: str | Unset = UNSET,
) -> Response[BusinessOut]:
    """Update a business

     Partially updates the business profile. Only the fields present in the request body are changed. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        business_id (str | Unset):
        body (BusinessUpdateRequest): Partial update for a business's profile. Optional fields
            only; unset ones are left alone.

            Kept intentionally narrow (name + timezone) so GOG-3129 (business hours) can extend this
            same endpoint with an `hours` field later instead of introducing a second PATCH route.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessOut]
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
    body: BusinessUpdateRequest,
    business_id: str | Unset = UNSET,
) -> BusinessOut | None:
    """Update a business

     Partially updates the business profile. Only the fields present in the request body are changed. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        business_id (str | Unset):
        body (BusinessUpdateRequest): Partial update for a business's profile. Optional fields
            only; unset ones are left alone.

            Kept intentionally narrow (name + timezone) so GOG-3129 (business hours) can extend this
            same endpoint with an `hours` field later instead of introducing a second PATCH route.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessOut
    """

    return sync_detailed(
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BusinessUpdateRequest,
    business_id: str | Unset = UNSET,
) -> Response[BusinessOut]:
    """Update a business

     Partially updates the business profile. Only the fields present in the request body are changed. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        business_id (str | Unset):
        body (BusinessUpdateRequest): Partial update for a business's profile. Optional fields
            only; unset ones are left alone.

            Kept intentionally narrow (name + timezone) so GOG-3129 (business hours) can extend this
            same endpoint with an `hours` field later instead of introducing a second PATCH route.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessOut]
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
    body: BusinessUpdateRequest,
    business_id: str | Unset = UNSET,
) -> BusinessOut | None:
    """Update a business

     Partially updates the business profile. Only the fields present in the request body are changed. The
    business is taken from the `business-id` header rather than the URL; the path-scoped form of this
    operation is deprecated.

    Args:
        business_id (str | Unset):
        body (BusinessUpdateRequest): Partial update for a business's profile. Optional fields
            only; unset ones are left alone.

            Kept intentionally narrow (name + timezone) so GOG-3129 (business hours) can extend this
            same endpoint with an `hours` field later instead of introducing a second PATCH route.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
