from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookTestingTestEventPayload")


@_attrs_define
class WebhookTestingTestEventPayload:
    """
    Attributes:
        event_name (Literal['testing.testEvent']):
        event_time (int): Unix timestamp in seconds.
        message (Literal['test']):
        webhook_schema_version (Literal['1.0.0']):
    """

    event_name: Literal["testing.testEvent"]
    event_time: int
    message: Literal["test"]
    webhook_schema_version: Literal["1.0.0"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        event_time = self.event_time

        message = self.message

        webhook_schema_version = self.webhook_schema_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventName": event_name,
                "eventTime": event_time,
                "message": message,
                "webhookSchemaVersion": webhook_schema_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_name = cast(Literal["testing.testEvent"], d.pop("eventName"))
        if event_name != "testing.testEvent":
            raise ValueError(f"eventName must match const 'testing.testEvent', got '{event_name}'")

        event_time = d.pop("eventTime")

        message = cast(Literal["test"], d.pop("message"))
        if message != "test":
            raise ValueError(f"message must match const 'test', got '{message}'")

        webhook_schema_version = cast(Literal["1.0.0"], d.pop("webhookSchemaVersion"))
        if webhook_schema_version != "1.0.0":
            raise ValueError(f"webhookSchemaVersion must match const '1.0.0', got '{webhook_schema_version}'")

        webhook_testing_test_event_payload = cls(
            event_name=event_name,
            event_time=event_time,
            message=message,
            webhook_schema_version=webhook_schema_version,
        )

        webhook_testing_test_event_payload.additional_properties = d
        return webhook_testing_test_event_payload

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
