from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview_row_error_out import PreviewRowErrorOut
    from ..models.transmission_preview_out_column_mapping import TransmissionPreviewOutColumnMapping


T = TypeVar("T", bound="TransmissionPreviewOut")


@_attrs_define
class TransmissionPreviewOut:
    """
    Attributes:
        business_id (UUID):
        column_mapping (TransmissionPreviewOutColumnMapping):
        duplicate_count (int):
        estimated_duration_seconds (int):
        invalid_count (int):
        name (str):
        phone_column (str):
        recipient_count (int):
        sample_errors (list[PreviewRowErrorOut]):
        scheduled_at (datetime.datetime | None):
        status (str):
        template_language (str):
        template_name (str):
        transmission_id (UUID):
        transmission_type (str):
        uses_named_variables (bool):
        valid_count (int):
        warnings (list[str]):
        not_on_whatsapp_count (int | Unset):  Default: 0.
    """

    business_id: UUID
    column_mapping: TransmissionPreviewOutColumnMapping
    duplicate_count: int
    estimated_duration_seconds: int
    invalid_count: int
    name: str
    phone_column: str
    recipient_count: int
    sample_errors: list[PreviewRowErrorOut]
    scheduled_at: datetime.datetime | None
    status: str
    template_language: str
    template_name: str
    transmission_id: UUID
    transmission_type: str
    uses_named_variables: bool
    valid_count: int
    warnings: list[str]
    not_on_whatsapp_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id = str(self.business_id)

        column_mapping = self.column_mapping.to_dict()

        duplicate_count = self.duplicate_count

        estimated_duration_seconds = self.estimated_duration_seconds

        invalid_count = self.invalid_count

        name = self.name

        phone_column = self.phone_column

        recipient_count = self.recipient_count

        sample_errors = []
        for sample_errors_item_data in self.sample_errors:
            sample_errors_item = sample_errors_item_data.to_dict()
            sample_errors.append(sample_errors_item)

        scheduled_at: None | str
        if isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        status = self.status

        template_language = self.template_language

        template_name = self.template_name

        transmission_id = str(self.transmission_id)

        transmission_type = self.transmission_type

        uses_named_variables = self.uses_named_variables

        valid_count = self.valid_count

        warnings = self.warnings

        not_on_whatsapp_count = self.not_on_whatsapp_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_id": business_id,
                "column_mapping": column_mapping,
                "duplicate_count": duplicate_count,
                "estimated_duration_seconds": estimated_duration_seconds,
                "invalid_count": invalid_count,
                "name": name,
                "phone_column": phone_column,
                "recipient_count": recipient_count,
                "sample_errors": sample_errors,
                "scheduled_at": scheduled_at,
                "status": status,
                "template_language": template_language,
                "template_name": template_name,
                "transmission_id": transmission_id,
                "transmission_type": transmission_type,
                "uses_named_variables": uses_named_variables,
                "valid_count": valid_count,
                "warnings": warnings,
            }
        )
        if not_on_whatsapp_count is not UNSET:
            field_dict["not_on_whatsapp_count"] = not_on_whatsapp_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_row_error_out import PreviewRowErrorOut  # noqa: PLC0415
        from ..models.transmission_preview_out_column_mapping import (
            TransmissionPreviewOutColumnMapping,  # noqa: PLC0415
        )

        d = dict(src_dict)
        business_id = UUID(d.pop("business_id"))

        column_mapping = TransmissionPreviewOutColumnMapping.from_dict(d.pop("column_mapping"))

        duplicate_count = d.pop("duplicate_count")

        estimated_duration_seconds = d.pop("estimated_duration_seconds")

        invalid_count = d.pop("invalid_count")

        name = d.pop("name")

        phone_column = d.pop("phone_column")

        recipient_count = d.pop("recipient_count")

        sample_errors = []
        _sample_errors = d.pop("sample_errors")
        for sample_errors_item_data in _sample_errors:
            sample_errors_item = PreviewRowErrorOut.from_dict(sample_errors_item_data)

            sample_errors.append(sample_errors_item)

        def _parse_scheduled_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduled_at"))

        status = d.pop("status")

        template_language = d.pop("template_language")

        template_name = d.pop("template_name")

        transmission_id = UUID(d.pop("transmission_id"))

        transmission_type = d.pop("transmission_type")

        uses_named_variables = d.pop("uses_named_variables")

        valid_count = d.pop("valid_count")

        warnings = cast(list[str], d.pop("warnings"))

        not_on_whatsapp_count = d.pop("not_on_whatsapp_count", UNSET)

        transmission_preview_out = cls(
            business_id=business_id,
            column_mapping=column_mapping,
            duplicate_count=duplicate_count,
            estimated_duration_seconds=estimated_duration_seconds,
            invalid_count=invalid_count,
            name=name,
            phone_column=phone_column,
            recipient_count=recipient_count,
            sample_errors=sample_errors,
            scheduled_at=scheduled_at,
            status=status,
            template_language=template_language,
            template_name=template_name,
            transmission_id=transmission_id,
            transmission_type=transmission_type,
            uses_named_variables=uses_named_variables,
            valid_count=valid_count,
            warnings=warnings,
            not_on_whatsapp_count=not_on_whatsapp_count,
        )

        transmission_preview_out.additional_properties = d
        return transmission_preview_out

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
