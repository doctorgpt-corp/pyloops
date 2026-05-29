from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadLimitExceededFailureResponse")


@_attrs_define
class UploadLimitExceededFailureResponse:
    """
    Attributes:
        success (bool | Unset):
        message (str | Unset):
        max_uploads (int | Unset): The maximum number of uploads allowed per window.
        window_hours (int | Unset): The number of hours in the upload limit window.
    """

    success: bool | Unset = UNSET
    message: str | Unset = UNSET
    max_uploads: int | Unset = UNSET
    window_hours: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        max_uploads = self.max_uploads

        window_hours = self.window_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message
        if max_uploads is not UNSET:
            field_dict["maxUploads"] = max_uploads
        if window_hours is not UNSET:
            field_dict["windowHours"] = window_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        max_uploads = d.pop("maxUploads", UNSET)

        window_hours = d.pop("windowHours", UNSET)

        upload_limit_exceeded_failure_response = cls(
            success=success,
            message=message,
            max_uploads=max_uploads,
            window_hours=window_hours,
        )

        upload_limit_exceeded_failure_response.additional_properties = d
        return upload_limit_exceeded_failure_response

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
