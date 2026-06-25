from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.simplified_add_to_list_trigger_workflow_node_type_name import (
    SimplifiedAddToListTriggerWorkflowNodeTypeName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplifiedAddToListTriggerWorkflowNode")


@_attrs_define
class SimplifiedAddToListTriggerWorkflowNode:
    """
    Attributes:
        type_name (SimplifiedAddToListTriggerWorkflowNodeTypeName):
        next_node_ids (list[str]):
        mailing_list_id (str | Unset):
        re_eligible (bool | Unset):
    """

    type_name: SimplifiedAddToListTriggerWorkflowNodeTypeName
    next_node_ids: list[str]
    mailing_list_id: str | Unset = UNSET
    re_eligible: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        mailing_list_id = self.mailing_list_id

        re_eligible = self.re_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
            }
        )
        if mailing_list_id is not UNSET:
            field_dict["mailingListId"] = mailing_list_id
        if re_eligible is not UNSET:
            field_dict["reEligible"] = re_eligible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_name = SimplifiedAddToListTriggerWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        mailing_list_id = d.pop("mailingListId", UNSET)

        re_eligible = d.pop("reEligible", UNSET)

        simplified_add_to_list_trigger_workflow_node = cls(
            type_name=type_name,
            next_node_ids=next_node_ids,
            mailing_list_id=mailing_list_id,
            re_eligible=re_eligible,
        )

        return simplified_add_to_list_trigger_workflow_node
