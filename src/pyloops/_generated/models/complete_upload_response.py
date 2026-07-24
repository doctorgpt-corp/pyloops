from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompleteUploadResponse")


@_attrs_define
class CompleteUploadResponse:
    """
    Attributes:
        email_asset_id (str): The ID of the created asset.
        final_url (str): The public URL of the uploaded asset.
    """

    email_asset_id: str
    final_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email_asset_id = self.email_asset_id

        final_url = self.final_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emailAssetId": email_asset_id,
                "finalUrl": final_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email_asset_id = d.pop("emailAssetId")

        final_url = d.pop("finalUrl")

        complete_upload_response = cls(
            email_asset_id=email_asset_id,
            final_url=final_url,
        )

        complete_upload_response.additional_properties = d
        return complete_upload_response

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
