from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.footer_placement import FooterPlacement

T = TypeVar("T", bound="Footer")


@_attrs_define
class Footer:
    """
    Attributes:
        id (str): The ID of the footer.
        name (str): The name of the footer.
        is_default (bool): Whether this is the team's default footer. New campaign and workflow emails use the default
            footer.
        placement (FooterPlacement): Whether the footer is rendered inside the email body (`inside`) or below it
            (`below`).
        created_at (datetime.datetime): ISO 8601 timestamp for when the footer was created.
        updated_at (datetime.datetime): ISO 8601 timestamp for when the footer's own fields last changed, such as its
            name or placement. Not changed when a variant is updated.
    """

    id: str
    name: str
    is_default: bool
    placement: FooterPlacement
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_default = self.is_default

        placement = self.placement.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "isDefault": is_default,
                "placement": placement,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_default = d.pop("isDefault")

        placement = FooterPlacement(d.pop("placement"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        footer = cls(
            id=id,
            name=name,
            is_default=is_default,
            placement=placement,
            created_at=created_at,
            updated_at=updated_at,
        )

        footer.additional_properties = d
        return footer

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
