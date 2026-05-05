from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Component")


@_attrs_define
class Component:
    """
    Attributes:
        component_id (str):
        name (str):
        lmx (str): The component body serialized as LMX.
    """

    component_id: str
    name: str
    lmx: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_id = self.component_id

        name = self.name

        lmx = self.lmx

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "componentId": component_id,
                "name": name,
                "lmx": lmx,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_id = d.pop("componentId")

        name = d.pop("name")

        lmx = d.pop("lmx")

        component = cls(
            component_id=component_id,
            name=name,
            lmx=lmx,
        )

        component.additional_properties = d
        return component

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
