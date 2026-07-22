from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_queued_contact_delete_preview_status import WorkflowQueuedContactDeletePreviewStatus

T = TypeVar("T", bound="WorkflowQueuedContactDeletePreview")


@_attrs_define
class WorkflowQueuedContactDeletePreview:
    """
    Attributes:
        status (WorkflowQueuedContactDeletePreviewStatus):
        node_ids (list[str]): The IDs of the nodes that would be deleted.
        queued_contact_count (float): The number of queued contacts that would be removed from the workflow due to the
            node deletion.
        queued_contact_limit_reached (bool): Whether the queued contact limit would be reached if the nodes were
            deleted.
    """

    status: WorkflowQueuedContactDeletePreviewStatus
    node_ids: list[str]
    queued_contact_count: float
    queued_contact_limit_reached: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        node_ids = self.node_ids

        queued_contact_count = self.queued_contact_count

        queued_contact_limit_reached = self.queued_contact_limit_reached

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "nodeIds": node_ids,
                "queuedContactCount": queued_contact_count,
                "queuedContactLimitReached": queued_contact_limit_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = WorkflowQueuedContactDeletePreviewStatus(d.pop("status"))

        node_ids = cast(list[str], d.pop("nodeIds"))

        queued_contact_count = d.pop("queuedContactCount")

        queued_contact_limit_reached = d.pop("queuedContactLimitReached")

        workflow_queued_contact_delete_preview = cls(
            status=status,
            node_ids=node_ids,
            queued_contact_count=queued_contact_count,
            queued_contact_limit_reached=queued_contact_limit_reached,
        )

        workflow_queued_contact_delete_preview.additional_properties = d
        return workflow_queued_contact_delete_preview

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
