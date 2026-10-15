"""A minimal iZap webhook receiver, standard library only.

    IZAP_WEBHOOK_SECRET=izap_whsec_... python examples/webhook_receiver.py

Expose it over HTTPS (iZap only delivers to https:// on port 443) and register that
URL as a webhook endpoint.
"""

from __future__ import annotations

import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import izap

SECRET = os.environ.get("IZAP_WEBHOOK_SECRET", "")
seen_deliveries: set[str] = set()


class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        body = self.rfile.read(int(self.headers.get("Content-Length", "0")))
        try:
            event = izap.webhooks.verify(body, dict(self.headers.items()), SECRET)
        except izap.WebhookVerificationError as exc:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(str(exc).encode())
            return

        # Retries and manual resends reuse the delivery id; handle each event once.
        if event.id not in seen_deliveries:
            seen_deliveries.add(event.id)
            message = event.data.get("message") or {}
            print(f"{event.type} from {message.get('from')}: {message.get('text')!r}")

        self.send_response(204)
        self.end_headers()


def main() -> None:
    if not SECRET:
        raise SystemExit("Set IZAP_WEBHOOK_SECRET to the endpoint's signing secret.")
    address = (os.environ.get("HOST", "127.0.0.1"), int(os.environ.get("PORT", "8080")))
    print(f"Listening on http://{address[0]}:{address[1]}")
    HTTPServer(address, WebhookHandler).serve_forever()


if __name__ == "__main__":
    main()
