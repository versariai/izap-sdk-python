from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.whats_app_number_out_messaging_backend import (
    WhatsAppNumberOutMessagingBackend,
    check_whats_app_number_out_messaging_backend,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WhatsAppNumberOut")


@_attrs_define
class WhatsAppNumberOut:
    """
    Attributes:
        id (UUID):
        phone_number (str):
        assistant_id (None | Unset | UUID):
        assistant_name (None | str | Unset):
        code_verification_status (None | str | Unset):
        display_phone_number (None | str | Unset):
        messaging_backend (WhatsAppNumberOutMessagingBackend | Unset):  Default: 'izap'.
        phone_number_id (None | str | Unset):
        platform_type (None | str | Unset):
        quality_rating (None | str | Unset):
        status (None | str | Unset):
        verified_name (None | str | Unset):
        waba_id (None | str | Unset):
    """

    id: UUID
    phone_number: str
    assistant_id: None | Unset | UUID = UNSET
    assistant_name: None | str | Unset = UNSET
    code_verification_status: None | str | Unset = UNSET
    display_phone_number: None | str | Unset = UNSET
    messaging_backend: WhatsAppNumberOutMessagingBackend | Unset = "izap"
    phone_number_id: None | str | Unset = UNSET
    platform_type: None | str | Unset = UNSET
    quality_rating: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    verified_name: None | str | Unset = UNSET
    waba_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        phone_number = self.phone_number

        assistant_id: None | str | Unset
        if isinstance(self.assistant_id, Unset):
            assistant_id = UNSET
        elif isinstance(self.assistant_id, UUID):
            assistant_id = str(self.assistant_id)
        else:
            assistant_id = self.assistant_id

        assistant_name: None | str | Unset
        if isinstance(self.assistant_name, Unset):
            assistant_name = UNSET
        else:
            assistant_name = self.assistant_name

        code_verification_status: None | str | Unset
        if isinstance(self.code_verification_status, Unset):
            code_verification_status = UNSET
        else:
            code_verification_status = self.code_verification_status

        display_phone_number: None | str | Unset
        if isinstance(self.display_phone_number, Unset):
            display_phone_number = UNSET
        else:
            display_phone_number = self.display_phone_number

        messaging_backend: str | Unset = UNSET
        if not isinstance(self.messaging_backend, Unset):
            messaging_backend = self.messaging_backend

        phone_number_id: None | str | Unset
        if isinstance(self.phone_number_id, Unset):
            phone_number_id = UNSET
        else:
            phone_number_id = self.phone_number_id

        platform_type: None | str | Unset
        if isinstance(self.platform_type, Unset):
            platform_type = UNSET
        else:
            platform_type = self.platform_type

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

        waba_id: None | str | Unset
        if isinstance(self.waba_id, Unset):
            waba_id = UNSET
        else:
            waba_id = self.waba_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "phone_number": phone_number,
            }
        )
        if assistant_id is not UNSET:
            field_dict["assistant_id"] = assistant_id
        if assistant_name is not UNSET:
            field_dict["assistant_name"] = assistant_name
        if code_verification_status is not UNSET:
            field_dict["code_verification_status"] = code_verification_status
        if display_phone_number is not UNSET:
            field_dict["display_phone_number"] = display_phone_number
        if messaging_backend is not UNSET:
            field_dict["messaging_backend"] = messaging_backend
        if phone_number_id is not UNSET:
            field_dict["phone_number_id"] = phone_number_id
        if platform_type is not UNSET:
            field_dict["platform_type"] = platform_type
        if quality_rating is not UNSET:
            field_dict["quality_rating"] = quality_rating
        if status is not UNSET:
            field_dict["status"] = status
        if verified_name is not UNSET:
            field_dict["verified_name"] = verified_name
        if waba_id is not UNSET:
            field_dict["waba_id"] = waba_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        phone_number = d.pop("phone_number")

        def _parse_assistant_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assistant_id_type_0 = UUID(data)

                return assistant_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        assistant_id = _parse_assistant_id(d.pop("assistant_id", UNSET))

        def _parse_assistant_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assistant_name = _parse_assistant_name(d.pop("assistant_name", UNSET))

        def _parse_code_verification_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_verification_status = _parse_code_verification_status(d.pop("code_verification_status", UNSET))

        def _parse_display_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_phone_number = _parse_display_phone_number(d.pop("display_phone_number", UNSET))

        _messaging_backend = d.pop("messaging_backend", UNSET)
        messaging_backend: WhatsAppNumberOutMessagingBackend | Unset
        if isinstance(_messaging_backend, Unset):
            messaging_backend = UNSET
        else:
            messaging_backend = check_whats_app_number_out_messaging_backend(_messaging_backend)

        def _parse_phone_number_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number_id = _parse_phone_number_id(d.pop("phone_number_id", UNSET))

        def _parse_platform_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform_type = _parse_platform_type(d.pop("platform_type", UNSET))

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

        def _parse_waba_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        waba_id = _parse_waba_id(d.pop("waba_id", UNSET))

        whats_app_number_out = cls(
            id=id,
            phone_number=phone_number,
            assistant_id=assistant_id,
            assistant_name=assistant_name,
            code_verification_status=code_verification_status,
            display_phone_number=display_phone_number,
            messaging_backend=messaging_backend,
            phone_number_id=phone_number_id,
            platform_type=platform_type,
            quality_rating=quality_rating,
            status=status,
            verified_name=verified_name,
            waba_id=waba_id,
        )

        whats_app_number_out.additional_properties = d
        return whats_app_number_out

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
