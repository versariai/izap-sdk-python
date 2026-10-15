from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessLibraryImageOut")


@_attrs_define
class BusinessLibraryImageOut:
    """Metadata for an image stored in the business library.

    Backed by the :class:`aizap.models.documents.Document` model, filtered to
    image document types.

        Attributes:
            business_id (None | UUID):
            content_type (str):
            created (datetime.datetime):
            document_type (str):
            file_size (int):
            filename (str):
            id (UUID):
            original_filename (str):
            url (str):
            description (None | str | Unset):
            tags (list[str] | None | Unset):
            title (None | str | Unset):
            uploaded_by_user_id (None | Unset | UUID):
    """

    business_id: None | UUID
    content_type: str
    created: datetime.datetime
    document_type: str
    file_size: int
    filename: str
    id: UUID
    original_filename: str
    url: str
    description: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    title: None | str | Unset = UNSET
    uploaded_by_user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id: None | str
        if isinstance(self.business_id, UUID):
            business_id = str(self.business_id)
        else:
            business_id = self.business_id

        content_type = self.content_type

        created = self.created.isoformat()

        document_type = self.document_type

        file_size = self.file_size

        filename = self.filename

        id = str(self.id)

        original_filename = self.original_filename

        url = self.url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        uploaded_by_user_id: None | str | Unset
        if isinstance(self.uploaded_by_user_id, Unset):
            uploaded_by_user_id = UNSET
        elif isinstance(self.uploaded_by_user_id, UUID):
            uploaded_by_user_id = str(self.uploaded_by_user_id)
        else:
            uploaded_by_user_id = self.uploaded_by_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_id": business_id,
                "content_type": content_type,
                "created": created,
                "document_type": document_type,
                "file_size": file_size,
                "filename": filename,
                "id": id,
                "original_filename": original_filename,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if title is not UNSET:
            field_dict["title"] = title
        if uploaded_by_user_id is not UNSET:
            field_dict["uploaded_by_user_id"] = uploaded_by_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_business_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_id_type_0 = UUID(data)

                return business_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        business_id = _parse_business_id(d.pop("business_id"))

        content_type = d.pop("content_type")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        document_type = d.pop("document_type")

        file_size = d.pop("file_size")

        filename = d.pop("filename")

        id = UUID(d.pop("id"))

        original_filename = d.pop("original_filename")

        url = d.pop("url")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_uploaded_by_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                uploaded_by_user_id_type_0 = UUID(data)

                return uploaded_by_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        uploaded_by_user_id = _parse_uploaded_by_user_id(d.pop("uploaded_by_user_id", UNSET))

        business_library_image_out = cls(
            business_id=business_id,
            content_type=content_type,
            created=created,
            document_type=document_type,
            file_size=file_size,
            filename=filename,
            id=id,
            original_filename=original_filename,
            url=url,
            description=description,
            tags=tags,
            title=title,
            uploaded_by_user_id=uploaded_by_user_id,
        )

        business_library_image_out.additional_properties = d
        return business_library_image_out

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
