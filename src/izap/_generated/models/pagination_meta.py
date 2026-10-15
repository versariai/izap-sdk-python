from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaginationMeta")


@_attrs_define
class PaginationMeta:
    """
    Attributes:
        has_next (bool):
        has_previous (bool):
        page (int):
        page_size (int):
        total_count (int):
        total_pages (int):
    """

    has_next: bool
    has_previous: bool
    page: int
    page_size: int
    total_count: int
    total_pages: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_next = self.has_next

        has_previous = self.has_previous

        page = self.page

        page_size = self.page_size

        total_count = self.total_count

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_next": has_next,
                "has_previous": has_previous,
                "page": page,
                "page_size": page_size,
                "total_count": total_count,
                "total_pages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_next = d.pop("has_next")

        has_previous = d.pop("has_previous")

        page = d.pop("page")

        page_size = d.pop("page_size")

        total_count = d.pop("total_count")

        total_pages = d.pop("total_pages")

        pagination_meta = cls(
            has_next=has_next,
            has_previous=has_previous,
            page=page,
            page_size=page_size,
            total_count=total_count,
            total_pages=total_pages,
        )

        pagination_meta.additional_properties = d
        return pagination_meta

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
