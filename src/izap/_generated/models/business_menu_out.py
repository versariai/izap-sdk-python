from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.menus_out import MenusOut


T = TypeVar("T", bound="BusinessMenuOut")


@_attrs_define
class BusinessMenuOut:
    """
    Attributes:
        business_name (str):
        id (UUID):
        menus (list[MenusOut]):
    """

    business_name: str
    id: UUID
    menus: list[MenusOut]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_name = self.business_name

        id = str(self.id)

        menus = []
        for menus_item_data in self.menus:
            menus_item = menus_item_data.to_dict()
            menus.append(menus_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_name": business_name,
                "id": id,
                "menus": menus,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.menus_out import MenusOut  # noqa: PLC0415

        d = dict(src_dict)
        business_name = d.pop("business_name")

        id = UUID(d.pop("id"))

        menus = []
        _menus = d.pop("menus")
        for menus_item_data in _menus:
            menus_item = MenusOut.from_dict(menus_item_data)

            menus.append(menus_item)

        business_menu_out = cls(
            business_name=business_name,
            id=id,
            menus=menus,
        )

        business_menu_out.additional_properties = d
        return business_menu_out

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
