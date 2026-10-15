from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.registration_task_status import RegistrationTaskStatus, check_registration_task_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="WhatsAppCloudRegisterAccepted")


@_attrs_define
class WhatsAppCloudRegisterAccepted:
    """202 body of ``POST /{business_id}/whatsapp_cloud/register``.

    Attributes:
        task_id (UUID):
        status (RegistrationTaskStatus | Unset): Lifecycle of an async registration job.

            ``PENDING`` is created by ``POST /auth/register`` before the worker picks it
            up. ``PROCESSING`` means the dramatiq actor is running. Terminal states are
            ``COMPLETED`` (account ready) and ``FAILED`` (see ``error_code`` / ``error_detail``).
    """

    task_id: UUID
    status: RegistrationTaskStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = str(self.task_id)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_id = UUID(d.pop("task_id"))

        _status = d.pop("status", UNSET)
        status: RegistrationTaskStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_registration_task_status(_status)

        whats_app_cloud_register_accepted = cls(
            task_id=task_id,
            status=status,
        )

        whats_app_cloud_register_accepted.additional_properties = d
        return whats_app_cloud_register_accepted

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
