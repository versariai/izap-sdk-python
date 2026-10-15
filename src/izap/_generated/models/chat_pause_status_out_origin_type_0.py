from typing import Literal

ChatPauseStatusOutOriginType0 = Literal["api", "human_support", "mcp", "off_hours", "operator", "smb_echo"]

CHAT_PAUSE_STATUS_OUT_ORIGIN_TYPE_0_VALUES: set[ChatPauseStatusOutOriginType0] = {
    "api",
    "human_support",
    "mcp",
    "off_hours",
    "operator",
    "smb_echo",
}


def check_chat_pause_status_out_origin_type_0(value: str) -> ChatPauseStatusOutOriginType0:
    if value in CHAT_PAUSE_STATUS_OUT_ORIGIN_TYPE_0_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHAT_PAUSE_STATUS_OUT_ORIGIN_TYPE_0_VALUES!r}")
