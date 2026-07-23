from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.simplified_add_to_list_trigger_workflow_node import SimplifiedAddToListTriggerWorkflowNode
    from ..models.simplified_audience_filter_workflow_node import SimplifiedAudienceFilterWorkflowNode
    from ..models.simplified_blank_trigger_workflow_node import SimplifiedBlankTriggerWorkflowNode
    from ..models.simplified_branch_workflow_node import SimplifiedBranchWorkflowNode
    from ..models.simplified_contact_property_trigger_workflow_node import SimplifiedContactPropertyTriggerWorkflowNode
    from ..models.simplified_event_trigger_workflow_node import SimplifiedEventTriggerWorkflowNode
    from ..models.simplified_exit_action_workflow_node import SimplifiedExitActionWorkflowNode
    from ..models.simplified_experiment_branch_workflow_node import SimplifiedExperimentBranchWorkflowNode
    from ..models.simplified_send_email_action_workflow_node import SimplifiedSendEmailActionWorkflowNode
    from ..models.simplified_signup_trigger_workflow_node import SimplifiedSignupTriggerWorkflowNode
    from ..models.simplified_timer_action_workflow_node import SimplifiedTimerActionWorkflowNode
    from ..models.simplified_variant_workflow_node import SimplifiedVariantWorkflowNode


T = TypeVar("T", bound="SimplifiedWorkflowNodes")


