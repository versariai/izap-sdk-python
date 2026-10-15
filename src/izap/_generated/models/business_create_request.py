from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessCreateRequest")


@_attrs_define
class BusinessCreateRequest:
    """
    Attributes:
        business_name (str):
        owner_contact (None | str | Unset):
        owner_name (None | str | Unset):
    """

    business_name: str
    owner_contact: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_name = self.business_name

        owner_contact: None | str | Unset
        if isinstance(self.owner_contact, Unset):
            owner_contact = UNSET
        else:
            owner_contact = self.owner_contact

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_name": business_name,
            }
        )
        if owner_contact is not UNSET:
            field_dict["owner_contact"] = owner_contact
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_name = d.pop("business_name")

        def _parse_owner_contact(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_contact = _parse_owner_contact(d.pop("owner_contact", UNSET))

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("owner_name", UNSET))

        business_create_request = cls(
            business_name=business_name,
            owner_contact=owner_contact,
            owner_name=owner_name,
        )

        business_create_request.additional_properties = d
        return business_create_request

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
