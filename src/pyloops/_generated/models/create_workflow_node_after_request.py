from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_workflow_node_after_request_insert_mode import CreateWorkflowNodeAfterRequestInsertMode
from ..models.create_workflow_node_type_name import CreateWorkflowNodeTypeName

T = TypeVar("T", bound="CreateWorkflowNodeAfterRequest")


@_attrs_define
class CreateWorkflowNodeAfterRequest:
    """Insert a new node after `fromNodeId`. This is valid only when `fromNodeId` has exactly one outgoing node. It is
    invalid when `fromNodeId` has no outgoing nodes, multiple outgoing nodes, or is an exit node. When the source has
    multiple outgoing nodes, use `between` with the exact `toNodeId` instead.

        Attributes:
            expected_revision_id (None | str): The workflow revision token returned by the latest workflow read or mutation.
                Older workflows may return `null` before their first revision-aware mutation; pass `null` back as
                `expectedRevisionId` in that case. If the token is stale, the API returns a `409 Conflict` error.
            insert_mode (CreateWorkflowNodeAfterRequestInsertMode):
            node_type_name (CreateWorkflowNodeTypeName): Node types that can be created with the API. `*Trigger` nodes and
                `ExitAction` nodes cannot be created.
            from_node_id (str): The node to insert after. This node must currently have exactly one outgoing node.
    """

    expected_revision_id: None | str
    insert_mode: CreateWorkflowNodeAfterRequestInsertMode
    node_type_name: CreateWorkflowNodeTypeName
    from_node_id: str

    def to_dict(self) -> dict[str, Any]:
        expected_revision_id: None | str
        expected_revision_id = self.expected_revision_id

        insert_mode = self.insert_mode.value

        node_type_name = self.node_type_name.value

        from_node_id = self.from_node_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expectedRevisionId": expected_revision_id,
                "insertMode": insert_mode,
                "nodeTypeName": node_type_name,
                "fromNodeId": from_node_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expected_revision_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expected_revision_id = _parse_expected_revision_id(d.pop("expectedRevisionId"))

        insert_mode = CreateWorkflowNodeAfterRequestInsertMode(d.pop("insertMode"))

        node_type_name = CreateWorkflowNodeTypeName(d.pop("nodeTypeName"))

        from_node_id = d.pop("fromNodeId")

        create_workflow_node_after_request = cls(
            expected_revision_id=expected_revision_id,
            insert_mode=insert_mode,
            node_type_name=node_type_name,
            from_node_id=from_node_id,
        )

        return create_workflow_node_after_request
