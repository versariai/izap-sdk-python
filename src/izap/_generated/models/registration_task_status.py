from typing import Literal

RegistrationTaskStatus = Literal["completed", "failed", "pending", "processing"]

REGISTRATION_TASK_STATUS_VALUES: set[RegistrationTaskStatus] = {
    "completed",
    "failed",
    "pending",
    "processing",
}


def check_registration_task_status(value: str) -> RegistrationTaskStatus:
    if value in REGISTRATION_TASK_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGISTRATION_TASK_STATUS_VALUES!r}")
