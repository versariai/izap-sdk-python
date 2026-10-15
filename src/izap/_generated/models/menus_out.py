from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reasoning_choices import ReasoningChoices, check_reasoning_choices
from ..types import UNSET, Unset

T = TypeVar("T", bound="MenusOut")


@_attrs_define
class MenusOut:
    """
    Attributes:
        menu_json (Any):
        ai_model (None | str | Unset):
        ai_model_reasoning (None | ReasoningChoices | Unset):
        id (None | Unset | UUID):
    """

    menu_json: Any
    ai_model: None | str | Unset = UNSET
    ai_model_reasoning: None | ReasoningChoices | Unset = UNSET
    id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        menu_json = self.menu_json

        ai_model: None | str | Unset
        if isinstance(self.ai_model, Unset):
            ai_model = UNSET
        else:
            ai_model = self.ai_model

        ai_model_reasoning: None | str | Unset
        if isinstance(self.ai_model_reasoning, Unset):
            ai_model_reasoning = UNSET
        elif isinstance(self.ai_model_reasoning, str):
            ai_model_reasoning = self.ai_model_reasoning
        else:
            ai_model_reasoning = self.ai_model_reasoning

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "menu_json": menu_json,
            }
        )
        if ai_model is not UNSET:
            field_dict["ai_model"] = ai_model
        if ai_model_reasoning is not UNSET:
            field_dict["ai_model_reasoning"] = ai_model_reasoning
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        menu_json = d.pop("menu_json")

        def _parse_ai_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ai_model = _parse_ai_model(d.pop("ai_model", UNSET))

        def _parse_ai_model_reasoning(data: object) -> None | ReasoningChoices | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ai_model_reasoning_type_0 = check_reasoning_choices(data)

                return ai_model_reasoning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReasoningChoices | Unset, data)

        ai_model_reasoning = _parse_ai_model_reasoning(d.pop("ai_model_reasoning", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        menus_out = cls(
            menu_json=menu_json,
            ai_model=ai_model,
            ai_model_reasoning=ai_model_reasoning,
            id=id,
        )

        menus_out.additional_properties = d
        return menus_out

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
