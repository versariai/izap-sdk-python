from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_output_function import ResponseOutputFunction
    from ..models.single_chat_message import SingleChatMessage


T = TypeVar("T", bound="ChatMessageDetailsOut")


@_attrs_define
class ChatMessageDetailsOut:
    """
    Attributes:
        chat_id (UUID):
        id (UUID):
        sender (str):
        timestamp (datetime.datetime):
        chat_messages (list[SingleChatMessage] | None | Unset):
        function_calls (list[ResponseOutputFunction] | None | Unset):
        last_message_id (None | Unset | UUID):
        receiver (None | str | Unset):
        reply_group (ChatMessageDetailsOut | None | Unset):
        resp_id (None | str | Unset):
        user_message (None | SingleChatMessage | Unset):
    """

    chat_id: UUID
    id: UUID
    sender: str
    timestamp: datetime.datetime
    chat_messages: list[SingleChatMessage] | None | Unset = UNSET
    function_calls: list[ResponseOutputFunction] | None | Unset = UNSET
    last_message_id: None | Unset | UUID = UNSET
    receiver: None | str | Unset = UNSET
    reply_group: ChatMessageDetailsOut | None | Unset = UNSET
    resp_id: None | str | Unset = UNSET
    user_message: None | SingleChatMessage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.single_chat_message import SingleChatMessage  # noqa: PLC0415

        chat_id = str(self.chat_id)

        id = str(self.id)

        sender = self.sender

        timestamp = self.timestamp.isoformat()

        chat_messages: list[dict[str, Any]] | None | Unset
        if isinstance(self.chat_messages, Unset):
            chat_messages = UNSET
        elif isinstance(self.chat_messages, list):
            chat_messages = []
            for chat_messages_type_0_item_data in self.chat_messages:
                chat_messages_type_0_item = chat_messages_type_0_item_data.to_dict()
                chat_messages.append(chat_messages_type_0_item)

        else:
            chat_messages = self.chat_messages

        function_calls: list[dict[str, Any]] | None | Unset
        if isinstance(self.function_calls, Unset):
            function_calls = UNSET
        elif isinstance(self.function_calls, list):
            function_calls = []
            for function_calls_type_0_item_data in self.function_calls:
                function_calls_type_0_item = function_calls_type_0_item_data.to_dict()
                function_calls.append(function_calls_type_0_item)

        else:
            function_calls = self.function_calls

        last_message_id: None | str | Unset
        if isinstance(self.last_message_id, Unset):
            last_message_id = UNSET
        elif isinstance(self.last_message_id, UUID):
            last_message_id = str(self.last_message_id)
        else:
            last_message_id = self.last_message_id

        receiver: None | str | Unset
        if isinstance(self.receiver, Unset):
            receiver = UNSET
        else:
            receiver = self.receiver

        reply_group: dict[str, Any] | None | Unset
        if isinstance(self.reply_group, Unset):
            reply_group = UNSET
        elif isinstance(self.reply_group, ChatMessageDetailsOut):
            reply_group = self.reply_group.to_dict()
        else:
            reply_group = self.reply_group

        resp_id: None | str | Unset
        if isinstance(self.resp_id, Unset):
            resp_id = UNSET
        else:
            resp_id = self.resp_id

        user_message: dict[str, Any] | None | Unset
        if isinstance(self.user_message, Unset):
            user_message = UNSET
        elif isinstance(self.user_message, SingleChatMessage):
            user_message = self.user_message.to_dict()
        else:
            user_message = self.user_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chat_id": chat_id,
                "id": id,
                "sender": sender,
                "timestamp": timestamp,
            }
        )
        if chat_messages is not UNSET:
            field_dict["chat_messages"] = chat_messages
        if function_calls is not UNSET:
            field_dict["function_calls"] = function_calls
        if last_message_id is not UNSET:
            field_dict["last_message_id"] = last_message_id
        if receiver is not UNSET:
            field_dict["receiver"] = receiver
        if reply_group is not UNSET:
            field_dict["reply_group"] = reply_group
        if resp_id is not UNSET:
            field_dict["resp_id"] = resp_id
        if user_message is not UNSET:
            field_dict["user_message"] = user_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_output_function import ResponseOutputFunction  # noqa: PLC0415
        from ..models.single_chat_message import SingleChatMessage  # noqa: PLC0415

        d = dict(src_dict)
        chat_id = UUID(d.pop("chat_id"))

        id = UUID(d.pop("id"))

        sender = d.pop("sender")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        def _parse_chat_messages(data: object) -> list[SingleChatMessage] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                chat_messages_type_0 = []
                _chat_messages_type_0 = data
                for chat_messages_type_0_item_data in _chat_messages_type_0:
                    chat_messages_type_0_item = SingleChatMessage.from_dict(chat_messages_type_0_item_data)

                    chat_messages_type_0.append(chat_messages_type_0_item)

                return chat_messages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SingleChatMessage] | None | Unset, data)

        chat_messages = _parse_chat_messages(d.pop("chat_messages", UNSET))

        def _parse_function_calls(data: object) -> list[ResponseOutputFunction] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                function_calls_type_0 = []
                _function_calls_type_0 = data
                for function_calls_type_0_item_data in _function_calls_type_0:
                    function_calls_type_0_item = ResponseOutputFunction.from_dict(function_calls_type_0_item_data)

                    function_calls_type_0.append(function_calls_type_0_item)

                return function_calls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ResponseOutputFunction] | None | Unset, data)

        function_calls = _parse_function_calls(d.pop("function_calls", UNSET))

        def _parse_last_message_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_message_id_type_0 = UUID(data)

                return last_message_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        last_message_id = _parse_last_message_id(d.pop("last_message_id", UNSET))

        def _parse_receiver(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        receiver = _parse_receiver(d.pop("receiver", UNSET))

        def _parse_reply_group(data: object) -> ChatMessageDetailsOut | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reply_group_type_0 = ChatMessageDetailsOut.from_dict(data)

                return reply_group_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatMessageDetailsOut | None | Unset, data)

        reply_group = _parse_reply_group(d.pop("reply_group", UNSET))

        def _parse_resp_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resp_id = _parse_resp_id(d.pop("resp_id", UNSET))

        def _parse_user_message(data: object) -> None | SingleChatMessage | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_message_type_0 = SingleChatMessage.from_dict(data)

                return user_message_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SingleChatMessage | Unset, data)

        user_message = _parse_user_message(d.pop("user_message", UNSET))

        chat_message_details_out = cls(
            chat_id=chat_id,
            id=id,
            sender=sender,
            timestamp=timestamp,
            chat_messages=chat_messages,
            function_calls=function_calls,
            last_message_id=last_message_id,
            receiver=receiver,
            reply_group=reply_group,
            resp_id=resp_id,
            user_message=user_message,
        )

        chat_message_details_out.additional_properties = d
        return chat_message_details_out

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
