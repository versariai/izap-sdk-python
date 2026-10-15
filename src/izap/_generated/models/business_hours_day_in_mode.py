from typing import Literal

BusinessHoursDayInMode = Literal["closed", "custom", "open_all_day"]

BUSINESS_HOURS_DAY_IN_MODE_VALUES: set[BusinessHoursDayInMode] = {
    "closed",
    "custom",
    "open_all_day",
}


def check_business_hours_day_in_mode(value: str) -> BusinessHoursDayInMode:
    if value in BUSINESS_HOURS_DAY_IN_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUSINESS_HOURS_DAY_IN_MODE_VALUES!r}")
