from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_mailing_list_updated_response_status import WorkflowMailingListUpdatedResponseStatus

T = TypeVar("T", bound="WorkflowMailingListUpdatedResponse")


@_attrs_define
class WorkflowMailingListUpdatedResponse:
    """
    Attributes:
        status (WorkflowMailingListUpdatedResponseStatus):
        mailing_list_id (None | str):
        workflow_revision_id (str): The current workflow revision token. Pass the latest value as `expectedRevisionId`
            on the next workflow mutation.
        queued_contact_count (float): The number of queued contacts that were removed from the workflow due to the
            mailing list changing.
        queued_contact_limit_reached (bool): Whether the queued contact limit was reached due to the mailing list
            changing.
    """

    status: WorkflowMailingListUpdatedResponseStatus
    mailing_list_id: None | str
    workflow_revision_id: str
    queued_contact_count: float
    queued_contact_limit_reached: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        mailing_list_id: None | str
        mailing_list_id = self.mailing_list_id

        workflow_revision_id: str
        workflow_revision_id = self.workflow_revision_id

        queued_contact_count = self.queued_contact_count

        queued_contact_limit_reached = self.queued_contact_limit_reached

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "mailingListId": mailing_list_id,
                "workflowRevisionId": workflow_revision_id,
                "queuedContactCount": queued_contact_count,
                "queuedContactLimitReached": queued_contact_limit_reached,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = WorkflowMailingListUpdatedResponseStatus(d.pop("status"))

        def _parse_mailing_list_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mailing_list_id = _parse_mailing_list_id(d.pop("mailingListId"))

        def _parse_workflow_revision_id(data: object) -> str:
            return cast(str, data)

        workflow_revision_id = _parse_workflow_revision_id(d.pop("workflowRevisionId"))

        queued_contact_count = d.pop("queuedContactCount")

        queued_contact_limit_reached = d.pop("queuedContactLimitReached")

        workflow_mailing_list_updated_response = cls(
            status=status,
            mailing_list_id=mailing_list_id,
            workflow_revision_id=workflow_revision_id,
            queued_contact_count=queued_contact_count,
            queued_contact_limit_reached=queued_contact_limit_reached,
        )

        workflow_mailing_list_updated_response.additional_properties = d
        return workflow_mailing_list_updated_response

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
