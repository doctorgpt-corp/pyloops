from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.workflow_add_to_list_trigger_payload_type_name import WorkflowAddToListTriggerPayloadTypeName
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowAddToListTriggerPayload")


@_attrs_define
class WorkflowAddToListTriggerPayload:
    """Updates an add-to-list trigger, or changes an existing trigger node to an add-to-list trigger.

    Attributes:
        type_name (WorkflowAddToListTriggerPayloadTypeName | Unset):
        re_eligible (bool | Unset): If `true`, the contacts will be able to enter this workflow every time the trigger
            is matched. If `false`, contacts will only ever enter this workflow once. Matches the "Trigger frequency" option
            in the UI.
    """

    type_name: WorkflowAddToListTriggerPayloadTypeName | Unset = UNSET
    re_eligible: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_name: str | Unset = UNSET
        if not isinstance(self.type_name, Unset):
            type_name = self.type_name.value

        re_eligible = self.re_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_name is not UNSET:
            field_dict["typeName"] = type_name
        if re_eligible is not UNSET:
            field_dict["reEligible"] = re_eligible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_name = d.pop("typeName", UNSET)
        type_name: WorkflowAddToListTriggerPayloadTypeName | Unset
        if isinstance(_type_name, Unset):
            type_name = UNSET
        else:
            type_name = WorkflowAddToListTriggerPayloadTypeName(_type_name)

        re_eligible = d.pop("reEligible", UNSET)

        workflow_add_to_list_trigger_payload = cls(
            type_name=type_name,
            re_eligible=re_eligible,
        )

        return workflow_add_to_list_trigger_payload
