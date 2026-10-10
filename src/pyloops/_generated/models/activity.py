from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_action import ActivityAction
from ..models.activity_target import ActivityTarget
from ..models.activity_type import ActivityType

T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """Matches contacts by their activity on a campaign or workflow.

    Attributes:
        type_ (ActivityType):
        action (ActivityAction):
        negate (bool):
        target (ActivityTarget):
        id (str): The ID of the campaign, workflow, or workflow email.
    """

    type_: ActivityType
    action: ActivityAction
    negate: bool
    target: ActivityTarget
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        action = self.action.value

        negate = self.negate

        target = self.target.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "action": action,
                "negate": negate,
                "target": target,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ActivityType(d.pop("type"))

        action = ActivityAction(d.pop("action"))

        negate = d.pop("negate")

        target = ActivityTarget(d.pop("target"))

        id = d.pop("id")

        activity = cls(
            type_=type_,
            action=action,
            negate=negate,
            target=target,
            id=id,
        )

        activity.additional_properties = d
        return activity

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
