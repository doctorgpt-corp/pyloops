from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mailing_list_change_preview_status import MailingListChangePreviewStatus

T = TypeVar("T", bound="MailingListChangePreview")


@_attrs_define
class MailingListChangePreview:
    """
    Attributes:
        status (MailingListChangePreviewStatus):
        mailing_list_id (None | str):
        queued_contact_count (float): The number of queued contacts that would be removed from the workflow due to the
            mailing list changing.
    """

    status: MailingListChangePreviewStatus
    mailing_list_id: None | str
    queued_contact_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        mailing_list_id: None | str
        mailing_list_id = self.mailing_list_id

        queued_contact_count = self.queued_contact_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "mailingListId": mailing_list_id,
                "queuedContactCount": queued_contact_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = MailingListChangePreviewStatus(d.pop("status"))

        def _parse_mailing_list_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mailing_list_id = _parse_mailing_list_id(d.pop("mailingListId"))

        queued_contact_count = d.pop("queuedContactCount")

        mailing_list_change_preview = cls(
            status=status,
            mailing_list_id=mailing_list_id,
            queued_contact_count=queued_contact_count,
        )

        mailing_list_change_preview.additional_properties = d
        return mailing_list_change_preview

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
