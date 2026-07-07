from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateComponentResponse")


@_attrs_define
class UpdateComponentResponse:
    """
    Attributes:
        id (str):
        name (str):
        lmx (str): The component body serialized as LMX.
        affected_email_count (float): The number of emails using this component that were updated by the body change.
            `0` when only the name changed.
    """

    id: str
    name: str
    lmx: str
    affected_email_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        lmx = self.lmx

        affected_email_count = self.affected_email_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "lmx": lmx,
                "affectedEmailCount": affected_email_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        lmx = d.pop("lmx")

        affected_email_count = d.pop("affectedEmailCount")

        update_component_response = cls(
            id=id,
            name=name,
            lmx=lmx,
            affected_email_count=affected_email_count,
        )

        update_component_response.additional_properties = d
        return update_component_response

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
