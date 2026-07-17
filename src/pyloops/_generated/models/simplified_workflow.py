from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.simplified_workflow_status import SimplifiedWorkflowStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.simplified_workflow_nodes import SimplifiedWorkflowNodes


T = TypeVar("T", bound="SimplifiedWorkflow")


@_attrs_define
class SimplifiedWorkflow:
    """
    Attributes:
        id (str):
        status (SimplifiedWorkflowStatus):
        mailing_list_id (None | str):
        root_node_id (str):
        nodes (SimplifiedWorkflowNodes):
        name (str | Unset):
        description (str | Unset):
    """

    id: str
    status: SimplifiedWorkflowStatus
    mailing_list_id: None | str
    root_node_id: str
    nodes: SimplifiedWorkflowNodes
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        mailing_list_id: None | str
        mailing_list_id = self.mailing_list_id

        root_node_id = self.root_node_id

        nodes = self.nodes.to_dict()

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "mailingListId": mailing_list_id,
                "rootNodeId": root_node_id,
                "nodes": nodes,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simplified_workflow_nodes import SimplifiedWorkflowNodes

        d = dict(src_dict)
        id = d.pop("id")

        status = SimplifiedWorkflowStatus(d.pop("status"))

        def _parse_mailing_list_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mailing_list_id = _parse_mailing_list_id(d.pop("mailingListId"))

        root_node_id = d.pop("rootNodeId")

        nodes = SimplifiedWorkflowNodes.from_dict(d.pop("nodes"))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        simplified_workflow = cls(
            id=id,
            status=status,
            mailing_list_id=mailing_list_id,
            root_node_id=root_node_id,
            nodes=nodes,
            name=name,
            description=description,
        )

        simplified_workflow.additional_properties = d
        return simplified_workflow

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
