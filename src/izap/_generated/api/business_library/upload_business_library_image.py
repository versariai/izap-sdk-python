from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.business_library_image_out import BusinessLibraryImageOut
from ...models.upload_business_library_image_body import UploadBusinessLibraryImageBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UploadBusinessLibraryImageBody,
    business_id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(business_id, Unset):
        headers["business-id"] = business_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/businesses/library/images",
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BusinessLibraryImageOut | None:
    if response.status_code == 201:
        response_201 = BusinessLibraryImageOut.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BusinessLibraryImageOut]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UploadBusinessLibraryImageBody,
    business_id: str | Unset = UNSET,
) -> Response[BusinessLibraryImageOut]:
    """Upload a library image

     Uploads an image to the library of the authenticated user's business so it can later be attached to
    messages. The business is taken from the credential; this operation accepts no business parameter.

    Args:
        business_id (str | Unset):
        body (UploadBusinessLibraryImageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessLibraryImageOut]
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
    body: UploadBusinessLibraryImageBody,
    business_id: str | Unset = UNSET,
) -> BusinessLibraryImageOut | None:
    """Upload a library image

     Uploads an image to the library of the authenticated user's business so it can later be attached to
    messages. The business is taken from the credential; this operation accepts no business parameter.

    Args:
        business_id (str | Unset):
        body (UploadBusinessLibraryImageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessLibraryImageOut
    """

    return sync_detailed(
        client=client,
        body=body,
        business_id=business_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UploadBusinessLibraryImageBody,
    business_id: str | Unset = UNSET,
) -> Response[BusinessLibraryImageOut]:
    """Upload a library image

     Uploads an image to the library of the authenticated user's business so it can later be attached to
    messages. The business is taken from the credential; this operation accepts no business parameter.

    Args:
        business_id (str | Unset):
        body (UploadBusinessLibraryImageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessLibraryImageOut]
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
    body: UploadBusinessLibraryImageBody,
    business_id: str | Unset = UNSET,
) -> BusinessLibraryImageOut | None:
    """Upload a library image

     Uploads an image to the library of the authenticated user's business so it can later be attached to
    messages. The business is taken from the credential; this operation accepts no business parameter.

    Args:
        business_id (str | Unset):
        body (UploadBusinessLibraryImageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessLibraryImageOut
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            business_id=business_id,
        )
    ).parsed
