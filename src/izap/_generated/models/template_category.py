from typing import Literal

TemplateCategory = Literal["authentication", "marketing", "utility"]

TEMPLATE_CATEGORY_VALUES: set[TemplateCategory] = {
    "authentication",
    "marketing",
    "utility",
}


def check_template_category(value: str) -> TemplateCategory:
    if value in TEMPLATE_CATEGORY_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEMPLATE_CATEGORY_VALUES!r}")
