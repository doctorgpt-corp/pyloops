from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.workflow_add_to_list_trigger_payload import WorkflowAddToListTriggerPayload
    from ..models.workflow_audience_filter_payload import WorkflowAudienceFilterPayload
    from ..models.workflow_contact_property_trigger_payload import WorkflowContactPropertyTriggerPayload
    from ..models.workflow_event_trigger_payload import WorkflowEventTriggerPayload
    from ..models.workflow_experiment_branch_payload import WorkflowExperimentBranchPayload
    from ..models.workflow_signup_trigger_payload import WorkflowSignupTriggerPayload
    from ..models.workflow_timer_action_payload import WorkflowTimerActionPayload
    from ..models.workflow_variant_payload import WorkflowVariantPayload


T = TypeVar("T", bound="UpdateWorkflowNodeRequest")


@_attrs_define
class UpdateWorkflowNodeRequest:
    """
    Attributes:
        expected_revision_id (None | str): The workflow revision token returned by the latest workflow read or mutation.
            Older workflows may return `null` before their first revision-aware mutation; pass `null` back as
            `expectedRevisionId` in that case. If the token is stale, the API returns a `409 Conflict` error.
        payload (WorkflowAddToListTriggerPayload | WorkflowAudienceFilterPayload | WorkflowContactPropertyTriggerPayload
            | WorkflowEventTriggerPayload | WorkflowExperimentBranchPayload | WorkflowSignupTriggerPayload |
            WorkflowTimerActionPayload | WorkflowVariantPayload): Node-type-specific fields to update. The allowed fields
            depend on the existing node type. Trigger node updates may include `typeName` when changing one trigger node
            type to another trigger node type.
    """

    expected_revision_id: None | str
    payload: (
        WorkflowAddToListTriggerPayload
        | WorkflowAudienceFilterPayload
        | WorkflowContactPropertyTriggerPayload
        | WorkflowEventTriggerPayload
        | WorkflowExperimentBranchPayload
        | WorkflowSignupTriggerPayload
        | WorkflowTimerActionPayload
        | WorkflowVariantPayload
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_add_to_list_trigger_payload import WorkflowAddToListTriggerPayload  # noqa: PLC0415
        from ..models.workflow_audience_filter_payload import WorkflowAudienceFilterPayload  # noqa: PLC0415
        from ..models.workflow_contact_property_trigger_payload import (
            WorkflowContactPropertyTriggerPayload,  # noqa: PLC0415
        )
        from ..models.workflow_event_trigger_payload import WorkflowEventTriggerPayload  # noqa: PLC0415
        from ..models.workflow_experiment_branch_payload import WorkflowExperimentBranchPayload  # noqa: PLC0415
        from ..models.workflow_signup_trigger_payload import WorkflowSignupTriggerPayload  # noqa: PLC0415
        from ..models.workflow_timer_action_payload import WorkflowTimerActionPayload  # noqa: PLC0415

        expected_revision_id: None | str
        expected_revision_id = self.expected_revision_id

        payload: dict[str, Any]
        if isinstance(self.payload, WorkflowSignupTriggerPayload):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, WorkflowEventTriggerPayload):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, WorkflowContactPropertyTriggerPayload):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, WorkflowAddToListTriggerPayload):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, WorkflowAudienceFilterPayload):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, WorkflowTimerActionPayload):
            payload = self.payload.to_dict()
        elif isinstance(self.payload, WorkflowExperimentBranchPayload):
            payload = self.payload.to_dict()
        else:
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expectedRevisionId": expected_revision_id,
                "payload": payload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_add_to_list_trigger_payload import WorkflowAddToListTriggerPayload  # noqa: PLC0415
        from ..models.workflow_audience_filter_payload import WorkflowAudienceFilterPayload  # noqa: PLC0415
        from ..models.workflow_contact_property_trigger_payload import (
            WorkflowContactPropertyTriggerPayload,  # noqa: PLC0415
        )
        from ..models.workflow_event_trigger_payload import WorkflowEventTriggerPayload  # noqa: PLC0415
        from ..models.workflow_experiment_branch_payload import WorkflowExperimentBranchPayload  # noqa: PLC0415
        from ..models.workflow_signup_trigger_payload import WorkflowSignupTriggerPayload  # noqa: PLC0415
        from ..models.workflow_timer_action_payload import WorkflowTimerActionPayload  # noqa: PLC0415
        from ..models.workflow_variant_payload import WorkflowVariantPayload  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_expected_revision_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expected_revision_id = _parse_expected_revision_id(d.pop("expectedRevisionId"))

        def _parse_payload(
            data: object,
        ) -> (
            WorkflowAddToListTriggerPayload
            | WorkflowAudienceFilterPayload
            | WorkflowContactPropertyTriggerPayload
            | WorkflowEventTriggerPayload
            | WorkflowExperimentBranchPayload
            | WorkflowSignupTriggerPayload
            | WorkflowTimerActionPayload
            | WorkflowVariantPayload
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_payload_type_0 = WorkflowSignupTriggerPayload.from_dict(data)

                return componentsschemas_update_workflow_node_payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_payload_type_1 = WorkflowEventTriggerPayload.from_dict(data)

                return componentsschemas_update_workflow_node_payload_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_payload_type_2 = WorkflowContactPropertyTriggerPayload.from_dict(
                    data
                )

                return componentsschemas_update_workflow_node_payload_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_payload_type_3 = WorkflowAddToListTriggerPayload.from_dict(data)

                return componentsschemas_update_workflow_node_payload_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_payload_type_4 = WorkflowAudienceFilterPayload.from_dict(data)

                return componentsschemas_update_workflow_node_payload_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_payload_type_5 = WorkflowTimerActionPayload.from_dict(data)

                return componentsschemas_update_workflow_node_payload_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_update_workflow_node_payload_type_6 = WorkflowExperimentBranchPayload.from_dict(data)

                return componentsschemas_update_workflow_node_payload_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_update_workflow_node_payload_type_7 = WorkflowVariantPayload.from_dict(data)

            return componentsschemas_update_workflow_node_payload_type_7

        payload = _parse_payload(d.pop("payload"))

        update_workflow_node_request = cls(
            expected_revision_id=expected_revision_id,
            payload=payload,
        )

        return update_workflow_node_request
