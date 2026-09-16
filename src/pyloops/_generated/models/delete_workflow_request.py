from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteWorkflowRequest")


@_attrs_define
class DeleteWorkflowRequest:
    """
    Attributes:
        expected_revision_id (None | str): The workflow revision token returned by the latest workflow read or mutation.
            Older workflows may return `null` before their first revision-aware mutation; pass `null` back as
            `expectedRevisionId` in that case. If the token is stale, the API returns a `409 Conflict` error.
        confirm_delete (bool | Unset): Set to `true` after a confirmation-required `409 Conflict` response to confirm
            deleting a sending workflow or a workflow with queued contacts.
    """

    expected_revision_id: None | str
    confirm_delete: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expected_revision_id: None | str
        expected_revision_id = self.expected_revision_id

        confirm_delete = self.confirm_delete

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expectedRevisionId": expected_revision_id,
            }
        )
        if confirm_delete is not UNSET:
            field_dict["confirmDelete"] = confirm_delete

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expected_revision_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expected_revision_id = _parse_expected_revision_id(d.pop("expectedRevisionId"))

        confirm_delete = d.pop("confirmDelete", UNSET)

        delete_workflow_request = cls(
            expected_revision_id=expected_revision_id,
            confirm_delete=confirm_delete,
        )

        return delete_workflow_request
