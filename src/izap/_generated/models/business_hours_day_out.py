from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.business_hours_day_out_mode import BusinessHoursDayOutMode, check_business_hours_day_out_mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_range_out import TimeRangeOut


T = TypeVar("T", bound="BusinessHoursDayOut")


@_attrs_define
class BusinessHoursDayOut:
    """
    Attributes:
        mode (BusinessHoursDayOutMode):
        ranges (list[TimeRangeOut] | Unset):
    """

    mode: BusinessHoursDayOutMode
    ranges: list[TimeRangeOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: str = self.mode

        ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if ranges is not UNSET:
            field_dict["ranges"] = ranges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time_range_out import TimeRangeOut  # noqa: PLC0415

        d = dict(src_dict)
        mode = check_business_hours_day_out_mode(d.pop("mode"))

        _ranges = d.pop("ranges", UNSET)
        ranges: list[TimeRangeOut] | Unset = UNSET
        if _ranges is not UNSET:
            ranges = []
            for ranges_item_data in _ranges:
                ranges_item = TimeRangeOut.from_dict(ranges_item_data)

                ranges.append(ranges_item)

        business_hours_day_out = cls(
            mode=mode,
            ranges=ranges,
        )

        business_hours_day_out.additional_properties = d
        return business_hours_day_out

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
