from typing import Literal

ContactFilterList = Literal["allow", "block"]

CONTACT_FILTER_LIST_VALUES: set[ContactFilterList] = {
    "allow",
    "block",
}


def check_contact_filter_list(value: str) -> ContactFilterList:
    if value in CONTACT_FILTER_LIST_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_FILTER_LIST_VALUES!r}")
