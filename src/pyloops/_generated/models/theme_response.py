from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.theme_styles import ThemeStyles


T = TypeVar("T", bound="ThemeResponse")


@_attrs_define
class ThemeResponse:
    """
    Attributes:
        success (bool):
        theme_id (str):
        name (str):
        styles (ThemeStyles): Flat map of style attributes, matching the attribute names accepted by the LMX `<Style />`
            tag. Only keys with a value set on the theme are returned; all keys are optional.
        is_default (bool): Whether this theme is the team's default.
        created_at (str): ISO 8601 timestamp.
        updated_at (str): ISO 8601 timestamp.
    """

    success: bool
    theme_id: str
    name: str
    styles: ThemeStyles
    is_default: bool
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        theme_id = self.theme_id

        name = self.name

        styles = self.styles.to_dict()

        is_default = self.is_default

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "themeId": theme_id,
                "name": name,
                "styles": styles,
                "isDefault": is_default,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.theme_styles import ThemeStyles

        d = dict(src_dict)
        success = d.pop("success")

        theme_id = d.pop("themeId")

        name = d.pop("name")

        styles = ThemeStyles.from_dict(d.pop("styles"))

        is_default = d.pop("isDefault")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        theme_response = cls(
            success=success,
            theme_id=theme_id,
            name=name,
            styles=styles,
            is_default=is_default,
            created_at=created_at,
            updated_at=updated_at,
        )

        theme_response.additional_properties = d
        return theme_response

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
