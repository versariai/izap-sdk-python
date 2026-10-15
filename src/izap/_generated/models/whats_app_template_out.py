from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_category import TemplateCategory, check_template_category
from ..models.template_header_format import TemplateHeaderFormat, check_template_header_format
from ..models.template_status import TemplateStatus, check_template_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_button_out import TemplateButtonOut


T = TypeVar("T", bound="WhatsAppTemplateOut")


@_attrs_define
class WhatsAppTemplateOut:
    """
    Attributes:
        body_text (str):
        business_id (UUID):
        created (datetime.datetime):
        id (UUID):
        modified (datetime.datetime):
        name (str):
        status (TemplateStatus): Lifecycle/approval status of a template.

            DRAFT is local-only (not yet submitted to Meta). The remaining values mirror
            the statuses returned by the WhatsApp Cloud API.
        buttons (list[TemplateButtonOut] | Unset):
        category (TemplateCategory | Unset): WhatsApp/Meta template category. Drives approval rules and pricing.
        display_name (None | str | Unset):
        example_variables (list[str] | Unset):
        footer_text (None | str | Unset):
        header_format (TemplateHeaderFormat | Unset):
        header_text (None | str | Unset):
        language (str | Unset):  Default: 'pt_BR'.
        last_synced_at (datetime.datetime | None | Unset):
        provider_template_id (None | str | Unset):
        quality_score (None | str | Unset):
        rejection_reason (None | str | Unset):
    """

    body_text: str
    business_id: UUID
    created: datetime.datetime
    id: UUID
    modified: datetime.datetime
    name: str
    status: TemplateStatus
    buttons: list[TemplateButtonOut] | Unset = UNSET
    category: TemplateCategory | Unset = UNSET
    display_name: None | str | Unset = UNSET
    example_variables: list[str] | Unset = UNSET
    footer_text: None | str | Unset = UNSET
    header_format: TemplateHeaderFormat | Unset = UNSET
    header_text: None | str | Unset = UNSET
    language: str | Unset = "pt_BR"
    last_synced_at: datetime.datetime | None | Unset = UNSET
    provider_template_id: None | str | Unset = UNSET
    quality_score: None | str | Unset = UNSET
    rejection_reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_text = self.body_text

        business_id = str(self.business_id)

        created = self.created.isoformat()

        id = str(self.id)

        modified = self.modified.isoformat()

        name = self.name

        status: str = self.status

        buttons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        example_variables: list[str] | Unset = UNSET
        if not isinstance(self.example_variables, Unset):
            example_variables = self.example_variables

        footer_text: None | str | Unset
        if isinstance(self.footer_text, Unset):
            footer_text = UNSET
        else:
            footer_text = self.footer_text

        header_format: str | Unset = UNSET
        if not isinstance(self.header_format, Unset):
            header_format = self.header_format

        header_text: None | str | Unset
        if isinstance(self.header_text, Unset):
            header_text = UNSET
        else:
            header_text = self.header_text

        language = self.language

        last_synced_at: None | str | Unset
        if isinstance(self.last_synced_at, Unset):
            last_synced_at = UNSET
        elif isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        provider_template_id: None | str | Unset
        if isinstance(self.provider_template_id, Unset):
            provider_template_id = UNSET
        else:
            provider_template_id = self.provider_template_id

        quality_score: None | str | Unset
        if isinstance(self.quality_score, Unset):
            quality_score = UNSET
        else:
            quality_score = self.quality_score

        rejection_reason: None | str | Unset
        if isinstance(self.rejection_reason, Unset):
            rejection_reason = UNSET
        else:
            rejection_reason = self.rejection_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body_text": body_text,
                "business_id": business_id,
                "created": created,
                "id": id,
                "modified": modified,
                "name": name,
                "status": status,
            }
        )
        if buttons is not UNSET:
            field_dict["buttons"] = buttons
        if category is not UNSET:
            field_dict["category"] = category
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if example_variables is not UNSET:
            field_dict["example_variables"] = example_variables
        if footer_text is not UNSET:
            field_dict["footer_text"] = footer_text
        if header_format is not UNSET:
            field_dict["header_format"] = header_format
        if header_text is not UNSET:
            field_dict["header_text"] = header_text
        if language is not UNSET:
            field_dict["language"] = language
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at
        if provider_template_id is not UNSET:
            field_dict["provider_template_id"] = provider_template_id
        if quality_score is not UNSET:
            field_dict["quality_score"] = quality_score
        if rejection_reason is not UNSET:
            field_dict["rejection_reason"] = rejection_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_button_out import TemplateButtonOut  # noqa: PLC0415

        d = dict(src_dict)
        body_text = d.pop("body_text")

        business_id = UUID(d.pop("business_id"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        id = UUID(d.pop("id"))

        modified = datetime.datetime.fromisoformat(d.pop("modified"))

        name = d.pop("name")

        status = check_template_status(d.pop("status"))

        _buttons = d.pop("buttons", UNSET)
        buttons: list[TemplateButtonOut] | Unset = UNSET
        if _buttons is not UNSET:
            buttons = []
            for buttons_item_data in _buttons:
                buttons_item = TemplateButtonOut.from_dict(buttons_item_data)

                buttons.append(buttons_item)

        _category = d.pop("category", UNSET)
        category: TemplateCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_template_category(_category)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        example_variables = cast(list[str], d.pop("example_variables", UNSET))

        def _parse_footer_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        footer_text = _parse_footer_text(d.pop("footer_text", UNSET))

        _header_format = d.pop("header_format", UNSET)
        header_format: TemplateHeaderFormat | Unset
        if isinstance(_header_format, Unset):
            header_format = UNSET
        else:
            header_format = check_template_header_format(_header_format)

        def _parse_header_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_text = _parse_header_text(d.pop("header_text", UNSET))

        language = d.pop("language", UNSET)

        def _parse_last_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_synced_at = _parse_last_synced_at(d.pop("last_synced_at", UNSET))

        def _parse_provider_template_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_template_id = _parse_provider_template_id(d.pop("provider_template_id", UNSET))

        def _parse_quality_score(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quality_score = _parse_quality_score(d.pop("quality_score", UNSET))

        def _parse_rejection_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejection_reason", UNSET))

        whats_app_template_out = cls(
            body_text=body_text,
            business_id=business_id,
            created=created,
            id=id,
            modified=modified,
            name=name,
            status=status,
            buttons=buttons,
            category=category,
            display_name=display_name,
            example_variables=example_variables,
            footer_text=footer_text,
            header_format=header_format,
            header_text=header_text,
            language=language,
            last_synced_at=last_synced_at,
            provider_template_id=provider_template_id,
            quality_score=quality_score,
            rejection_reason=rejection_reason,
        )

        whats_app_template_out.additional_properties = d
        return whats_app_template_out

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
