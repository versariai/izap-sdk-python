from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WhatsAppCloudRegisterRequest")


@_attrs_define
class WhatsAppCloudRegisterRequest:
    """
    Attributes:
        code (str):
        phone_number_id (None | str | Unset):
        redirect_uri (None | str | Unset):
        waba_business_id (None | str | Unset):
        waba_id (None | str | Unset):
    """

    code: str
    phone_number_id: None | str | Unset = UNSET
    redirect_uri: None | str | Unset = UNSET
    waba_business_id: None | str | Unset = UNSET
    waba_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        phone_number_id: None | str | Unset
        if isinstance(self.phone_number_id, Unset):
            phone_number_id = UNSET
        else:
            phone_number_id = self.phone_number_id

        redirect_uri: None | str | Unset
        if isinstance(self.redirect_uri, Unset):
            redirect_uri = UNSET
        else:
            redirect_uri = self.redirect_uri

        waba_business_id: None | str | Unset
        if isinstance(self.waba_business_id, Unset):
            waba_business_id = UNSET
        else:
            waba_business_id = self.waba_business_id

        waba_id: None | str | Unset
        if isinstance(self.waba_id, Unset):
            waba_id = UNSET
        else:
            waba_id = self.waba_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
            }
        )
        if phone_number_id is not UNSET:
            field_dict["phone_number_id"] = phone_number_id
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if waba_business_id is not UNSET:
            field_dict["waba_business_id"] = waba_business_id
        if waba_id is not UNSET:
            field_dict["waba_id"] = waba_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        def _parse_phone_number_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number_id = _parse_phone_number_id(d.pop("phone_number_id", UNSET))

        def _parse_redirect_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        redirect_uri = _parse_redirect_uri(d.pop("redirect_uri", UNSET))

        def _parse_waba_business_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        waba_business_id = _parse_waba_business_id(d.pop("waba_business_id", UNSET))

        def _parse_waba_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        waba_id = _parse_waba_id(d.pop("waba_id", UNSET))

        whats_app_cloud_register_request = cls(
            code=code,
            phone_number_id=phone_number_id,
            redirect_uri=redirect_uri,
            waba_business_id=waba_business_id,
            waba_id=waba_id,
        )

        whats_app_cloud_register_request.additional_properties = d
        return whats_app_cloud_register_request

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
