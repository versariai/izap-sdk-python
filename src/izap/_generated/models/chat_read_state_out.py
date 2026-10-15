from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatReadStateOut")


@_attrs_define
class ChatReadStateOut:
    """The shared read / snooze state of one conversation.

    Attributes:
        business_id (UUID):
        chat_id (UUID):
        last_read_at (datetime.datetime | None | Unset):
        snoozed_until (datetime.datetime | None | Unset):
    """

    business_id: UUID
    chat_id: UUID
    last_read_at: datetime.datetime | None | Unset = UNSET
    snoozed_until: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id = str(self.business_id)

        chat_id = str(self.chat_id)

        last_read_at: None | str | Unset
        if isinstance(self.last_read_at, Unset):
            last_read_at = UNSET
        elif isinstance(self.last_read_at, datetime.datetime):
            last_read_at = self.last_read_at.isoformat()
        else:
            last_read_at = self.last_read_at

        snoozed_until: None | str | Unset
        if isinstance(self.snoozed_until, Unset):
            snoozed_until = UNSET
        elif isinstance(self.snoozed_until, datetime.datetime):
            snoozed_until = self.snoozed_until.isoformat()
        else:
            snoozed_until = self.snoozed_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_id": business_id,
                "chat_id": chat_id,
            }
        )
        if last_read_at is not UNSET:
            field_dict["last_read_at"] = last_read_at
        if snoozed_until is not UNSET:
            field_dict["snoozed_until"] = snoozed_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_id = UUID(d.pop("business_id"))

        chat_id = UUID(d.pop("chat_id"))

        def _parse_last_read_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_read_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_read_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_read_at = _parse_last_read_at(d.pop("last_read_at", UNSET))

        def _parse_snoozed_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                snoozed_until_type_0 = datetime.datetime.fromisoformat(data)

                return snoozed_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        snoozed_until = _parse_snoozed_until(d.pop("snoozed_until", UNSET))

        chat_read_state_out = cls(
            business_id=business_id,
            chat_id=chat_id,
            last_read_at=last_read_at,
            snoozed_until=snoozed_until,
        )

        chat_read_state_out.additional_properties = d
        return chat_read_state_out

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
