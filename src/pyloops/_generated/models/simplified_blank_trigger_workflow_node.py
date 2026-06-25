from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_blank_trigger_workflow_node_type_name import SimplifiedBlankTriggerWorkflowNodeTypeName

T = TypeVar("T", bound="SimplifiedBlankTriggerWorkflowNode")


@_attrs_define
class SimplifiedBlankTriggerWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedBlankTriggerWorkflowNodeTypeName):
        next_node_ids (list[str]):
    """

    type_name: SimplifiedBlankTriggerWorkflowNodeTypeName
    next_node_ids: list[str]

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = SimplifiedBlankTriggerWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        simplified_blank_trigger_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
        )

        return simplified_blank_trigger_workflow_node
