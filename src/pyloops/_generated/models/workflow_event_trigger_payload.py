from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.workflow_event_trigger_payload_type_name import WorkflowEventTriggerPayloadTypeName
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowEventTriggerPayload")


@_attrs_define
class WorkflowEventTriggerPayload:
    """Updates an event trigger, or changes an existing trigger node to an event trigger. Assign the event pattern with
    either `eventPatternId` or `eventName`, not both. Set either field to `null` to clear the event-pattern
    relationship.

        Attributes:
            type_name (WorkflowEventTriggerPayloadTypeName | Unset):
            event_pattern_id (None | str | Unset): The ID of the event pattern to trigger on. Use either `eventPatternId` or
                `eventName`, not both. Set to `null` to clear the event-pattern relationship.
            event_name (None | str | Unset): The name of the event pattern to trigger on. Use this when you know the event
                name but not the internal event pattern ID. Use either `eventName` or `eventPatternId`, not both. Set to `null`
                to clear the event-pattern relationship.
            re_eligible (bool | Unset): If `true`, the contacts will be able to enter this workflow every time the trigger
                is matched. If `false`, contacts will only ever enter this workflow once. Matches the "Trigger frequency" option
                in the UI.
    """

    type_name: WorkflowEventTriggerPayloadTypeName | Unset = UNSET
    event_pattern_id: None | str | Unset = UNSET
    event_name: None | str | Unset = UNSET
    re_eligible: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_name: str | Unset = UNSET
        if not isinstance(self.type_name, Unset):
            type_name = self.type_name.value

        event_pattern_id: None | str | Unset
        if isinstance(self.event_pattern_id, Unset):
            event_pattern_id = UNSET
        else:
            event_pattern_id = self.event_pattern_id

        event_name: None | str | Unset
        if isinstance(self.event_name, Unset):
            event_name = UNSET
        else:
            event_name = self.event_name

        re_eligible = self.re_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_name is not UNSET:
            field_dict["typeName"] = type_name
        if event_pattern_id is not UNSET:
            field_dict["eventPatternId"] = event_pattern_id
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if re_eligible is not UNSET:
            field_dict["reEligible"] = re_eligible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_name = d.pop("typeName", UNSET)
        type_name: WorkflowEventTriggerPayloadTypeName | Unset
        if isinstance(_type_name, Unset):
            type_name = UNSET
        else:
            type_name = WorkflowEventTriggerPayloadTypeName(_type_name)

        def _parse_event_pattern_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_pattern_id = _parse_event_pattern_id(d.pop("eventPatternId", UNSET))

        def _parse_event_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_name = _parse_event_name(d.pop("eventName", UNSET))

        re_eligible = d.pop("reEligible", UNSET)

        workflow_event_trigger_payload = cls(
            type_name=type_name,
            event_pattern_id=event_pattern_id,
            event_name=event_name,
            re_eligible=re_eligible,
        )

        return workflow_event_trigger_payload
