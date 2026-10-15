from typing import Literal

WhatsAppNumberOutMessagingBackend = Literal["external", "izap"]

WHATS_APP_NUMBER_OUT_MESSAGING_BACKEND_VALUES: set[WhatsAppNumberOutMessagingBackend] = {
    "external",
    "izap",
}


def check_whats_app_number_out_messaging_backend(value: str) -> WhatsAppNumberOutMessagingBackend:
    if value in WHATS_APP_NUMBER_OUT_MESSAGING_BACKEND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WHATS_APP_NUMBER_OUT_MESSAGING_BACKEND_VALUES!r}")
