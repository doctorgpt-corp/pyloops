from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audience_filter_in_request_type_0 import AudienceFilterInRequestType0


T = TypeVar("T", bound="WorkflowAudienceFilterPayload")


@_attrs_define
class WorkflowAudienceFilterPayload:
    """Configuration for the audience filter node.

    Attributes:
        audience_segment_id (None | str | Unset): The ID of an audience segment. Setting this without also providing
            `audienceFilter` clears any existing `audienceFilter`. If both are provided, the filter is applied on top of the
            segment's filter.
        audience_filter (AudienceFilterInRequestType0 | None | Unset): A tree of audience conditions combined with
            `match`. Setting this without also providing `audienceSegmentId` clears any existing `audienceSegmentId`. When
            both are provided, this filter is applied on top of the segment's filter.
        applies_downstream (bool | Unset): If `true`, the audience filter will apply to all downstream nodes. If
            `false`, the audience filter will only apply to the current node. Matches the "Filter scope" option in the UI.
    """

    audience_segment_id: None | str | Unset = UNSET
    audience_filter: AudienceFilterInRequestType0 | None | Unset = UNSET
    applies_downstream: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.audience_filter_in_request_type_0 import AudienceFilterInRequestType0  # noqa: PLC0415

        audience_segment_id: None | str | Unset
        if isinstance(self.audience_segment_id, Unset):
            audience_segment_id = UNSET
        else:
            audience_segment_id = self.audience_segment_id

        audience_filter: dict[str, Any] | None | Unset
        if isinstance(self.audience_filter, Unset):
            audience_filter = UNSET
        elif isinstance(self.audience_filter, AudienceFilterInRequestType0):
            audience_filter = self.audience_filter.to_dict()
        else:
            audience_filter = self.audience_filter

        applies_downstream = self.applies_downstream

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if audience_segment_id is not UNSET:
            field_dict["audienceSegmentId"] = audience_segment_id
        if audience_filter is not UNSET:
            field_dict["audienceFilter"] = audience_filter
        if applies_downstream is not UNSET:
            field_dict["appliesDownstream"] = applies_downstream

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audience_filter_in_request_type_0 import AudienceFilterInRequestType0  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_audience_segment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audience_segment_id = _parse_audience_segment_id(d.pop("audienceSegmentId", UNSET))

        def _parse_audience_filter(data: object) -> AudienceFilterInRequestType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_audience_filter_in_request_type_0 = AudienceFilterInRequestType0.from_dict(data)

                return componentsschemas_audience_filter_in_request_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AudienceFilterInRequestType0 | None | Unset, data)

        audience_filter = _parse_audience_filter(d.pop("audienceFilter", UNSET))

        applies_downstream = d.pop("appliesDownstream", UNSET)

        workflow_audience_filter_payload = cls(
            audience_segment_id=audience_segment_id,
            audience_filter=audience_filter,
            applies_downstream=applies_downstream,
        )

        return workflow_audience_filter_payload
