from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateUploadRequest")


@_attrs_define
class CreateUploadRequest:
    """
    Attributes:
        content_type (str): The MIME type of the file to upload. Supported types are `image/jpeg`, `image/png`,
            `image/gif` and `image/webp`.
        content_length (int): The size of the file in bytes. Must be a positive integer no greater than 4,000,000 bytes.
    """

    content_type: str
    content_length: int

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        content_length = self.content_length

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contentType": content_type,
                "contentLength": content_length,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("contentType")

        content_length = d.pop("contentLength")

        create_upload_request = cls(
            content_type=content_type,
            content_length=content_length,
        )

        return create_upload_request
