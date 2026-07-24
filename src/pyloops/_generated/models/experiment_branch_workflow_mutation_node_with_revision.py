from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.experiment_branch_workflow_mutation_node_type_name import ExperimentBranchWorkflowMutationNodeTypeName

T = TypeVar("T", bound="ExperimentBranchWorkflowMutationNodeWithRevision")


@_attrs_define
class ExperimentBranchWorkflowMutationNodeWithRevision:
    """
    Attributes:
        id (str):
        type_name (ExperimentBranchWorkflowMutationNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        sampling_rate (float): The percentage of contacts that will be sent to variant branches, between `0` and `100`.
            The remaining percentage will be sent to the control branch. `100` sends all contacts to variant branches.
        workflow_revision_id (str): The current workflow revision token. Pass the latest value as `expectedRevisionId`
            on the next workflow mutation.
    """

    id: str
    type_name: ExperimentBranchWorkflowMutationNodeTypeName
    next_node_ids: list[str]
    sampling_rate: float
    workflow_revision_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        sampling_rate = self.sampling_rate

        workflow_revision_id: str
        workflow_revision_id = self.workflow_revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "samplingRate": sampling_rate,
                "workflowRevisionId": workflow_revision_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_name = ExperimentBranchWorkflowMutationNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        sampling_rate = d.pop("samplingRate")

        def _parse_workflow_revision_id(data: object) -> str:
            return cast(str, data)

        workflow_revision_id = _parse_workflow_revision_id(d.pop("workflowRevisionId"))

        experiment_branch_workflow_mutation_node_with_revision = cls(
            id=id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            sampling_rate=sampling_rate,
            workflow_revision_id=workflow_revision_id,
        )

        experiment_branch_workflow_mutation_node_with_revision.additional_properties = d
        return experiment_branch_workflow_mutation_node_with_revision

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
