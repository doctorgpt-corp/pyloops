from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_audience_segment_request_filter import CreateAudienceSegmentRequestFilter


T = TypeVar("T", bound="CreateAudienceSegmentRequest")


@_attrs_define
class CreateAudienceSegmentRequest:
    """
    Attributes:
        name (str): The name of the audience segment. Must be unique within the team.
        filter_ (CreateAudienceSegmentRequestFilter): A tree of audience conditions combined with `match`.
        description (str | Unset): An optional description of the audience segment.
    """

    name: str
    filter_: CreateAudienceSegmentRequestFilter
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        filter_ = self.filter_.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "filter": filter_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_audience_segment_request_filter import CreateAudienceSegmentRequestFilter  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        filter_ = CreateAudienceSegmentRequestFilter.from_dict(d.pop("filter"))

        description = d.pop("description", UNSET)

        create_audience_segment_request = cls(
            name=name,
            filter_=filter_,
            description=description,
        )

        return create_audience_segment_request
