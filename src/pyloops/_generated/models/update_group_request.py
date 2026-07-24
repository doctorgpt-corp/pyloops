from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateGroupRequest")


@_attrs_define
class UpdateGroupRequest:
    """At least one field must be provided.

    Attributes:
        name (str | Unset): The group name. Cannot be the reserved name "Unsorted".
        description (str | Unset): A description for the group.
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        update_group_request = cls(
            name=name,
            description=description,
        )

        return update_group_request
