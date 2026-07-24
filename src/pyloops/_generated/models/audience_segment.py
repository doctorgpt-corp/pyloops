from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.audience_filter_type_0 import AudienceFilterType0


T = TypeVar("T", bound="AudienceSegment")


@_attrs_define
class AudienceSegment:
    """
    Attributes:
        id (str): The ID of the audience segment.
        name (str): The name of the audience segment.
        description (None | str): An optional description of the audience segment.
        created_at (str): ISO 8601 timestamp for when the audience segment was created.
        updated_at (str): ISO 8601 timestamp for when the audience segment was last updated.
        filter_ (AudienceFilterType0 | None): A tree of audience conditions combined with `match`.
    """

    id: str
    name: str
    description: None | str
    created_at: str
    updated_at: str
    filter_: AudienceFilterType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audience_filter_type_0 import AudienceFilterType0

        id = self.id

        name = self.name

        description: None | str
        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at

        filter_: dict[str, Any] | None
        if isinstance(self.filter_, AudienceFilterType0):
            filter_ = self.filter_.to_dict()
        else:
            filter_ = self.filter_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "filter": filter_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audience_filter_type_0 import AudienceFilterType0

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        def _parse_filter_(data: object) -> AudienceFilterType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_audience_filter_type_0 = AudienceFilterType0.from_dict(data)

                return componentsschemas_audience_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AudienceFilterType0 | None, data)

        filter_ = _parse_filter_(d.pop("filter"))

        audience_segment = cls(
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            filter_=filter_,
        )

        audience_segment.additional_properties = d
        return audience_segment

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
