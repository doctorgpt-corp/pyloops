from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.send_email_action_workflow_node_type_name import SendEmailActionWorkflowNodeTypeName
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendEmailActionWorkflowNode")


@_attrs_define
class SendEmailActionWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (SendEmailActionWorkflowNodeTypeName):
        next_node_ids (list[str]):
        subject (str | Unset):
    """

    id: str
    workflow_id: str
    type_name: SendEmailActionWorkflowNodeTypeName
    next_node_ids: list[str]
    subject: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        subject = self.subject

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
            }
        )
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        type_name = SendEmailActionWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        subject = d.pop("subject", UNSET)

        send_email_action_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            subject=subject,
        )

        return send_email_action_workflow_node
