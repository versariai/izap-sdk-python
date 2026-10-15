from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.business_library_image_out import BusinessLibraryImageOut


T = TypeVar("T", bound="BusinessLibraryDocumentListResponse")


@_attrs_define
class BusinessLibraryDocumentListResponse:
    """Paginated list of library documents and videos (newest first).

    Same row shape as the image listing — the two differ in which document types they
    carry, not in what is known about one — but a distinct model so the OpenAPI schema
    names the collection for what it holds.

        Attributes:
            documents (list[BusinessLibraryImageOut]):
            has_next (bool):
            limit (int):
            offset (int):
            total (int):
    """

    documents: list[BusinessLibraryImageOut]
    has_next: bool
    limit: int
    offset: int
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        has_next = self.has_next

        limit = self.limit

        offset = self.offset

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documents": documents,
                "has_next": has_next,
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
        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = BusinessLibraryImageOut.from_dict(documents_item_data)

            documents.append(documents_item)

        has_next = d.pop("has_next")

        limit = d.pop("limit")

        offset = d.pop("offset")

        total = d.pop("total")

        business_library_document_list_response = cls(
            documents=documents,
            has_next=has_next,
            limit=limit,
            offset=offset,
            total=total,
        )

        business_library_document_list_response.additional_properties = d
        return business_library_document_list_response

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
