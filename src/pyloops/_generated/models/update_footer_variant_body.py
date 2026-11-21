from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateFooterVariantBody")


@_attrs_define
class UpdateFooterVariantBody:
    """
    Attributes:
        expected_revision_id (str): The `contentRevisionId` you last fetched.
        lmx (str): The new draft content as LMX. Footer LMX can use `{system.company_name}`, `{system.company_address}`,
            `{system.mailing_list_name}`, `{system.unsubscribe_link}` and `{contact.email}`. It cannot use `<Style />`,
            components, other contact properties, event properties or data variables.
    """

    expected_revision_id: str
    lmx: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_revision_id = self.expected_revision_id

        lmx = self.lmx

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expectedRevisionId": expected_revision_id,
                "lmx": lmx,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_revision_id = d.pop("expectedRevisionId")

        lmx = d.pop("lmx")

        update_footer_variant_body = cls(
            expected_revision_id=expected_revision_id,
            lmx=lmx,
        )

        update_footer_variant_body.additional_properties = d
        return update_footer_variant_body

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
