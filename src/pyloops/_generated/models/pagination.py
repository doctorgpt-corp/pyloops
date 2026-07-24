from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        total_results (float):
        returned_results (float):
        per_page (float):
        total_pages (float):
        next_cursor (None | str):
        next_page (None | str):
    """

    total_results: float
    returned_results: float
    per_page: float
    total_pages: float
    next_cursor: None | str
    next_page: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_results = self.total_results

        returned_results = self.returned_results

        per_page = self.per_page

        total_pages = self.total_pages

        next_cursor: None | str
        next_cursor = self.next_cursor

        next_page: None | str
        next_page = self.next_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalResults": total_results,
                "returnedResults": returned_results,
                "perPage": per_page,
                "totalPages": total_pages,
                "nextCursor": next_cursor,
                "nextPage": next_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_results = d.pop("totalResults")

        returned_results = d.pop("returnedResults")

        per_page = d.pop("perPage")

        total_pages = d.pop("totalPages")

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor"))

        def _parse_next_page(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_page = _parse_next_page(d.pop("nextPage"))

        pagination = cls(
            total_results=total_results,
            returned_results=returned_results,
            per_page=per_page,
            total_pages=total_pages,
            next_cursor=next_cursor,
            next_page=next_page,
        )

        pagination.additional_properties = d
        return pagination

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
