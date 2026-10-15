from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_message_status import ChatMessageStatus, check_chat_message_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatMessageSummaryOut")


@_attrs_define
class ChatMessageSummaryOut:
    """A chat message as embedded in the send-message responses below.

    Attributes:
        content (None | str):
        error_code (int | None):
        error_reason (None | str):
        id (UUID):
        no_reply (bool):
        sender_user_id (None | UUID):
        status (ChatMessageStatus | None):
        timestamp (datetime.datetime):
        message_sid (None | str | Unset):
        receiver (None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    content: None | str
    error_code: int | None
    error_reason: None | str
    id: UUID
    no_reply: bool
    sender_user_id: None | UUID
    status: ChatMessageStatus | None
    timestamp: datetime.datetime
    message_sid: None | str | Unset = UNSET
    receiver: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: None | str
        content = self.content

        error_code: int | None
        error_code = self.error_code

        error_reason: None | str
        error_reason = self.error_reason

        id = str(self.id)

        no_reply = self.no_reply

        sender_user_id: None | str
        if isinstance(self.sender_user_id, UUID):
            sender_user_id = str(self.sender_user_id)
        else:
            sender_user_id = self.sender_user_id

        status: None | str
        if isinstance(self.status, str):
            status = self.status
        else:
            status = self.status

        timestamp = self.timestamp.isoformat()

        message_sid: None | str | Unset
        if isinstance(self.message_sid, Unset):
            message_sid = UNSET
        else:
            message_sid = self.message_sid

        receiver: None | str | Unset
        if isinstance(self.receiver, Unset):
            receiver = UNSET
        else:
            receiver = self.receiver

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "error_code": error_code,
                "error_reason": error_reason,
                "id": id,
                "no_reply": no_reply,
                "sender_user_id": sender_user_id,
                "status": status,
                "timestamp": timestamp,
            }
        )
        if message_sid is not UNSET:
            field_dict["message_sid"] = message_sid
        if receiver is not UNSET:
            field_dict["receiver"] = receiver
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_content(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content = _parse_content(d.pop("content"))

        def _parse_error_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        error_code = _parse_error_code(d.pop("error_code"))

        def _parse_error_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_reason = _parse_error_reason(d.pop("error_reason"))

        id = UUID(d.pop("id"))

        no_reply = d.pop("no_reply")

        def _parse_sender_user_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sender_user_id_type_0 = UUID(data)

                return sender_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        sender_user_id = _parse_sender_user_id(d.pop("sender_user_id"))

        def _parse_status(data: object) -> ChatMessageStatus | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = check_chat_message_status(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatMessageStatus | None, data)

        status = _parse_status(d.pop("status"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        def _parse_message_sid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_sid = _parse_message_sid(d.pop("message_sid", UNSET))

        def _parse_receiver(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        receiver = _parse_receiver(d.pop("receiver", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        chat_message_summary_out = cls(
            content=content,
            error_code=error_code,
            error_reason=error_reason,
            id=id,
            no_reply=no_reply,
            sender_user_id=sender_user_id,
            status=status,
            timestamp=timestamp,
            message_sid=message_sid,
            receiver=receiver,
            updated_at=updated_at,
        )

        chat_message_summary_out.additional_properties = d
        return chat_message_summary_out

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
