from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.email_message_response_email_format import EmailMessageResponseEmailFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_message_response_contact_properties_fallbacks import (
        EmailMessageResponseContactPropertiesFallbacks,
    )
    from ..models.email_message_response_data_variables_fallbacks import EmailMessageResponseDataVariablesFallbacks
    from ..models.email_message_response_event_properties_fallbacks import EmailMessageResponseEventPropertiesFallbacks
    from ..models.email_message_response_warnings_item import EmailMessageResponseWarningsItem


T = TypeVar("T", bound="EmailMessageResponse")


@_attrs_define
class EmailMessageResponse:
    """
    Attributes:
        id (str):
        subject (str):
        preview_text (str):
        from_name (str):
        from_email (str):
        reply_to_email (str):
        email_format (EmailMessageResponseEmailFormat): The rendering format of the email.
        lmx (str): The email body serialized as LMX.
        content_revision_id (None | str): The current content revision. Pass this as `expectedRevisionId` on your next
            update.
        updated_at (datetime.datetime):
        campaign_id (str | Unset): The campaign this email message belongs to. Present only when the message belongs to
            a campaign (mutually exclusive with `transactionalId`).
        transactional_id (str | Unset): The transactional email this email message belongs to. Present only when the
            message belongs to a transactional email (mutually exclusive with `campaignId`).
        cc_email (str | Unset): Only present when set.
        bcc_email (str | Unset): Only present when set.
        language_code (str | Unset): Only present when set.
        contact_properties_fallbacks (EmailMessageResponseContactPropertiesFallbacks | Unset): Fallback values for
            contact properties. Only present when set.
        event_properties_fallbacks (EmailMessageResponseEventPropertiesFallbacks | Unset): Fallback values for event
            properties. Only present when set.
        data_variables_fallbacks (EmailMessageResponseDataVariablesFallbacks | Unset): Fallback values for data
            variables. Only present when set.
        warnings (list[EmailMessageResponseWarningsItem] | Unset): Non-fatal issues raised while compiling the submitted
            LMX. Only present on update responses when warnings were produced.
    """

    id: str
    subject: str
    preview_text: str
    from_name: str
    from_email: str
    reply_to_email: str
    email_format: EmailMessageResponseEmailFormat
    lmx: str
    content_revision_id: None | str
    updated_at: datetime.datetime
    campaign_id: str | Unset = UNSET
    transactional_id: str | Unset = UNSET
    cc_email: str | Unset = UNSET
    bcc_email: str | Unset = UNSET
    language_code: str | Unset = UNSET
    contact_properties_fallbacks: EmailMessageResponseContactPropertiesFallbacks | Unset = UNSET
    event_properties_fallbacks: EmailMessageResponseEventPropertiesFallbacks | Unset = UNSET
    data_variables_fallbacks: EmailMessageResponseDataVariablesFallbacks | Unset = UNSET
    warnings: list[EmailMessageResponseWarningsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subject = self.subject

        preview_text = self.preview_text

        from_name = self.from_name

        from_email = self.from_email

        reply_to_email = self.reply_to_email

        email_format = self.email_format.value

        lmx = self.lmx

        content_revision_id: None | str
        content_revision_id = self.content_revision_id

        updated_at = self.updated_at.isoformat()

        campaign_id = self.campaign_id

        transactional_id = self.transactional_id

        cc_email = self.cc_email

        bcc_email = self.bcc_email

        language_code = self.language_code

        contact_properties_fallbacks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_properties_fallbacks, Unset):
            contact_properties_fallbacks = self.contact_properties_fallbacks.to_dict()

        event_properties_fallbacks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_properties_fallbacks, Unset):
            event_properties_fallbacks = self.event_properties_fallbacks.to_dict()

        data_variables_fallbacks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_variables_fallbacks, Unset):
            data_variables_fallbacks = self.data_variables_fallbacks.to_dict()

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
                "id": id,
                "subject": subject,
                "previewText": preview_text,
                "fromName": from_name,
                "fromEmail": from_email,
                "replyToEmail": reply_to_email,
                "emailFormat": email_format,
                "lmx": lmx,
                "contentRevisionId": content_revision_id,
                "updatedAt": updated_at,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if transactional_id is not UNSET:
            field_dict["transactionalId"] = transactional_id
        if cc_email is not UNSET:
            field_dict["ccEmail"] = cc_email
        if bcc_email is not UNSET:
            field_dict["bccEmail"] = bcc_email
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if contact_properties_fallbacks is not UNSET:
            field_dict["contactPropertiesFallbacks"] = contact_properties_fallbacks
        if event_properties_fallbacks is not UNSET:
            field_dict["eventPropertiesFallbacks"] = event_properties_fallbacks
        if data_variables_fallbacks is not UNSET:
            field_dict["dataVariablesFallbacks"] = data_variables_fallbacks
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_message_response_contact_properties_fallbacks import (
            EmailMessageResponseContactPropertiesFallbacks,
        )
        from ..models.email_message_response_data_variables_fallbacks import EmailMessageResponseDataVariablesFallbacks
        from ..models.email_message_response_event_properties_fallbacks import (
            EmailMessageResponseEventPropertiesFallbacks,
        )
        from ..models.email_message_response_warnings_item import EmailMessageResponseWarningsItem

        d = dict(src_dict)
        id = d.pop("id")

        subject = d.pop("subject")

        preview_text = d.pop("previewText")

        from_name = d.pop("fromName")

        from_email = d.pop("fromEmail")

        reply_to_email = d.pop("replyToEmail")

        email_format = EmailMessageResponseEmailFormat(d.pop("emailFormat"))

        lmx = d.pop("lmx")

        def _parse_content_revision_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        content_revision_id = _parse_content_revision_id(d.pop("contentRevisionId"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        campaign_id = d.pop("campaignId", UNSET)

        transactional_id = d.pop("transactionalId", UNSET)

        cc_email = d.pop("ccEmail", UNSET)

        bcc_email = d.pop("bccEmail", UNSET)

        language_code = d.pop("languageCode", UNSET)

        _contact_properties_fallbacks = d.pop("contactPropertiesFallbacks", UNSET)
        contact_properties_fallbacks: EmailMessageResponseContactPropertiesFallbacks | Unset
        if isinstance(_contact_properties_fallbacks, Unset):
            contact_properties_fallbacks = UNSET
        else:
            contact_properties_fallbacks = EmailMessageResponseContactPropertiesFallbacks.from_dict(
                _contact_properties_fallbacks
            )

        _event_properties_fallbacks = d.pop("eventPropertiesFallbacks", UNSET)
        event_properties_fallbacks: EmailMessageResponseEventPropertiesFallbacks | Unset
        if isinstance(_event_properties_fallbacks, Unset):
            event_properties_fallbacks = UNSET
        else:
            event_properties_fallbacks = EmailMessageResponseEventPropertiesFallbacks.from_dict(
                _event_properties_fallbacks
            )

        _data_variables_fallbacks = d.pop("dataVariablesFallbacks", UNSET)
        data_variables_fallbacks: EmailMessageResponseDataVariablesFallbacks | Unset
        if isinstance(_data_variables_fallbacks, Unset):
            data_variables_fallbacks = UNSET
        else:
            data_variables_fallbacks = EmailMessageResponseDataVariablesFallbacks.from_dict(_data_variables_fallbacks)

        _warnings = d.pop("warnings", UNSET)
        warnings: list[EmailMessageResponseWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = EmailMessageResponseWarningsItem.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        email_message_response = cls(
            id=id,
            subject=subject,
            preview_text=preview_text,
            from_name=from_name,
            from_email=from_email,
            reply_to_email=reply_to_email,
            email_format=email_format,
            lmx=lmx,
            content_revision_id=content_revision_id,
            updated_at=updated_at,
            campaign_id=campaign_id,
            transactional_id=transactional_id,
            cc_email=cc_email,
            bcc_email=bcc_email,
            language_code=language_code,
            contact_properties_fallbacks=contact_properties_fallbacks,
            event_properties_fallbacks=event_properties_fallbacks,
            data_variables_fallbacks=data_variables_fallbacks,
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
