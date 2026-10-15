from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatbotWhatsAppNumberOut")


@_attrs_define
class ChatbotWhatsAppNumberOut:
    """The WhatsApp number a chatbot answers on, as shown in the dash assistant card.

    Attributes:
        phone_number (str):
        display_phone_number (None | str | Unset):
        phone_number_id (None | str | Unset):
        quality_rating (None | str | Unset):
        status (None | str | Unset):
        verified_name (None | str | Unset):
    """

    phone_number: str
    display_phone_number: None | str | Unset = UNSET
    phone_number_id: None | str | Unset = UNSET
    quality_rating: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    verified_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_number = self.phone_number

        display_phone_number: None | str | Unset
        if isinstance(self.display_phone_number, Unset):
            display_phone_number = UNSET
        else:
            display_phone_number = self.display_phone_number

        phone_number_id: None | str | Unset
        if isinstance(self.phone_number_id, Unset):
            phone_number_id = UNSET
        else:
            phone_number_id = self.phone_number_id

        quality_rating: None | str | Unset
        if isinstance(self.quality_rating, Unset):
            quality_rating = UNSET
        else:
            quality_rating = self.quality_rating

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        verified_name: None | str | Unset
        if isinstance(self.verified_name, Unset):
            verified_name = UNSET
        else:
            verified_name = self.verified_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone_number": phone_number,
            }
        )
        if display_phone_number is not UNSET:
            field_dict["display_phone_number"] = display_phone_number
        if phone_number_id is not UNSET:
            field_dict["phone_number_id"] = phone_number_id
        if quality_rating is not UNSET:
            field_dict["quality_rating"] = quality_rating
        if status is not UNSET:
            field_dict["status"] = status
        if verified_name is not UNSET:
            field_dict["verified_name"] = verified_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone_number = d.pop("phone_number")

        def _parse_display_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_phone_number = _parse_display_phone_number(d.pop("display_phone_number", UNSET))

        def _parse_phone_number_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number_id = _parse_phone_number_id(d.pop("phone_number_id", UNSET))

        def _parse_quality_rating(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quality_rating = _parse_quality_rating(d.pop("quality_rating", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_verified_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        verified_name = _parse_verified_name(d.pop("verified_name", UNSET))

        chatbot_whats_app_number_out = cls(
            phone_number=phone_number,
            display_phone_number=display_phone_number,
            phone_number_id=phone_number_id,
            quality_rating=quality_rating,
            status=status,
            verified_name=verified_name,
        )

        chatbot_whats_app_number_out.additional_properties = d
        return chatbot_whats_app_number_out

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
