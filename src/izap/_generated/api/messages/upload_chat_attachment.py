from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_upload_response import FileUploadResponse
from ...models.upload_chat_attachment_body import UploadChatAttachmentBody
from ...types import Response


def _get_kwargs(
    chat_id: UUID,
    *,
    body: UploadChatAttachmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/chats/{chat_id}/upload".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FileUploadResponse | None:
    if response.status_code == 200:
        response_200 = FileUploadResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FileUploadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UploadChatAttachmentBody,
) -> Response[FileUploadResponse]:
    """Upload an attachment

     Uploads a file to be attached to a message on this conversation, and returns the stored reference to
    pass when sending that message.

    Args:
        chat_id (UUID):
        body (UploadChatAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileUploadResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UploadChatAttachmentBody,
) -> FileUploadResponse | None:
    """Upload an attachment

     Uploads a file to be attached to a message on this conversation, and returns the stored reference to
    pass when sending that message.

    Args:
        chat_id (UUID):
        body (UploadChatAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileUploadResponse
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UploadChatAttachmentBody,
) -> Response[FileUploadResponse]:
    """Upload an attachment

     Uploads a file to be attached to a message on this conversation, and returns the stored reference to
    pass when sending that message.

    Args:
        chat_id (UUID):
        body (UploadChatAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileUploadResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UploadChatAttachmentBody,
) -> FileUploadResponse | None:
    """Upload an attachment

     Uploads a file to be attached to a message on this conversation, and returns the stored reference to
    pass when sending that message.

    Args:
        chat_id (UUID):
        body (UploadChatAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileUploadResponse
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
            body=body,
        )
    ).parsed
