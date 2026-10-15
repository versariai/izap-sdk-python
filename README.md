# izap

The Python SDK for the [iZap](https://izap.ai) API: WhatsApp messages, templates, chats,
transmissions and webhooks for your business.

- Typed request and response models, generated from iZap's public OpenAPI schema
- Sync and `asyncio` calls through one client
- Retries with backoff for idempotent requests, and one exception type for API errors
- Webhook signature verification

Requires Python 3.11 or newer. Python 3.10 is not supported: it reaches end of life in
October 2026, and 3.11 is the floor of the code generator the SDK is built with.

```bash
pip install izap
```

## Authentication

The SDK authenticates with a **personal access token**. Create one in the iZap dashboard
under **User Settings → API Keys**, which is available on plans that include the REST API.
Tokens start with `izap_pat_` and are shown once, so store yours as a secret.

Business-scoped endpoints act on the business selected by the `business-id` header
rather than a path parameter. Pass it once on the client:

```python
import os

import izap

client = izap.Client(os.environ["IZAP_TOKEN"], business_id=os.environ["IZAP_BUSINESS_ID"])
```

`client.with_business(other_id)` returns a copy scoped to another business, and passing
`business_id` directly to an endpoint function overrides the client for that call.

## Quickstart

Endpoint functions live in `izap.api`, one module per API area, and models in
`izap.models`. Each endpoint has four functions: `sync`, `sync_detailed` (which also
returns the status code and headers), `asyncio` and `asyncio_detailed`.

### List WhatsApp templates

```python
from izap.api.whatsapp_templates import list_whats_app_templates

with client:
    templates = list_whats_app_templates.sync(client=client, status="approved")
    for template in templates.templates:
        print(template.name, template.language)
```

### Send a message

```python
from izap.api.chats import list_current_business_chats
from izap.api.messages import send_chat_message
from izap.models import CreateMessageIn

with client:
    chats = list_current_business_chats.sync(client=client, kind="real", page_size=1)
    chat = chats.chats[0]
    sent = send_chat_message.sync(chat.id, client=client, body=CreateMessageIn(content="Your order is on its way"))
    print(sent.user_message.id)
```

`send_chat_message` sends as a human agent, and the assistant does not reply to it.
[`examples/quickstart.py`](examples/quickstart.py) runs both steps from the command line.

### Async

```python
import asyncio

import izap
from izap.api.whatsapp_templates import list_whats_app_templates


async def main() -> None:
    async with izap.AsyncClient(token, business_id=business_id) as client:
        templates = await list_whats_app_templates.asyncio(client=client)


asyncio.run(main())
```

## Errors

Every 4xx and 5xx response raises `izap.IzapApiError`:

```python
try:
    send_chat_message.sync(chat_id, client=client, body=CreateMessageIn(content="Hi"))
except izap.IzapApiError as error:
    print(error.status, error.code, error.message)
```

| Attribute  | Contents |
| ---------- | -------- |
| `status`   | The HTTP status code |
| `code`     | The machine-readable code when the API sends one, e.g. `plan_limit_event_webhooks` |
| `message`  | A human-readable summary |
| `detail`   | The raw `detail`: a string, a `{code, message}` object, or a 422's validation errors |
| `response` | The `httpx.Response` |

A successful response whose status the schema does not document returns `None`.

## Retries and timeouts

`GET`, `HEAD`, `OPTIONS`, `PUT` and `DELETE` requests answered with 429, 502, 503 or 504
are retried up to `max_retries` times (default 2). The client waits as long as
`Retry-After` asks, up to 60 seconds, and otherwise backs off exponentially from 0.5
seconds. `POST` and `PATCH` are never retried. `timeout` (default 30 seconds) applies to
each attempt.

```python
import httpx

client = izap.Client(token, max_retries=4, timeout=10.0, transport=httpx.HTTPTransport(proxy="http://proxy:3128"))
```

## Webhooks

iZap signs every webhook delivery. Verify it against the raw request body before you
trust it:

```python
import os

from flask import Flask, request

import izap

app = Flask(__name__)


@app.post("/hooks/izap")
def izap_webhook():
    try:
        event = izap.webhooks.verify(request.get_data(), request.headers, os.environ["IZAP_WEBHOOK_SECRET"])
    except izap.WebhookVerificationError:
        return "", 400
    if event.type == "message.received":
        handle_message(event.id, event.data["message"])
    return "", 204
```

Every delivery carries both `izap-webhook-signature` (v1) and the stronger
`izap-webhook-signature-v2`, which also covers the delivery id and closes a replay gap
in v1. `verify` requires v2 by default. Pass `allow_v1=True` only for senders from
before v2 existed; when both headers are present, v2 alone decides. It also rejects a
delivery whose
timestamp is more than `tolerance` seconds (default 300) from now, and returns a
`WebhookEvent` with `id`, `type`, `timestamp` and the parsed `data`. Retries and resends
of a delivery keep the same `event.id`, so use it to process each one once.
[`examples/webhook_receiver.py`](examples/webhook_receiver.py) is a receiver built on the
standard library, and the [webhook guide](https://devs.izap.ai/en/api-reference/webhooks)
covers registering endpoints and the event catalog.

## API reference

The modules in `izap.api` follow the [API reference](https://devs.izap.ai): `api_tokens`,
`business_library`, `businesses`, `chats`, `menus`, `messages`, `transmissions`,
`webhooks`, `whatsapp_cloud` and `whatsapp_templates`. Each function's docstring
describes its parameters and result.

## Development

This package lives in the iZap monorepo under `sdk/python`, as a standalone uv project.

```bash
uv sync
uv run python scripts/generate.py --check   # regenerate from the schema snapshot, fail on drift
uv run ruff check && uv run ruff format --check && uv run ty check
uv run pytest
bash scripts/ci.sh                          # all of the above, plus the tests on Python 3.11
```

`src/izap/_generated/` is generated by
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client),
pinned in `pyproject.toml`, from `openapi/izap-public.json`, a vendored copy of iZap's
public OpenAPI schema. Do not edit it by hand. `uv run python scripts/sync_schema.py`
refreshes the snapshot from the monorepo's `doc/external/devdocs/api-reference/openapi.json`
(or from `IZAP_OPENAPI_INPUT`), and `uv run python scripts/generate.py` regenerates from
it; commit both. Before generating, the script declares path parameters the schema
leaves undeclared, makes the `business-id` header an optional string and drops error
responses; its docstrings explain why.

The webhook vectors in `tests/fixtures/webhook_vectors.json` are signed by the backend's
own signer, so the tests pin the SDK to what the server sends. Regenerate them with
`scripts/webhook_vectors.py`.

## License

[MIT](LICENSE)
