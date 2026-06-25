from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTransactionalRequest")


@_attrs_define
class UpdateTransactionalRequest:
    """At least one field must be provided.

    Attributes:
        name (str | Unset):
        transactional_group_id (str | Unset): The ID of the group to move this transactional email to.
    """

    name: str | Unset = UNSET
    transactional_group_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        transactional_group_id = self.transactional_group_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if transactional_group_id is not UNSET:
            field_dict["transactionalGroupId"] = transactional_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        transactional_group_id = d.pop("transactionalGroupId", UNSET)

        update_transactional_request = cls(
            name=name,
            transactional_group_id=transactional_group_id,
        )

        return update_transactional_request
