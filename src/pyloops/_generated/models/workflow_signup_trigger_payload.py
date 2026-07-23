from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.workflow_signup_trigger_payload_type_name import WorkflowSignupTriggerPayloadTypeName

T = TypeVar("T", bound="WorkflowSignupTriggerPayload")


@_attrs_define
class WorkflowSignupTriggerPayload:
    """Changes an existing trigger node to a signup trigger.

    Attributes:
        type_name (WorkflowSignupTriggerPayloadTypeName):
    """

    type_name: WorkflowSignupTriggerPayloadTypeName

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = WorkflowSignupTriggerPayloadTypeName(d.pop("typeName"))

        workflow_signup_trigger_payload = cls(
            type_name=type_name,
        )

        return workflow_signup_trigger_payload
