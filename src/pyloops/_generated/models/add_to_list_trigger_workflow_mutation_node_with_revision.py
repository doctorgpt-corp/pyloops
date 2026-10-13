from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_to_list_trigger_workflow_mutation_node_type_name import AddToListTriggerWorkflowMutationNodeTypeName

T = TypeVar("T", bound="AddToListTriggerWorkflowMutationNodeWithRevision")


@_attrs_define
class AddToListTriggerWorkflowMutationNodeWithRevision:
    """
    Attributes:
        id (str):
        type_name (AddToListTriggerWorkflowMutationNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        mailing_list_id (None | str): The ID of the mailing list this trigger sends to, if set.
        re_eligible (bool): If `true`, the contacts will be able to enter this workflow every time the trigger is
            matched. If `false`, contacts will only ever enter this workflow once. Matches the "Trigger frequency" option in
            the UI.
        workflow_revision_id (str): The current workflow revision token. Pass the latest value as `expectedRevisionId`
            on the next workflow mutation.
    """

    id: str
    type_name: AddToListTriggerWorkflowMutationNodeTypeName
    next_node_ids: list[str]
    mailing_list_id: None | str
    re_eligible: bool
    workflow_revision_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        mailing_list_id: None | str
        mailing_list_id = self.mailing_list_id

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
                "mailingListId": mailing_list_id,
                "reEligible": re_eligible,
                "workflowRevisionId": workflow_revision_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_name = AddToListTriggerWorkflowMutationNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        def _parse_mailing_list_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mailing_list_id = _parse_mailing_list_id(d.pop("mailingListId"))

        re_eligible = d.pop("reEligible")

        def _parse_workflow_revision_id(data: object) -> str:
            return cast(str, data)

        workflow_revision_id = _parse_workflow_revision_id(d.pop("workflowRevisionId"))

        add_to_list_trigger_workflow_mutation_node_with_revision = cls(
            id=id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            mailing_list_id=mailing_list_id,
            re_eligible=re_eligible,
            workflow_revision_id=workflow_revision_id,
        )

        add_to_list_trigger_workflow_mutation_node_with_revision.additional_properties = d
        return add_to_list_trigger_workflow_mutation_node_with_revision

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
