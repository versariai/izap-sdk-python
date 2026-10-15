from typing import Literal

ChatAssistantPauseOutStatus = Literal["paused", "unpaused"]

CHAT_ASSISTANT_PAUSE_OUT_STATUS_VALUES: set[ChatAssistantPauseOutStatus] = {
    "paused",
    "unpaused",
}


def check_chat_assistant_pause_out_status(value: str) -> ChatAssistantPauseOutStatus:
    if value in CHAT_ASSISTANT_PAUSE_OUT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHAT_ASSISTANT_PAUSE_OUT_STATUS_VALUES!r}")
