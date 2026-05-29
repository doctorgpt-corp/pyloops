from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_message_response_warnings_item import EmailMessageResponseWarningsItem


T = TypeVar("T", bound="EmailMessageResponse")


@_attrs_define
class EmailMessageResponse:
    """
    Attributes:
        success (bool):
        email_message_id (str):
        campaign_id (None | str):
        subject (str):
        preview_text (str):
        from_name (str):
        from_email (str):
        reply_to_email (str):
        lmx (str): The email body serialized as LMX.
        content_revision_id (None | str): The current content revision. Pass this as `expectedRevisionId` on your next
            update.
        updated_at (datetime.datetime):
        warnings (list[EmailMessageResponseWarningsItem] | Unset): Non-fatal issues raised while compiling the submitted
            LMX. Only present on update responses when warnings were produced.
    """

    success: bool
    email_message_id: str
    campaign_id: None | str
    subject: str
    preview_text: str
    from_name: str
    from_email: str
    reply_to_email: str
    lmx: str
    content_revision_id: None | str
    updated_at: datetime.datetime
    warnings: list[EmailMessageResponseWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        email_message_id = self.email_message_id

        campaign_id: None | str
        campaign_id = self.campaign_id

        subject = self.subject

        preview_text = self.preview_text

        from_name = self.from_name

        from_email = self.from_email

        reply_to_email = self.reply_to_email

        lmx = self.lmx

        content_revision_id: None | str
        content_revision_id = self.content_revision_id

        updated_at = self.updated_at.isoformat()

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "emailMessageId": email_message_id,
                "campaignId": campaign_id,
                "subject": subject,
                "previewText": preview_text,
                "fromName": from_name,
                "fromEmail": from_email,
                "replyToEmail": reply_to_email,
                "lmx": lmx,
                "contentRevisionId": content_revision_id,
                "updatedAt": updated_at,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_message_response_warnings_item import EmailMessageResponseWarningsItem

        d = dict(src_dict)
        success = d.pop("success")

        email_message_id = d.pop("emailMessageId")

        def _parse_campaign_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        campaign_id = _parse_campaign_id(d.pop("campaignId"))

        subject = d.pop("subject")

        preview_text = d.pop("previewText")

        from_name = d.pop("fromName")

        from_email = d.pop("fromEmail")

        reply_to_email = d.pop("replyToEmail")

        lmx = d.pop("lmx")

        def _parse_content_revision_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_revision_id = _parse_content_revision_id(d.pop("contentRevisionId"))

        updated_at = isoparse(d.pop("updatedAt"))

        _warnings = d.pop("warnings", UNSET)
        warnings: list[EmailMessageResponseWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = EmailMessageResponseWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        email_message_response = cls(
            success=success,
            email_message_id=email_message_id,
            campaign_id=campaign_id,
            subject=subject,
            preview_text=preview_text,
            from_name=from_name,
            from_email=from_email,
            reply_to_email=reply_to_email,
            lmx=lmx,
            content_revision_id=content_revision_id,
            updated_at=updated_at,
            warnings=warnings,
        )

        email_message_response.additional_properties = d
        return email_message_response

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
