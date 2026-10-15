from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_consumer_out import ChatConsumerOut
    from ..models.last_message_out import LastMessageOut


T = TypeVar("T", bound="ChatOut")


@_attrs_define
class ChatOut:
    """
    Attributes:
        business_id (UUID):
        created (datetime.datetime):
        id (UUID):
        messages (list[Any]):
        session_id (UUID):
        timestamp (datetime.datetime):
        consumer (ChatConsumerOut | None | Unset):
        conversation_id (None | Unset | UUID):
        custom_instructions (list[Any] | None | Unset):
        instructions (list[Any] | None | Unset):
        kind (str | Unset):  Default: 'real'.
        last_message (LastMessageOut | None | Unset):
        refine_reviewed (bool | Unset):  Default: False.
        refine_verdict (None | str | Unset):
    """

    business_id: UUID
    created: datetime.datetime
    id: UUID
    messages: list[Any]
    session_id: UUID
    timestamp: datetime.datetime
    consumer: ChatConsumerOut | None | Unset = UNSET
    conversation_id: None | Unset | UUID = UNSET
    custom_instructions: list[Any] | None | Unset = UNSET
    instructions: list[Any] | None | Unset = UNSET
    kind: str | Unset = "real"
    last_message: LastMessageOut | None | Unset = UNSET
    refine_reviewed: bool | Unset = False
    refine_verdict: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_consumer_out import ChatConsumerOut  # noqa: PLC0415
        from ..models.last_message_out import LastMessageOut  # noqa: PLC0415

        business_id = str(self.business_id)

        created = self.created.isoformat()

        id = str(self.id)

        messages = self.messages

        session_id = str(self.session_id)

        timestamp = self.timestamp.isoformat()

        consumer: dict[str, Any] | None | Unset
        if isinstance(self.consumer, Unset):
            consumer = UNSET
        elif isinstance(self.consumer, ChatConsumerOut):
            consumer = self.consumer.to_dict()
        else:
            consumer = self.consumer

        conversation_id: None | str | Unset
        if isinstance(self.conversation_id, Unset):
            conversation_id = UNSET
        elif isinstance(self.conversation_id, UUID):
            conversation_id = str(self.conversation_id)
        else:
            conversation_id = self.conversation_id

        custom_instructions: list[Any] | None | Unset
        if isinstance(self.custom_instructions, Unset):
            custom_instructions = UNSET
        elif isinstance(self.custom_instructions, list):
            custom_instructions = self.custom_instructions

        else:
            custom_instructions = self.custom_instructions

        instructions: list[Any] | None | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        elif isinstance(self.instructions, list):
            instructions = self.instructions

        else:
            instructions = self.instructions

        kind = self.kind

        last_message: dict[str, Any] | None | Unset
        if isinstance(self.last_message, Unset):
            last_message = UNSET
        elif isinstance(self.last_message, LastMessageOut):
            last_message = self.last_message.to_dict()
        else:
            last_message = self.last_message

        refine_reviewed = self.refine_reviewed

        refine_verdict: None | str | Unset
        if isinstance(self.refine_verdict, Unset):
            refine_verdict = UNSET
        else:
            refine_verdict = self.refine_verdict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_id": business_id,
                "created": created,
                "id": id,
                "messages": messages,
                "session_id": session_id,
                "timestamp": timestamp,
            }
        )
        if consumer is not UNSET:
            field_dict["consumer"] = consumer
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if custom_instructions is not UNSET:
            field_dict["custom_instructions"] = custom_instructions
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if kind is not UNSET:
            field_dict["kind"] = kind
        if last_message is not UNSET:
            field_dict["last_message"] = last_message
        if refine_reviewed is not UNSET:
            field_dict["refine_reviewed"] = refine_reviewed
        if refine_verdict is not UNSET:
            field_dict["refine_verdict"] = refine_verdict

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_consumer_out import ChatConsumerOut  # noqa: PLC0415
        from ..models.last_message_out import LastMessageOut  # noqa: PLC0415

        d = dict(src_dict)
        business_id = UUID(d.pop("business_id"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = UUID(d.pop("id"))

        messages = cast(list[Any], d.pop("messages"))

        session_id = UUID(d.pop("session_id"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        def _parse_consumer(data: object) -> ChatConsumerOut | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                consumer_type_0 = ChatConsumerOut.from_dict(data)

                return consumer_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatConsumerOut | None | Unset, data)

        consumer = _parse_consumer(d.pop("consumer", UNSET))

        def _parse_conversation_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conversation_id_type_0 = UUID(data)

                return conversation_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        conversation_id = _parse_conversation_id(d.pop("conversation_id", UNSET))

        def _parse_custom_instructions(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_instructions_type_0 = cast(list[Any], data)

                return custom_instructions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        custom_instructions = _parse_custom_instructions(d.pop("custom_instructions", UNSET))

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

        kind = d.pop("kind", UNSET)

        def _parse_last_message(data: object) -> LastMessageOut | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_message_type_0 = LastMessageOut.from_dict(data)

                return last_message_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LastMessageOut | None | Unset, data)

        last_message = _parse_last_message(d.pop("last_message", UNSET))

        refine_reviewed = d.pop("refine_reviewed", UNSET)

        def _parse_refine_verdict(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refine_verdict = _parse_refine_verdict(d.pop("refine_verdict", UNSET))

        chat_out = cls(
            business_id=business_id,
            created=created,
            id=id,
            messages=messages,
            session_id=session_id,
            timestamp=timestamp,
            consumer=consumer,
            conversation_id=conversation_id,
            custom_instructions=custom_instructions,
            instructions=instructions,
            kind=kind,
            last_message=last_message,
            refine_reviewed=refine_reviewed,
            refine_verdict=refine_verdict,
        )

        chat_out.additional_properties = d
        return chat_out

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
