from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_request_event_properties import EventRequestEventProperties
    from ..models.event_request_mailing_lists import EventRequestMailingLists


T = TypeVar("T", bound="EventRequest")


@_attrs_define
class EventRequest:
    """
    Attributes:
        event_name (str):
        email (str | Unset):
        user_id (str | Unset):
        event_properties (EventRequestEventProperties | Unset): An object containing event property data for the event,
            available in emails sent by the event.
        mailing_lists (EventRequestMailingLists | Unset): An object of mailing list IDs and boolean subscription
            statuses.
    """

    event_name: str
    email: str | Unset = UNSET
    user_id: str | Unset = UNSET
    event_properties: EventRequestEventProperties | Unset = UNSET
    mailing_lists: EventRequestMailingLists | Unset = UNSET
    additional_properties: dict[str, bool | float | str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        email = self.email

        user_id = self.user_id

        event_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_properties, Unset):
            event_properties = self.event_properties.to_dict()

        mailing_lists: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mailing_lists, Unset):
            mailing_lists = self.mailing_lists.to_dict()

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        field_dict.update(
            {
                "eventName": event_name,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if event_properties is not UNSET:
            field_dict["eventProperties"] = event_properties
        if mailing_lists is not UNSET:
            field_dict["mailingLists"] = mailing_lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_request_event_properties import EventRequestEventProperties
        from ..models.event_request_mailing_lists import EventRequestMailingLists

        d = dict(src_dict)
        event_name = d.pop("eventName")

        email = d.pop("email", UNSET)

        user_id = d.pop("userId", UNSET)

        _event_properties = d.pop("eventProperties", UNSET)
        event_properties: EventRequestEventProperties | Unset
        if isinstance(_event_properties, Unset):
            event_properties = UNSET
        else:
            event_properties = EventRequestEventProperties.from_dict(_event_properties)

        _mailing_lists = d.pop("mailingLists", UNSET)
        mailing_lists: EventRequestMailingLists | Unset
        if isinstance(_mailing_lists, Unset):
            mailing_lists = UNSET
        else:
            mailing_lists = EventRequestMailingLists.from_dict(_mailing_lists)

        event_request = cls(
            event_name=event_name,
            email=email,
            user_id=user_id,
            event_properties=event_properties,
            mailing_lists=mailing_lists,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> bool | float | str:
                return cast(bool | float | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        event_request.additional_properties = additional_properties
        return event_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> bool | float | str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: bool | float | str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
