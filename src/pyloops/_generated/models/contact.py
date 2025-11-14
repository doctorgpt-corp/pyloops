from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_opt_in_status_type_1 import ContactOptInStatusType1
from ..models.contact_opt_in_status_type_2_type_1 import ContactOptInStatusType2Type1
from ..models.contact_opt_in_status_type_3_type_1 import ContactOptInStatusType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_mailing_lists import ContactMailingLists


T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        id (str | Unset):
        email (str | Unset):
        first_name (None | str | Unset):
        last_name (None | str | Unset):
        source (str | Unset):
        subscribed (bool | Unset):
        user_group (str | Unset):
        user_id (None | str | Unset):
        mailing_lists (ContactMailingLists | Unset): An object of mailing list IDs and boolean subscription statuses.
        opt_in_status (ContactOptInStatusType1 | ContactOptInStatusType2Type1 | ContactOptInStatusType3Type1 | None |
            Unset): Double opt-in status.
    """

    id: str | Unset = UNSET
    email: str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    source: str | Unset = UNSET
    subscribed: bool | Unset = UNSET
    user_group: str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    mailing_lists: ContactMailingLists | Unset = UNSET
    opt_in_status: (
        ContactOptInStatusType1 | ContactOptInStatusType2Type1 | ContactOptInStatusType3Type1 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        source = self.source

        subscribed = self.subscribed

        user_group = self.user_group

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        mailing_lists: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mailing_lists, Unset):
            mailing_lists = self.mailing_lists.to_dict()

        opt_in_status: None | str | Unset
        if isinstance(self.opt_in_status, Unset):
            opt_in_status = UNSET
        elif isinstance(self.opt_in_status, ContactOptInStatusType1):
            opt_in_status = self.opt_in_status.value
        elif isinstance(self.opt_in_status, ContactOptInStatusType2Type1):
            opt_in_status = self.opt_in_status.value
        elif isinstance(self.opt_in_status, ContactOptInStatusType3Type1):
            opt_in_status = self.opt_in_status.value
        else:
            opt_in_status = self.opt_in_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
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
        if opt_in_status is not UNSET:
            field_dict["optInStatus"] = opt_in_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_mailing_lists import ContactMailingLists

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        source = d.pop("source", UNSET)

        subscribed = d.pop("subscribed", UNSET)

        user_group = d.pop("userGroup", UNSET)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        _mailing_lists = d.pop("mailingLists", UNSET)
        mailing_lists: ContactMailingLists | Unset
        if isinstance(_mailing_lists, Unset):
            mailing_lists = UNSET
        else:
            mailing_lists = ContactMailingLists.from_dict(_mailing_lists)

        def _parse_opt_in_status(
            data: object,
        ) -> ContactOptInStatusType1 | ContactOptInStatusType2Type1 | ContactOptInStatusType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opt_in_status_type_1 = ContactOptInStatusType1(data)

                return opt_in_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opt_in_status_type_2_type_1 = ContactOptInStatusType2Type1(data)

                return opt_in_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opt_in_status_type_3_type_1 = ContactOptInStatusType3Type1(data)

                return opt_in_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ContactOptInStatusType1 | ContactOptInStatusType2Type1 | ContactOptInStatusType3Type1 | None | Unset,
                data,
            )

        opt_in_status = _parse_opt_in_status(d.pop("optInStatus", UNSET))

        contact = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            source=source,
            subscribed=subscribed,
            user_group=user_group,
            user_id=user_id,
            mailing_lists=mailing_lists,
            opt_in_status=opt_in_status,
        )

        contact.additional_properties = d
        return contact

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
