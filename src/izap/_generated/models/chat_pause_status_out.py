from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_pause_status_out_origin_type_0 import (
    ChatPauseStatusOutOriginType0,
    check_chat_pause_status_out_origin_type_0,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatPauseStatusOut")


@_attrs_define
class ChatPauseStatusOut:
    """Response for ``GET /chats/{chat_id}/pause-status``.

    Attributes:
        business_id (UUID):
        chat_id (UUID):
        hold (bool):
        is_paused (bool):
        phone_number (None | str):
        ttl_seconds (int | None):
        held_at (datetime.datetime | None | Unset):
        held_by_user_id (None | Unset | UUID):
        origin (ChatPauseStatusOutOriginType0 | None | Unset):
    """

    business_id: UUID
    chat_id: UUID
    hold: bool
    is_paused: bool
    phone_number: None | str
    ttl_seconds: int | None
    held_at: datetime.datetime | None | Unset = UNSET
    held_by_user_id: None | Unset | UUID = UNSET
    origin: ChatPauseStatusOutOriginType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id = str(self.business_id)

        chat_id = str(self.chat_id)

        hold = self.hold

        is_paused = self.is_paused

        phone_number: None | str
        phone_number = self.phone_number

        ttl_seconds: int | None
        ttl_seconds = self.ttl_seconds

        held_at: None | str | Unset
        if isinstance(self.held_at, Unset):
            held_at = UNSET
        elif isinstance(self.held_at, datetime.datetime):
            held_at = self.held_at.isoformat()
        else:
            held_at = self.held_at

        held_by_user_id: None | str | Unset
        if isinstance(self.held_by_user_id, Unset):
            held_by_user_id = UNSET
        elif isinstance(self.held_by_user_id, UUID):
            held_by_user_id = str(self.held_by_user_id)
        else:
            held_by_user_id = self.held_by_user_id

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        elif isinstance(self.origin, str):
            origin = self.origin
        else:
            origin = self.origin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_id": business_id,
                "chat_id": chat_id,
                "hold": hold,
                "is_paused": is_paused,
                "phone_number": phone_number,
                "ttl_seconds": ttl_seconds,
            }
        )
        if held_at is not UNSET:
            field_dict["held_at"] = held_at
        if held_by_user_id is not UNSET:
            field_dict["held_by_user_id"] = held_by_user_id
        if origin is not UNSET:
            field_dict["origin"] = origin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_id = UUID(d.pop("business_id"))

        chat_id = UUID(d.pop("chat_id"))

        hold = d.pop("hold")

        is_paused = d.pop("is_paused")

        def _parse_phone_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone_number = _parse_phone_number(d.pop("phone_number"))

        def _parse_ttl_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ttl_seconds = _parse_ttl_seconds(d.pop("ttl_seconds"))

        def _parse_held_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                held_at_type_0 = datetime.datetime.fromisoformat(data)

                return held_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        held_at = _parse_held_at(d.pop("held_at", UNSET))

        def _parse_held_by_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                held_by_user_id_type_0 = UUID(data)

                return held_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        held_by_user_id = _parse_held_by_user_id(d.pop("held_by_user_id", UNSET))

        def _parse_origin(data: object) -> ChatPauseStatusOutOriginType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_0 = check_chat_pause_status_out_origin_type_0(data)

                return origin_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatPauseStatusOutOriginType0 | None | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        chat_pause_status_out = cls(
            business_id=business_id,
            chat_id=chat_id,
            hold=hold,
            is_paused=is_paused,
            phone_number=phone_number,
            ttl_seconds=ttl_seconds,
            held_at=held_at,
            held_by_user_id=held_by_user_id,
            origin=origin,
        )

        chat_pause_status_out.additional_properties = d
        return chat_pause_status_out

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
