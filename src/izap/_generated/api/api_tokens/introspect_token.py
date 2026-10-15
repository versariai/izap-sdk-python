from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.principal_response import PrincipalResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/auth/token/introspect",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PrincipalResponse | None:
    if response.status_code == 200:
        response_200 = PrincipalResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PrincipalResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[PrincipalResponse]:
    """Introspect the presented credential

     Resolves the credential on the request to its principal, or returns `401` if it is not valid.
    Accepts a JWT, a session cookie, a personal access token or a business API key — use it to confirm
    that a token is still good and who it belongs to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrincipalResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> PrincipalResponse | None:
    """Introspect the presented credential

     Resolves the credential on the request to its principal, or returns `401` if it is not valid.
    Accepts a JWT, a session cookie, a personal access token or a business API key — use it to confirm
    that a token is still good and who it belongs to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PrincipalResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[PrincipalResponse]:
    """Introspect the presented credential

     Resolves the credential on the request to its principal, or returns `401` if it is not valid.
    Accepts a JWT, a session cookie, a personal access token or a business API key — use it to confirm
    that a token is still good and who it belongs to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrincipalResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> PrincipalResponse | None:
    """Introspect the presented credential

     Resolves the credential on the request to its principal, or returns `401` if it is not valid.
    Accepts a JWT, a session cookie, a personal access token or a business API key — use it to confirm
    that a token is still good and who it belongs to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PrincipalResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
