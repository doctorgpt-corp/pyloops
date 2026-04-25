from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCampaignsResponsePagination")


@_attrs_define
class ListCampaignsResponsePagination:
    """
    Attributes:
        total_results (float | Unset):
        returned_results (float | Unset):
        per_page (float | Unset):
        total_pages (float | Unset):
        next_cursor (None | str | Unset):
        next_page (None | str | Unset):
    """

    total_results: float | Unset = UNSET
    returned_results: float | Unset = UNSET
    per_page: float | Unset = UNSET
    total_pages: float | Unset = UNSET
    next_cursor: None | str | Unset = UNSET
    next_page: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_results = self.total_results

        returned_results = self.returned_results

        per_page = self.per_page

        total_pages = self.total_pages

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        next_page: None | str | Unset
        if isinstance(self.next_page, Unset):
            next_page = UNSET
        else:
            next_page = self.next_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_results is not UNSET:
            field_dict["totalResults"] = total_results
        if returned_results is not UNSET:
            field_dict["returnedResults"] = returned_results
        if per_page is not UNSET:
            field_dict["perPage"] = per_page
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if next_page is not UNSET:
            field_dict["nextPage"] = next_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_results = d.pop("totalResults", UNSET)

        returned_results = d.pop("returnedResults", UNSET)

        per_page = d.pop("perPage", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        def _parse_next_page(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page = _parse_next_page(d.pop("nextPage", UNSET))

        list_campaigns_response_pagination = cls(
            total_results=total_results,
            returned_results=returned_results,
            per_page=per_page,
            total_pages=total_pages,
            next_cursor=next_cursor,
            next_page=next_page,
        )

        list_campaigns_response_pagination.additional_properties = d
        return list_campaigns_response_pagination

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
