from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audience_filter_workflow_mutation_node_type_name import AudienceFilterWorkflowMutationNodeTypeName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audience_filter_type_0 import AudienceFilterType0


T = TypeVar("T", bound="AudienceFilterWorkflowMutationNodeWithRevision")


@_attrs_define
class AudienceFilterWorkflowMutationNodeWithRevision:
    """
    Attributes:
        id (str):
        type_name (AudienceFilterWorkflowMutationNodeTypeName):
        next_node_ids (list[str]): The IDs of the nodes that are downstream of this node.
        applies_downstream (bool): If `true`, the audience filter will apply to all downstream nodes. If `false`, the
            audience filter will only apply to the current node. Matches the "Filter scope" option in the UI.
        workflow_revision_id (str): The current workflow revision token. Pass the latest value as `expectedRevisionId`
            on the next workflow mutation.
        audience_filter (AudienceFilterType0 | None | Unset): A tree of audience conditions combined with `match`.
        audience_segment_id (str | Unset): The ID of the audience segment this trigger targets.
    """

    id: str
    type_name: AudienceFilterWorkflowMutationNodeTypeName
    next_node_ids: list[str]
    applies_downstream: bool
    workflow_revision_id: str
    audience_filter: AudienceFilterType0 | None | Unset = UNSET
    audience_segment_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audience_filter_type_0 import AudienceFilterType0

        id = self.id

        type_name = self.type_name.value

        next_node_ids = self.next_node_ids

        applies_downstream = self.applies_downstream

        workflow_revision_id: str
        workflow_revision_id = self.workflow_revision_id

        audience_filter: dict[str, Any] | None | Unset
        if isinstance(self.audience_filter, Unset):
            audience_filter = UNSET
        elif isinstance(self.audience_filter, AudienceFilterType0):
            audience_filter = self.audience_filter.to_dict()
        else:
            audience_filter = self.audience_filter

        audience_segment_id = self.audience_segment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "typeName": type_name,
                "nextNodeIds": next_node_ids,
                "appliesDownstream": applies_downstream,
                "workflowRevisionId": workflow_revision_id,
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

        type_name = AudienceFilterWorkflowMutationNodeTypeName(d.pop("typeName"))

        next_node_ids = cast(list[str], d.pop("nextNodeIds"))

        applies_downstream = d.pop("appliesDownstream")

        def _parse_workflow_revision_id(data: object) -> str:
            return cast(str, data)

        workflow_revision_id = _parse_workflow_revision_id(d.pop("workflowRevisionId"))

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

        audience_filter_workflow_mutation_node_with_revision = cls(
            id=id,
            type_name=type_name,
            next_node_ids=next_node_ids,
            applies_downstream=applies_downstream,
            workflow_revision_id=workflow_revision_id,
            audience_filter=audience_filter,
            audience_segment_id=audience_segment_id,
        )

        audience_filter_workflow_mutation_node_with_revision.additional_properties = d
        return audience_filter_workflow_mutation_node_with_revision

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
