from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.experiment_branch_workflow_node_type_name import ExperimentBranchWorkflowNodeTypeName

T = TypeVar("T", bound="ExperimentBranchWorkflowNode")


@_attrs_define
class ExperimentBranchWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (ExperimentBranchWorkflowNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        sampling_rate (float): The percentage of contacts that will be sent to variant branches, between `0` and `100`.
            The remaining percentage will be sent to the control branch. `100` sends all contacts to variant branches.
    """

    id: str
    workflow_id: str
    type_name: ExperimentBranchWorkflowNodeTypeName
    next_node_ids: list[str]
    sampling_rate: float

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        sampling_rate = self.sampling_rate

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "samplingRate": sampling_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        type_name = ExperimentBranchWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        sampling_rate = d.pop("samplingRate")

        experiment_branch_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            sampling_rate=sampling_rate,
        )

        return experiment_branch_workflow_node
