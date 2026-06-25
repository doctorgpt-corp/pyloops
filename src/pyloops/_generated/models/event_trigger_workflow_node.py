from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.event_trigger_workflow_node_type_name import EventTriggerWorkflowNodeTypeName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_event_property import WorkflowEventProperty


T = TypeVar("T", bound="EventTriggerWorkflowNode")


@_attrs_define
class EventTriggerWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (EventTriggerWorkflowNodeTypeName):
        next_node_ids (list[str]):
        re_eligible (bool):
        event_name (str | Unset):
        event_properties (list[WorkflowEventProperty] | Unset):
    """

    id: str
    workflow_id: str
    type_name: EventTriggerWorkflowNodeTypeName
    next_node_ids: list[str]
    re_eligible: bool
    event_name: str | Unset = UNSET
    event_properties: list[WorkflowEventProperty] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        re_eligible = self.re_eligible

        event_name = self.event_name

        event_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.event_properties, Unset):
            event_properties = []
            for event_properties_item_data in self.event_properties:
                event_properties_item = event_properties_item_data.to_dict()
                event_properties.append(event_properties_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "reEligible": re_eligible,
            }
        )
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if event_properties is not UNSET:
            field_dict["eventProperties"] = event_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_event_property import WorkflowEventProperty

        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        type_name = EventTriggerWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        re_eligible = d.pop("reEligible")

        event_name = d.pop("eventName", UNSET)

        _event_properties = d.pop("eventProperties", UNSET)
        event_properties: list[WorkflowEventProperty] | Unset = UNSET
        if _event_properties is not UNSET:
            event_properties = []
            for event_properties_item_data in _event_properties:
                event_properties_item = WorkflowEventProperty.from_dict(event_properties_item_data)

                event_properties.append(event_properties_item)

        event_trigger_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            re_eligible=re_eligible,
            event_name=event_name,
            event_properties=event_properties,
        )

        return event_trigger_workflow_node
