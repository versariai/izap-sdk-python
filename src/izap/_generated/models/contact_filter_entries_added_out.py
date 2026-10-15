from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.contact_filter_entry_out import ContactFilterEntryOut


T = TypeVar("T", bound="ContactFilterEntriesAddedOut")


@_attrs_define
class ContactFilterEntriesAddedOut:
    """
    Attributes:
        added (list[ContactFilterEntryOut]):
        already_listed (list[str]): Contacts that were already on the list, in canonical form.
        invalid (list[str]): Inputs that are not a usable phone number, as sent.
    """

    added: list[ContactFilterEntryOut]
    already_listed: list[str]
    invalid: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added = []
        for added_item_data in self.added:
            added_item = added_item_data.to_dict()
            added.append(added_item)

        already_listed = self.already_listed

        invalid = self.invalid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "added": added,
                "already_listed": already_listed,
                "invalid": invalid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_filter_entry_out import ContactFilterEntryOut  # noqa: PLC0415

        d = dict(src_dict)
        added = []
        _added = d.pop("added")
        for added_item_data in _added:
            added_item = ContactFilterEntryOut.from_dict(added_item_data)

            added.append(added_item)

        already_listed = cast(list[str], d.pop("already_listed"))

        invalid = cast(list[str], d.pop("invalid"))

        contact_filter_entries_added_out = cls(
            added=added,
            already_listed=already_listed,
            invalid=invalid,
        )

        contact_filter_entries_added_out.additional_properties = d
        return contact_filter_entries_added_out

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
