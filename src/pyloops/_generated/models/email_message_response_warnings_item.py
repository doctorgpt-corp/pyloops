from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.email_message_response_warnings_item_severity import EmailMessageResponseWarningsItemSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailMessageResponseWarningsItem")


@_attrs_define
class EmailMessageResponseWarningsItem:
    """
    Attributes:
        rule (str):
        severity (EmailMessageResponseWarningsItemSeverity):
        message (str):
        path (str | Unset):
    """

    rule: str
    severity: EmailMessageResponseWarningsItemSeverity
    message: str
    path: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule = self.rule

        severity = self.severity.value

        message = self.message

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule": rule,
                "severity": severity,
                "message": message,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule = d.pop("rule")

        severity = EmailMessageResponseWarningsItemSeverity(d.pop("severity"))

        message = d.pop("message")

        path = d.pop("path", UNSET)

        email_message_response_warnings_item = cls(
            rule=rule,
            severity=severity,
            message=message,
            path=path,
        )

        email_message_response_warnings_item.additional_properties = d
        return email_message_response_warnings_item

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
