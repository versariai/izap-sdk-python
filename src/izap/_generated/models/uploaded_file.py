from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UploadedFile")


@_attrs_define
class UploadedFile:
    """Schema for uploaded file metadata.

    Files can be stored in either S3 (object storage) or local filesystem,
    depending on the storage backend configuration. The URL format depends
    on the storage backend:
    - Local filesystem: `/uploads/chats/{chat_id}/{filename}`
    - S3: Presigned URL or direct bucket URL (format depends on S3 configuration)

        Attributes:
            file_size (int):
            file_type (str):
            filename (str):
            id (UUID):
            url (str):
    """

    file_size: int
    file_type: str
    filename: str
    id: UUID
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_size = self.file_size

        file_type = self.file_type

        filename = self.filename

        id = str(self.id)

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_size": file_size,
                "file_type": file_type,
                "filename": filename,
                "id": id,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_size = d.pop("file_size")

        file_type = d.pop("file_type")

        filename = d.pop("filename")

        id = UUID(d.pop("id"))

        url = d.pop("url")

        uploaded_file = cls(
            file_size=file_size,
            file_type=file_type,
            filename=filename,
            id=id,
            url=url,
        )

        uploaded_file.additional_properties = d
        return uploaded_file

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
