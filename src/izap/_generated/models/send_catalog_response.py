from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_catalog_response_error_type_0 import SendCatalogResponseErrorType0


T = TypeVar("T", bound="SendCatalogResponse")


@_attrs_define
class SendCatalogResponse:
    """
    Attributes:
        source (str):
        status (str):
        error (None | SendCatalogResponseErrorType0 | Unset):
        message_id (None | str | Unset):
    """

    source: str
    status: str
    error: None | SendCatalogResponseErrorType0 | Unset = UNSET
    message_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.send_catalog_response_error_type_0 import SendCatalogResponseErrorType0  # noqa: PLC0415

        source = self.source

        status = self.status

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, SendCatalogResponseErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        else:
            message_id = self.message_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if message_id is not UNSET:
            field_dict["message_id"] = message_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_catalog_response_error_type_0 import SendCatalogResponseErrorType0  # noqa: PLC0415

        d = dict(src_dict)
        source = d.pop("source")

        status = d.pop("status")

        def _parse_error(data: object) -> None | SendCatalogResponseErrorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = SendCatalogResponseErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SendCatalogResponseErrorType0 | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_id = _parse_message_id(d.pop("message_id", UNSET))

        send_catalog_response = cls(
            source=source,
            status=status,
            error=error,
            message_id=message_id,
        )

        send_catalog_response.additional_properties = d
        return send_catalog_response

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
