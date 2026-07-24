from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.add_to_list_trigger_workflow_mutation_node_with_revision import (
        AddToListTriggerWorkflowMutationNodeWithRevision,
    )
    from ..models.audience_filter_workflow_mutation_node_with_revision import (
        AudienceFilterWorkflowMutationNodeWithRevision,
    )
    from ..models.blank_trigger_workflow_mutation_node_with_revision import BlankTriggerWorkflowMutationNodeWithRevision
    from ..models.branch_workflow_mutation_node_with_revision import BranchWorkflowMutationNodeWithRevision
    from ..models.contact_property_trigger_workflow_mutation_node_with_revision import (
        ContactPropertyTriggerWorkflowMutationNodeWithRevision,
    )
    from ..models.event_trigger_workflow_mutation_node_with_revision import EventTriggerWorkflowMutationNodeWithRevision
    from ..models.exit_action_workflow_mutation_node_with_revision import ExitActionWorkflowMutationNodeWithRevision
    from ..models.experiment_branch_workflow_mutation_node_with_revision import (
        ExperimentBranchWorkflowMutationNodeWithRevision,
    )
    from ..models.send_email_action_workflow_mutation_node_with_revision import (
        SendEmailActionWorkflowMutationNodeWithRevision,
    )
    from ..models.signup_trigger_workflow_mutation_node_with_revision import (
        SignupTriggerWorkflowMutationNodeWithRevision,
    )
    from ..models.simplified_workflow import SimplifiedWorkflow
    from ..models.timer_action_workflow_mutation_node_with_revision import TimerActionWorkflowMutationNodeWithRevision
    from ..models.variant_workflow_mutation_node_with_revision import VariantWorkflowMutationNodeWithRevision


T = TypeVar("T", bound="AddWorkflowBranchResponse")


