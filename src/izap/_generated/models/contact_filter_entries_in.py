from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_filter_list import ContactFilterList, check_contact_filter_list
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactFilterEntriesIn")


@_attrs_define
class ContactFilterEntriesIn:
    """
    Attributes:
        list_ (ContactFilterList):
        phone_numbers (list[str]): A WhatsApp phone number with its country code (`+5585987504325`; spaces, dashes and
            parentheses are ignored), or a WhatsApp business-scoped user ID for contacts whose number is hidden. Numbers are
            stored in canonical E.164 form.
        label (None | str | Unset): Optional note stored with each contact.
    """

    list_: ContactFilterList
    phone_numbers: list[str]
    label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_: str = self.list_

        phone_numbers = self.phone_numbers

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "list": list_,
                "phone_numbers": phone_numbers,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        list_ = check_contact_filter_list(d.pop("list"))

        phone_numbers = cast(list[str], d.pop("phone_numbers"))

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        contact_filter_entries_in = cls(
            list_=list_,
            phone_numbers=phone_numbers,
            label=label,
        )

        contact_filter_entries_in.additional_properties = d
        return contact_filter_entries_in

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
