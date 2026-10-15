from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_transmission_preview_in_recipients_item import CreateTransmissionPreviewInRecipientsItem


T = TypeVar("T", bound="CreateTransmissionPreviewIn")


@_attrs_define
class CreateTransmissionPreviewIn:
    """Validate CSV recipients against a template and create a DRAFT transmission.

    No messages are sent. ``recipients`` are parsed CSV rows (header -> value); each
    row must contain ``phone_column`` and the columns that fill the template's
    variables. Confirm the returned draft id with ``confirm_transmission`` to send.

        Attributes:
            name (str): Human label for the transmission.
            recipients (list[CreateTransmissionPreviewInRecipientsItem]): Parsed CSV rows; each row maps a string column
                header to its string cell value. Must include the phone column and the columns that supply the template's
                variables.
            template_name (str): Name of the pre-approved WhatsApp Cloud API template to send.
            business_id (None | Unset | UUID):
            max_messages_per_minute (int | Unset): Sending pace cap. Must be between 1 and 200 messages per minute. Default:
                60.
            phone_column (str | Unset): Name of the CSV column holding the recipient phone number (E.164 or local). Default:
                'phone'.
            scheduled_at (datetime.datetime | None | Unset): When to send. Omit or null to send immediately on confirm. If
                the value has no timezone offset it is interpreted in 'timezone'.
            template_language (str | Unset): Template language/locale code as registered with Meta, e.g. 'pt_BR'. Default:
                'pt_BR'.
            timezone (str | Unset): IANA timezone used to interpret a naive 'scheduled_at'. Default: 'America/Sao_Paulo'.
            transmission_type (Literal['whatsapp_template'] | Unset): Only 'whatsapp_template' is supported for now.
                Default: 'whatsapp_template'.
            variable_columns (list[str] | None | Unset): For positional templates ({{1}}, {{2}}, ...): the ordered CSV
                header names mapping to {{1}}, {{2}}, ... If omitted, the first non-phone columns are used in order. Ignored for
                templates with named placeholders.
    """

    name: str
    recipients: list[CreateTransmissionPreviewInRecipientsItem]
    template_name: str
    business_id: None | Unset | UUID = UNSET
    max_messages_per_minute: int | Unset = 60
    phone_column: str | Unset = "phone"
    scheduled_at: datetime.datetime | None | Unset = UNSET
    template_language: str | Unset = "pt_BR"
    timezone: str | Unset = "America/Sao_Paulo"
    transmission_type: Literal["whatsapp_template"] | Unset = "whatsapp_template"
    variable_columns: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        recipients = []
        for recipients_item_data in self.recipients:
            recipients_item = recipients_item_data.to_dict()
            recipients.append(recipients_item)

        template_name = self.template_name

        business_id: None | str | Unset
        if isinstance(self.business_id, Unset):
            business_id = UNSET
        elif isinstance(self.business_id, UUID):
            business_id = str(self.business_id)
        else:
            business_id = self.business_id

        max_messages_per_minute = self.max_messages_per_minute

        phone_column = self.phone_column

        scheduled_at: None | str | Unset
        if isinstance(self.scheduled_at, Unset):
            scheduled_at = UNSET
        elif isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        template_language = self.template_language

        timezone = self.timezone

        transmission_type = self.transmission_type

        variable_columns: list[str] | None | Unset
        if isinstance(self.variable_columns, Unset):
            variable_columns = UNSET
        elif isinstance(self.variable_columns, list):
            variable_columns = self.variable_columns

        else:
            variable_columns = self.variable_columns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "recipients": recipients,
                "template_name": template_name,
            }
        )
        if business_id is not UNSET:
            field_dict["business_id"] = business_id
        if max_messages_per_minute is not UNSET:
            field_dict["max_messages_per_minute"] = max_messages_per_minute
        if phone_column is not UNSET:
            field_dict["phone_column"] = phone_column
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if template_language is not UNSET:
            field_dict["template_language"] = template_language
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if transmission_type is not UNSET:
            field_dict["transmission_type"] = transmission_type
        if variable_columns is not UNSET:
            field_dict["variable_columns"] = variable_columns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_transmission_preview_in_recipients_item import (
            CreateTransmissionPreviewInRecipientsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        name = d.pop("name")

        recipients = []
        _recipients = d.pop("recipients")
        for recipients_item_data in _recipients:
            recipients_item = CreateTransmissionPreviewInRecipientsItem.from_dict(recipients_item_data)

            recipients.append(recipients_item)

        template_name = d.pop("template_name")

        def _parse_business_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                business_id_type_0 = UUID(data)

                return business_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        business_id = _parse_business_id(d.pop("business_id", UNSET))

        max_messages_per_minute = d.pop("max_messages_per_minute", UNSET)

        phone_column = d.pop("phone_column", UNSET)

        def _parse_scheduled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduled_at", UNSET))

        template_language = d.pop("template_language", UNSET)

        timezone = d.pop("timezone", UNSET)

        transmission_type = cast(Literal["whatsapp_template"] | Unset, d.pop("transmission_type", UNSET))
        if transmission_type != "whatsapp_template" and not isinstance(transmission_type, Unset):
            raise ValueError(f"transmission_type must match const 'whatsapp_template', got '{transmission_type}'")

        def _parse_variable_columns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variable_columns_type_0 = cast(list[str], data)

                return variable_columns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        variable_columns = _parse_variable_columns(d.pop("variable_columns", UNSET))

        create_transmission_preview_in = cls(
            name=name,
            recipients=recipients,
            template_name=template_name,
            business_id=business_id,
            max_messages_per_minute=max_messages_per_minute,
            phone_column=phone_column,
            scheduled_at=scheduled_at,
            template_language=template_language,
            timezone=timezone,
            transmission_type=transmission_type,
            variable_columns=variable_columns,
        )

        create_transmission_preview_in.additional_properties = d
        return create_transmission_preview_in

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
