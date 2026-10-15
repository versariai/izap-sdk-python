from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrincipalResponse")


@_attrs_define
class PrincipalResponse:
    """Introspection result: who the presented credential authenticates as.

    Attributes:
        kind (str): 'user' or 'business_api_key'.
        business_id (None | Unset | UUID): Set when authenticated as a business API key.
        token_id (None | Unset | UUID): Id of the token row used, if any.
        user_id (None | Unset | UUID): Set when authenticated as a user.
    """

    kind: str
    business_id: None | Unset | UUID = UNSET
    token_id: None | Unset | UUID = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        business_id: None | str | Unset
        if isinstance(self.business_id, Unset):
            business_id = UNSET
        elif isinstance(self.business_id, UUID):
            business_id = str(self.business_id)
        else:
            business_id = self.business_id

        token_id: None | str | Unset
        if isinstance(self.token_id, Unset):
            token_id = UNSET
        elif isinstance(self.token_id, UUID):
            token_id = str(self.token_id)
        else:
            token_id = self.token_id

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
            }
        )
        if business_id is not UNSET:
            field_dict["business_id"] = business_id
        if token_id is not UNSET:
            field_dict["token_id"] = token_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind")

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

        def _parse_token_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                token_id_type_0 = UUID(data)

                return token_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        token_id = _parse_token_id(d.pop("token_id", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        principal_response = cls(
            kind=kind,
            business_id=business_id,
            token_id=token_id,
            user_id=user_id,
        )

        principal_response.additional_properties = d
        return principal_response

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
