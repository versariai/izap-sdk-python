from typing import Literal

ChatbotOutMessagingBackend = Literal["external", "izap"]

CHATBOT_OUT_MESSAGING_BACKEND_VALUES: set[ChatbotOutMessagingBackend] = {
    "external",
    "izap",
}


def check_chatbot_out_messaging_backend(value: str) -> ChatbotOutMessagingBackend:
    if value in CHATBOT_OUT_MESSAGING_BACKEND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHATBOT_OUT_MESSAGING_BACKEND_VALUES!r}")
