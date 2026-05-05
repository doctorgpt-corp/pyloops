from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEmailMessageRequest")


@_attrs_define
class UpdateEmailMessageRequest:
    """
    Attributes:
        expected_revision_id (str | Unset): The `contentRevisionId` you last fetched. Used for optimistic concurrency —
            the request is rejected with 409 if the server's revision has advanced.
        subject (str | Unset):
        preview_text (str | Unset):
        from_name (str | Unset):
        from_email (str | Unset): The sender username (without `@` or domain). The team's sending domain is appended
            automatically.
        reply_to_email (str | Unset): Reply-to email. Must be empty or a valid email address.
        lmx (str | Unset): The email body serialized as LMX. Styles must be embedded in the LMX `<Style />` tag.
    """

    expected_revision_id: str | Unset = UNSET
    subject: str | Unset = UNSET
    preview_text: str | Unset = UNSET
    from_name: str | Unset = UNSET
    from_email: str | Unset = UNSET
    reply_to_email: str | Unset = UNSET
    lmx: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expected_revision_id = self.expected_revision_id

        subject = self.subject

        preview_text = self.preview_text

        from_name = self.from_name

        from_email = self.from_email

        reply_to_email = self.reply_to_email

        lmx = self.lmx

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
        if lmx is not UNSET:
            field_dict["lmx"] = lmx

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_revision_id = d.pop("expectedRevisionId", UNSET)

        subject = d.pop("subject", UNSET)

        preview_text = d.pop("previewText", UNSET)

        from_name = d.pop("fromName", UNSET)

        from_email = d.pop("fromEmail", UNSET)

        reply_to_email = d.pop("replyToEmail", UNSET)

        lmx = d.pop("lmx", UNSET)

        update_email_message_request = cls(
            expected_revision_id=expected_revision_id,
            subject=subject,
            preview_text=preview_text,
            from_name=from_name,
            from_email=from_email,
            reply_to_email=reply_to_email,
            lmx=lmx,
        )

        return update_email_message_request
