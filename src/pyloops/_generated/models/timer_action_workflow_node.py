from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.timer_action_workflow_node_type_name import TimerActionWorkflowNodeTypeName
from ..models.workflow_timer_unit import WorkflowTimerUnit

T = TypeVar("T", bound="TimerActionWorkflowNode")


@_attrs_define
class TimerActionWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (TimerActionWorkflowNodeTypeName):
        next_node_ids (list[str]):
        amount (float):
        unit (WorkflowTimerUnit):
    """

    id: str
    workflow_id: str
    type_name: TimerActionWorkflowNodeTypeName
    next_node_ids: list[str]
    amount: float
    unit: WorkflowTimerUnit

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        amount = self.amount

        unit = self.unit.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
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

        workflow_id = d.pop("workflowId")

        type_name = TimerActionWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        amount = d.pop("amount")

        unit = WorkflowTimerUnit(d.pop("unit"))

        timer_action_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            amount=amount,
            unit=unit,
        )

        return timer_action_workflow_node
