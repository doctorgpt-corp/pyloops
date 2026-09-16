from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_pattern_incoming_webhook_platform import EventPatternIncomingWebhookPlatform

if TYPE_CHECKING:
    from ..models.workflow_event_property import WorkflowEventProperty


T = TypeVar("T", bound="EventPattern")


@_attrs_define
class EventPattern:
    """
    Attributes:
        id (str):
        event_name (str): The name of the event pattern. Use this when sending events with the API.
        event_properties (list[WorkflowEventProperty]): The properties of the event pattern, which can be used in
            emails.
        incoming_webhook_platform (EventPatternIncomingWebhookPlatform): The platform that sent this event pattern, if
            the event pattern is from an incoming webhook. Will be `null` for custom events.
    """

    id: str
    event_name: str
    event_properties: list[WorkflowEventProperty]
    incoming_webhook_platform: EventPatternIncomingWebhookPlatform
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_name = self.event_name

        event_properties = []
        for event_properties_item_data in self.event_properties:
            event_properties_item = event_properties_item_data.to_dict()
            event_properties.append(event_properties_item)

        incoming_webhook_platform = self.incoming_webhook_platform.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "eventName": event_name,
                "eventProperties": event_properties,
                "incomingWebhookPlatform": incoming_webhook_platform,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_event_property import WorkflowEventProperty  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        event_name = d.pop("eventName")

        event_properties = []
        _event_properties = d.pop("eventProperties")
        for event_properties_item_data in _event_properties:
            event_properties_item = WorkflowEventProperty.from_dict(event_properties_item_data)

            event_properties.append(event_properties_item)

        incoming_webhook_platform = EventPatternIncomingWebhookPlatform(d.pop("incomingWebhookPlatform"))

        event_pattern = cls(
            id=id,
            event_name=event_name,
            event_properties=event_properties,
            incoming_webhook_platform=incoming_webhook_platform,
        )

        event_pattern.additional_properties = d
        return event_pattern

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