@_attrs_define
class AddWorkflowBranchResponse:
    """
    Attributes:
        node (AddToListTriggerWorkflowMutationNodeWithRevision | AudienceFilterWorkflowMutationNodeWithRevision |
            BlankTriggerWorkflowMutationNodeWithRevision | BranchWorkflowMutationNodeWithRevision |
            ContactPropertyTriggerWorkflowMutationNodeWithRevision | EventTriggerWorkflowMutationNodeWithRevision |
            ExitActionWorkflowMutationNodeWithRevision | ExperimentBranchWorkflowMutationNodeWithRevision |
            SendEmailActionWorkflowMutationNodeWithRevision | SignupTriggerWorkflowMutationNodeWithRevision |
            TimerActionWorkflowMutationNodeWithRevision | VariantWorkflowMutationNodeWithRevision): Detailed workflow node
            returned from a mutation, plus the latest workflow revision token.
        workflow (SimplifiedWorkflow):
    """

    node: (
        AddToListTriggerWorkflowMutationNodeWithRevision
        | AudienceFilterWorkflowMutationNodeWithRevision
        | BlankTriggerWorkflowMutationNodeWithRevision
        | BranchWorkflowMutationNodeWithRevision
        | ContactPropertyTriggerWorkflowMutationNodeWithRevision
        | EventTriggerWorkflowMutationNodeWithRevision
        | ExitActionWorkflowMutationNodeWithRevision
        | ExperimentBranchWorkflowMutationNodeWithRevision
        | SendEmailActionWorkflowMutationNodeWithRevision
        | SignupTriggerWorkflowMutationNodeWithRevision
        | TimerActionWorkflowMutationNodeWithRevision
        | VariantWorkflowMutationNodeWithRevision
    )
    workflow: SimplifiedWorkflow

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_to_list_trigger_workflow_mutation_node_with_revision import (
            AddToListTriggerWorkflowMutationNodeWithRevision,
        )
        from ..models.audience_filter_workflow_mutation_node_with_revision import (
            AudienceFilterWorkflowMutationNodeWithRevision,
        )
        from ..models.blank_trigger_workflow_mutation_node_with_revision import (
            BlankTriggerWorkflowMutationNodeWithRevision,
        )
        from ..models.branch_workflow_mutation_node_with_revision import BranchWorkflowMutationNodeWithRevision
        from ..models.contact_property_trigger_workflow_mutation_node_with_revision import (
            ContactPropertyTriggerWorkflowMutationNodeWithRevision,
        )
        from ..models.event_trigger_workflow_mutation_node_with_revision import (
            EventTriggerWorkflowMutationNodeWithRevision,
        )
        from ..models.exit_action_workflow_mutation_node_with_revision import ExitActionWorkflowMutationNodeWithRevision
        from ..models.experiment_branch_workflow_mutation_node_with_revision import (
            ExperimentBranchWorkflowMutationNodeWithRevision,
        )
        from ..models.send_email_action_workflow_mutation_node_with_revision import (
            SendEmailActionWorkflowMutationNodeWithRevision,
        )
        from ..models.signup_trigger_workflow_mutation_node_with_revision import (
            SignupTriggerWorkflowMutationNodeWithRevision,
        )
        from ..models.timer_action_workflow_mutation_node_with_revision import (
            TimerActionWorkflowMutationNodeWithRevision,
        )

        node: dict[str, Any]
        if isinstance(self.node, SignupTriggerWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        elif isinstance(self.node, EventTriggerWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        elif isinstance(self.node, ContactPropertyTriggerWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        elif isinstance(self.node, AddToListTriggerWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        elif isinstance(self.node, BlankTriggerWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        elif isinstance(self.node, AudienceFilterWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        elif isinstance(self.node, TimerActionWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        elif isinstance(self.node, SendEmailActionWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        elif isinstance(self.node, ExitActionWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        elif isinstance(self.node, BranchWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        elif isinstance(self.node, ExperimentBranchWorkflowMutationNodeWithRevision):
            node = self.node.to_dict()
        else:
            node = self.node.to_dict()

        workflow = self.workflow.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "node": node,
                "workflow": workflow,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_to_list_trigger_workflow_mutation_node_with_revision import (
            AddToListTriggerWorkflowMutationNodeWithRevision,
        )
        from ..models.audience_filter_workflow_mutation_node_with_revision import (
            AudienceFilterWorkflowMutationNodeWithRevision,
        )
        from ..models.blank_trigger_workflow_mutation_node_with_revision import (
            BlankTriggerWorkflowMutationNodeWithRevision,
        )
        from ..models.branch_workflow_mutation_node_with_revision import BranchWorkflowMutationNodeWithRevision
        from ..models.contact_property_trigger_workflow_mutation_node_with_revision import (
            ContactPropertyTriggerWorkflowMutationNodeWithRevision,
        )
        from ..models.event_trigger_workflow_mutation_node_with_revision import (
            EventTriggerWorkflowMutationNodeWithRevision,
        )
        from ..models.exit_action_workflow_mutation_node_with_revision import ExitActionWorkflowMutationNodeWithRevision
        from ..models.experiment_branch_workflow_mutation_node_with_revision import (
            ExperimentBranchWorkflowMutationNodeWithRevision,
        )
        from ..models.send_email_action_workflow_mutation_node_with_revision import (
            SendEmailActionWorkflowMutationNodeWithRevision,
        )
        from ..models.signup_trigger_workflow_mutation_node_with_revision import (
            SignupTriggerWorkflowMutationNodeWithRevision,
        )
        from ..models.simplified_workflow import SimplifiedWorkflow
        from ..models.timer_action_workflow_mutation_node_with_revision import (
            TimerActionWorkflowMutationNodeWithRevision,
        )
        from ..models.variant_workflow_mutation_node_with_revision import VariantWorkflowMutationNodeWithRevision

        d = dict(src_dict)

        def _parse_node(
            data: object,
        ) -> (
            AddToListTriggerWorkflowMutationNodeWithRevision
            | AudienceFilterWorkflowMutationNodeWithRevision
            | BlankTriggerWorkflowMutationNodeWithRevision
            | BranchWorkflowMutationNodeWithRevision
            | ContactPropertyTriggerWorkflowMutationNodeWithRevision
            | EventTriggerWorkflowMutationNodeWithRevision
            | ExitActionWorkflowMutationNodeWithRevision
            | ExperimentBranchWorkflowMutationNodeWithRevision
            | SendEmailActionWorkflowMutationNodeWithRevision
            | SignupTriggerWorkflowMutationNodeWithRevision
            | TimerActionWorkflowMutationNodeWithRevision
            | VariantWorkflowMutationNodeWithRevision
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_0 = (
                    SignupTriggerWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_1 = (
                    EventTriggerWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_2 = (
                    ContactPropertyTriggerWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_3 = (
                    AddToListTriggerWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_4 = (
                    BlankTriggerWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_5 = (
                    AudienceFilterWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_6 = (
                    TimerActionWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_7 = (
                    SendEmailActionWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_8 = (
                    ExitActionWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_9 = (
                    BranchWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_workflow_mutation_node_with_revision_type_10 = (
                    ExperimentBranchWorkflowMutationNodeWithRevision.from_dict(data)
                )

                return componentsschemas_workflow_mutation_node_with_revision_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_workflow_mutation_node_with_revision_type_11 = (
                VariantWorkflowMutationNodeWithRevision.from_dict(data)
            )

            return componentsschemas_workflow_mutation_node_with_revision_type_11

        node = _parse_node(d.pop("node"))

        workflow = SimplifiedWorkflow.from_dict(d.pop("workflow"))

        add_workflow_branch_response = cls(
            node=node,
            workflow=workflow,
        )

        return add_workflow_branch_response
