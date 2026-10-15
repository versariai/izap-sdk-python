from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookEndpointCreated")


@_attrs_define
class WebhookEndpointCreated:
    """``WebhookEndpointOut`` plus the one-time secret. Returned by create and rotate only.

    Attributes:
        consecutive_failures (int):
        created (datetime.datetime):
        enabled (bool):
        id (UUID):
        label (str):
        last_delivery_at (datetime.datetime | None):
        last_error (None | str):
        signing_secret (str):
        subscribed_events (list[str]):
        url (str):
    """

    consecutive_failures: int
    created: datetime.datetime
    enabled: bool
    id: UUID
    label: str
    last_delivery_at: datetime.datetime | None
    last_error: None | str
    signing_secret: str
    subscribed_events: list[str]
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consecutive_failures = self.consecutive_failures

        created = self.created.isoformat()

        enabled = self.enabled

        id = str(self.id)

        label = self.label

        last_delivery_at: None | str
        if isinstance(self.last_delivery_at, datetime.datetime):
            last_delivery_at = self.last_delivery_at.isoformat()
        else:
            last_delivery_at = self.last_delivery_at

        last_error: None | str
        last_error = self.last_error

        signing_secret = self.signing_secret

        subscribed_events = self.subscribed_events

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "consecutive_failures": consecutive_failures,
                "created": created,
                "enabled": enabled,
                "id": id,
                "label": label,
                "last_delivery_at": last_delivery_at,
                "last_error": last_error,
                "signing_secret": signing_secret,
                "subscribed_events": subscribed_events,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        consecutive_failures = d.pop("consecutive_failures")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        enabled = d.pop("enabled")

        id = UUID(d.pop("id"))

        label = d.pop("label")

        def _parse_last_delivery_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_delivery_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_delivery_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_delivery_at = _parse_last_delivery_at(d.pop("last_delivery_at"))

        def _parse_last_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error = _parse_last_error(d.pop("last_error"))

        signing_secret = d.pop("signing_secret")

        subscribed_events = cast(list[str], d.pop("subscribed_events"))

        url = d.pop("url")

        webhook_endpoint_created = cls(
            consecutive_failures=consecutive_failures,
            created=created,
            enabled=enabled,
            id=id,
            label=label,
            last_delivery_at=last_delivery_at,
            last_error=last_error,
            signing_secret=signing_secret,
            subscribed_events=subscribed_events,
            url=url,
        )

        webhook_endpoint_created.additional_properties = d
        return webhook_endpoint_created

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
