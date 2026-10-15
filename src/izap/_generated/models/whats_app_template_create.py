from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_category import TemplateCategory, check_template_category
from ..models.template_header_format import TemplateHeaderFormat, check_template_header_format
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_button import TemplateButton


T = TypeVar("T", bound="WhatsAppTemplateCreate")


@_attrs_define
class WhatsAppTemplateCreate:
    """
    Attributes:
        body_text (str):
        name (str):
        buttons (list[TemplateButton] | Unset):
        category (TemplateCategory | Unset): WhatsApp/Meta template category. Drives approval rules and pricing.
        display_name (None | str | Unset):
        example_variables (list[str] | Unset):
        footer_text (None | str | Unset):
        header_format (TemplateHeaderFormat | Unset):
        header_text (None | str | Unset):
        language (str | Unset):  Default: 'pt_BR'.
    """

    body_text: str
    name: str
    buttons: list[TemplateButton] | Unset = UNSET
    category: TemplateCategory | Unset = UNSET
    display_name: None | str | Unset = UNSET
    example_variables: list[str] | Unset = UNSET
    footer_text: None | str | Unset = UNSET
    header_format: TemplateHeaderFormat | Unset = UNSET
    header_text: None | str | Unset = UNSET
    language: str | Unset = "pt_BR"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_text = self.body_text

        name = self.name

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body_text": body_text,
                "name": name,
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_button import TemplateButton  # noqa: PLC0415

        d = dict(src_dict)
        body_text = d.pop("body_text")

        name = d.pop("name")

        _buttons = d.pop("buttons", UNSET)
        buttons: list[TemplateButton] | Unset = UNSET
        if _buttons is not UNSET:
            buttons = []
            for buttons_item_data in _buttons:
                buttons_item = TemplateButton.from_dict(buttons_item_data)

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

        whats_app_template_create = cls(
            body_text=body_text,
            name=name,
            buttons=buttons,
            category=category,
            display_name=display_name,
            example_variables=example_variables,
            footer_text=footer_text,
            header_format=header_format,
            header_text=header_text,
            language=language,
        )

        whats_app_template_create.additional_properties = d
        return whats_app_template_create

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
