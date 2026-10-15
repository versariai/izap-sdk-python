from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenResponse")


@_attrs_define
class TokenResponse:
    """Non-secret view of a token, safe to list.

    Attributes:
        created (datetime.datetime):
        expires_at (datetime.datetime | None):
        id (UUID):
        last_used_at (datetime.datetime | None):
        name (str):
        revoked (bool):
        token_prefix (str): Non-secret leading chars, e.g. 'izap_pat_AbC'.
        last_four (None | str | Unset): Last four chars of the token, for recognition.
        scopes (list[str] | None | Unset): Permission scopes. Null means full access within the credential's normal
            permissions.
    """

    created: datetime.datetime
    expires_at: datetime.datetime | None
    id: UUID
    last_used_at: datetime.datetime | None
    name: str
    revoked: bool
    token_prefix: str
    last_four: None | str | Unset = UNSET
    scopes: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        expires_at: None | str
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        id = str(self.id)

        last_used_at: None | str
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        name = self.name

        revoked = self.revoked

        token_prefix = self.token_prefix

        last_four: None | str | Unset
        if isinstance(self.last_four, Unset):
            last_four = UNSET
        else:
            last_four = self.last_four

        scopes: list[str] | None | Unset
        if isinstance(self.scopes, Unset):
            scopes = UNSET
        elif isinstance(self.scopes, list):
            scopes = self.scopes

        else:
            scopes = self.scopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "expires_at": expires_at,
                "id": id,
                "last_used_at": last_used_at,
                "name": name,
                "revoked": revoked,
                "token_prefix": token_prefix,
            }
        )
        if last_four is not UNSET:
            field_dict["last_four"] = last_four
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = datetime.datetime.fromisoformat(d.pop("created"))

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        id = UUID(d.pop("id"))

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        name = d.pop("name")

        revoked = d.pop("revoked")

        token_prefix = d.pop("token_prefix")

        def _parse_last_four(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_four = _parse_last_four(d.pop("last_four", UNSET))

        def _parse_scopes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scopes = _parse_scopes(d.pop("scopes", UNSET))

        token_response = cls(
            created=created,
            expires_at=expires_at,
            id=id,
            last_used_at=last_used_at,
            name=name,
            revoked=revoked,
            token_prefix=token_prefix,
            last_four=last_four,
            scopes=scopes,
        )

        token_response.additional_properties = d
        return token_response

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
