from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chatbot_out_locale_source import ChatbotOutLocaleSource, check_chatbot_out_locale_source
from ..models.chatbot_out_messaging_backend import ChatbotOutMessagingBackend, check_chatbot_out_messaging_backend
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chatbot_whats_app_number_out import ChatbotWhatsAppNumberOut


T = TypeVar("T", bound="ChatbotOut")


@_attrs_define
class ChatbotOut:
    """
    Attributes:
        effective_locale (str):
        id (UUID):
        ai_model_name (None | str | Unset):
        ai_pause_minutes (int | None | Unset):
        ai_pause_minutes_default (int | Unset):  Default: 60.
        avatar (None | str | Unset):
        custom_instructions (list[Any] | None | Unset):
        detect_client_language (bool | Unset):  Default: False.
        is_active (bool | Unset):  Default: False.
        locale (None | str | Unset):
        locale_source (ChatbotOutLocaleSource | Unset):  Default: 'default'.
        messaging_backend (ChatbotOutMessagingBackend | Unset):  Default: 'izap'.
        name (None | str | Unset):
        objective (None | str | Unset):
        phone_number (None | str | Unset):
        platform (Literal['whatsapp'] | None | Unset):
        whatsapp_numbers (list[ChatbotWhatsAppNumberOut] | Unset):
    """

    effective_locale: str
    id: UUID
    ai_model_name: None | str | Unset = UNSET
    ai_pause_minutes: int | None | Unset = UNSET
    ai_pause_minutes_default: int | Unset = 60
    avatar: None | str | Unset = UNSET
    custom_instructions: list[Any] | None | Unset = UNSET
    detect_client_language: bool | Unset = False
    is_active: bool | Unset = False
    locale: None | str | Unset = UNSET
    locale_source: ChatbotOutLocaleSource | Unset = "default"
    messaging_backend: ChatbotOutMessagingBackend | Unset = "izap"
    name: None | str | Unset = UNSET
    objective: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    platform: Literal["whatsapp"] | None | Unset = UNSET
    whatsapp_numbers: list[ChatbotWhatsAppNumberOut] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        effective_locale = self.effective_locale

        id = str(self.id)

        ai_model_name: None | str | Unset
        if isinstance(self.ai_model_name, Unset):
            ai_model_name = UNSET
        else:
            ai_model_name = self.ai_model_name

        ai_pause_minutes: int | None | Unset
        if isinstance(self.ai_pause_minutes, Unset):
            ai_pause_minutes = UNSET
        else:
            ai_pause_minutes = self.ai_pause_minutes

        ai_pause_minutes_default = self.ai_pause_minutes_default

        avatar: None | str | Unset
        if isinstance(self.avatar, Unset):
            avatar = UNSET
        else:
            avatar = self.avatar

        custom_instructions: list[Any] | None | Unset
        if isinstance(self.custom_instructions, Unset):
            custom_instructions = UNSET
        elif isinstance(self.custom_instructions, list):
            custom_instructions = self.custom_instructions

        else:
            custom_instructions = self.custom_instructions

        detect_client_language = self.detect_client_language

        is_active = self.is_active

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        locale_source: str | Unset = UNSET
        if not isinstance(self.locale_source, Unset):
            locale_source = self.locale_source

        messaging_backend: str | Unset = UNSET
        if not isinstance(self.messaging_backend, Unset):
            messaging_backend = self.messaging_backend

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        objective: None | str | Unset
        if isinstance(self.objective, Unset):
            objective = UNSET
        else:
            objective = self.objective

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        platform: Literal["whatsapp"] | None | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        whatsapp_numbers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.whatsapp_numbers, Unset):
            whatsapp_numbers = []
            for whatsapp_numbers_item_data in self.whatsapp_numbers:
                whatsapp_numbers_item = whatsapp_numbers_item_data.to_dict()
                whatsapp_numbers.append(whatsapp_numbers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "effective_locale": effective_locale,
                "id": id,
            }
        )
        if ai_model_name is not UNSET:
            field_dict["ai_model_name"] = ai_model_name
        if ai_pause_minutes is not UNSET:
            field_dict["ai_pause_minutes"] = ai_pause_minutes
        if ai_pause_minutes_default is not UNSET:
            field_dict["ai_pause_minutes_default"] = ai_pause_minutes_default
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if custom_instructions is not UNSET:
            field_dict["custom_instructions"] = custom_instructions
        if detect_client_language is not UNSET:
            field_dict["detect_client_language"] = detect_client_language
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if locale is not UNSET:
            field_dict["locale"] = locale
        if locale_source is not UNSET:
            field_dict["locale_source"] = locale_source
        if messaging_backend is not UNSET:
            field_dict["messaging_backend"] = messaging_backend
        if name is not UNSET:
            field_dict["name"] = name
        if objective is not UNSET:
            field_dict["objective"] = objective
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if platform is not UNSET:
            field_dict["platform"] = platform
        if whatsapp_numbers is not UNSET:
            field_dict["whatsapp_numbers"] = whatsapp_numbers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chatbot_whats_app_number_out import ChatbotWhatsAppNumberOut  # noqa: PLC0415

        d = dict(src_dict)
        effective_locale = d.pop("effective_locale")

        id = UUID(d.pop("id"))

        def _parse_ai_model_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ai_model_name = _parse_ai_model_name(d.pop("ai_model_name", UNSET))

        def _parse_ai_pause_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ai_pause_minutes = _parse_ai_pause_minutes(d.pop("ai_pause_minutes", UNSET))

        ai_pause_minutes_default = d.pop("ai_pause_minutes_default", UNSET)

        def _parse_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar = _parse_avatar(d.pop("avatar", UNSET))

        def _parse_custom_instructions(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_instructions_type_0 = cast(list[Any], data)

                return custom_instructions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        custom_instructions = _parse_custom_instructions(d.pop("custom_instructions", UNSET))

        detect_client_language = d.pop("detect_client_language", UNSET)

        is_active = d.pop("is_active", UNSET)

        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))

        _locale_source = d.pop("locale_source", UNSET)
        locale_source: ChatbotOutLocaleSource | Unset
        if isinstance(_locale_source, Unset):
            locale_source = UNSET
        else:
            locale_source = check_chatbot_out_locale_source(_locale_source)

        _messaging_backend = d.pop("messaging_backend", UNSET)
        messaging_backend: ChatbotOutMessagingBackend | Unset
        if isinstance(_messaging_backend, Unset):
            messaging_backend = UNSET
        else:
            messaging_backend = check_chatbot_out_messaging_backend(_messaging_backend)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_objective(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        objective = _parse_objective(d.pop("objective", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phone_number", UNSET))

        def _parse_platform(data: object) -> Literal["whatsapp"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            platform_type_0 = cast(Literal["whatsapp"], data)
            if platform_type_0 != "whatsapp":
                raise ValueError(f"platform_type_0 must match const 'whatsapp', got '{platform_type_0}'")
            return platform_type_0
            return cast(Literal["whatsapp"] | None | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        _whatsapp_numbers = d.pop("whatsapp_numbers", UNSET)
        whatsapp_numbers: list[ChatbotWhatsAppNumberOut] | Unset = UNSET
        if _whatsapp_numbers is not UNSET:
            whatsapp_numbers = []
            for whatsapp_numbers_item_data in _whatsapp_numbers:
                whatsapp_numbers_item = ChatbotWhatsAppNumberOut.from_dict(whatsapp_numbers_item_data)

                whatsapp_numbers.append(whatsapp_numbers_item)

        chatbot_out = cls(
            effective_locale=effective_locale,
            id=id,
            ai_model_name=ai_model_name,
            ai_pause_minutes=ai_pause_minutes,
            ai_pause_minutes_default=ai_pause_minutes_default,
            avatar=avatar,
            custom_instructions=custom_instructions,
            detect_client_language=detect_client_language,
            is_active=is_active,
            locale=locale,
            locale_source=locale_source,
            messaging_backend=messaging_backend,
            name=name,
            objective=objective,
            phone_number=phone_number,
            platform=platform,
            whatsapp_numbers=whatsapp_numbers,
        )

        chatbot_out.additional_properties = d
        return chatbot_out

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
