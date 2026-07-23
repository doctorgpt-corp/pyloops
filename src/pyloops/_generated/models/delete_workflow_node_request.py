from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.workflow_queued_contact_policy import WorkflowQueuedContactPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteWorkflowNodeRequest")


@_attrs_define
class DeleteWorkflowNodeRequest:
    """
    Attributes:
        expected_revision_id (None | str): The workflow revision token returned by the latest workflow read or mutation.
            Older workflows may return `null` before their first revision-aware mutation; pass `null` back as
            `expectedRevisionId` in that case. If the token is stale, the API returns a `409 Conflict` error.
        dry_run (bool | Unset): If `true`, the request will be validated but the workflow will not be modified.
        queued_contact_policy (WorkflowQueuedContactPolicy | Unset): `fail` returns queued-contact impact instead of
            mutating. `discard` confirms that matching queued contacts should be discarded. Defaults to `fail` when omitted.
    """

    expected_revision_id: None | str
    dry_run: bool | Unset = UNSET
    queued_contact_policy: WorkflowQueuedContactPolicy | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expected_revision_id: None | str
        expected_revision_id = self.expected_revision_id

        dry_run = self.dry_run

        queued_contact_policy: str | Unset = UNSET
        if not isinstance(self.queued_contact_policy, Unset):
            queued_contact_policy = self.queued_contact_policy.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expectedRevisionId": expected_revision_id,
            }
        )
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if queued_contact_policy is not UNSET:
            field_dict["queuedContactPolicy"] = queued_contact_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expected_revision_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expected_revision_id = _parse_expected_revision_id(d.pop("expectedRevisionId"))

        dry_run = d.pop("dryRun", UNSET)

        _queued_contact_policy = d.pop("queuedContactPolicy", UNSET)
        queued_contact_policy: WorkflowQueuedContactPolicy | Unset
        if isinstance(_queued_contact_policy, Unset):
            queued_contact_policy = UNSET
        else:
            queued_contact_policy = WorkflowQueuedContactPolicy(_queued_contact_policy)

        delete_workflow_node_request = cls(
            expected_revision_id=expected_revision_id,
            dry_run=dry_run,
            queued_contact_policy=queued_contact_policy,
        )

        return delete_workflow_node_request
