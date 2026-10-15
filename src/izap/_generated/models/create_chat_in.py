from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateChatIn")


@_attrs_define
class CreateChatIn:
    """
    Attributes:
        chatbot_id (None | Unset | UUID):
        instructions (list[Any] | None | Unset):
        session_id (None | Unset | UUID):
    """

    chatbot_id: None | Unset | UUID = UNSET
    instructions: list[Any] | None | Unset = UNSET
    session_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chatbot_id: None | str | Unset
        if isinstance(self.chatbot_id, Unset):
            chatbot_id = UNSET
        elif isinstance(self.chatbot_id, UUID):
            chatbot_id = str(self.chatbot_id)
        else:
            chatbot_id = self.chatbot_id

        instructions: list[Any] | None | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        elif isinstance(self.instructions, list):
            instructions = self.instructions

        else:
            instructions = self.instructions

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        elif isinstance(self.session_id, UUID):
            session_id = str(self.session_id)
        else:
            session_id = self.session_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chatbot_id is not UNSET:
            field_dict["chatbot_id"] = chatbot_id
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if session_id is not UNSET:
            field_dict["session_id"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_chatbot_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chatbot_id_type_0 = UUID(data)

                return chatbot_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        chatbot_id = _parse_chatbot_id(d.pop("chatbot_id", UNSET))

        def _parse_instructions(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                instructions_type_0 = cast(list[Any], data)

                return instructions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))

        def _parse_session_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                session_id_type_0 = UUID(data)

                return session_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        create_chat_in = cls(
            chatbot_id=chatbot_id,
            instructions=instructions,
            session_id=session_id,
        )

        create_chat_in.additional_properties = d
        return create_chat_in

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
