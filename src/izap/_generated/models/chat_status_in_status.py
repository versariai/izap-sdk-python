from typing import Literal

ChatStatusInStatus = Literal["archived", "blocked", "open", "pending", "resolved"]

CHAT_STATUS_IN_STATUS_VALUES: set[ChatStatusInStatus] = {
    "archived",
    "blocked",
    "open",
    "pending",
    "resolved",
}


def check_chat_status_in_status(value: str) -> ChatStatusInStatus:
    if value in CHAT_STATUS_IN_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHAT_STATUS_IN_STATUS_VALUES!r}")
