from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransmissionStatusOut")


@_attrs_define
class TransmissionStatusOut:
    """
    Attributes:
        business_id (UUID):
        completed_at (datetime.datetime | None):
        failed_count (int):
        name (str):
        pending_count (int):
        progress_pct (float):
        scheduled_at (datetime.datetime | None):
        sent_count (int):
        started_at (datetime.datetime | None):
        status (str):
        template_name (str):
        total_recipients (int):
        transmission_id (UUID):
        transmission_type (str):
        created (datetime.datetime | None | Unset):
    """

    business_id: UUID
    completed_at: datetime.datetime | None
    failed_count: int
    name: str
    pending_count: int
    progress_pct: float
    scheduled_at: datetime.datetime | None
    sent_count: int
    started_at: datetime.datetime | None
    status: str
    template_name: str
    total_recipients: int
    transmission_id: UUID
    transmission_type: str
    created: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id = str(self.business_id)

        completed_at: None | str
        if isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        failed_count = self.failed_count

        name = self.name

        pending_count = self.pending_count

        progress_pct = self.progress_pct

        scheduled_at: None | str
        if isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        sent_count = self.sent_count

        started_at: None | str
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        status = self.status

        template_name = self.template_name

        total_recipients = self.total_recipients

        transmission_id = str(self.transmission_id)

        transmission_type = self.transmission_type

        created: None | str | Unset
        if isinstance(self.created, Unset):
            created = UNSET
        elif isinstance(self.created, datetime.datetime):
            created = self.created.isoformat()
        else:
            created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_id": business_id,
                "completed_at": completed_at,
                "failed_count": failed_count,
                "name": name,
                "pending_count": pending_count,
                "progress_pct": progress_pct,
                "scheduled_at": scheduled_at,
                "sent_count": sent_count,
                "started_at": started_at,
                "status": status,
                "template_name": template_name,
                "total_recipients": total_recipients,
                "transmission_id": transmission_id,
                "transmission_type": transmission_type,
            }
        )
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_id = UUID(d.pop("business_id"))

        def _parse_completed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        completed_at = _parse_completed_at(d.pop("completed_at"))

        failed_count = d.pop("failed_count")

        name = d.pop("name")

        pending_count = d.pop("pending_count")

        progress_pct = d.pop("progress_pct")

        def _parse_scheduled_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduled_at"))

        sent_count = d.pop("sent_count")

        def _parse_started_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        started_at = _parse_started_at(d.pop("started_at"))

        status = d.pop("status")

        template_name = d.pop("template_name")

        total_recipients = d.pop("total_recipients")

        transmission_id = UUID(d.pop("transmission_id"))

        transmission_type = d.pop("transmission_type")

        def _parse_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_type_0 = datetime.datetime.fromisoformat(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created = _parse_created(d.pop("created", UNSET))

        transmission_status_out = cls(
            business_id=business_id,
            completed_at=completed_at,
            failed_count=failed_count,
            name=name,
            pending_count=pending_count,
            progress_pct=progress_pct,
            scheduled_at=scheduled_at,
            sent_count=sent_count,
            started_at=started_at,
            status=status,
            template_name=template_name,
            total_recipients=total_recipients,
            transmission_id=transmission_id,
            transmission_type=transmission_type,
            created=created,
        )

        transmission_status_out.additional_properties = d
        return transmission_status_out

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
