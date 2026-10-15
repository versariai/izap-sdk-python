from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.business_hours_day_out import BusinessHoursDayOut


T = TypeVar("T", bound="BusinessHoursOut")


@_attrs_define
class BusinessHoursOut:
    """
    Attributes:
        friday (BusinessHoursDayOut):
        monday (BusinessHoursDayOut):
        saturday (BusinessHoursDayOut):
        sunday (BusinessHoursDayOut):
        thursday (BusinessHoursDayOut):
        tuesday (BusinessHoursDayOut):
        wednesday (BusinessHoursDayOut):
    """

    friday: BusinessHoursDayOut
    monday: BusinessHoursDayOut
    saturday: BusinessHoursDayOut
    sunday: BusinessHoursDayOut
    thursday: BusinessHoursDayOut
    tuesday: BusinessHoursDayOut
    wednesday: BusinessHoursDayOut
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        friday = self.friday.to_dict()

        monday = self.monday.to_dict()

        saturday = self.saturday.to_dict()

        sunday = self.sunday.to_dict()

        thursday = self.thursday.to_dict()

        tuesday = self.tuesday.to_dict()

        wednesday = self.wednesday.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "friday": friday,
                "monday": monday,
                "saturday": saturday,
                "sunday": sunday,
                "thursday": thursday,
                "tuesday": tuesday,
                "wednesday": wednesday,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_hours_day_out import BusinessHoursDayOut  # noqa: PLC0415

        d = dict(src_dict)
        friday = BusinessHoursDayOut.from_dict(d.pop("friday"))

        monday = BusinessHoursDayOut.from_dict(d.pop("monday"))

        saturday = BusinessHoursDayOut.from_dict(d.pop("saturday"))

        sunday = BusinessHoursDayOut.from_dict(d.pop("sunday"))

        thursday = BusinessHoursDayOut.from_dict(d.pop("thursday"))

        tuesday = BusinessHoursDayOut.from_dict(d.pop("tuesday"))

        wednesday = BusinessHoursDayOut.from_dict(d.pop("wednesday"))

        business_hours_out = cls(
            friday=friday,
            monday=monday,
            saturday=saturday,
            sunday=sunday,
            thursday=thursday,
            tuesday=tuesday,
            wednesday=wednesday,
        )

        business_hours_out.additional_properties = d
        return business_hours_out

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
