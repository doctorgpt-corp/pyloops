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
        id (str): The ID of the workflow.
        url (str): The URL of the workflow in the Loops app.
        workflow_revision_id (None | str): The current workflow revision token. Pass the latest value as
            `expectedRevisionId` on the next workflow mutation. Will be `null` for workflows without a revision token yet.
        status (SimplifiedWorkflowStatus):
        mailing_list_id (None | str): The ID of the mailing list the workflow sends to.
        root_node_id (str): The ID of the root node in the workflow graph.
        nodes (SimplifiedWorkflowNodes): A map of node IDs to simplified node objects. Each node includes `typeName` and
            `nextNodeIds`, plus type-specific fields when present. To get the full node object, use the `GET
            /v1/workflows/{workflowId}/nodes/{nodeId}` endpoint. Example: {'cf16k73gq014h3mmj5b6jdi9r': {'typeName':
            'SignupTrigger', 'nextNodeIds': ['cf16k73gq014h3mmj5b4jdifg', 'cf16k73gq014h3mmj5b4jdifh']}}.
        name (str | Unset): The name of the workflow.
        description (str | Unset): The description of the workflow.
    """

    id: str
    url: str
    workflow_revision_id: None | str
    status: SimplifiedWorkflowStatus
    mailing_list_id: None | str
    root_node_id: str
    nodes: SimplifiedWorkflowNodes
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        workflow_revision_id: None | str
        workflow_revision_id = self.workflow_revision_id

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
                "url": url,
                "workflowRevisionId": workflow_revision_id,
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
        from ..models.simplified_workflow_nodes import SimplifiedWorkflowNodes  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        def _parse_workflow_revision_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workflow_revision_id = _parse_workflow_revision_id(d.pop("workflowRevisionId"))

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
            url=url,
            workflow_revision_id=workflow_revision_id,
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
