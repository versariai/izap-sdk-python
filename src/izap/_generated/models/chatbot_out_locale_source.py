from typing import Literal

ChatbotOutLocaleSource = Literal["configured", "default", "inferred"]

CHATBOT_OUT_LOCALE_SOURCE_VALUES: set[ChatbotOutLocaleSource] = {
    "configured",
    "default",
    "inferred",
}


def check_chatbot_out_locale_source(value: str) -> ChatbotOutLocaleSource:
    if value in CHATBOT_OUT_LOCALE_SOURCE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHATBOT_OUT_LOCALE_SOURCE_VALUES!r}")
