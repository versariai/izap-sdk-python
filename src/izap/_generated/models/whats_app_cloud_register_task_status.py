from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.registration_task_status import RegistrationTaskStatus, check_registration_task_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_simple_out import BusinessSimpleOut
    from ..models.whats_app_cloud_register_task_status_error_type_0 import WhatsAppCloudRegisterTaskStatusErrorType0


T = TypeVar("T", bound="WhatsAppCloudRegisterTaskStatus")


@_attrs_define
class WhatsAppCloudRegisterTaskStatus:
    """Poll body of ``GET /{business_id}/whatsapp_cloud/register/tasks/{task_id}``.

    Attributes:
        status (RegistrationTaskStatus): Lifecycle of an async registration job.

            ``PENDING`` is created by ``POST /auth/register`` before the worker picks it
            up. ``PROCESSING`` means the dramatiq actor is running. Terminal states are
            ``COMPLETED`` (account ready) and ``FAILED`` (see ``error_code`` / ``error_detail``).
        task_id (UUID):
        business (BusinessSimpleOut | None | Unset):
        error (None | Unset | WhatsAppCloudRegisterTaskStatusErrorType0):
    """

    status: RegistrationTaskStatus
    task_id: UUID
    business: BusinessSimpleOut | None | Unset = UNSET
    error: None | Unset | WhatsAppCloudRegisterTaskStatusErrorType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.business_simple_out import BusinessSimpleOut  # noqa: PLC0415
        from ..models.whats_app_cloud_register_task_status_error_type_0 import (
            WhatsAppCloudRegisterTaskStatusErrorType0,  # noqa: PLC0415
        )

        status: str = self.status

        task_id = str(self.task_id)

        business: dict[str, Any] | None | Unset
        if isinstance(self.business, Unset):
            business = UNSET
        elif isinstance(self.business, BusinessSimpleOut):
            business = self.business.to_dict()
        else:
            business = self.business

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, WhatsAppCloudRegisterTaskStatusErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "task_id": task_id,
            }
        )
        if business is not UNSET:
            field_dict["business"] = business
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_simple_out import BusinessSimpleOut  # noqa: PLC0415
        from ..models.whats_app_cloud_register_task_status_error_type_0 import (
            WhatsAppCloudRegisterTaskStatusErrorType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = check_registration_task_status(d.pop("status"))

        task_id = UUID(d.pop("task_id"))

        def _parse_business(data: object) -> BusinessSimpleOut | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                business_type_0 = BusinessSimpleOut.from_dict(data)

                return business_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BusinessSimpleOut | None | Unset, data)

        business = _parse_business(d.pop("business", UNSET))

        def _parse_error(data: object) -> None | Unset | WhatsAppCloudRegisterTaskStatusErrorType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = WhatsAppCloudRegisterTaskStatusErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WhatsAppCloudRegisterTaskStatusErrorType0, data)

        error = _parse_error(d.pop("error", UNSET))

        whats_app_cloud_register_task_status = cls(
            status=status,
            task_id=task_id,
            business=business,
            error=error,
        )

        whats_app_cloud_register_task_status.additional_properties = d
        return whats_app_cloud_register_task_status

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
