from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResponseOutputFunction")


@_attrs_define
class ResponseOutputFunction:
    """
    Attributes:
        arguments (str):
        call_id (str):
        name (str):
        type_ (Literal['function_call']):
    """

    arguments: str
    call_id: str
    name: str
    type_: Literal["function_call"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arguments = self.arguments

        call_id = self.call_id

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "arguments": arguments,
                "call_id": call_id,
                "name": name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arguments = d.pop("arguments")

        call_id = d.pop("call_id")

        name = d.pop("name")

        type_ = cast(Literal["function_call"], d.pop("type"))
        if type_ != "function_call":
            raise ValueError(f"type must match const 'function_call', got '{type_}'")

        response_output_function = cls(
            arguments=arguments,
            call_id=call_id,
            name=name,
            type_=type_,
        )

        response_output_function.additional_properties = d
        return response_output_function

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
