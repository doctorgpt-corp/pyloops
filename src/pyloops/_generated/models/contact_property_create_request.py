from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_property_create_request_type import ContactPropertyCreateRequestType

T = TypeVar("T", bound="ContactPropertyCreateRequest")


@_attrs_define
class ContactPropertyCreateRequest:
    """There are a few [reserved names](https://loops.so/docs/contacts/properties#reserved-names) that you cannot use for
    contact properties.

        Attributes:
            name (str): The name of the property. This should be in camelCase, like `planName` or `importDate`.
            type_ (ContactPropertyCreateRequestType): The type of property.
    """

    name: str
    type_: ContactPropertyCreateRequestType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = ContactPropertyCreateRequestType(d.pop("type"))

        contact_property_create_request = cls(
            name=name,
            type_=type_,
        )

        contact_property_create_request.additional_properties = d
        return contact_property_create_request

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
