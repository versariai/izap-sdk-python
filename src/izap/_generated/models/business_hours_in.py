from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.business_hours_day_in import BusinessHoursDayIn


T = TypeVar("T", bound="BusinessHoursIn")


@_attrs_define
class BusinessHoursIn:
    """
    Attributes:
        friday (BusinessHoursDayIn):
        monday (BusinessHoursDayIn):
        saturday (BusinessHoursDayIn):
        sunday (BusinessHoursDayIn):
        thursday (BusinessHoursDayIn):
        tuesday (BusinessHoursDayIn):
        wednesday (BusinessHoursDayIn):
    """

    friday: BusinessHoursDayIn
    monday: BusinessHoursDayIn
    saturday: BusinessHoursDayIn
    sunday: BusinessHoursDayIn
    thursday: BusinessHoursDayIn
    tuesday: BusinessHoursDayIn
    wednesday: BusinessHoursDayIn
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
        from ..models.business_hours_day_in import BusinessHoursDayIn  # noqa: PLC0415

        d = dict(src_dict)
        friday = BusinessHoursDayIn.from_dict(d.pop("friday"))

        monday = BusinessHoursDayIn.from_dict(d.pop("monday"))

        saturday = BusinessHoursDayIn.from_dict(d.pop("saturday"))

        sunday = BusinessHoursDayIn.from_dict(d.pop("sunday"))

        thursday = BusinessHoursDayIn.from_dict(d.pop("thursday"))

        tuesday = BusinessHoursDayIn.from_dict(d.pop("tuesday"))

        wednesday = BusinessHoursDayIn.from_dict(d.pop("wednesday"))

        business_hours_in = cls(
            friday=friday,
            monday=monday,
            saturday=saturday,
            sunday=sunday,
            thursday=thursday,
            tuesday=tuesday,
            wednesday=wednesday,
        )

        business_hours_in.additional_properties = d
        return business_hours_in

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
