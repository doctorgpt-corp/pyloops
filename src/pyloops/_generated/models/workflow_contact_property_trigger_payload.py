from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.workflow_contact_property_trigger_payload_type_name import WorkflowContactPropertyTriggerPayloadTypeName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery


T = TypeVar("T", bound="WorkflowContactPropertyTriggerPayload")


@_attrs_define
class WorkflowContactPropertyTriggerPayload:
    """Updates a contact-property trigger, or changes an existing trigger node to a contact-property trigger.

    Attributes:
        type_name (WorkflowContactPropertyTriggerPayloadTypeName | Unset):
        contact_property_query (WorkflowContactPropertyQuery | Unset): Define the contact property change that triggers
            the workflow. In update requests, `key` must resolve to an existing contact property that is available for
            Contact Updated triggers. Hidden or unsupported fields, such as `createdAt`, `notes`, and computed contact
            properties, are rejected.
        re_eligible (bool | Unset): If `true`, the contacts will be able to enter this workflow every time the trigger
            is matched. If `false`, contacts will only ever enter this workflow once. Matches the "Trigger frequency" option
            in the UI.
    """

    type_name: WorkflowContactPropertyTriggerPayloadTypeName | Unset = UNSET
    contact_property_query: WorkflowContactPropertyQuery | Unset = UNSET
    re_eligible: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_name: str | Unset = UNSET
        if not isinstance(self.type_name, Unset):
            type_name = self.type_name.value

        contact_property_query: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_property_query, Unset):
            contact_property_query = self.contact_property_query.to_dict()

        re_eligible = self.re_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_name is not UNSET:
            field_dict["typeName"] = type_name
        if contact_property_query is not UNSET:
            field_dict["contactPropertyQuery"] = contact_property_query
        if re_eligible is not UNSET:
            field_dict["reEligible"] = re_eligible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_contact_property_query import WorkflowContactPropertyQuery  # noqa: PLC0415

        d = dict(src_dict)
        _type_name = d.pop("typeName", UNSET)
        type_name: WorkflowContactPropertyTriggerPayloadTypeName | Unset
        if isinstance(_type_name, Unset):
            type_name = UNSET
        else:
            type_name = WorkflowContactPropertyTriggerPayloadTypeName(_type_name)

        _contact_property_query = d.pop("contactPropertyQuery", UNSET)
        contact_property_query: WorkflowContactPropertyQuery | Unset
        if isinstance(_contact_property_query, Unset):
            contact_property_query = UNSET
        else:
            contact_property_query = WorkflowContactPropertyQuery.from_dict(_contact_property_query)

        re_eligible = d.pop("reEligible", UNSET)

        workflow_contact_property_trigger_payload = cls(
            type_name=type_name,
            contact_property_query=contact_property_query,
            re_eligible=re_eligible,
        )

        return workflow_contact_property_trigger_payload
