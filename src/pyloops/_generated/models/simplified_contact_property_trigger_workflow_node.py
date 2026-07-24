from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_contact_property_trigger_workflow_node_type_name import (
    SimplifiedContactPropertyTriggerWorkflowNodeTypeName,
)

if TYPE_CHECKING:
    from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery


T = TypeVar("T", bound="SimplifiedContactPropertyTriggerWorkflowNode")


@_attrs_define
class SimplifiedContactPropertyTriggerWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedContactPropertyTriggerWorkflowNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        contact_property_query (None | WorkflowContactPropertyQuery):
        re_eligible (bool): If `true`, the contacts will be able to enter this workflow every time the trigger is
            matched. If `false`, contacts will only ever enter this workflow once. Matches the "Trigger frequency" option in
            the UI.
    """

    type_name: SimplifiedContactPropertyTriggerWorkflowNodeTypeName
    next_node_ids: list[str]
    contact_property_query: None | WorkflowContactPropertyQuery
    re_eligible: bool

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        contact_property_query: dict[str, Any] | None
        if isinstance(self.contact_property_query, WorkflowContactPropertyQuery):
            contact_property_query = self.contact_property_query.to_dict()
        else:
            contact_property_query = self.contact_property_query

        re_eligible = self.re_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "contactPropertyQuery": contact_property_query,
                "reEligible": re_eligible,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery

        d = dict(src_dict)
        type_name = SimplifiedContactPropertyTriggerWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        def _parse_contact_property_query(data: object) -> None | WorkflowContactPropertyQuery:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                contact_property_query_type_0 = WorkflowContactPropertyQuery.from_dict(data)

                return contact_property_query_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkflowContactPropertyQuery, data)

        contact_property_query = _parse_contact_property_query(d.pop("contactPropertyQuery"))

        re_eligible = d.pop("reEligible")

        simplified_contact_property_trigger_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
            contact_property_query=contact_property_query,
            re_eligible=re_eligible,
        )

        return simplified_contact_property_trigger_workflow_node
