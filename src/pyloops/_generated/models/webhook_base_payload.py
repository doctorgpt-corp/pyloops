from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_contact_identity import WebhookContactIdentity


T = TypeVar("T", bound="WebhookBasePayload")


@_attrs_define
class WebhookBasePayload:
    """
    Attributes:
        event_name (str):
        event_time (int): Unix timestamp in seconds.
        webhook_schema_version (Literal['1.0.0']):
        contact_identity (WebhookContactIdentity):
    """

    event_name: str
    event_time: int
    webhook_schema_version: Literal["1.0.0"]
    contact_identity: WebhookContactIdentity
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        event_time = self.event_time

        webhook_schema_version = self.webhook_schema_version

        contact_identity = self.contact_identity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventName": event_name,
                "eventTime": event_time,
                "webhookSchemaVersion": webhook_schema_version,
                "contactIdentity": contact_identity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_contact_identity import WebhookContactIdentity

        d = dict(src_dict)
        event_name = d.pop("eventName")

        event_time = d.pop("eventTime")

        webhook_schema_version = cast(Literal["1.0.0"], d.pop("webhookSchemaVersion"))
        if webhook_schema_version != "1.0.0":
            raise ValueError(f"webhookSchemaVersion must match const '1.0.0', got '{webhook_schema_version}'")

        contact_identity = WebhookContactIdentity.from_dict(d.pop("contactIdentity"))

        webhook_base_payload = cls(
            event_name=event_name,
            event_time=event_time,
            webhook_schema_version=webhook_schema_version,
            contact_identity=contact_identity,
        )

        webhook_base_payload.additional_properties = d
        return webhook_base_payload

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
