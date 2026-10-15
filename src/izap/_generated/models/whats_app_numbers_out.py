from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.whats_app_number_out import WhatsAppNumberOut


T = TypeVar("T", bound="WhatsAppNumbersOut")


@_attrs_define
class WhatsAppNumbersOut:
    """
    Attributes:
        numbers (list[WhatsAppNumberOut]):
        viewer_is_owner (bool):
    """

    numbers: list[WhatsAppNumberOut]
    viewer_is_owner: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        numbers = []
        for numbers_item_data in self.numbers:
            numbers_item = numbers_item_data.to_dict()
            numbers.append(numbers_item)

        viewer_is_owner = self.viewer_is_owner

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "numbers": numbers,
                "viewer_is_owner": viewer_is_owner,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_number_out import WhatsAppNumberOut  # noqa: PLC0415

        d = dict(src_dict)
        numbers = []
        _numbers = d.pop("numbers")
        for numbers_item_data in _numbers:
            numbers_item = WhatsAppNumberOut.from_dict(numbers_item_data)

            numbers.append(numbers_item)

        viewer_is_owner = d.pop("viewer_is_owner")

        whats_app_numbers_out = cls(
            numbers=numbers,
            viewer_is_owner=viewer_is_owner,
        )

        whats_app_numbers_out.additional_properties = d
        return whats_app_numbers_out

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
