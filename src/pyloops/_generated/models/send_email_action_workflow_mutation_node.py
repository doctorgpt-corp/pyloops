from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_email_action_workflow_mutation_node_type_name import SendEmailActionWorkflowMutationNodeTypeName

T = TypeVar("T", bound="SendEmailActionWorkflowMutationNode")


@_attrs_define
class SendEmailActionWorkflowMutationNode:
    """
    Attributes:
        id (str):
        type_name (SendEmailActionWorkflowMutationNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        email_message_id (str): The ID of the email message to send. To edit this email, use the `POST /v1/email-
            messages/{emailMessageId}` endpoint.
        subject (str):
    """

    id: str
    type_name: SendEmailActionWorkflowMutationNodeTypeName
    next_node_ids: list[str]
    email_message_id: str
    subject: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        email_message_id = self.email_message_id

        subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "emailMessageId": email_message_id,
                "subject": subject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_name = SendEmailActionWorkflowMutationNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        email_message_id = d.pop("emailMessageId")

        subject = d.pop("subject")

        send_email_action_workflow_mutation_node = cls(
            id=id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            email_message_id=email_message_id,
            subject=subject,
        )

        send_email_action_workflow_mutation_node.additional_properties = d
        return send_email_action_workflow_mutation_node

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
