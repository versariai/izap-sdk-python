from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_status_out_status import ChatStatusOutStatus, check_chat_status_out_status

T = TypeVar("T", bound="ChatStatusOut")


@_attrs_define
class ChatStatusOut:
    """
    Attributes:
        business_id (UUID):
        chat_id (UUID):
        status (ChatStatusOutStatus):
    """

    business_id: UUID
    chat_id: UUID
    status: ChatStatusOutStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id = str(self.business_id)

        chat_id = str(self.chat_id)

        status: str = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_id": business_id,
                "chat_id": chat_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_id = UUID(d.pop("business_id"))

        chat_id = UUID(d.pop("chat_id"))

        status = check_chat_status_out_status(d.pop("status"))

        chat_status_out = cls(
            business_id=business_id,
            chat_id=chat_id,
            status=status,
        )

        chat_status_out.additional_properties = d
        return chat_status_out

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
