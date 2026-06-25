from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.add_to_list_trigger_workflow_node_type_name import AddToListTriggerWorkflowNodeTypeName

T = TypeVar("T", bound="AddToListTriggerWorkflowNode")


@_attrs_define
class AddToListTriggerWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (AddToListTriggerWorkflowNodeTypeName):
        next_node_ids (list[str]):
        mailing_list_id (str):
        re_eligible (bool):
    """

    id: str
    workflow_id: str
    type_name: AddToListTriggerWorkflowNodeTypeName
    next_node_ids: list[str]
    mailing_list_id: str
    re_eligible: bool

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        mailing_list_id = self.mailing_list_id

        re_eligible = self.re_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
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
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        type_name = AddToListTriggerWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        mailing_list_id = d.pop("mailingListId")

        re_eligible = d.pop("reEligible")

        add_to_list_trigger_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            mailing_list_id=mailing_list_id,
            re_eligible=re_eligible,
        )

        return add_to_list_trigger_workflow_node
