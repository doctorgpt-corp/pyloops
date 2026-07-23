from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_workflow_node_before_request_insert_mode import CreateWorkflowNodeBeforeRequestInsertMode
from ..models.create_workflow_node_type_name import CreateWorkflowNodeTypeName

T = TypeVar("T", bound="CreateWorkflowNodeBeforeRequest")


@_attrs_define
class CreateWorkflowNodeBeforeRequest:
    """Insert a new node before `beforeNodeId`.

    Attributes:
        expected_revision_id (None | str): The workflow revision token returned by the latest workflow read or mutation.
            Older workflows may return `null` before their first revision-aware mutation; pass `null` back as
            `expectedRevisionId` in that case. If the token is stale, the API returns a `409 Conflict` error.
        insert_mode (CreateWorkflowNodeBeforeRequestInsertMode):
        node_type_name (CreateWorkflowNodeTypeName): Node types that can be created with the API. `*Trigger` nodes and
            `ExitAction` nodes cannot be created.
        before_node_id (str): The node to insert before. The target must have at least one incoming parent and cannot be
            a trigger node.
    """

    expected_revision_id: None | str
    insert_mode: CreateWorkflowNodeBeforeRequestInsertMode
    node_type_name: CreateWorkflowNodeTypeName
    before_node_id: str

    def to_dict(self) -> dict[str, Any]:
        expected_revision_id: None | str
        expected_revision_id = self.expected_revision_id

        insert_mode = self.insert_mode.value

        node_type_name = self.node_type_name.value

        before_node_id = self.before_node_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expectedRevisionId": expected_revision_id,
                "insertMode": insert_mode,
                "nodeTypeName": node_type_name,
                "beforeNodeId": before_node_id,
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

        insert_mode = CreateWorkflowNodeBeforeRequestInsertMode(d.pop("insertMode"))

        node_type_name = CreateWorkflowNodeTypeName(d.pop("nodeTypeName"))

        before_node_id = d.pop("beforeNodeId")

        create_workflow_node_before_request = cls(
            expected_revision_id=expected_revision_id,
            insert_mode=insert_mode,
            node_type_name=node_type_name,
            before_node_id=before_node_id,
        )

        return create_workflow_node_before_request
