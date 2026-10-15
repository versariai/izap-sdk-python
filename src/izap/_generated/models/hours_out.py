from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HoursOut")


@_attrs_define
class HoursOut:
    """
    Attributes:
        end_hour (str):
        operating_days (list[Any]):
        start_hour (str):
    """

    end_hour: str
    operating_days: list[Any]
    start_hour: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_hour = self.end_hour

        operating_days = self.operating_days

        start_hour = self.start_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_hour": end_hour,
                "operating_days": operating_days,
                "start_hour": start_hour,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_hour = d.pop("end_hour")

        operating_days = cast(list[Any], d.pop("operating_days"))

        start_hour = d.pop("start_hour")

        hours_out = cls(
            end_hour=end_hour,
            operating_days=operating_days,
            start_hour=start_hour,
        )

        hours_out.additional_properties = d
        return hours_out

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
