from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mailing_list_subscriptions import MailingListSubscriptions


T = TypeVar("T", bound="ContactUpdateRequest")


@_attrs_define
class ContactUpdateRequest:
    """
    Attributes:
        email (str | Unset): The contact's email address. **Required if `userId` is not provided.**
        first_name (str | Unset): The contact's first name.
        last_name (str | Unset): The contact's last name.
        source (str | Unset): A custom source value to replace the default “API”.
        subscribed (bool | Unset): Whether the contact will receive campaign and workflow emails. We recommend leaving
            this field out of your update requests unless you specifically want to unsubscribe (`false`) or re-subscribe
            (`true`) a contact. All new contacts are subscribed by default.
        user_group (str | Unset): The contact's user group.
        user_id (str | Unset): The contact's unique user ID. **Required if `email` is not provided.**
        mailing_lists (MailingListSubscriptions | Unset): Manage mailing list subscriptions.

            Include key-value pairs of mailing list IDs and a `boolean` denoting if the contact should be added (`true`) or
            removed (`false`) from the list.
    """

    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    source: str | Unset = UNSET
    subscribed: bool | Unset = UNSET
    user_group: str | Unset = UNSET
    user_id: str | Unset = UNSET
    mailing_lists: MailingListSubscriptions | Unset = UNSET
    additional_properties: dict[str, bool | float | str] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        source = self.source

        subscribed = self.subscribed

        user_group = self.user_group

        user_id = self.user_id

        mailing_lists: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mailing_lists, Unset):
            mailing_lists = self.mailing_lists.to_dict()

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if source is not UNSET:
            field_dict["source"] = source
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed
        if user_group is not UNSET:
            field_dict["userGroup"] = user_group
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if mailing_lists is not UNSET:
            field_dict["mailingLists"] = mailing_lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mailing_list_subscriptions import MailingListSubscriptions

        d = dict(src_dict)
        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        source = d.pop("source", UNSET)

        subscribed = d.pop("subscribed", UNSET)

        user_group = d.pop("userGroup", UNSET)

        user_id = d.pop("userId", UNSET)

        _mailing_lists = d.pop("mailingLists", UNSET)
        mailing_lists: MailingListSubscriptions | Unset
        if isinstance(_mailing_lists, Unset):
            mailing_lists = UNSET
        else:
            mailing_lists = MailingListSubscriptions.from_dict(_mailing_lists)

        contact_update_request = cls(
            email=email,
            first_name=first_name,
            last_name=last_name,
            source=source,
            subscribed=subscribed,
            user_group=user_group,
            user_id=user_id,
            mailing_lists=mailing_lists,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> bool | float | str:
                return cast(bool | float | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        contact_update_request.additional_properties = additional_properties
        return contact_update_request

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
