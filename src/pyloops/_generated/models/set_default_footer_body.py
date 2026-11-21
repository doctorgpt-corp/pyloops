from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_default_footer_body_existing_emails import SetDefaultFooterBodyExistingEmails

T = TypeVar("T", bound="SetDefaultFooterBody")


@_attrs_define
class SetDefaultFooterBody:
    """
    Attributes:
        existing_emails (SetDefaultFooterBodyExistingEmails): Which existing campaign and workflow emails switch to this
            footer: the ones that use the previous default footer (`previousDefault`), all of them (`all`), or none
            (`none`). With `none`, existing emails keep their footer and only new emails use this footer.
    """

    existing_emails: SetDefaultFooterBodyExistingEmails
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        existing_emails = self.existing_emails.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "existingEmails": existing_emails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        existing_emails = SetDefaultFooterBodyExistingEmails(d.pop("existingEmails"))

        set_default_footer_body = cls(
            existing_emails=existing_emails,
        )

        set_default_footer_body.additional_properties = d
        return set_default_footer_body

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
