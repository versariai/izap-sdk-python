from typing import Literal

TemplateHeaderFormat = Literal["document", "image", "none", "text", "video"]

TEMPLATE_HEADER_FORMAT_VALUES: set[TemplateHeaderFormat] = {
    "document",
    "image",
    "none",
    "text",
    "video",
}


def check_template_header_format(value: str) -> TemplateHeaderFormat:
    if value in TEMPLATE_HEADER_FORMAT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEMPLATE_HEADER_FORMAT_VALUES!r}")
