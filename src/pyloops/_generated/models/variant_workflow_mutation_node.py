from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.variant_workflow_mutation_node_type_name import VariantWorkflowMutationNodeTypeName
from ..types import UNSET, Unset

T = TypeVar("T", bound="VariantWorkflowMutationNode")


@_attrs_define
class VariantWorkflowMutationNode:
    """
    Attributes:
        id (str):
        type_name (VariantWorkflowMutationNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        is_control (bool | Unset): Whether this is the control variant of an experiment.
    """

    id: str
    type_name: VariantWorkflowMutationNodeTypeName
    next_node_ids: list[str]
    is_control: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        is_control = self.is_control

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
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

        type_name = VariantWorkflowMutationNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        is_control = d.pop("isControl", UNSET)

        variant_workflow_mutation_node = cls(
            id=id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            is_control=is_control,
        )

        variant_workflow_mutation_node.additional_properties = d
        return variant_workflow_mutation_node

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
