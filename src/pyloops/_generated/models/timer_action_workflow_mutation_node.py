from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.timer_action_workflow_mutation_node_type_name import TimerActionWorkflowMutationNodeTypeName
from ..models.workflow_timer_unit import WorkflowTimerUnit

T = TypeVar("T", bound="TimerActionWorkflowMutationNode")


@_attrs_define
class TimerActionWorkflowMutationNode:
    """
    Attributes:
        id (str):
        type_name (TimerActionWorkflowMutationNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        amount (float): The amount of time to wait before triggering the next node. Set to `0` to move to the next node
            immediately.
        unit (WorkflowTimerUnit): The unit of time for the timer action node. m = minutes, h = hours, d = days.
    """

    id: str
    type_name: TimerActionWorkflowMutationNodeTypeName
    next_node_ids: list[str]
    amount: float
    unit: WorkflowTimerUnit
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        amount = self.amount

        unit = self.unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "amount": amount,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_name = TimerActionWorkflowMutationNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        amount = d.pop("amount")

        unit = WorkflowTimerUnit(d.pop("unit"))

        timer_action_workflow_mutation_node = cls(
            id=id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            amount=amount,
            unit=unit,
        )

        timer_action_workflow_mutation_node.additional_properties = d
        return timer_action_workflow_mutation_node

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
