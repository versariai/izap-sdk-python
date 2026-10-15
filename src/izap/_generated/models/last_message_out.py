from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LastMessageOut")


@_attrs_define
class LastMessageOut:
    """
    Attributes:
        content (str):
        status (str):
        no_reply (bool | Unset):  Default: False.
    """

    content: str
    status: str
    no_reply: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        status = self.status

        no_reply = self.no_reply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "status": status,
            }
        )
        if no_reply is not UNSET:
            field_dict["no_reply"] = no_reply

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        status = d.pop("status")

        no_reply = d.pop("no_reply", UNSET)

        last_message_out = cls(
            content=content,
            status=status,
            no_reply=no_reply,
        )

        last_message_out.additional_properties = d
        return last_message_out

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
