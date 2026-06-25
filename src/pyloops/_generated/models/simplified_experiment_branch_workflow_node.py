from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_experiment_branch_workflow_node_type_name import SimplifiedExperimentBranchWorkflowNodeTypeName
from ..models.workflow_experiment_type import WorkflowExperimentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplifiedExperimentBranchWorkflowNode")


@_attrs_define
class SimplifiedExperimentBranchWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedExperimentBranchWorkflowNodeTypeName):
        next_node_ids (list[str]):
        sampling_rate (float | Unset):
        url (str | Unset):
        experiment_id (str | Unset):
        experiment_type (WorkflowExperimentType | Unset):
    """

    type_name: SimplifiedExperimentBranchWorkflowNodeTypeName
    next_node_ids: list[str]
    sampling_rate: float | Unset = UNSET
    url: str | Unset = UNSET
    experiment_id: str | Unset = UNSET
    experiment_type: WorkflowExperimentType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        sampling_rate = self.sampling_rate

        url = self.url

        experiment_id = self.experiment_id

        experiment_type: str | Unset = UNSET
        if not isinstance(self.experiment_type, Unset):
            experiment_type = self.experiment_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
            }
        )
        if sampling_rate is not UNSET:
            field_dict["samplingRate"] = sampling_rate
        if url is not UNSET:
            field_dict["url"] = url
        if experiment_id is not UNSET:
            field_dict["experimentId"] = experiment_id
        if experiment_type is not UNSET:
            field_dict["experimentType"] = experiment_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = SimplifiedExperimentBranchWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        sampling_rate = d.pop("samplingRate", UNSET)

        url = d.pop("url", UNSET)

        experiment_id = d.pop("experimentId", UNSET)

        _experiment_type = d.pop("experimentType", UNSET)
        experiment_type: WorkflowExperimentType | Unset
        if isinstance(_experiment_type, Unset):
            experiment_type = UNSET
        else:
            experiment_type = WorkflowExperimentType(_experiment_type)

        simplified_experiment_branch_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
            sampling_rate=sampling_rate,
            url=url,
            experiment_id=experiment_id,
            experiment_type=experiment_type,
        )

        return simplified_experiment_branch_workflow_node
