from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_token_request import CreateTokenRequest
from ...models.token_created_response import TokenCreatedResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateTokenRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/me/api-tokens",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TokenCreatedResponse | None:
    if response.status_code == 201:
        response_201 = TokenCreatedResponse.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TokenCreatedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTokenRequest,
) -> Response[TokenCreatedResponse]:
    """Create a personal access token

     Issues a new personal access token for the authenticated user. The token value appears exactly once,
    in this response — store it before discarding the response, because it cannot be retrieved again.

    Args:
        body (CreateTokenRequest): Mint a new token. ``expires_in_days`` omitted/null means it
            never expires.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenCreatedResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateTokenRequest,
) -> TokenCreatedResponse | None:
    """Create a personal access token

     Issues a new personal access token for the authenticated user. The token value appears exactly once,
    in this response — store it before discarding the response, because it cannot be retrieved again.

    Args:
        body (CreateTokenRequest): Mint a new token. ``expires_in_days`` omitted/null means it
            never expires.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TokenCreatedResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateTokenRequest,
) -> Response[TokenCreatedResponse]:
    """Create a personal access token

     Issues a new personal access token for the authenticated user. The token value appears exactly once,
    in this response — store it before discarding the response, because it cannot be retrieved again.

    Args:
        body (CreateTokenRequest): Mint a new token. ``expires_in_days`` omitted/null means it
            never expires.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenCreatedResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateTokenRequest,
) -> TokenCreatedResponse | None:
    """Create a personal access token

     Issues a new personal access token for the authenticated user. The token value appears exactly once,
    in this response — store it before discarding the response, because it cannot be retrieved again.

    Args:
        body (CreateTokenRequest): Mint a new token. ``expires_in_days`` omitted/null means it
            never expires.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TokenCreatedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
