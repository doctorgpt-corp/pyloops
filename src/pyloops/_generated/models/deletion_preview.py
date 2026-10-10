from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deletion_preview_status import DeletionPreviewStatus

T = TypeVar("T", bound="DeletionPreview")


@_attrs_define
class DeletionPreview:
    """
    Attributes:
        status (DeletionPreviewStatus):
        node_ids (list[str]): The IDs of the nodes that would be deleted.
        queued_contact_count (float): The number of queued contacts that would be removed from the workflow due to the
            node deletion.
    """

    status: DeletionPreviewStatus
    node_ids: list[str]
    queued_contact_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        node_ids = self.node_ids

        queued_contact_count = self.queued_contact_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "nodeIds": node_ids,
                "queuedContactCount": queued_contact_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = DeletionPreviewStatus(d.pop("status"))

        node_ids = cast(list[str], d.pop("nodeIds"))

        queued_contact_count = d.pop("queuedContactCount")

        deletion_preview = cls(
            status=status,
            node_ids=node_ids,
            queued_contact_count=queued_contact_count,
        )

        deletion_preview.additional_properties = d
        return deletion_preview

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
