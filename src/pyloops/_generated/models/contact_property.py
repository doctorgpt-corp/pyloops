from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_property_type import ContactPropertyType

T = TypeVar("T", bound="ContactProperty")


@_attrs_define
class ContactProperty:
    """
    Attributes:
        key (str): The key of the contact property.
        label (str): The human-friendly label for this property.
        type_ (ContactPropertyType): The type of property.
    """

    key: str
    label: str
    type_: ContactPropertyType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "label": label,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        type_ = ContactPropertyType(d.pop("type"))

        contact_property = cls(
            key=key,
            label=label,
            type_=type_,
        )

        contact_property.additional_properties = d
        return contact_property

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
