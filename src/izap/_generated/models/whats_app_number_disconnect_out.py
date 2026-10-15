from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WhatsAppNumberDisconnectOut")


@_attrs_define
class WhatsAppNumberDisconnectOut:
    """
    Attributes:
        access_revoked (bool):
        deregistered (bool):
        removed (bool):
        detail (None | str | Unset):
        warnings (list[str] | Unset):
    """

    access_revoked: bool
    deregistered: bool
    removed: bool
    detail: None | str | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_revoked = self.access_revoked

        deregistered = self.deregistered

        removed = self.removed

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_revoked": access_revoked,
                "deregistered": deregistered,
                "removed": removed,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_revoked = d.pop("access_revoked")

        deregistered = d.pop("deregistered")

        removed = d.pop("removed")

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        whats_app_number_disconnect_out = cls(
            access_revoked=access_revoked,
            deregistered=deregistered,
            removed=removed,
            detail=detail,
            warnings=warnings,
        )

        whats_app_number_disconnect_out.additional_properties = d
        return whats_app_number_disconnect_out

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
