from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CampaignListItem")


@_attrs_define
class CampaignListItem:
    """
    Attributes:
        campaign_id (str):
        email_message_id (None | str):
        name (str):
        subject (str):
        status (str): Campaign lifecycle status.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    campaign_id: str
    email_message_id: None | str
    name: str
    subject: str
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        campaign_id = self.campaign_id

        email_message_id: None | str
        email_message_id = self.email_message_id

        name = self.name

        subject = self.subject

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campaignId": campaign_id,
                "emailMessageId": email_message_id,
                "name": name,
                "subject": subject,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        campaign_id = d.pop("campaignId")

        def _parse_email_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email_message_id = _parse_email_message_id(d.pop("emailMessageId"))

        name = d.pop("name")

        subject = d.pop("subject")

        status = d.pop("status")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        campaign_list_item = cls(
            campaign_id=campaign_id,
            email_message_id=email_message_id,
            name=name,
            subject=subject,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
        )

        campaign_list_item.additional_properties = d
        return campaign_list_item

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
