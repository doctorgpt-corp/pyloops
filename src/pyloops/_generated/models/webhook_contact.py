from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_contact_opt_in_status_type_1 import WebhookContactOptInStatusType1
from ..models.webhook_contact_opt_in_status_type_2_type_1 import WebhookContactOptInStatusType2Type1
from ..models.webhook_contact_opt_in_status_type_3_type_1 import WebhookContactOptInStatusType3Type1
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_contact_mailing_lists import WebhookContactMailingLists


T = TypeVar("T", bound="WebhookContact")


@_attrs_define
class WebhookContact:
    """Full contact object, including custom properties.

    Attributes:
        id (str):
        email (str):
        first_name (None | str):
        last_name (None | str):
        source (str):
        subscribed (bool):
        user_group (str):
        user_id (None | str):
        mailing_lists (WebhookContactMailingLists): An object of mailing list IDs and boolean subscription statuses.
        opt_in_status (None | WebhookContactOptInStatusType1 | WebhookContactOptInStatusType2Type1 |
            WebhookContactOptInStatusType3Type1): Double opt-in status.
        notes (None | str | Unset):
    """

    id: str
    email: str
    first_name: None | str
    last_name: None | str
    source: str
    subscribed: bool
    user_group: str
    user_id: None | str
    mailing_lists: WebhookContactMailingLists
    opt_in_status: (
        None
        | WebhookContactOptInStatusType1
        | WebhookContactOptInStatusType2Type1
        | WebhookContactOptInStatusType3Type1
    )
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name: None | str
        first_name = self.first_name

        last_name: None | str
        last_name = self.last_name

        source = self.source

        subscribed = self.subscribed

        user_group = self.user_group

        user_id: None | str
        user_id = self.user_id

        mailing_lists = self.mailing_lists.to_dict()

        opt_in_status: None | str
        if isinstance(self.opt_in_status, WebhookContactOptInStatusType1):
            opt_in_status = self.opt_in_status.value
        elif isinstance(self.opt_in_status, WebhookContactOptInStatusType2Type1):
            opt_in_status = self.opt_in_status.value
        elif isinstance(self.opt_in_status, WebhookContactOptInStatusType3Type1):
            opt_in_status = self.opt_in_status.value
        else:
            opt_in_status = self.opt_in_status

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "source": source,
                "subscribed": subscribed,
                "userGroup": user_group,
                "userId": user_id,
                "mailingLists": mailing_lists,
                "optInStatus": opt_in_status,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_contact_mailing_lists import WebhookContactMailingLists

        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("firstName"))

        def _parse_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_name = _parse_last_name(d.pop("lastName"))

        source = d.pop("source")

        subscribed = d.pop("subscribed")

        user_group = d.pop("userGroup")

        def _parse_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        user_id = _parse_user_id(d.pop("userId"))

        mailing_lists = WebhookContactMailingLists.from_dict(d.pop("mailingLists"))

        def _parse_opt_in_status(
            data: object,
        ) -> (
            None
            | WebhookContactOptInStatusType1
            | WebhookContactOptInStatusType2Type1
            | WebhookContactOptInStatusType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opt_in_status_type_1 = WebhookContactOptInStatusType1(data)

                return opt_in_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opt_in_status_type_2_type_1 = WebhookContactOptInStatusType2Type1(data)

                return opt_in_status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opt_in_status_type_3_type_1 = WebhookContactOptInStatusType3Type1(data)

                return opt_in_status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | WebhookContactOptInStatusType1
                | WebhookContactOptInStatusType2Type1
                | WebhookContactOptInStatusType3Type1,
                data,
            )

        opt_in_status = _parse_opt_in_status(d.pop("optInStatus"))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        webhook_contact = cls(
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
            notes=notes,
        )

        webhook_contact.additional_properties = d
        return webhook_contact

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
