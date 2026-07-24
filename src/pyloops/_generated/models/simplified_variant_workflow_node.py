from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_variant_workflow_node_type_name import SimplifiedVariantWorkflowNodeTypeName

T = TypeVar("T", bound="SimplifiedVariantWorkflowNode")


@_attrs_define
class SimplifiedVariantWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedVariantWorkflowNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        is_control (bool): Whether this is the control variant of an experiment.
    """

    type_name: SimplifiedVariantWorkflowNodeTypeName
    next_node_ids: list[str]
    is_control: bool

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        is_control = self.is_control

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "isControl": is_control,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = SimplifiedVariantWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        is_control = d.pop("isControl")

        simplified_variant_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
            is_control=is_control,
        )

        return simplified_variant_workflow_node
