from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.experiment_branch_workflow_node_type_name import ExperimentBranchWorkflowNodeTypeName
from ..models.workflow_experiment_type import WorkflowExperimentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExperimentBranchWorkflowNode")


@_attrs_define
class ExperimentBranchWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (ExperimentBranchWorkflowNodeTypeName):
        next_node_ids (list[str]):
        sampling_rate (float):
        experiment_type (WorkflowExperimentType):
        url (str | Unset):
        experiment_id (str | Unset):
    """

    id: str
    workflow_id: str
    type_name: ExperimentBranchWorkflowNodeTypeName
    next_node_ids: list[str]
    sampling_rate: float
    experiment_type: WorkflowExperimentType
    url: str | Unset = UNSET
    experiment_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        sampling_rate = self.sampling_rate

        experiment_type = self.experiment_type.value

        url = self.url

        experiment_id = self.experiment_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "samplingRate": sampling_rate,
                "experimentType": experiment_type,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if experiment_id is not UNSET:
            field_dict["experimentId"] = experiment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        type_name = ExperimentBranchWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        sampling_rate = d.pop("samplingRate")

        experiment_type = WorkflowExperimentType(d.pop("experimentType"))

        url = d.pop("url", UNSET)

        experiment_id = d.pop("experimentId", UNSET)

        experiment_branch_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            sampling_rate=sampling_rate,
            experiment_type=experiment_type,
            url=url,
            experiment_id=experiment_id,
        )

        return experiment_branch_workflow_node
