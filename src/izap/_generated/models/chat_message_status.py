from typing import Literal

ChatMessageStatus = Literal[
    "accepted",
    "cancelled",
    "delivered",
    "failed",
    "new",
    "played",
    "queued",
    "read",
    "received",
    "receiving",
    "scheduled",
    "sending",
    "sent",
    "undelivered",
]

CHAT_MESSAGE_STATUS_VALUES: set[ChatMessageStatus] = {
    "accepted",
    "cancelled",
    "delivered",
    "failed",
    "new",
    "played",
    "queued",
    "read",
    "received",
    "receiving",
    "scheduled",
    "sending",
    "sent",
    "undelivered",
}


def check_chat_message_status(value: str) -> ChatMessageStatus:
    if value in CHAT_MESSAGE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHAT_MESSAGE_STATUS_VALUES!r}")
