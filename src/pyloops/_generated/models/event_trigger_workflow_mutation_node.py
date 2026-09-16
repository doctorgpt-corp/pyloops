from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_trigger_workflow_mutation_node_type_name import EventTriggerWorkflowMutationNodeTypeName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_event_property import WorkflowEventProperty


T = TypeVar("T", bound="EventTriggerWorkflowMutationNode")


@_attrs_define
class EventTriggerWorkflowMutationNode:
    """
    Attributes:
        id (str):
        type_name (EventTriggerWorkflowMutationNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        re_eligible (bool): If `true`, the contacts will be able to enter this workflow every time the trigger is
            matched. If `false`, contacts will only ever enter this workflow once. Matches the "Trigger frequency" option in
            the UI.
        event_name (str | Unset): The name of the event pattern that triggers this node.
        event_properties (list[WorkflowEventProperty] | Unset): The properties of the event pattern, which can be used
            in emails.
    """

    id: str
    type_name: EventTriggerWorkflowMutationNodeTypeName
    next_node_ids: list[str]
    re_eligible: bool
    event_name: str | Unset = UNSET
    event_properties: list[WorkflowEventProperty] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
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
        from ..models.workflow_event_property import WorkflowEventProperty  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        type_name = EventTriggerWorkflowMutationNodeTypeName(d.pop("typeName"))

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

        event_trigger_workflow_mutation_node = cls(
            id=id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            re_eligible=re_eligible,
            event_name=event_name,
            event_properties=event_properties,
        )

        event_trigger_workflow_mutation_node.additional_properties = d
        return event_trigger_workflow_mutation_node

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
