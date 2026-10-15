from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_error_detail import ApiErrorDetail


T = TypeVar("T", bound="ApiError")


@_attrs_define
class ApiError:
    """The response body of a handled API error.

    ``detail`` is either a plain string (FastAPI's default for an
    ``HTTPException`` raised with a string, and for the ``default`` fastapi-users
    messages like ``"Not authenticated"``) or the structured
    :class:`ApiErrorDetail` object described above. ``code`` is present only on
    the top-level shape ``aizap.core.exceptions.AppException`` produces for its
    own 5xx responses (``"INTERNAL_ERROR"`` / ``"DB_ERROR"``); it does not
    duplicate the ``code`` nested inside a structured ``detail``.

        Attributes:
            detail (ApiErrorDetail | str):
            code (None | str | Unset):
    """

    detail: ApiErrorDetail | str
    code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_error_detail import ApiErrorDetail  # noqa: PLC0415

        detail: dict[str, Any] | str
        if isinstance(self.detail, ApiErrorDetail):
            detail = self.detail.to_dict()
        else:
            detail = self.detail

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_error_detail import ApiErrorDetail  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_detail(data: object) -> ApiErrorDetail | str:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detail_type_1 = ApiErrorDetail.from_dict(data)

                return detail_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ApiErrorDetail | str, data)

        detail = _parse_detail(d.pop("detail"))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        api_error = cls(
            detail=detail,
            code=code,
        )

        api_error.additional_properties = d
        return api_error

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
