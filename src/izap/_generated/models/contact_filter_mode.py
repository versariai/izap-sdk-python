from typing import Literal

ContactFilterMode = Literal["allowlist", "blocklist", "off"]

CONTACT_FILTER_MODE_VALUES: set[ContactFilterMode] = {
    "allowlist",
    "blocklist",
    "off",
}


def check_contact_filter_mode(value: str) -> ContactFilterMode:
    if value in CONTACT_FILTER_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_FILTER_MODE_VALUES!r}")
