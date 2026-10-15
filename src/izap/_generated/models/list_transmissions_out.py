from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transmission_status_out import TransmissionStatusOut


T = TypeVar("T", bound="ListTransmissionsOut")


@_attrs_define
class ListTransmissionsOut:
    """
    Attributes:
        business_id (UUID):
        total (int):
        transmissions (list[TransmissionStatusOut]):
    """

    business_id: UUID
    total: int
    transmissions: list[TransmissionStatusOut]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_id = str(self.business_id)

        total = self.total

        transmissions = []
        for transmissions_item_data in self.transmissions:
            transmissions_item = transmissions_item_data.to_dict()
            transmissions.append(transmissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "business_id": business_id,
                "total": total,
                "transmissions": transmissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transmission_status_out import TransmissionStatusOut  # noqa: PLC0415

        d = dict(src_dict)
        business_id = UUID(d.pop("business_id"))

        total = d.pop("total")

        transmissions = []
        _transmissions = d.pop("transmissions")
        for transmissions_item_data in _transmissions:
            transmissions_item = TransmissionStatusOut.from_dict(transmissions_item_data)

            transmissions.append(transmissions_item)

        list_transmissions_out = cls(
            business_id=business_id,
            total=total,
            transmissions=transmissions,
        )

        list_transmissions_out.additional_properties = d
        return list_transmissions_out

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
