from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TransactionalDraftResponse")


@_attrs_define
class TransactionalDraftResponse:
    """
    Attributes:
        success (bool):
        transactional_id (str):
        name (str):
        draft_email_message_id (None | str):
        draft_email_message_content_revision_id (None | str): The `contentRevisionId` of the draft email message. Pass
            this as `expectedRevisionId` on your first update via `/email-messages/{emailMessageId}`.
        published_email_message_id (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    success: bool
    transactional_id: str
    name: str
    draft_email_message_id: None | str
    draft_email_message_content_revision_id: None | str
    published_email_message_id: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        transactional_id = self.transactional_id

        name = self.name

        draft_email_message_id: None | str
        draft_email_message_id = self.draft_email_message_id

        draft_email_message_content_revision_id: None | str
        draft_email_message_content_revision_id = self.draft_email_message_content_revision_id

        published_email_message_id: None | str
        published_email_message_id = self.published_email_message_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "transactionalId": transactional_id,
                "name": name,
                "draftEmailMessageId": draft_email_message_id,
                "draftEmailMessageContentRevisionId": draft_email_message_content_revision_id,
                "publishedEmailMessageId": published_email_message_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        transactional_id = d.pop("transactionalId")

        name = d.pop("name")

        def _parse_draft_email_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        draft_email_message_id = _parse_draft_email_message_id(d.pop("draftEmailMessageId"))

        def _parse_draft_email_message_content_revision_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        draft_email_message_content_revision_id = _parse_draft_email_message_content_revision_id(
            d.pop("draftEmailMessageContentRevisionId")
        )

        def _parse_published_email_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_email_message_id = _parse_published_email_message_id(d.pop("publishedEmailMessageId"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        transactional_draft_response = cls(
            success=success,
            transactional_id=transactional_id,
            name=name,
            draft_email_message_id=draft_email_message_id,
            draft_email_message_content_revision_id=draft_email_message_content_revision_id,
            published_email_message_id=published_email_message_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        transactional_draft_response.additional_properties = d
        return transactional_draft_response

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
