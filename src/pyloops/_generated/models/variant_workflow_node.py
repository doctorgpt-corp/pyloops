from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.variant_workflow_node_type_name import VariantWorkflowNodeTypeName
from ..types import UNSET, Unset

T = TypeVar("T", bound="VariantWorkflowNode")


@_attrs_define
class VariantWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (VariantWorkflowNodeTypeName):
        next_node_ids (list[str]):
        is_control (bool | Unset):
    """

    id: str
    workflow_id: str
    type_name: VariantWorkflowNodeTypeName
    next_node_ids: list[str]
    is_control: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        is_control = self.is_control

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
            }
        )
        if is_control is not UNSET:
            field_dict["isControl"] = is_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        type_name = VariantWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        is_control = d.pop("isControl", UNSET)

        variant_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            is_control=is_control,
        )

        return variant_workflow_node
