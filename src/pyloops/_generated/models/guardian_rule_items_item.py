from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GuardianRuleItemsItem")


@_attrs_define
class GuardianRuleItemsItem:
    """
    Attributes:
        label (str): A human-readable label for the item  (for example, link text or a property name).
        code_name (str | Unset): Machine-readable identifier when the rule refers to a property or variable, when
            applicable. Example: firstName.
    """

    label: str
    code_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        code_name = self.code_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if code_name is not UNSET:
            field_dict["codeName"] = code_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        code_name = d.pop("codeName", UNSET)

        guardian_rule_items_item = cls(
            label=label,
            code_name=code_name,
        )

        guardian_rule_items_item.additional_properties = d
        return guardian_rule_items_item

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
