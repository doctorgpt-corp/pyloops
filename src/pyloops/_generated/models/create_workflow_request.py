from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWorkflowRequest")


@_attrs_define
class CreateWorkflowRequest:
    """
    Attributes:
        name (str): The name of the workflow.
        description (str | Unset): The description of the workflow.
        mailing_list_id (None | str | Unset): The ID of a mailing list the workflow sends to. After creation, the
            mailing list can be changed with the `/v1/workflows/{workflowId}/mailing-list` endpoint.
    """

    name: str
    description: str | Unset = UNSET
    mailing_list_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        mailing_list_id: None | str | Unset
        if isinstance(self.mailing_list_id, Unset):
            mailing_list_id = UNSET
        else:
            mailing_list_id = self.mailing_list_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if mailing_list_id is not UNSET:
            field_dict["mailingListId"] = mailing_list_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        def _parse_mailing_list_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mailing_list_id = _parse_mailing_list_id(d.pop("mailingListId", UNSET))

        create_workflow_request = cls(
            name=name,
            description=description,
            mailing_list_id=mailing_list_id,
        )

        return create_workflow_request
