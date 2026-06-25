from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_timer_action_workflow_node_type_name import SimplifiedTimerActionWorkflowNodeTypeName
from ..models.workflow_timer_unit import WorkflowTimerUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplifiedTimerActionWorkflowNode")


@_attrs_define
class SimplifiedTimerActionWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedTimerActionWorkflowNodeTypeName):
        next_node_ids (list[str]):
        amount (float | Unset):
        unit (WorkflowTimerUnit | Unset):
    """

    type_name: SimplifiedTimerActionWorkflowNodeTypeName
    next_node_ids: list[str]
    amount: float | Unset = UNSET
    unit: WorkflowTimerUnit | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        amount = self.amount

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
            }
        )
        if amount is not UNSET:
            field_dict["amount"] = amount
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = SimplifiedTimerActionWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        amount = d.pop("amount", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: WorkflowTimerUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = WorkflowTimerUnit(_unit)

        simplified_timer_action_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
            amount=amount,
            unit=unit,
        )

        return simplified_timer_action_workflow_node
