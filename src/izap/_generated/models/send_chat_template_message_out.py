from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_message_summary_out import ChatMessageSummaryOut


T = TypeVar("T", bound="SendChatTemplateMessageOut")


@_attrs_define
class SendChatTemplateMessageOut:
    """Response for ``POST /chats/{chat_id}/messages/template``.

    Attributes:
        user_message (ChatMessageSummaryOut): A chat message as embedded in the send-message responses below.
    """

    user_message: ChatMessageSummaryOut
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_message = self.user_message.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_message": user_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_message_summary_out import ChatMessageSummaryOut  # noqa: PLC0415

        d = dict(src_dict)
        user_message = ChatMessageSummaryOut.from_dict(d.pop("user_message"))

        send_chat_template_message_out = cls(
            user_message=user_message,
        )

        send_chat_template_message_out.additional_properties = d
        return send_chat_template_message_out

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