@_attrs_define
class SimplifiedWorkflowNodes:
    """A map of node IDs to simplified node objects. Each node includes `typeName` and `nextNodeIds`, plus type-specific
    fields when present. To get the full node object, use the `GET /v1/workflows/{workflowId}/nodes/{nodeId}` endpoint.

        Example:
            {'cf16k73gq014h3mmj5b6jdi9r': {'typeName': 'SignupTrigger', 'nextNodeIds': ['cf16k73gq014h3mmj5b4jdifg',
                'cf16k73gq014h3mmj5b4jdifh']}}

    """

    additional_properties: dict[
        str,
        SimplifiedAddToListTriggerWorkflowNode
        | SimplifiedAudienceFilterWorkflowNode
        | SimplifiedBlankTriggerWorkflowNode
        | SimplifiedBranchWorkflowNode
        | SimplifiedContactPropertyTriggerWorkflowNode
        | SimplifiedEventTriggerWorkflowNode
        | SimplifiedExitActionWorkflowNode
        | SimplifiedExperimentBranchWorkflowNode
        | SimplifiedSendEmailActionWorkflowNode
        | SimplifiedSignupTriggerWorkflowNode
        | SimplifiedTimerActionWorkflowNode
        | SimplifiedVariantWorkflowNode,
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.simplified_add_to_list_trigger_workflow_node import SimplifiedAddToListTriggerWorkflowNode
        from ..models.simplified_audience_filter_workflow_node import SimplifiedAudienceFilterWorkflowNode
        from ..models.simplified_blank_trigger_workflow_node import SimplifiedBlankTriggerWorkflowNode
        from ..models.simplified_branch_workflow_node import SimplifiedBranchWorkflowNode
        from ..models.simplified_contact_property_trigger_workflow_node import (
            SimplifiedContactPropertyTriggerWorkflowNode,
        )
        from ..models.simplified_event_trigger_workflow_node import SimplifiedEventTriggerWorkflowNode
        from ..models.simplified_exit_action_workflow_node import SimplifiedExitActionWorkflowNode
        from ..models.simplified_experiment_branch_workflow_node import SimplifiedExperimentBranchWorkflowNode
        from ..models.simplified_send_email_action_workflow_node import SimplifiedSendEmailActionWorkflowNode
        from ..models.simplified_signup_trigger_workflow_node import SimplifiedSignupTriggerWorkflowNode
        from ..models.simplified_timer_action_workflow_node import SimplifiedTimerActionWorkflowNode

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, SimplifiedSignupTriggerWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SimplifiedEventTriggerWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SimplifiedContactPropertyTriggerWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SimplifiedAddToListTriggerWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SimplifiedBlankTriggerWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SimplifiedAudienceFilterWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SimplifiedTimerActionWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SimplifiedSendEmailActionWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SimplifiedExitActionWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SimplifiedBranchWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, SimplifiedExperimentBranchWorkflowNode):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simplified_add_to_list_trigger_workflow_node import SimplifiedAddToListTriggerWorkflowNode
        from ..models.simplified_audience_filter_workflow_node import SimplifiedAudienceFilterWorkflowNode
        from ..models.simplified_blank_trigger_workflow_node import SimplifiedBlankTriggerWorkflowNode
        from ..models.simplified_branch_workflow_node import SimplifiedBranchWorkflowNode
        from ..models.simplified_contact_property_trigger_workflow_node import (
            SimplifiedContactPropertyTriggerWorkflowNode,
        )
        from ..models.simplified_event_trigger_workflow_node import SimplifiedEventTriggerWorkflowNode
        from ..models.simplified_exit_action_workflow_node import SimplifiedExitActionWorkflowNode
        from ..models.simplified_experiment_branch_workflow_node import SimplifiedExperimentBranchWorkflowNode
        from ..models.simplified_send_email_action_workflow_node import SimplifiedSendEmailActionWorkflowNode
        from ..models.simplified_signup_trigger_workflow_node import SimplifiedSignupTriggerWorkflowNode
        from ..models.simplified_timer_action_workflow_node import SimplifiedTimerActionWorkflowNode
        from ..models.simplified_variant_workflow_node import SimplifiedVariantWorkflowNode

        d = dict(src_dict)
        simplified_workflow_nodes = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> (
                SimplifiedAddToListTriggerWorkflowNode
                | SimplifiedAudienceFilterWorkflowNode
                | SimplifiedBlankTriggerWorkflowNode
                | SimplifiedBranchWorkflowNode
                | SimplifiedContactPropertyTriggerWorkflowNode
                | SimplifiedEventTriggerWorkflowNode
                | SimplifiedExitActionWorkflowNode
                | SimplifiedExperimentBranchWorkflowNode
                | SimplifiedSendEmailActionWorkflowNode
                | SimplifiedSignupTriggerWorkflowNode
                | SimplifiedTimerActionWorkflowNode
                | SimplifiedVariantWorkflowNode
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_0 = SimplifiedSignupTriggerWorkflowNode.from_dict(
                        data
                    )

                    return componentsschemas_simplified_workflow_node_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_1 = SimplifiedEventTriggerWorkflowNode.from_dict(
                        data
                    )

                    return componentsschemas_simplified_workflow_node_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_2 = (
                        SimplifiedContactPropertyTriggerWorkflowNode.from_dict(data)
                    )

                    return componentsschemas_simplified_workflow_node_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_3 = (
                        SimplifiedAddToListTriggerWorkflowNode.from_dict(data)
                    )

                    return componentsschemas_simplified_workflow_node_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_4 = SimplifiedBlankTriggerWorkflowNode.from_dict(
                        data
                    )

                    return componentsschemas_simplified_workflow_node_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_5 = SimplifiedAudienceFilterWorkflowNode.from_dict(
                        data
                    )

                    return componentsschemas_simplified_workflow_node_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_6 = SimplifiedTimerActionWorkflowNode.from_dict(
                        data
                    )

                    return componentsschemas_simplified_workflow_node_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_7 = SimplifiedSendEmailActionWorkflowNode.from_dict(
                        data
                    )

                    return componentsschemas_simplified_workflow_node_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_8 = SimplifiedExitActionWorkflowNode.from_dict(data)

                    return componentsschemas_simplified_workflow_node_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_9 = SimplifiedBranchWorkflowNode.from_dict(data)

                    return componentsschemas_simplified_workflow_node_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_simplified_workflow_node_type_10 = (
                        SimplifiedExperimentBranchWorkflowNode.from_dict(data)
                    )

                    return componentsschemas_simplified_workflow_node_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_simplified_workflow_node_type_11 = SimplifiedVariantWorkflowNode.from_dict(data)

                return componentsschemas_simplified_workflow_node_type_11

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        simplified_workflow_nodes.additional_properties = additional_properties
        return simplified_workflow_nodes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> (
        SimplifiedAddToListTriggerWorkflowNode
        | SimplifiedAudienceFilterWorkflowNode
        | SimplifiedBlankTriggerWorkflowNode
        | SimplifiedBranchWorkflowNode
        | SimplifiedContactPropertyTriggerWorkflowNode
        | SimplifiedEventTriggerWorkflowNode
        | SimplifiedExitActionWorkflowNode
        | SimplifiedExperimentBranchWorkflowNode
        | SimplifiedSendEmailActionWorkflowNode
        | SimplifiedSignupTriggerWorkflowNode
        | SimplifiedTimerActionWorkflowNode
        | SimplifiedVariantWorkflowNode
    ):
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: SimplifiedAddToListTriggerWorkflowNode
        | SimplifiedAudienceFilterWorkflowNode
        | SimplifiedBlankTriggerWorkflowNode
        | SimplifiedBranchWorkflowNode
        | SimplifiedContactPropertyTriggerWorkflowNode
        | SimplifiedEventTriggerWorkflowNode
        | SimplifiedExitActionWorkflowNode
        | SimplifiedExperimentBranchWorkflowNode
        | SimplifiedSendEmailActionWorkflowNode
        | SimplifiedSignupTriggerWorkflowNode
        | SimplifiedTimerActionWorkflowNode
        | SimplifiedVariantWorkflowNode,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
