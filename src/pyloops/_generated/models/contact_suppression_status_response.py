from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.contact_suppression_removal_quota import ContactSuppressionRemovalQuota
    from ..models.contact_suppression_status_response_contact import ContactSuppressionStatusResponseContact


T = TypeVar("T", bound="ContactSuppressionStatusResponse")


@_attrs_define
class ContactSuppressionStatusResponse:
    """
    Attributes:
        contact (ContactSuppressionStatusResponseContact):
        is_suppressed (bool):
        removal_quota (ContactSuppressionRemovalQuota):
    """

    contact: ContactSuppressionStatusResponseContact
    is_suppressed: bool
    removal_quota: ContactSuppressionRemovalQuota
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact = self.contact.to_dict()

        is_suppressed = self.is_suppressed

        removal_quota = self.removal_quota.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contact": contact,
                "isSuppressed": is_suppressed,
                "removalQuota": removal_quota,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_suppression_removal_quota import ContactSuppressionRemovalQuota
        from ..models.contact_suppression_status_response_contact import ContactSuppressionStatusResponseContact

        d = dict(src_dict)
        contact = ContactSuppressionStatusResponseContact.from_dict(d.pop("contact"))

        is_suppressed = d.pop("isSuppressed")

        removal_quota = ContactSuppressionRemovalQuota.from_dict(d.pop("removalQuota"))

        contact_suppression_status_response = cls(
            contact=contact,
            is_suppressed=is_suppressed,
            removal_quota=removal_quota,
        )

        contact_suppression_status_response.additional_properties = d
        return contact_suppression_status_response

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
