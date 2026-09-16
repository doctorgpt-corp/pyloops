from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_property_trigger_workflow_mutation_node_type_name import (
    ContactPropertyTriggerWorkflowMutationNodeTypeName,
)

if TYPE_CHECKING:
    from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery


T = TypeVar("T", bound="ContactPropertyTriggerWorkflowMutationNodeWithRevision")


@_attrs_define
class ContactPropertyTriggerWorkflowMutationNodeWithRevision:
    """
    Attributes:
        id (str):
        type_name (ContactPropertyTriggerWorkflowMutationNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        contact_property_query (None | WorkflowContactPropertyQuery):
        re_eligible (bool): If `true`, the contacts will be able to enter this workflow every time the trigger is
            matched. If `false`, contacts will only ever enter this workflow once. Matches the "Trigger frequency" option in
            the UI.
        workflow_revision_id (str): The current workflow revision token. Pass the latest value as `expectedRevisionId`
            on the next workflow mutation.
    """

    id: str
    type_name: ContactPropertyTriggerWorkflowMutationNodeTypeName
    next_node_ids: list[str]
    contact_property_query: None | WorkflowContactPropertyQuery
    re_eligible: bool
    workflow_revision_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery  # noqa: PLC0415

        id = self.id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        contact_property_query: dict[str, Any] | None
        if isinstance(self.contact_property_query, WorkflowContactPropertyQuery):
            contact_property_query = self.contact_property_query.to_dict()
        else:
            contact_property_query = self.contact_property_query

        re_eligible = self.re_eligible

        workflow_revision_id: str
        workflow_revision_id = self.workflow_revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "contactPropertyQuery": contact_property_query,
                "reEligible": re_eligible,
                "workflowRevisionId": workflow_revision_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        type_name = ContactPropertyTriggerWorkflowMutationNodeTypeName(d.pop("typeName"))

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

        def _parse_workflow_revision_id(data: object) -> str:
            return cast(str, data)

        workflow_revision_id = _parse_workflow_revision_id(d.pop("workflowRevisionId"))

        contact_property_trigger_workflow_mutation_node_with_revision = cls(
            id=id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            contact_property_query=contact_property_query,
            re_eligible=re_eligible,
            workflow_revision_id=workflow_revision_id,
        )

        contact_property_trigger_workflow_mutation_node_with_revision.additional_properties = d
        return contact_property_trigger_workflow_mutation_node_with_revision

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
