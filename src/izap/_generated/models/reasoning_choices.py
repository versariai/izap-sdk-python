from typing import Literal

ReasoningChoices = Literal["high", "low", "medium", "minimal", "none", "xhigh"]

REASONING_CHOICES_VALUES: set[ReasoningChoices] = {
    "high",
    "low",
    "medium",
    "minimal",
    "none",
    "xhigh",
}


def check_reasoning_choices(value: str) -> ReasoningChoices:
    if value in REASONING_CHOICES_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REASONING_CHOICES_VALUES!r}")
