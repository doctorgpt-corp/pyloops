from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_event_trigger_workflow_node_type_name import SimplifiedEventTriggerWorkflowNodeTypeName

T = TypeVar("T", bound="SimplifiedEventTriggerWorkflowNode")


@_attrs_define
class SimplifiedEventTriggerWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedEventTriggerWorkflowNodeTypeName):
        next_node_ids (list[str]):
        event_name (None | str):
        re_eligible (bool):
    """

    type_name: SimplifiedEventTriggerWorkflowNodeTypeName
    next_node_ids: list[str]
    event_name: None | str
    re_eligible: bool

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        event_name: None | str
        event_name = self.event_name

        re_eligible = self.re_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "eventName": event_name,
                "reEligible": re_eligible,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = SimplifiedEventTriggerWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        def _parse_event_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        event_name = _parse_event_name(d.pop("eventName"))

        re_eligible = d.pop("reEligible")

        simplified_event_trigger_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
            event_name=event_name,
            re_eligible=re_eligible,
        )

        return simplified_event_trigger_workflow_node
