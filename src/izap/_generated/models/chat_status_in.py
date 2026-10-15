from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_status_in_status import ChatStatusInStatus, check_chat_status_in_status

T = TypeVar("T", bound="ChatStatusIn")


@_attrs_define
class ChatStatusIn:
    """The conversation's CRM status, as shown by the inbox status filter.

    Attributes:
        status (ChatStatusInStatus): New status for the conversation.
    """

    status: ChatStatusInStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = check_chat_status_in_status(d.pop("status"))

        chat_status_in = cls(
            status=status,
        )

        chat_status_in.additional_properties = d
        return chat_status_in

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
