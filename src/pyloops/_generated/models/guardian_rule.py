from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.guardian_rule_rule import GuardianRuleRule

if TYPE_CHECKING:
    from ..models.guardian_rule_items_item import GuardianRuleItemsItem


T = TypeVar("T", bound="GuardianRule")


@_attrs_define
class GuardianRule:
    """
    Attributes:
        rule (GuardianRuleRule): The identifier of the Guardian rule that fired.
        title (str): A short summary of the rule.
        description (str): A longer explanation of why the issue matters.
        items (list[GuardianRuleItemsItem]): The specific elements that triggered the rule.
    """

    rule: GuardianRuleRule
    title: str
    description: str
    items: list[GuardianRuleItemsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule = self.rule.value

        title = self.title

        description = self.description

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
                "title": title,
                "description": description,
                "items": items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guardian_rule_items_item import GuardianRuleItemsItem

        d = dict(src_dict)
        rule = GuardianRuleRule(d.pop("rule"))

        title = d.pop("title")

        description = d.pop("description")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = GuardianRuleItemsItem.from_dict(items_item_data)

            items.append(items_item)

        guardian_rule = cls(
            rule=rule,
            title=title,
            description=description,
            items=items,
        )

        guardian_rule.additional_properties = d
        return guardian_rule

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
