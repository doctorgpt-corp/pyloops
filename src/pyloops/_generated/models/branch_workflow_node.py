from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.branch_workflow_node_type_name import BranchWorkflowNodeTypeName

T = TypeVar("T", bound="BranchWorkflowNode")


@_attrs_define
class BranchWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (BranchWorkflowNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
    """

    id: str
    workflow_id: str
    type_name: BranchWorkflowNodeTypeName
    next_node_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        type_name = BranchWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        branch_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
        )

        return branch_workflow_node
