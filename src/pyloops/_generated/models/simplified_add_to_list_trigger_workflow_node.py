from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_add_to_list_trigger_workflow_node_type_name import (
    SimplifiedAddToListTriggerWorkflowNodeTypeName,
)

T = TypeVar("T", bound="SimplifiedAddToListTriggerWorkflowNode")


@_attrs_define
class SimplifiedAddToListTriggerWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedAddToListTriggerWorkflowNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        mailing_list_id (None | str): The ID of the mailing list that triggers the workflow.
        re_eligible (bool): If `true`, the contacts will be able to enter this workflow every time the trigger is
            matched. If `false`, contacts will only ever enter this workflow once. Matches the "Trigger frequency" option in
            the UI.
    """

    type_name: SimplifiedAddToListTriggerWorkflowNodeTypeName
    next_node_ids: list[str]
    mailing_list_id: None | str
    re_eligible: bool

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        mailing_list_id: None | str
        mailing_list_id = self.mailing_list_id

        re_eligible = self.re_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "mailingListId": mailing_list_id,
                "reEligible": re_eligible,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = SimplifiedAddToListTriggerWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        def _parse_mailing_list_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mailing_list_id = _parse_mailing_list_id(d.pop("mailingListId"))

        re_eligible = d.pop("reEligible")

        simplified_add_to_list_trigger_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
            mailing_list_id=mailing_list_id,
            re_eligible=re_eligible,
        )

        return simplified_add_to_list_trigger_workflow_node
