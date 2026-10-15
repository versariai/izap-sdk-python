from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chatbot_out import ChatbotOut
    from ..models.hours_out import HoursOut
    from ..models.menus_out import MenusOut


T = TypeVar("T", bound="BusinessOut")


@_attrs_define
class BusinessOut:
    """
    Attributes:
        business_name (str):
        hours (list[HoursOut]):
        id (UUID):
        menus (list[MenusOut]):
        chatbot (ChatbotOut | None | Unset):
        chatbots (list[ChatbotOut] | Unset):
        industry (None | str | Unset):
        timezone (None | str | Unset):
    """

    business_name: str
    hours: list[HoursOut]
    id: UUID
    menus: list[MenusOut]
    chatbot: ChatbotOut | None | Unset = UNSET
    chatbots: list[ChatbotOut] | Unset = UNSET
    industry: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chatbot_out import ChatbotOut  # noqa: PLC0415

        business_name = self.business_name

        hours = []
        for hours_item_data in self.hours:
            hours_item = hours_item_data.to_dict()
            hours.append(hours_item)

        id = str(self.id)

        menus = []
        for menus_item_data in self.menus:
            menus_item = menus_item_data.to_dict()
            menus.append(menus_item)

        chatbot: dict[str, Any] | None | Unset
        if isinstance(self.chatbot, Unset):
            chatbot = UNSET
        elif isinstance(self.chatbot, ChatbotOut):
            chatbot = self.chatbot.to_dict()
        else:
            chatbot = self.chatbot

        chatbots: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.chatbots, Unset):
            chatbots = []
            for chatbots_item_data in self.chatbots:
                chatbots_item = chatbots_item_data.to_dict()
                chatbots.append(chatbots_item)

        industry: None | str | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        else:
            industry = self.industry

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_name": business_name,
                "hours": hours,
                "id": id,
                "menus": menus,
            }
        )
        if chatbot is not UNSET:
            field_dict["chatbot"] = chatbot
        if chatbots is not UNSET:
            field_dict["chatbots"] = chatbots
        if industry is not UNSET:
            field_dict["industry"] = industry
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chatbot_out import ChatbotOut  # noqa: PLC0415
        from ..models.hours_out import HoursOut  # noqa: PLC0415
        from ..models.menus_out import MenusOut  # noqa: PLC0415

        d = dict(src_dict)
        business_name = d.pop("business_name")

        hours = []
        _hours = d.pop("hours")
        for hours_item_data in _hours:
            hours_item = HoursOut.from_dict(hours_item_data)

            hours.append(hours_item)

        id = UUID(d.pop("id"))

        menus = []
        _menus = d.pop("menus")
        for menus_item_data in _menus:
            menus_item = MenusOut.from_dict(menus_item_data)

            menus.append(menus_item)

        def _parse_chatbot(data: object) -> ChatbotOut | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                chatbot_type_0 = ChatbotOut.from_dict(data)

                return chatbot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatbotOut | None | Unset, data)

        chatbot = _parse_chatbot(d.pop("chatbot", UNSET))

        _chatbots = d.pop("chatbots", UNSET)
        chatbots: list[ChatbotOut] | Unset = UNSET
        if _chatbots is not UNSET:
            chatbots = []
            for chatbots_item_data in _chatbots:
                chatbots_item = ChatbotOut.from_dict(chatbots_item_data)

                chatbots.append(chatbots_item)

        def _parse_industry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        business_out = cls(
            business_name=business_name,
            hours=hours,
            id=id,
            menus=menus,
            chatbot=chatbot,
            chatbots=chatbots,
            industry=industry,
            timezone=timezone,
        )

        business_out.additional_properties = d
        return business_out

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
