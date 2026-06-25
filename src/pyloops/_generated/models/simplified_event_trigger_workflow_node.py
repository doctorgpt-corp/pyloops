from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_event_trigger_workflow_node_type_name import SimplifiedEventTriggerWorkflowNodeTypeName
from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplifiedEventTriggerWorkflowNode")


@_attrs_define
class SimplifiedEventTriggerWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedEventTriggerWorkflowNodeTypeName):
        next_node_ids (list[str]):
        event_name (str | Unset):
        re_eligible (bool | Unset):
    """

    type_name: SimplifiedEventTriggerWorkflowNodeTypeName
    next_node_ids: list[str]
    event_name: str | Unset = UNSET
    re_eligible: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        event_name = self.event_name

        re_eligible = self.re_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
            }
        )
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if re_eligible is not UNSET:
            field_dict["reEligible"] = re_eligible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = SimplifiedEventTriggerWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        event_name = d.pop("eventName", UNSET)

        re_eligible = d.pop("reEligible", UNSET)

        simplified_event_trigger_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
            event_name=event_name,
            re_eligible=re_eligible,
        )

        return simplified_event_trigger_workflow_node
