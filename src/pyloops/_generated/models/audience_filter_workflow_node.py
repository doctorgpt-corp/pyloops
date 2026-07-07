from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.audience_filter_workflow_node_type_name import AudienceFilterWorkflowNodeTypeName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audience_filter_type_0 import AudienceFilterType0


T = TypeVar("T", bound="AudienceFilterWorkflowNode")


@_attrs_define
class AudienceFilterWorkflowNode:
    """
    Attributes:
        id (str):
        workflow_id (str):
        type_name (AudienceFilterWorkflowNodeTypeName):
        next_node_ids (list[str]):
        applies_downstream (bool):
        audience_filter (AudienceFilterType0 | None | Unset): A tree of audience conditions combined with `match`. Null
            when the campaign targets a mailing list or segment without an explicit filter.
        audience_segment_id (str | Unset):
    """

    id: str
    workflow_id: str
    type_name: AudienceFilterWorkflowNodeTypeName
    next_node_ids: list[str]
    applies_downstream: bool
    audience_filter: AudienceFilterType0 | None | Unset = UNSET
    audience_segment_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.audience_filter_type_0 import AudienceFilterType0

        id = self.id

        workflow_id = self.workflow_id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        applies_downstream = self.applies_downstream

        audience_filter: dict[str, Any] | None | Unset
        if isinstance(self.audience_filter, Unset):
            audience_filter = UNSET
        elif isinstance(self.audience_filter, AudienceFilterType0):
            audience_filter = self.audience_filter.to_dict()
        else:
            audience_filter = self.audience_filter

        audience_segment_id = self.audience_segment_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "appliesDownstream": applies_downstream,
            }
        )
        if audience_filter is not UNSET:
            field_dict["audienceFilter"] = audience_filter
        if audience_segment_id is not UNSET:
            field_dict["audienceSegmentId"] = audience_segment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audience_filter_type_0 import AudienceFilterType0

        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        type_name = AudienceFilterWorkflowNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        applies_downstream = d.pop("appliesDownstream")

        def _parse_audience_filter(data: object) -> AudienceFilterType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_audience_filter_type_0 = AudienceFilterType0.from_dict(data)

                return componentsschemas_audience_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AudienceFilterType0 | None | Unset, data)

        audience_filter = _parse_audience_filter(d.pop("audienceFilter", UNSET))

        audience_segment_id = d.pop("audienceSegmentId", UNSET)

        audience_filter_workflow_node = cls(
            id=id,
            workflow_id=workflow_id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            applies_downstream=applies_downstream,
            audience_filter=audience_filter,
            audience_segment_id=audience_segment_id,
        )

        return audience_filter_workflow_node
