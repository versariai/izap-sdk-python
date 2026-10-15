from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessUpdateRequest")


@_attrs_define
class BusinessUpdateRequest:
    """Partial update for a business's profile. Optional fields only; unset ones are left alone.

    Kept intentionally narrow (name + timezone) so GOG-3129 (business hours) can extend this
    same endpoint with an `hours` field later instead of introducing a second PATCH route.

        Attributes:
            business_name (None | str | Unset):
            industry (None | str | Unset):
            timezone (None | str | Unset):
    """

    business_name: None | str | Unset = UNSET
    industry: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_name: None | str | Unset
        if isinstance(self.business_name, Unset):
            business_name = UNSET
        else:
            business_name = self.business_name

        industry: None | str | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        else:
            industry = self.industry

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_name is not UNSET:
            field_dict["business_name"] = business_name
        if industry is not UNSET:
            field_dict["industry"] = industry
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_business_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        business_name = _parse_business_name(d.pop("business_name", UNSET))

        def _parse_industry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        business_update_request = cls(
            business_name=business_name,
            industry=industry,
            timezone=timezone,
        )

        business_update_request.additional_properties = d
        return business_update_request

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
