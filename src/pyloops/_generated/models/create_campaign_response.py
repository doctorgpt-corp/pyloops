from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateCampaignResponse")


@_attrs_define
class CreateCampaignResponse:
    """
    Attributes:
        id (str):
        name (str):
        status (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        email_message_id (str): The ID of the empty email message created for this campaign. Use `/email-
            messages/{emailMessageId}` to set its fields and LMX content.
        email_message_content_revision_id (None | str): The `contentRevisionId` of the newly created email message. Pass
            this as `expectedRevisionId` on your first update.
    """

    id: str
    name: str
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    email_message_id: str
    email_message_content_revision_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        email_message_id = self.email_message_id

        email_message_content_revision_id: None | str
        email_message_content_revision_id = self.email_message_content_revision_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "emailMessageId": email_message_id,
                "emailMessageContentRevisionId": email_message_content_revision_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        email_message_id = d.pop("emailMessageId")

        def _parse_email_message_content_revision_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email_message_content_revision_id = _parse_email_message_content_revision_id(
            d.pop("emailMessageContentRevisionId")
        )

        create_campaign_response = cls(
            id=id,
            name=name,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            email_message_id=email_message_id,
            email_message_content_revision_id=email_message_content_revision_id,
        )

        create_campaign_response.additional_properties = d
        return create_campaign_response

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
