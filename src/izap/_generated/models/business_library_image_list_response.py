from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.business_library_image_out import BusinessLibraryImageOut


T = TypeVar("T", bound="BusinessLibraryImageListResponse")


@_attrs_define
class BusinessLibraryImageListResponse:
    """Paginated list of library images with stable ordering (newest first).

    Attributes:
        has_next (bool):
        images (list[BusinessLibraryImageOut]):
        limit (int):
        offset (int):
        total (int):
    """

    has_next: bool
    images: list[BusinessLibraryImageOut]
    limit: int
    offset: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_next = self.has_next

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        limit = self.limit

        offset = self.offset

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_next": has_next,
                "images": images,
                "limit": limit,
                "offset": offset,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_library_image_out import BusinessLibraryImageOut  # noqa: PLC0415

        d = dict(src_dict)
        has_next = d.pop("has_next")

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = BusinessLibraryImageOut.from_dict(images_item_data)

            images.append(images_item)

        limit = d.pop("limit")

        offset = d.pop("offset")

        total = d.pop("total")

        business_library_image_list_response = cls(
            has_next=has_next,
            images=images,
            limit=limit,
            offset=offset,
            total=total,
        )

        business_library_image_list_response.additional_properties = d
        return business_library_image_list_response

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
