from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_contact_property_trigger_workflow_node_type_name import (
    SimplifiedContactPropertyTriggerWorkflowNodeTypeName,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery


T = TypeVar("T", bound="SimplifiedContactPropertyTriggerWorkflowNode")


@_attrs_define
class SimplifiedContactPropertyTriggerWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedContactPropertyTriggerWorkflowNodeTypeName):
        next_node_ids (list[str]):
        contact_property_query (WorkflowContactPropertyQuery | Unset):
        re_eligible (bool | Unset):
    """

    type_name: SimplifiedContactPropertyTriggerWorkflowNodeTypeName
    next_node_ids: list[str]
    contact_property_query: WorkflowContactPropertyQuery | Unset = UNSET
    re_eligible: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        contact_property_query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_property_query, Unset):
            contact_property_query = self.contact_property_query.to_dict()

        re_eligible = self.re_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
            }
        )
        if contact_property_query is not UNSET:
            field_dict["contactPropertyQuery"] = contact_property_query
        if re_eligible is not UNSET:
            field_dict["reEligible"] = re_eligible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery

        d = dict(src_dict)
        type_name = SimplifiedContactPropertyTriggerWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        _contact_property_query = d.pop("contactPropertyQuery", UNSET)
        contact_property_query: WorkflowContactPropertyQuery | Unset
        if isinstance(_contact_property_query, Unset):
            contact_property_query = UNSET
        else:
            contact_property_query = WorkflowContactPropertyQuery.from_dict(_contact_property_query)

        re_eligible = d.pop("reEligible", UNSET)

        simplified_contact_property_trigger_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
            contact_property_query=contact_property_query,
            re_eligible=re_eligible,
        )

        return simplified_contact_property_trigger_workflow_node
