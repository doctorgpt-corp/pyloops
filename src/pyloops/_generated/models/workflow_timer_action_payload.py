from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.workflow_timer_unit import WorkflowTimerUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowTimerActionPayload")


@_attrs_define
class WorkflowTimerActionPayload:
    """Configuration for the timer action node.

    Attributes:
        amount (float | Unset): The amount of time to wait before triggering the next node. Set to `0` to move to the
            next node immediately.
        unit (WorkflowTimerUnit | Unset): The unit of time for the timer action node. m = minutes, h = hours, d = days.
    """

    amount: float | Unset = UNSET
    unit: WorkflowTimerUnit | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: WorkflowTimerUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = WorkflowTimerUnit(_unit)

        workflow_timer_action_payload = cls(
            amount=amount,
            unit=unit,
        )

        return workflow_timer_action_payload
