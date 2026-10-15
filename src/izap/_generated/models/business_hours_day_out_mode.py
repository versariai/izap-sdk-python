from typing import Literal

BusinessHoursDayOutMode = Literal["closed", "custom", "open_all_day"]

BUSINESS_HOURS_DAY_OUT_MODE_VALUES: set[BusinessHoursDayOutMode] = {
    "closed",
    "custom",
    "open_all_day",
}


def check_business_hours_day_out_mode(value: str) -> BusinessHoursDayOutMode:
    if value in BUSINESS_HOURS_DAY_OUT_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BUSINESS_HOURS_DAY_OUT_MODE_VALUES!r}")
