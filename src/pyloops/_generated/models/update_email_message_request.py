from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_email_message_request_email_format import UpdateEmailMessageRequestEmailFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_email_message_request_contact_properties_fallbacks import (
        UpdateEmailMessageRequestContactPropertiesFallbacks,
    )
    from ..models.update_email_message_request_data_variables_fallbacks import (
        UpdateEmailMessageRequestDataVariablesFallbacks,
    )
    from ..models.update_email_message_request_event_properties_fallbacks import (
        UpdateEmailMessageRequestEventPropertiesFallbacks,
    )


T = TypeVar("T", bound="UpdateEmailMessageRequest")


@_attrs_define
class UpdateEmailMessageRequest:
    """
    Attributes:
        expected_revision_id (str | Unset): The `contentRevisionId` you last fetched, or the
            `emailMessageContentRevisionId` you received when creating the campaign.
        subject (str | Unset):
        preview_text (str | Unset):
        from_name (str | Unset):
        from_email (str | Unset): The email sender email address, without the team's sending domain.
        reply_to_email (str | Unset): Reply-to email. Must be empty or a valid email address.
        cc_email (str | Unset): CC email address. Requires the team to have CC/BCC enabled.
        bcc_email (str | Unset): BCC email address. Requires the team to have CC/BCC enabled.
        language_code (str | Unset): Language code for the email. Requires translation to be enabled for the team.
        email_format (UpdateEmailMessageRequestEmailFormat | Unset): The rendering format of the email.
        lmx (str | Unset): The email body serialized as LMX. Styles must be embedded in the LMX `<Style />` tag.
        contact_properties_fallbacks (UpdateEmailMessageRequestContactPropertiesFallbacks | Unset): Fallback values for
            contact properties, keyed by property name. Per-key merge: a string value sets the fallback, a null value
            deletes it, and keys omitted from the map are left unchanged.
        event_properties_fallbacks (UpdateEmailMessageRequestEventPropertiesFallbacks | Unset): Fallback values for
            event properties, keyed by property name. Per-key merge: a string value sets the fallback, a null value deletes
            it, and keys omitted from the map are left unchanged.
        data_variables_fallbacks (UpdateEmailMessageRequestDataVariablesFallbacks | Unset): Fallback values for data
            variables, keyed by variable name. Per-key merge: a string value sets the fallback, a null value deletes it, and
            keys omitted from the map are left unchanged.
    """

    expected_revision_id: str | Unset = UNSET
    subject: str | Unset = UNSET
    preview_text: str | Unset = UNSET
    from_name: str | Unset = UNSET
    from_email: str | Unset = UNSET
    reply_to_email: str | Unset = UNSET
    cc_email: str | Unset = UNSET
    bcc_email: str | Unset = UNSET
    language_code: str | Unset = UNSET
    email_format: UpdateEmailMessageRequestEmailFormat | Unset = UNSET
    lmx: str | Unset = UNSET
    contact_properties_fallbacks: UpdateEmailMessageRequestContactPropertiesFallbacks | Unset = UNSET
    event_properties_fallbacks: UpdateEmailMessageRequestEventPropertiesFallbacks | Unset = UNSET
    data_variables_fallbacks: UpdateEmailMessageRequestDataVariablesFallbacks | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expected_revision_id = self.expected_revision_id

        subject = self.subject

        preview_text = self.preview_text

        from_name = self.from_name

        from_email = self.from_email

        reply_to_email = self.reply_to_email

        cc_email = self.cc_email

        bcc_email = self.bcc_email

        language_code = self.language_code

        email_format: str | Unset = UNSET
        if not isinstance(self.email_format, Unset):
            email_format = self.email_format.value

        lmx = self.lmx

        contact_properties_fallbacks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_properties_fallbacks, Unset):
            contact_properties_fallbacks = self.contact_properties_fallbacks.to_dict()

        event_properties_fallbacks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_properties_fallbacks, Unset):
            event_properties_fallbacks = self.event_properties_fallbacks.to_dict()

        data_variables_fallbacks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_variables_fallbacks, Unset):
            data_variables_fallbacks = self.data_variables_fallbacks.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expected_revision_id is not UNSET:
            field_dict["expectedRevisionId"] = expected_revision_id
        if subject is not UNSET:
            field_dict["subject"] = subject
        if preview_text is not UNSET:
            field_dict["previewText"] = preview_text
        if from_name is not UNSET:
            field_dict["fromName"] = from_name
        if from_email is not UNSET:
            field_dict["fromEmail"] = from_email
        if reply_to_email is not UNSET:
            field_dict["replyToEmail"] = reply_to_email
        if cc_email is not UNSET:
            field_dict["ccEmail"] = cc_email
        if bcc_email is not UNSET:
            field_dict["bccEmail"] = bcc_email
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if email_format is not UNSET:
            field_dict["emailFormat"] = email_format
        if lmx is not UNSET:
            field_dict["lmx"] = lmx
        if contact_properties_fallbacks is not UNSET:
            field_dict["contactPropertiesFallbacks"] = contact_properties_fallbacks
        if event_properties_fallbacks is not UNSET:
            field_dict["eventPropertiesFallbacks"] = event_properties_fallbacks
        if data_variables_fallbacks is not UNSET:
            field_dict["dataVariablesFallbacks"] = data_variables_fallbacks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_email_message_request_contact_properties_fallbacks import (
            UpdateEmailMessageRequestContactPropertiesFallbacks,
        )
        from ..models.update_email_message_request_data_variables_fallbacks import (
            UpdateEmailMessageRequestDataVariablesFallbacks,
        )
        from ..models.update_email_message_request_event_properties_fallbacks import (
            UpdateEmailMessageRequestEventPropertiesFallbacks,
        )

        d = dict(src_dict)
        expected_revision_id = d.pop("expectedRevisionId", UNSET)

        subject = d.pop("subject", UNSET)

        preview_text = d.pop("previewText", UNSET)

        from_name = d.pop("fromName", UNSET)

        from_email = d.pop("fromEmail", UNSET)

        reply_to_email = d.pop("replyToEmail", UNSET)

        cc_email = d.pop("ccEmail", UNSET)

        bcc_email = d.pop("bccEmail", UNSET)

        language_code = d.pop("languageCode", UNSET)

        _email_format = d.pop("emailFormat", UNSET)
        email_format: UpdateEmailMessageRequestEmailFormat | Unset
        if isinstance(_email_format, Unset):
            email_format = UNSET
        else:
            email_format = UpdateEmailMessageRequestEmailFormat(_email_format)

        lmx = d.pop("lmx", UNSET)

        _contact_properties_fallbacks = d.pop("contactPropertiesFallbacks", UNSET)
        contact_properties_fallbacks: UpdateEmailMessageRequestContactPropertiesFallbacks | Unset
        if isinstance(_contact_properties_fallbacks, Unset):
            contact_properties_fallbacks = UNSET
        else:
            contact_properties_fallbacks = UpdateEmailMessageRequestContactPropertiesFallbacks.from_dict(
                _contact_properties_fallbacks
            )

        _event_properties_fallbacks = d.pop("eventPropertiesFallbacks", UNSET)
        event_properties_fallbacks: UpdateEmailMessageRequestEventPropertiesFallbacks | Unset
        if isinstance(_event_properties_fallbacks, Unset):
            event_properties_fallbacks = UNSET
        else:
            event_properties_fallbacks = UpdateEmailMessageRequestEventPropertiesFallbacks.from_dict(
                _event_properties_fallbacks
            )

        _data_variables_fallbacks = d.pop("dataVariablesFallbacks", UNSET)
        data_variables_fallbacks: UpdateEmailMessageRequestDataVariablesFallbacks | Unset
        if isinstance(_data_variables_fallbacks, Unset):
            data_variables_fallbacks = UNSET
        else:
            data_variables_fallbacks = UpdateEmailMessageRequestDataVariablesFallbacks.from_dict(
                _data_variables_fallbacks
            )

        update_email_message_request = cls(
            expected_revision_id=expected_revision_id,
            subject=subject,
            preview_text=preview_text,
            from_name=from_name,
            from_email=from_email,
            reply_to_email=reply_to_email,
            cc_email=cc_email,
            bcc_email=bcc_email,
            language_code=language_code,
            email_format=email_format,
            lmx=lmx,
            contact_properties_fallbacks=contact_properties_fallbacks,
            event_properties_fallbacks=event_properties_fallbacks,
            data_variables_fallbacks=data_variables_fallbacks,
        )

        return update_email_message_request
