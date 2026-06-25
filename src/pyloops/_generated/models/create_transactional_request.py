from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTransactionalRequest")


@_attrs_define
class CreateTransactionalRequest:
    """
    Attributes:
        name (str): The name of the transactional email.
        transactional_group_id (str | Unset): The ID of the group to add this transactional email to. Defaults to the
            team's default group when omitted.
    """

    name: str
    transactional_group_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        transactional_group_id = self.transactional_group_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if transactional_group_id is not UNSET:
            field_dict["transactionalGroupId"] = transactional_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        transactional_group_id = d.pop("transactionalGroupId", UNSET)

        create_transactional_request = cls(
            name=name,
            transactional_group_id=transactional_group_id,
        )

        return create_transactional_request
