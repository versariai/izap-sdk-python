from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_assistant_pause_out_status import ChatAssistantPauseOutStatus, check_chat_assistant_pause_out_status

T = TypeVar("T", bound="ChatAssistantPauseOut")


@_attrs_define
class ChatAssistantPauseOut:
    """Response for ``POST /chats/{chat_id}/pause`` and ``.../unpause``.

    Attributes:
        business_id (UUID):
        chat_id (UUID):
        phone_number (None | str):
        status (ChatAssistantPauseOutStatus):
    """

    business_id: UUID
    chat_id: UUID
    phone_number: None | str
    status: ChatAssistantPauseOutStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id = str(self.business_id)

        chat_id = str(self.chat_id)

        phone_number: None | str
        phone_number = self.phone_number

        status: str = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_id": business_id,
                "chat_id": chat_id,
                "phone_number": phone_number,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_id = UUID(d.pop("business_id"))

        chat_id = UUID(d.pop("chat_id"))

        def _parse_phone_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone_number = _parse_phone_number(d.pop("phone_number"))

        status = check_chat_assistant_pause_out_status(d.pop("status"))

        chat_assistant_pause_out = cls(
            business_id=business_id,
            chat_id=chat_id,
            phone_number=phone_number,
            status=status,
        )

        chat_assistant_pause_out.additional_properties = d
        return chat_assistant_pause_out

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
