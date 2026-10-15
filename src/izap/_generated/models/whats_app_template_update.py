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


T = TypeVar("T", bound="WhatsAppTemplateUpdate")


@_attrs_define
class WhatsAppTemplateUpdate:
    """Partial update. Approved templates can only be edited while in DRAFT/REJECTED.

    Attributes:
        body_text (None | str | Unset):
        buttons (list[TemplateButton] | None | Unset):
        category (None | TemplateCategory | Unset):
        display_name (None | str | Unset):
        example_variables (list[str] | None | Unset):
        footer_text (None | str | Unset):
        header_format (None | TemplateHeaderFormat | Unset):
        header_text (None | str | Unset):
        language (None | str | Unset):
    """

    body_text: None | str | Unset = UNSET
    buttons: list[TemplateButton] | None | Unset = UNSET
    category: None | TemplateCategory | Unset = UNSET
    display_name: None | str | Unset = UNSET
    example_variables: list[str] | None | Unset = UNSET
    footer_text: None | str | Unset = UNSET
    header_format: None | TemplateHeaderFormat | Unset = UNSET
    header_text: None | str | Unset = UNSET
    language: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body_text: None | str | Unset
        if isinstance(self.body_text, Unset):
            body_text = UNSET
        else:
            body_text = self.body_text

        buttons: list[dict[str, Any]] | None | Unset
        if isinstance(self.buttons, Unset):
            buttons = UNSET
        elif isinstance(self.buttons, list):
            buttons = []
            for buttons_type_0_item_data in self.buttons:
                buttons_type_0_item = buttons_type_0_item_data.to_dict()
                buttons.append(buttons_type_0_item)

        else:
            buttons = self.buttons

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, str):
            category = self.category
        else:
            category = self.category

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        example_variables: list[str] | None | Unset
        if isinstance(self.example_variables, Unset):
            example_variables = UNSET
        elif isinstance(self.example_variables, list):
            example_variables = self.example_variables

        else:
            example_variables = self.example_variables

        footer_text: None | str | Unset
        if isinstance(self.footer_text, Unset):
            footer_text = UNSET
        else:
            footer_text = self.footer_text

        header_format: None | str | Unset
        if isinstance(self.header_format, Unset):
            header_format = UNSET
        elif isinstance(self.header_format, str):
            header_format = self.header_format
        else:
            header_format = self.header_format

        header_text: None | str | Unset
        if isinstance(self.header_text, Unset):
            header_text = UNSET
        else:
            header_text = self.header_text

        language: None | str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        else:
            language = self.language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body_text is not UNSET:
            field_dict["body_text"] = body_text
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

        def _parse_body_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body_text = _parse_body_text(d.pop("body_text", UNSET))

        def _parse_buttons(data: object) -> list[TemplateButton] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                buttons_type_0 = []
                _buttons_type_0 = data
                for buttons_type_0_item_data in _buttons_type_0:
                    buttons_type_0_item = TemplateButton.from_dict(buttons_type_0_item_data)

                    buttons_type_0.append(buttons_type_0_item)

                return buttons_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TemplateButton] | None | Unset, data)

        buttons = _parse_buttons(d.pop("buttons", UNSET))

        def _parse_category(data: object) -> None | TemplateCategory | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                category_type_0 = check_template_category(data)

                return category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateCategory | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_example_variables(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                example_variables_type_0 = cast(list[str], data)

                return example_variables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        example_variables = _parse_example_variables(d.pop("example_variables", UNSET))

        def _parse_footer_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        footer_text = _parse_footer_text(d.pop("footer_text", UNSET))

        def _parse_header_format(data: object) -> None | TemplateHeaderFormat | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                header_format_type_0 = check_template_header_format(data)

                return header_format_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TemplateHeaderFormat | Unset, data)

        header_format = _parse_header_format(d.pop("header_format", UNSET))

        def _parse_header_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        header_text = _parse_header_text(d.pop("header_text", UNSET))

        def _parse_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language = _parse_language(d.pop("language", UNSET))

        whats_app_template_update = cls(
            body_text=body_text,
            buttons=buttons,
            category=category,
            display_name=display_name,
            example_variables=example_variables,
            footer_text=footer_text,
            header_format=header_format,
            header_text=header_text,
            language=language,
        )

        whats_app_template_update.additional_properties = d
        return whats_app_template_update

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
