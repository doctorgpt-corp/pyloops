from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FooterDeleteFailureResponse")


@_attrs_define
class FooterDeleteFailureResponse:
    """
    Attributes:
        message (str):
        email_count (float | Unset): How many emails use the footer. Only when emails use the footer.
    """

    message: str
    email_count: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        email_count = self.email_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if email_count is not UNSET:
            field_dict["emailCount"] = email_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        email_count = d.pop("emailCount", UNSET)

        footer_delete_failure_response = cls(
            message=message,
            email_count=email_count,
        )

        footer_delete_failure_response.additional_properties = d
        return footer_delete_failure_response

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
