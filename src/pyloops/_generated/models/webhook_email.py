from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WebhookEmail")


@_attrs_define
class WebhookEmail:
    """
    Attributes:
        id (str): The ID of the email.
        email_message_id (str): The ID of the sent version of the campaign, workflow or transactional email.
        subject (str): The subject of the email.
    """

    id: str
    email_message_id: str
    subject: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email_message_id = self.email_message_id

        subject = self.subject

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "emailMessageId": email_message_id,
                "subject": subject,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email_message_id = d.pop("emailMessageId")

        subject = d.pop("subject")

        webhook_email = cls(
            id=id,
            email_message_id=email_message_id,
            subject=subject,
        )

        webhook_email.additional_properties = d
        return webhook_email

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
