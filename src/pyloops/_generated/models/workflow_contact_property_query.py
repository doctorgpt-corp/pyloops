from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_contact_property_comparison import WorkflowContactPropertyComparison


T = TypeVar("T", bound="WorkflowContactPropertyQuery")


@_attrs_define
class WorkflowContactPropertyQuery:
    """
    Attributes:
        key (str):
        is_ (WorkflowContactPropertyComparison):
        was (WorkflowContactPropertyComparison):
    """

    key: str
    is_: WorkflowContactPropertyComparison
    was: WorkflowContactPropertyComparison
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        is_ = self.is_.to_dict()

        was = self.was.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "is": is_,
                "was": was,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_contact_property_comparison import WorkflowContactPropertyComparison

        d = dict(src_dict)
        key = d.pop("key")

        is_ = WorkflowContactPropertyComparison.from_dict(d.pop("is"))

        was = WorkflowContactPropertyComparison.from_dict(d.pop("was"))

        workflow_contact_property_query = cls(
            key=key,
            is_=is_,
            was=was,
        )

        workflow_contact_property_query.additional_properties = d
        return workflow_contact_property_query

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
