from typing import Literal

TemplateStatus = Literal["approved", "disabled", "draft", "paused", "pending", "rejected"]

TEMPLATE_STATUS_VALUES: set[TemplateStatus] = {
    "approved",
    "disabled",
    "draft",
    "paused",
    "pending",
    "rejected",
}


def check_template_status(value: str) -> TemplateStatus:
    if value in TEMPLATE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEMPLATE_STATUS_VALUES!r}")
