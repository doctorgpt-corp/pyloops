from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.footer_with_variants_placement import FooterWithVariantsPlacement

if TYPE_CHECKING:
    from ..models.footer_variant import FooterVariant


T = TypeVar("T", bound="FooterWithVariants")


@_attrs_define
class FooterWithVariants:
    """
    Attributes:
        id (str): The ID of the footer.
        name (str): The name of the footer.
        is_default (bool): Whether this is the team's default footer. New campaign and workflow emails use the default
            footer.
        placement (FooterWithVariantsPlacement): Whether the footer is rendered inside the email body (`inside`) or
            below it (`below`).
        created_at (datetime.datetime): ISO 8601 timestamp for when the footer was created.
        updated_at (datetime.datetime): ISO 8601 timestamp for when the footer's own fields last changed, such as its
            name or placement. Not changed when a variant is updated.
        variants (list[FooterVariant]): The footer's content variants. A footer has at most one variant. A footer
            created before variants has none.
    """

    id: str
    name: str
    is_default: bool
    placement: FooterWithVariantsPlacement
    created_at: datetime.datetime
    updated_at: datetime.datetime
    variants: list[FooterVariant]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_default = self.is_default

        placement = self.placement.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        variants = []
        for variants_item_data in self.variants:
            variants_item = variants_item_data.to_dict()
            variants.append(variants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "isDefault": is_default,
                "placement": placement,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "variants": variants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.footer_variant import FooterVariant  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        is_default = d.pop("isDefault")

        placement = FooterWithVariantsPlacement(d.pop("placement"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        variants = []
        _variants = d.pop("variants")
        for variants_item_data in _variants:
            variants_item = FooterVariant.from_dict(variants_item_data)

            variants.append(variants_item)

        footer_with_variants = cls(
            id=id,
            name=name,
            is_default=is_default,
            placement=placement,
            created_at=created_at,
            updated_at=updated_at,
            variants=variants,
        )

        footer_with_variants.additional_properties = d
        return footer_with_variants

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
