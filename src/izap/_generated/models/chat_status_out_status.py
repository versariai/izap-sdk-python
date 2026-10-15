from typing import Literal

ChatStatusOutStatus = Literal["archived", "blocked", "open", "pending", "resolved"]

CHAT_STATUS_OUT_STATUS_VALUES: set[ChatStatusOutStatus] = {
    "archived",
    "blocked",
    "open",
    "pending",
    "resolved",
}


def check_chat_status_out_status(value: str) -> ChatStatusOutStatus:
    if value in CHAT_STATUS_OUT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHAT_STATUS_OUT_STATUS_VALUES!r}")
