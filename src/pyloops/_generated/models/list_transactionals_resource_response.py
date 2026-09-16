from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.transactional_resource import TransactionalResource


T = TypeVar("T", bound="ListTransactionalsResourceResponse")


@_attrs_define
class ListTransactionalsResourceResponse:
    """
    Attributes:
        pagination (Pagination):
        data (list[TransactionalResource]):
    """

    pagination: Pagination
    data: list[TransactionalResource]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination = self.pagination.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagination": pagination,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination  # noqa: PLC0415
        from ..models.transactional_resource import TransactionalResource  # noqa: PLC0415

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = TransactionalResource.from_dict(data_item_data)

            data.append(data_item)

        list_transactionals_resource_response = cls(
            pagination=pagination,
            data=data,
        )

        list_transactionals_resource_response.additional_properties = d
        return list_transactionals_resource_response

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
