from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThemeStyles")


@_attrs_define
class ThemeStyles:
    """Flat map of style attributes, matching the attribute names accepted by the LMX `<Style />` tag. Only keys with a
    value set on the theme are returned; all keys are optional.

        Attributes:
            background_color (str | Unset):
            background_x_padding (float | Unset):
            background_y_padding (float | Unset):
            body_color (str | Unset):
            body_x_padding (float | Unset):
            body_y_padding (float | Unset):
            body_font_family (str | Unset):
            body_font_category (str | Unset):
            border_color (str | Unset):
            border_width (float | Unset):
            border_radius (float | Unset):
            button_body_color (str | Unset):
            button_body_x_padding (float | Unset):
            button_body_y_padding (float | Unset):
            button_border_color (str | Unset):
            button_border_width (float | Unset):
            button_border_radius (float | Unset):
            button_text_color (str | Unset):
            button_text_format (float | Unset):
            button_text_font_size (float | Unset):
            divider_color (str | Unset):
            divider_border_width (float | Unset):
            text_base_color (str | Unset):
            text_base_font_size (float | Unset):
            text_base_line_height (float | Unset):
            text_base_letter_spacing (float | Unset):
            text_link_color (str | Unset):
            heading_1_color (str | Unset):
            heading_1_font_size (float | Unset):
            heading_1_line_height (float | Unset):
            heading_1_letter_spacing (float | Unset):
            heading_2_color (str | Unset):
            heading_2_font_size (float | Unset):
            heading_2_line_height (float | Unset):
            heading_2_letter_spacing (float | Unset):
            heading_3_color (str | Unset):
            heading_3_font_size (float | Unset):
            heading_3_line_height (float | Unset):
            heading_3_letter_spacing (float | Unset):
    """

    background_color: str | Unset = UNSET
    background_x_padding: float | Unset = UNSET
    background_y_padding: float | Unset = UNSET
    body_color: str | Unset = UNSET
    body_x_padding: float | Unset = UNSET
    body_y_padding: float | Unset = UNSET
    body_font_family: str | Unset = UNSET
    body_font_category: str | Unset = UNSET
    border_color: str | Unset = UNSET
    border_width: float | Unset = UNSET
    border_radius: float | Unset = UNSET
    button_body_color: str | Unset = UNSET
    button_body_x_padding: float | Unset = UNSET
    button_body_y_padding: float | Unset = UNSET
    button_border_color: str | Unset = UNSET
    button_border_width: float | Unset = UNSET
    button_border_radius: float | Unset = UNSET
    button_text_color: str | Unset = UNSET
    button_text_format: float | Unset = UNSET
    button_text_font_size: float | Unset = UNSET
    divider_color: str | Unset = UNSET
    divider_border_width: float | Unset = UNSET
    text_base_color: str | Unset = UNSET
    text_base_font_size: float | Unset = UNSET
    text_base_line_height: float | Unset = UNSET
    text_base_letter_spacing: float | Unset = UNSET
    text_link_color: str | Unset = UNSET
    heading_1_color: str | Unset = UNSET
    heading_1_font_size: float | Unset = UNSET
    heading_1_line_height: float | Unset = UNSET
    heading_1_letter_spacing: float | Unset = UNSET
    heading_2_color: str | Unset = UNSET
    heading_2_font_size: float | Unset = UNSET
    heading_2_line_height: float | Unset = UNSET
    heading_2_letter_spacing: float | Unset = UNSET
    heading_3_color: str | Unset = UNSET
    heading_3_font_size: float | Unset = UNSET
    heading_3_line_height: float | Unset = UNSET
    heading_3_letter_spacing: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        background_color = self.background_color

        background_x_padding = self.background_x_padding

        background_y_padding = self.background_y_padding

        body_color = self.body_color

        body_x_padding = self.body_x_padding

        body_y_padding = self.body_y_padding

        body_font_family = self.body_font_family

        body_font_category = self.body_font_category

        border_color = self.border_color

        border_width = self.border_width

        border_radius = self.border_radius

        button_body_color = self.button_body_color

        button_body_x_padding = self.button_body_x_padding

        button_body_y_padding = self.button_body_y_padding

        button_border_color = self.button_border_color

        button_border_width = self.button_border_width

        button_border_radius = self.button_border_radius

        button_text_color = self.button_text_color

        button_text_format = self.button_text_format

        button_text_font_size = self.button_text_font_size

        divider_color = self.divider_color

        divider_border_width = self.divider_border_width

        text_base_color = self.text_base_color

        text_base_font_size = self.text_base_font_size

        text_base_line_height = self.text_base_line_height

        text_base_letter_spacing = self.text_base_letter_spacing

        text_link_color = self.text_link_color

        heading_1_color = self.heading_1_color

        heading_1_font_size = self.heading_1_font_size

        heading_1_line_height = self.heading_1_line_height

        heading_1_letter_spacing = self.heading_1_letter_spacing

        heading_2_color = self.heading_2_color

        heading_2_font_size = self.heading_2_font_size

        heading_2_line_height = self.heading_2_line_height

        heading_2_letter_spacing = self.heading_2_letter_spacing

        heading_3_color = self.heading_3_color

        heading_3_font_size = self.heading_3_font_size

        heading_3_line_height = self.heading_3_line_height

        heading_3_letter_spacing = self.heading_3_letter_spacing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if background_color is not UNSET:
            field_dict["backgroundColor"] = background_color
        if background_x_padding is not UNSET:
            field_dict["backgroundXPadding"] = background_x_padding
        if background_y_padding is not UNSET:
            field_dict["backgroundYPadding"] = background_y_padding
        if body_color is not UNSET:
            field_dict["bodyColor"] = body_color
        if body_x_padding is not UNSET:
            field_dict["bodyXPadding"] = body_x_padding
        if body_y_padding is not UNSET:
            field_dict["bodyYPadding"] = body_y_padding
        if body_font_family is not UNSET:
            field_dict["bodyFontFamily"] = body_font_family
        if body_font_category is not UNSET:
            field_dict["bodyFontCategory"] = body_font_category
        if border_color is not UNSET:
            field_dict["borderColor"] = border_color
        if border_width is not UNSET:
            field_dict["borderWidth"] = border_width
        if border_radius is not UNSET:
            field_dict["borderRadius"] = border_radius
        if button_body_color is not UNSET:
            field_dict["buttonBodyColor"] = button_body_color
        if button_body_x_padding is not UNSET:
            field_dict["buttonBodyXPadding"] = button_body_x_padding
        if button_body_y_padding is not UNSET:
            field_dict["buttonBodyYPadding"] = button_body_y_padding
        if button_border_color is not UNSET:
            field_dict["buttonBorderColor"] = button_border_color
        if button_border_width is not UNSET:
            field_dict["buttonBorderWidth"] = button_border_width
        if button_border_radius is not UNSET:
            field_dict["buttonBorderRadius"] = button_border_radius
        if button_text_color is not UNSET:
            field_dict["buttonTextColor"] = button_text_color
        if button_text_format is not UNSET:
            field_dict["buttonTextFormat"] = button_text_format
        if button_text_font_size is not UNSET:
            field_dict["buttonTextFontSize"] = button_text_font_size
        if divider_color is not UNSET:
            field_dict["dividerColor"] = divider_color
        if divider_border_width is not UNSET:
            field_dict["dividerBorderWidth"] = divider_border_width
        if text_base_color is not UNSET:
            field_dict["textBaseColor"] = text_base_color
        if text_base_font_size is not UNSET:
            field_dict["textBaseFontSize"] = text_base_font_size
        if text_base_line_height is not UNSET:
            field_dict["textBaseLineHeight"] = text_base_line_height
        if text_base_letter_spacing is not UNSET:
            field_dict["textBaseLetterSpacing"] = text_base_letter_spacing
        if text_link_color is not UNSET:
            field_dict["textLinkColor"] = text_link_color
        if heading_1_color is not UNSET:
            field_dict["heading1Color"] = heading_1_color
        if heading_1_font_size is not UNSET:
            field_dict["heading1FontSize"] = heading_1_font_size
        if heading_1_line_height is not UNSET:
            field_dict["heading1LineHeight"] = heading_1_line_height
        if heading_1_letter_spacing is not UNSET:
            field_dict["heading1LetterSpacing"] = heading_1_letter_spacing
        if heading_2_color is not UNSET:
            field_dict["heading2Color"] = heading_2_color
        if heading_2_font_size is not UNSET:
            field_dict["heading2FontSize"] = heading_2_font_size
        if heading_2_line_height is not UNSET:
            field_dict["heading2LineHeight"] = heading_2_line_height
        if heading_2_letter_spacing is not UNSET:
            field_dict["heading2LetterSpacing"] = heading_2_letter_spacing
        if heading_3_color is not UNSET:
            field_dict["heading3Color"] = heading_3_color
        if heading_3_font_size is not UNSET:
            field_dict["heading3FontSize"] = heading_3_font_size
        if heading_3_line_height is not UNSET:
            field_dict["heading3LineHeight"] = heading_3_line_height
        if heading_3_letter_spacing is not UNSET:
            field_dict["heading3LetterSpacing"] = heading_3_letter_spacing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        background_color = d.pop("backgroundColor", UNSET)

        background_x_padding = d.pop("backgroundXPadding", UNSET)

        background_y_padding = d.pop("backgroundYPadding", UNSET)

        body_color = d.pop("bodyColor", UNSET)

        body_x_padding = d.pop("bodyXPadding", UNSET)

        body_y_padding = d.pop("bodyYPadding", UNSET)

        body_font_family = d.pop("bodyFontFamily", UNSET)

        body_font_category = d.pop("bodyFontCategory", UNSET)

        border_color = d.pop("borderColor", UNSET)

        border_width = d.pop("borderWidth", UNSET)

        border_radius = d.pop("borderRadius", UNSET)

        button_body_color = d.pop("buttonBodyColor", UNSET)

        button_body_x_padding = d.pop("buttonBodyXPadding", UNSET)

        button_body_y_padding = d.pop("buttonBodyYPadding", UNSET)

        button_border_color = d.pop("buttonBorderColor", UNSET)

        button_border_width = d.pop("buttonBorderWidth", UNSET)

        button_border_radius = d.pop("buttonBorderRadius", UNSET)

        button_text_color = d.pop("buttonTextColor", UNSET)

        button_text_format = d.pop("buttonTextFormat", UNSET)

        button_text_font_size = d.pop("buttonTextFontSize", UNSET)

        divider_color = d.pop("dividerColor", UNSET)

        divider_border_width = d.pop("dividerBorderWidth", UNSET)

        text_base_color = d.pop("textBaseColor", UNSET)

        text_base_font_size = d.pop("textBaseFontSize", UNSET)

        text_base_line_height = d.pop("textBaseLineHeight", UNSET)

        text_base_letter_spacing = d.pop("textBaseLetterSpacing", UNSET)

        text_link_color = d.pop("textLinkColor", UNSET)

        heading_1_color = d.pop("heading1Color", UNSET)

        heading_1_font_size = d.pop("heading1FontSize", UNSET)

        heading_1_line_height = d.pop("heading1LineHeight", UNSET)

        heading_1_letter_spacing = d.pop("heading1LetterSpacing", UNSET)

        heading_2_color = d.pop("heading2Color", UNSET)

        heading_2_font_size = d.pop("heading2FontSize", UNSET)

        heading_2_line_height = d.pop("heading2LineHeight", UNSET)

        heading_2_letter_spacing = d.pop("heading2LetterSpacing", UNSET)

        heading_3_color = d.pop("heading3Color", UNSET)

        heading_3_font_size = d.pop("heading3FontSize", UNSET)

        heading_3_line_height = d.pop("heading3LineHeight", UNSET)

        heading_3_letter_spacing = d.pop("heading3LetterSpacing", UNSET)

        theme_styles = cls(
            background_color=background_color,
            background_x_padding=background_x_padding,
            background_y_padding=background_y_padding,
            body_color=body_color,
            body_x_padding=body_x_padding,
            body_y_padding=body_y_padding,
            body_font_family=body_font_family,
            body_font_category=body_font_category,
            border_color=border_color,
            border_width=border_width,
            border_radius=border_radius,
            button_body_color=button_body_color,
            button_body_x_padding=button_body_x_padding,
            button_body_y_padding=button_body_y_padding,
            button_border_color=button_border_color,
            button_border_width=button_border_width,
            button_border_radius=button_border_radius,
            button_text_color=button_text_color,
            button_text_format=button_text_format,
            button_text_font_size=button_text_font_size,
            divider_color=divider_color,
            divider_border_width=divider_border_width,
            text_base_color=text_base_color,
            text_base_font_size=text_base_font_size,
            text_base_line_height=text_base_line_height,
            text_base_letter_spacing=text_base_letter_spacing,
            text_link_color=text_link_color,
            heading_1_color=heading_1_color,
            heading_1_font_size=heading_1_font_size,
            heading_1_line_height=heading_1_line_height,
            heading_1_letter_spacing=heading_1_letter_spacing,
            heading_2_color=heading_2_color,
            heading_2_font_size=heading_2_font_size,
            heading_2_line_height=heading_2_line_height,
            heading_2_letter_spacing=heading_2_letter_spacing,
            heading_3_color=heading_3_color,
            heading_3_font_size=heading_3_font_size,
            heading_3_line_height=heading_3_line_height,
            heading_3_letter_spacing=heading_3_letter_spacing,
        )

        theme_styles.additional_properties = d
        return theme_styles

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
