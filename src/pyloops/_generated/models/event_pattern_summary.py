from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_pattern_summary_incoming_webhook_platform import EventPatternSummaryIncomingWebhookPlatform

T = TypeVar("T", bound="EventPatternSummary")


@_attrs_define
class EventPatternSummary:
    """
    Attributes:
        id (str): The ID of the event pattern.
        event_name (str): The name of the event pattern. Use this when sending events with the API.
        incoming_webhook_platform (EventPatternSummaryIncomingWebhookPlatform): The platform that sent this event
            pattern, if the event pattern is from an incoming webhook. Will be `null` for custom events.
    """

    id: str
    event_name: str
    incoming_webhook_platform: EventPatternSummaryIncomingWebhookPlatform
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_name = self.event_name

        incoming_webhook_platform = self.incoming_webhook_platform.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "eventName": event_name,
                "incomingWebhookPlatform": incoming_webhook_platform,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        event_name = d.pop("eventName")

        incoming_webhook_platform = EventPatternSummaryIncomingWebhookPlatform(d.pop("incomingWebhookPlatform"))

        event_pattern_summary = cls(
            id=id,
            event_name=event_name,
            incoming_webhook_platform=incoming_webhook_platform,
        )

        event_pattern_summary.additional_properties = d
        return event_pattern_summary

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
