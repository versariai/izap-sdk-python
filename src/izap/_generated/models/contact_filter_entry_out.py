from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactFilterEntryOut")


@_attrs_define
class ContactFilterEntryOut:
    """
    Attributes:
        created (datetime.datetime):
        id (UUID):
        phone_number (str): A WhatsApp phone number with its country code (`+5585987504325`; spaces, dashes and
            parentheses are ignored), or a WhatsApp business-scoped user ID for contacts whose number is hidden. Numbers are
            stored in canonical E.164 form.
        label (None | str | Unset):
    """

    created: datetime.datetime
    id: UUID
    phone_number: str
    label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        id = str(self.id)

        phone_number = self.phone_number

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "id": id,
                "phone_number": phone_number,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = UUID(d.pop("id"))

        phone_number = d.pop("phone_number")

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        contact_filter_entry_out = cls(
            created=created,
            id=id,
            phone_number=phone_number,
            label=label,
        )

        contact_filter_entry_out.additional_properties = d
        return contact_filter_entry_out

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
