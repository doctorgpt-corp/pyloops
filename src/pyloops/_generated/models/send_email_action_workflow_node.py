from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.send_email_action_workflow_node_type_name import SendEmailActionWorkflowNodeTypeName

T = TypeVar("T", bound="SendEmailActionWorkflowNode")


@_attrs_define
class SendEmailActionWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (SendEmailActionWorkflowNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        email_message_id (str): The ID of the email message to send. To edit this email, use the `POST /v1/email-
            messages/{emailMessageId}` endpoint.
        subject (str):
    """

    id: str
    workflow_id: str
    type_name: SendEmailActionWorkflowNodeTypeName
    next_node_ids: list[str]
    email_message_id: str
    subject: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        email_message_id = self.email_message_id

        subject = self.subject

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
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

        workflow_id = d.pop("workflowId")

        type_name = SendEmailActionWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        email_message_id = d.pop("emailMessageId")

        subject = d.pop("subject")

        send_email_action_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            email_message_id=email_message_id,
            subject=subject,
        )

        return send_email_action_workflow_node
