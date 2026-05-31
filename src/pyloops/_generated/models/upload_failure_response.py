from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadFailureResponse")


@_attrs_define
class UploadFailureResponse:
    """
    Attributes:
        success (bool):
        message (str):
        supported_content_types (list[str] | Unset): Present when the request was rejected for an unsupported
            `contentType`. Lists the accepted MIME types.
        max_bytes (int | Unset): Present when the upload exceeds the size limit. The maximum allowed size in bytes.
    """

    success: bool
    message: str
    supported_content_types: list[str] | Unset = UNSET
    max_bytes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        supported_content_types: list[str] | Unset = UNSET
        if not isinstance(self.supported_content_types, Unset):
            supported_content_types = self.supported_content_types

        max_bytes = self.max_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
            }
        )
        if supported_content_types is not UNSET:
            field_dict["supportedContentTypes"] = supported_content_types
        if max_bytes is not UNSET:
            field_dict["maxBytes"] = max_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        supported_content_types = cast(list[str], d.pop("supportedContentTypes", UNSET))

        max_bytes = d.pop("maxBytes", UNSET)

        upload_failure_response = cls(
            success=success,
            message=message,
            supported_content_types=supported_content_types,
            max_bytes=max_bytes,
        )

        upload_failure_response.additional_properties = d
        return upload_failure_response

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
