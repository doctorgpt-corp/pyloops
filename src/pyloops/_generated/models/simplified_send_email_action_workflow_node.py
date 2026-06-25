from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_send_email_action_workflow_node_type_name import SimplifiedSendEmailActionWorkflowNodeTypeName
from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplifiedSendEmailActionWorkflowNode")


@_attrs_define
class SimplifiedSendEmailActionWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedSendEmailActionWorkflowNodeTypeName):
        next_node_ids (list[str]):
        email_message_id (str | Unset):
        subject (str | Unset):
    """

    type_name: SimplifiedSendEmailActionWorkflowNodeTypeName
    next_node_ids: list[str]
    email_message_id: str | Unset = UNSET
    subject: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        email_message_id = self.email_message_id

        subject = self.subject

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
            }
        )
        if email_message_id is not UNSET:
            field_dict["emailMessageId"] = email_message_id
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = SimplifiedSendEmailActionWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        email_message_id = d.pop("emailMessageId", UNSET)

        subject = d.pop("subject", UNSET)

        simplified_send_email_action_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
            email_message_id=email_message_id,
            subject=subject,
        )

        return simplified_send_email_action_workflow_node
