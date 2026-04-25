from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ComponentResponse")


@_attrs_define
class ComponentResponse:
    """
    Attributes:
        success (bool):
        component_id (str):
        name (str):
        lmx (str): The component body serialized as LMX.
    """

    success: bool
    component_id: str
    name: str
    lmx: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        component_id = self.component_id

        name = self.name

        lmx = self.lmx

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "componentId": component_id,
                "name": name,
                "lmx": lmx,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        component_id = d.pop("componentId")

        name = d.pop("name")

        lmx = d.pop("lmx")

        component_response = cls(
            success=success,
            component_id=component_id,
            name=name,
            lmx=lmx,
        )

        component_response.additional_properties = d
        return component_response

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
