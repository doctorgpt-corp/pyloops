from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.footer import Footer
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ListFootersResponse")


@_attrs_define
class ListFootersResponse:
    """
    Attributes:
        pagination (Pagination):
        data (list[Footer]):
    """

    pagination: Pagination
    data: list[Footer]
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
        from ..models.footer import Footer  # noqa: PLC0415
        from ..models.pagination import Pagination  # noqa: PLC0415

        d = dict(src_dict)
        pagination = Pagination.from_dict(d.pop("pagination"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Footer.from_dict(data_item_data)

            data.append(data_item)

        list_footers_response = cls(
            pagination=pagination,
            data=data,
        )

        list_footers_response.additional_properties = d
        return list_footers_response

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
