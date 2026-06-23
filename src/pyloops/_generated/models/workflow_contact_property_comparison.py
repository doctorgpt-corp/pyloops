from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_contact_property_comparison_operator import WorkflowContactPropertyComparisonOperator

T = TypeVar("T", bound="WorkflowContactPropertyComparison")


@_attrs_define
class WorkflowContactPropertyComparison:
    """
    Attributes:
        value (bool | float | str):
        operator (WorkflowContactPropertyComparisonOperator):
    """

    value: bool | float | str
    operator: WorkflowContactPropertyComparisonOperator
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: bool | float | str
        value = self.value

        operator = self.operator.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "operator": operator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_value(data: object) -> bool | float | str:
            return cast(bool | float | str, data)

        value = _parse_value(d.pop("value"))

        operator = WorkflowContactPropertyComparisonOperator(d.pop("operator"))

        workflow_contact_property_comparison = cls(
            value=value,
            operator=operator,
        )

        workflow_contact_property_comparison.additional_properties = d
        return workflow_contact_property_comparison

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
