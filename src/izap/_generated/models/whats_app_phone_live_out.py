from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whats_app_phone_live_out_details_type_0 import WhatsAppPhoneLiveOutDetailsType0


T = TypeVar("T", bound="WhatsAppPhoneLiveOut")


@_attrs_define
class WhatsAppPhoneLiveOut:
    """
    Attributes:
        details (None | Unset | WhatsAppPhoneLiveOutDetailsType0):
        phone_number_id (None | str | Unset):
    """

    details: None | Unset | WhatsAppPhoneLiveOutDetailsType0 = UNSET
    phone_number_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.whats_app_phone_live_out_details_type_0 import WhatsAppPhoneLiveOutDetailsType0  # noqa: PLC0415

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, WhatsAppPhoneLiveOutDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        phone_number_id: None | str | Unset
        if isinstance(self.phone_number_id, Unset):
            phone_number_id = UNSET
        else:
            phone_number_id = self.phone_number_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if phone_number_id is not UNSET:
            field_dict["phone_number_id"] = phone_number_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_phone_live_out_details_type_0 import WhatsAppPhoneLiveOutDetailsType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_details(data: object) -> None | Unset | WhatsAppPhoneLiveOutDetailsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = WhatsAppPhoneLiveOutDetailsType0.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WhatsAppPhoneLiveOutDetailsType0, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_phone_number_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number_id = _parse_phone_number_id(d.pop("phone_number_id", UNSET))

        whats_app_phone_live_out = cls(
            details=details,
            phone_number_id=phone_number_id,
        )

        whats_app_phone_live_out.additional_properties = d
        return whats_app_phone_live_out

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
