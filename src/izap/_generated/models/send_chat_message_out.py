from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_message_summary_out import ChatMessageSummaryOut


T = TypeVar("T", bound="SendChatMessageOut")


@_attrs_define
class SendChatMessageOut:
    """Response for ``POST /chats/{chat_id}/messages``.

    ``ai_messages``/``ai_response_pending`` are absent on the human-assistant
    path (no AI reply was generated) and present on the AI path — kept absent
    rather than null via ``response_model_exclude_unset`` on the route.

        Attributes:
            user_message (ChatMessageSummaryOut): A chat message as embedded in the send-message responses below.
            ai_messages (list[ChatMessageSummaryOut] | None | Unset):
            ai_response_pending (bool | None | Unset):
    """

    user_message: ChatMessageSummaryOut
    ai_messages: list[ChatMessageSummaryOut] | None | Unset = UNSET
    ai_response_pending: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_message = self.user_message.to_dict()

        ai_messages: list[dict[str, Any]] | None | Unset
        if isinstance(self.ai_messages, Unset):
            ai_messages = UNSET
        elif isinstance(self.ai_messages, list):
            ai_messages = []
            for ai_messages_type_0_item_data in self.ai_messages:
                ai_messages_type_0_item = ai_messages_type_0_item_data.to_dict()
                ai_messages.append(ai_messages_type_0_item)

        else:
            ai_messages = self.ai_messages

        ai_response_pending: bool | None | Unset
        if isinstance(self.ai_response_pending, Unset):
            ai_response_pending = UNSET
        else:
            ai_response_pending = self.ai_response_pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_message": user_message,
            }
        )
        if ai_messages is not UNSET:
            field_dict["ai_messages"] = ai_messages
        if ai_response_pending is not UNSET:
            field_dict["ai_response_pending"] = ai_response_pending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_message_summary_out import ChatMessageSummaryOut  # noqa: PLC0415

        d = dict(src_dict)
        user_message = ChatMessageSummaryOut.from_dict(d.pop("user_message"))

        def _parse_ai_messages(data: object) -> list[ChatMessageSummaryOut] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ai_messages_type_0 = []
                _ai_messages_type_0 = data
                for ai_messages_type_0_item_data in _ai_messages_type_0:
                    ai_messages_type_0_item = ChatMessageSummaryOut.from_dict(ai_messages_type_0_item_data)

                    ai_messages_type_0.append(ai_messages_type_0_item)

                return ai_messages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ChatMessageSummaryOut] | None | Unset, data)

        ai_messages = _parse_ai_messages(d.pop("ai_messages", UNSET))

        def _parse_ai_response_pending(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ai_response_pending = _parse_ai_response_pending(d.pop("ai_response_pending", UNSET))

        send_chat_message_out = cls(
            user_message=user_message,
            ai_messages=ai_messages,
            ai_response_pending=ai_response_pending,
        )

        send_chat_message_out.additional_properties = d
        return send_chat_message_out

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
