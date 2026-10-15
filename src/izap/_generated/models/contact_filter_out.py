from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_filter_mode import ContactFilterMode, check_contact_filter_mode

if TYPE_CHECKING:
    from ..models.contact_filter_entry_out import ContactFilterEntryOut


T = TypeVar("T", bound="ContactFilterOut")


@_attrs_define
class ContactFilterOut:
    """
    Attributes:
        allowlist (list[ContactFilterEntryOut]):
        blocklist (list[ContactFilterEntryOut]):
        mode (ContactFilterMode):
    """

    allowlist: list[ContactFilterEntryOut]
    blocklist: list[ContactFilterEntryOut]
    mode: ContactFilterMode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowlist = []
        for allowlist_item_data in self.allowlist:
            allowlist_item = allowlist_item_data.to_dict()
            allowlist.append(allowlist_item)

        blocklist = []
        for blocklist_item_data in self.blocklist:
            blocklist_item = blocklist_item_data.to_dict()
            blocklist.append(blocklist_item)

        mode: str = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowlist": allowlist,
                "blocklist": blocklist,
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_filter_entry_out import ContactFilterEntryOut  # noqa: PLC0415

        d = dict(src_dict)
        allowlist = []
        _allowlist = d.pop("allowlist")
        for allowlist_item_data in _allowlist:
            allowlist_item = ContactFilterEntryOut.from_dict(allowlist_item_data)

            allowlist.append(allowlist_item)

        blocklist = []
        _blocklist = d.pop("blocklist")
        for blocklist_item_data in _blocklist:
            blocklist_item = ContactFilterEntryOut.from_dict(blocklist_item_data)

            blocklist.append(blocklist_item)

        mode = check_contact_filter_mode(d.pop("mode"))

        contact_filter_out = cls(
            allowlist=allowlist,
            blocklist=blocklist,
            mode=mode,
        )

        contact_filter_out.additional_properties = d
        return contact_filter_out

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
