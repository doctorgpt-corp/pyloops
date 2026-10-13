from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.contact_property_trigger_workflow_node_type_name import ContactPropertyTriggerWorkflowNodeTypeName

if TYPE_CHECKING:
    from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery


T = TypeVar("T", bound="ContactPropertyTriggerWorkflowNode")


@_attrs_define
class ContactPropertyTriggerWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (ContactPropertyTriggerWorkflowNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        contact_property_query (None | WorkflowContactPropertyQuery):
        re_eligible (bool): If `true`, the contacts will be able to enter this workflow every time the trigger is
            matched. If `false`, contacts will only ever enter this workflow once. Matches the "Trigger frequency" option in
            the UI.
    """

    id: str
    workflow_id: str
    type_name: ContactPropertyTriggerWorkflowNodeTypeName
    next_node_ids: list[str]
    contact_property_query: None | WorkflowContactPropertyQuery
    re_eligible: bool

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery  # noqa: PLC0415

        id = self.id

        workflow_id = self.workflow_id

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
                "id": id,
                "workflowId": workflow_id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "contactPropertyQuery": contact_property_query,
                "reEligible": re_eligible,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        type_name = ContactPropertyTriggerWorkflowNodeTypeName(d.pop("typeName"))

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

        contact_property_trigger_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            contact_property_query=contact_property_query,
            re_eligible=re_eligible,
        )

        return contact_property_trigger_workflow_node
