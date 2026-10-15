from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateSyncResponse")


@_attrs_define
class TemplateSyncResponse:
    """Result of a sync against the WhatsApp Cloud backend.

    Attributes:
        created (int):
        message (str):
        synced (int):
        updated (int):
        unchanged (int | Unset):  Default: 0.
    """

    created: int
    message: str
    synced: int
    updated: int
    unchanged: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        message = self.message

        synced = self.synced

        updated = self.updated

        unchanged = self.unchanged

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "message": message,
                "synced": synced,
                "updated": updated,
            }
        )
        if unchanged is not UNSET:
            field_dict["unchanged"] = unchanged

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        message = d.pop("message")

        synced = d.pop("synced")

        updated = d.pop("updated")

        unchanged = d.pop("unchanged", UNSET)

        template_sync_response = cls(
            created=created,
            message=message,
            synced=synced,
            updated=updated,
            unchanged=unchanged,
        )

        template_sync_response.additional_properties = d
        return template_sync_response

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
