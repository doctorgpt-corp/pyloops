from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.theme_styles import ThemeStyles


T = TypeVar("T", bound="UpdateThemeBody")


@_attrs_define
class UpdateThemeBody:
    """At least one of `name` or `styles` must be provided.

    Attributes:
        name (str | Unset):
        styles (ThemeStyles | Unset): Flat map of style attributes, matching the attribute names accepted by the LMX
            `<Style />` tag.
    """

    name: str | Unset = UNSET
    styles: ThemeStyles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        styles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.styles, Unset):
            styles = self.styles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if styles is not UNSET:
            field_dict["styles"] = styles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.theme_styles import ThemeStyles  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _styles = d.pop("styles", UNSET)
        styles: ThemeStyles | Unset
        if isinstance(_styles, Unset):
            styles = UNSET
        else:
            styles = ThemeStyles.from_dict(_styles)

        update_theme_body = cls(
            name=name,
            styles=styles,
        )

        update_theme_body.additional_properties = d
        return update_theme_body

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
