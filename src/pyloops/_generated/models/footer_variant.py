from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FooterVariant")


@_attrs_define
class FooterVariant:
    """
    Attributes:
        id (str): The ID of the variant.
        footer_id (str): The ID of the footer the variant belongs to.
        content_revision_id (str): The variant's current content revision. Pass it as `expectedRevisionId` when you
            update or publish the variant.
        published_at (datetime.datetime | None): ISO 8601 timestamp for when the variant was last published. `null` if
            it was never published.
        created_at (datetime.datetime): ISO 8601 timestamp for when the variant was created.
        draft_lmx (str): The draft content as LMX.
        published_lmx (None | str): The published content as LMX. `null` if the variant was never published.
        updated_at (datetime.datetime): ISO 8601 timestamp for when the variant's draft or published content last
            changed.
    """

    id: str
    footer_id: str
    content_revision_id: str
    published_at: datetime.datetime | None
    created_at: datetime.datetime
    draft_lmx: str
    published_lmx: None | str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        footer_id = self.footer_id

        content_revision_id = self.content_revision_id

        published_at: None | str
        if isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        created_at = self.created_at.isoformat()

        draft_lmx = self.draft_lmx

        published_lmx: None | str
        published_lmx = self.published_lmx

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "footerId": footer_id,
                "contentRevisionId": content_revision_id,
                "publishedAt": published_at,
                "createdAt": created_at,
                "draftLmx": draft_lmx,
                "publishedLmx": published_lmx,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        footer_id = d.pop("footerId")

        content_revision_id = d.pop("contentRevisionId")

        def _parse_published_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        published_at = _parse_published_at(d.pop("publishedAt"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        draft_lmx = d.pop("draftLmx")

        def _parse_published_lmx(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_lmx = _parse_published_lmx(d.pop("publishedLmx"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        footer_variant = cls(
            id=id,
            footer_id=footer_id,
            content_revision_id=content_revision_id,
            published_at=published_at,
            created_at=created_at,
            draft_lmx=draft_lmx,
            published_lmx=published_lmx,
            updated_at=updated_at,
        )

        footer_variant.additional_properties = d
        return footer_variant

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
