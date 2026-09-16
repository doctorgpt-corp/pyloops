from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.theme_styles import ThemeStyles


T = TypeVar("T", bound="UpdateThemeResponse")


@_attrs_define
class UpdateThemeResponse:
    """
    Attributes:
        id (str): The ID of the theme.
        name (str): The name of the theme.
        styles (ThemeStyles): Flat map of style attributes, matching the attribute names accepted by the LMX `<Style />`
            tag.
        is_default (bool): Whether this theme is the team's default.
        created_at (str): ISO 8601 timestamp for when the theme was created.
        updated_at (str): ISO 8601 timestamp for when the theme was last updated.
        affected_email_count (float): The number of emails using this theme that are affected by the style change. `0`
            when only the name changed.
    """

    id: str
    name: str
    styles: ThemeStyles
    is_default: bool
    created_at: str
    updated_at: str
    affected_email_count: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        styles = self.styles.to_dict()

        is_default = self.is_default

        created_at = self.created_at

        updated_at = self.updated_at

        affected_email_count = self.affected_email_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "styles": styles,
                "isDefault": is_default,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "affectedEmailCount": affected_email_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.theme_styles import ThemeStyles  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        styles = ThemeStyles.from_dict(d.pop("styles"))

        is_default = d.pop("isDefault")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        affected_email_count = d.pop("affectedEmailCount")

        update_theme_response = cls(
            id=id,
            name=name,
            styles=styles,
            is_default=is_default,
            created_at=created_at,
            updated_at=updated_at,
            affected_email_count=affected_email_count,
        )

        update_theme_response.additional_properties = d
        return update_theme_response

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
