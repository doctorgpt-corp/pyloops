from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.create_audience_segment_request_filter_match import CreateAudienceSegmentRequestFilterMatch

if TYPE_CHECKING:
    from ..models.activity_condition import ActivityCondition
    from ..models.opt_in_condition import OptInCondition
    from ..models.property_condition import PropertyCondition


T = TypeVar("T", bound="CreateAudienceSegmentRequestFilter")


@_attrs_define
class CreateAudienceSegmentRequestFilter:
    """A tree of audience conditions combined with `match`.

    Attributes:
        match (CreateAudienceSegmentRequestFilterMatch):
        conditions (list[ActivityCondition | OptInCondition | PropertyCondition]):
    """

    match: CreateAudienceSegmentRequestFilterMatch
    conditions: list[ActivityCondition | OptInCondition | PropertyCondition]

    def to_dict(self) -> dict[str, Any]:
        from ..models.opt_in_condition import OptInCondition  # noqa: PLC0415
        from ..models.property_condition import PropertyCondition  # noqa: PLC0415

        match = self.match.value

        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item: dict[str, Any]
            if isinstance(conditions_item_data, PropertyCondition):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(conditions_item_data, OptInCondition):
                conditions_item = conditions_item_data.to_dict()
            else:
                conditions_item = conditions_item_data.to_dict()

            conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "match": match,
                "conditions": conditions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_condition import ActivityCondition  # noqa: PLC0415
        from ..models.opt_in_condition import OptInCondition  # noqa: PLC0415
        from ..models.property_condition import PropertyCondition  # noqa: PLC0415

        d = dict(src_dict)
        match = CreateAudienceSegmentRequestFilterMatch(d.pop("match"))

        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:

            def _parse_conditions_item(data: object) -> ActivityCondition | OptInCondition | PropertyCondition:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_audience_filter_condition_type_0 = PropertyCondition.from_dict(data)

                    return componentsschemas_audience_filter_condition_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_audience_filter_condition_type_1 = OptInCondition.from_dict(data)

                    return componentsschemas_audience_filter_condition_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_audience_filter_condition_type_2 = ActivityCondition.from_dict(data)

                return componentsschemas_audience_filter_condition_type_2

            conditions_item = _parse_conditions_item(conditions_item_data)

            conditions.append(conditions_item)

        create_audience_segment_request_filter = cls(
            match=match,
            conditions=conditions,
        )

        return create_audience_segment_request_filter
