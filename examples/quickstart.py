"""List WhatsApp templates and chats, and send a message, with the iZap Python SDK.

export IZAP_TOKEN=izap_pat_...      # User Settings -> API Keys in the iZap dashboard
export IZAP_BUSINESS_ID=...         # the business to act on
python examples/quickstart.py                       # list templates and recent chats
python examples/quickstart.py <chat-id> "Hello!"    # ...and send a message to a chat
"""

from __future__ import annotations

import os
import sys
from uuid import UUID

import izap
from izap.api.chats import list_current_business_chats
from izap.api.messages import send_chat_message
from izap.api.whatsapp_templates import list_whats_app_templates
from izap.models import CreateMessageIn


def main() -> None:
    token = os.environ.get("IZAP_TOKEN")
    if not token:
        raise SystemExit("Set IZAP_TOKEN to a personal access token (User Settings -> API Keys).")

    try:
        with izap.Client(token, business_id=os.environ.get("IZAP_BUSINESS_ID")) as client:
            templates = list_whats_app_templates.sync(client=client)
            if templates is not None:
                print(f"{templates.total_count} WhatsApp templates")
                for template in templates.templates:
                    print(f"  {template.name} ({template.status})")

            chats = list_current_business_chats.sync(client=client, kind="real", page_size=5)
            if chats is not None:
                for chat in chats.chats:
                    print(f"chat {chat.id}")

            if len(sys.argv) >= 3:
                body = CreateMessageIn(content=sys.argv[2])
                sent = send_chat_message.sync(UUID(sys.argv[1]), client=client, body=body)
                if sent is not None:
                    print(f"sent message {sent.user_message.id}")
    except izap.IzapApiError as error:
        raise SystemExit(f"iZap API error: {error}") from error


if __name__ == "__main__":
    main()
