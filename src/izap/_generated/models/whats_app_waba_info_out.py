from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.whats_app_waba_info_out_info_type_0 import WhatsAppWabaInfoOutInfoType0


T = TypeVar("T", bound="WhatsAppWabaInfoOut")


@_attrs_define
class WhatsAppWabaInfoOut:
    """
    Attributes:
        info (None | Unset | WhatsAppWabaInfoOutInfoType0):
        waba_id (None | str | Unset):
    """

    info: None | Unset | WhatsAppWabaInfoOutInfoType0 = UNSET
    waba_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.whats_app_waba_info_out_info_type_0 import WhatsAppWabaInfoOutInfoType0  # noqa: PLC0415

        info: dict[str, Any] | None | Unset
        if isinstance(self.info, Unset):
            info = UNSET
        elif isinstance(self.info, WhatsAppWabaInfoOutInfoType0):
            info = self.info.to_dict()
        else:
            info = self.info

        waba_id: None | str | Unset
        if isinstance(self.waba_id, Unset):
            waba_id = UNSET
        else:
            waba_id = self.waba_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info
        if waba_id is not UNSET:
            field_dict["waba_id"] = waba_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.whats_app_waba_info_out_info_type_0 import WhatsAppWabaInfoOutInfoType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_info(data: object) -> None | Unset | WhatsAppWabaInfoOutInfoType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                info_type_0 = WhatsAppWabaInfoOutInfoType0.from_dict(data)

                return info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WhatsAppWabaInfoOutInfoType0, data)

        info = _parse_info(d.pop("info", UNSET))

        def _parse_waba_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        waba_id = _parse_waba_id(d.pop("waba_id", UNSET))

        whats_app_waba_info_out = cls(
            info=info,
            waba_id=waba_id,
        )

        whats_app_waba_info_out.additional_properties = d
        return whats_app_waba_info_out

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
