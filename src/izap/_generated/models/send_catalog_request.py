from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendCatalogRequest")


@_attrs_define
class SendCatalogRequest:
    """
    Attributes:
        body (str):
        to (str):
        footer (None | str | Unset):
        thumbnail_product_retailer_id (None | str | Unset):
    """

    body: str
    to: str
    footer: None | str | Unset = UNSET
    thumbnail_product_retailer_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        to = self.to

        footer: None | str | Unset
        if isinstance(self.footer, Unset):
            footer = UNSET
        else:
            footer = self.footer

        thumbnail_product_retailer_id: None | str | Unset
        if isinstance(self.thumbnail_product_retailer_id, Unset):
            thumbnail_product_retailer_id = UNSET
        else:
            thumbnail_product_retailer_id = self.thumbnail_product_retailer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
                "to": to,
            }
        )
        if footer is not UNSET:
            field_dict["footer"] = footer
        if thumbnail_product_retailer_id is not UNSET:
            field_dict["thumbnail_product_retailer_id"] = thumbnail_product_retailer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        to = d.pop("to")

        def _parse_footer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        footer = _parse_footer(d.pop("footer", UNSET))

        def _parse_thumbnail_product_retailer_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_product_retailer_id = _parse_thumbnail_product_retailer_id(
            d.pop("thumbnail_product_retailer_id", UNSET)
        )

        send_catalog_request = cls(
            body=body,
            to=to,
            footer=footer,
            thumbnail_product_retailer_id=thumbnail_product_retailer_id,
        )

        send_catalog_request.additional_properties = d
        return send_catalog_request

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
