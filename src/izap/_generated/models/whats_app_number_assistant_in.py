from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WhatsAppNumberAssistantIn")


@_attrs_define
class WhatsAppNumberAssistantIn:
    """``null`` detaches whichever assistant currently answers on the number.

    Attributes:
        assistant_id (None | Unset | UUID):
    """

    assistant_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistant_id: None | str | Unset
        if isinstance(self.assistant_id, Unset):
            assistant_id = UNSET
        elif isinstance(self.assistant_id, UUID):
            assistant_id = str(self.assistant_id)
        else:
            assistant_id = self.assistant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assistant_id is not UNSET:
            field_dict["assistant_id"] = assistant_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        whats_app_number_assistant_in = cls(
            assistant_id=assistant_id,
        )

        whats_app_number_assistant_in.additional_properties = d
        return whats_app_number_assistant_in

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
