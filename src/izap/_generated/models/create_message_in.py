from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_attachment import MessageAttachment


T = TypeVar("T", bound="CreateMessageIn")


@_attrs_define
class CreateMessageIn:
    """Schema for creating a new message in a chat

    Attributes:
        content (str):
        attachments (list[MessageAttachment] | None | Unset):
        sender (None | str | Unset):
        sender_user_id (None | Unset | UUID):
    """

    content: str
    attachments: list[MessageAttachment] | None | Unset = UNSET
    sender: None | str | Unset = UNSET
    sender_user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

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

        sender: None | str | Unset
        if isinstance(self.sender, Unset):
            sender = UNSET
        else:
            sender = self.sender

        sender_user_id: None | str | Unset
        if isinstance(self.sender_user_id, Unset):
            sender_user_id = UNSET
        elif isinstance(self.sender_user_id, UUID):
            sender_user_id = str(self.sender_user_id)
        else:
            sender_user_id = self.sender_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if sender is not UNSET:
            field_dict["sender"] = sender
        if sender_user_id is not UNSET:
            field_dict["sender_user_id"] = sender_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_attachment import MessageAttachment  # noqa: PLC0415

        d = dict(src_dict)
        content = d.pop("content")

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

        def _parse_sender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender = _parse_sender(d.pop("sender", UNSET))

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

        create_message_in = cls(
            content=content,
            attachments=attachments,
            sender=sender,
            sender_user_id=sender_user_id,
        )

        create_message_in.additional_properties = d
        return create_message_in

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
