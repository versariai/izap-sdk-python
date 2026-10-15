from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_attachment import MessageAttachment


T = TypeVar("T", bound="SingleChatMessage")


@_attrs_define
class SingleChatMessage:
    """
    Attributes:
        chat_id (UUID):
        id (UUID):
        message (str):
        sender (str):
        status (str):
        timestamp (datetime.datetime):
        attachments (list[MessageAttachment] | None | Unset):
        error_code (int | None | Unset):
        error_reason (None | str | Unset):
        message_sid (None | str | Unset):
        no_reply (bool | Unset):  Default: False.
        receiver (None | str | Unset):
        sender_type (None | str | Unset):
        sender_user_id (None | Unset | UUID):
        updated_at (datetime.datetime | None | Unset):
        user_message (None | SingleChatMessage | Unset):
    """

    chat_id: UUID
    id: UUID
    message: str
    sender: str
    status: str
    timestamp: datetime.datetime
    attachments: list[MessageAttachment] | None | Unset = UNSET
    error_code: int | None | Unset = UNSET
    error_reason: None | str | Unset = UNSET
    message_sid: None | str | Unset = UNSET
    no_reply: bool | Unset = False
    receiver: None | str | Unset = UNSET
    sender_type: None | str | Unset = UNSET
    sender_user_id: None | Unset | UUID = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    user_message: None | SingleChatMessage | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chat_id = str(self.chat_id)

        id = str(self.id)

        message = self.message

        sender = self.sender

        status = self.status

        timestamp = self.timestamp.isoformat()

        attachments: list[dict[str, Any]] | None | Unset
        if isinstance(self.attachments, Unset):
            attachments = UNSET
        elif isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)

        else:
            attachments = self.attachments

        error_code: int | None | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        error_reason: None | str | Unset
        if isinstance(self.error_reason, Unset):
            error_reason = UNSET
        else:
            error_reason = self.error_reason

        message_sid: None | str | Unset
        if isinstance(self.message_sid, Unset):
            message_sid = UNSET
        else:
            message_sid = self.message_sid

        no_reply = self.no_reply

        receiver: None | str | Unset
        if isinstance(self.receiver, Unset):
            receiver = UNSET
        else:
            receiver = self.receiver

        sender_type: None | str | Unset
        if isinstance(self.sender_type, Unset):
            sender_type = UNSET
        else:
            sender_type = self.sender_type

        sender_user_id: None | str | Unset
        if isinstance(self.sender_user_id, Unset):
            sender_user_id = UNSET
        elif isinstance(self.sender_user_id, UUID):
            sender_user_id = str(self.sender_user_id)
        else:
            sender_user_id = self.sender_user_id

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

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
                "message": message,
                "sender": sender,
                "status": status,
                "timestamp": timestamp,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_reason is not UNSET:
            field_dict["error_reason"] = error_reason
        if message_sid is not UNSET:
            field_dict["message_sid"] = message_sid
        if no_reply is not UNSET:
            field_dict["no_reply"] = no_reply
        if receiver is not UNSET:
            field_dict["receiver"] = receiver
        if sender_type is not UNSET:
            field_dict["sender_type"] = sender_type
        if sender_user_id is not UNSET:
            field_dict["sender_user_id"] = sender_user_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_message is not UNSET:
            field_dict["user_message"] = user_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_attachment import MessageAttachment  # noqa: PLC0415

        d = dict(src_dict)
        chat_id = UUID(d.pop("chat_id"))

        id = UUID(d.pop("id"))

        message = d.pop("message")

        sender = d.pop("sender")

        status = d.pop("status")

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        def _parse_attachments(data: object) -> list[MessageAttachment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in _attachments_type_0:
                    attachments_type_0_item = MessageAttachment.from_dict(attachments_type_0_item_data)

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MessageAttachment] | None | Unset, data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))

        def _parse_error_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        error_code = _parse_error_code(d.pop("error_code", UNSET))

        def _parse_error_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_reason = _parse_error_reason(d.pop("error_reason", UNSET))

        def _parse_message_sid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_sid = _parse_message_sid(d.pop("message_sid", UNSET))

        no_reply = d.pop("no_reply", UNSET)

        def _parse_receiver(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        receiver = _parse_receiver(d.pop("receiver", UNSET))

        def _parse_sender_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_type = _parse_sender_type(d.pop("sender_type", UNSET))

        def _parse_sender_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sender_user_id_type_0 = UUID(data)

                return sender_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sender_user_id = _parse_sender_user_id(d.pop("sender_user_id", UNSET))

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

        single_chat_message = cls(
            chat_id=chat_id,
            id=id,
            message=message,
            sender=sender,
            status=status,
            timestamp=timestamp,
            attachments=attachments,
            error_code=error_code,
            error_reason=error_reason,
            message_sid=message_sid,
            no_reply=no_reply,
            receiver=receiver,
            sender_type=sender_type,
            sender_user_id=sender_user_id,
            updated_at=updated_at,
            user_message=user_message,
        )

        single_chat_message.additional_properties = d
        return single_chat_message

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
