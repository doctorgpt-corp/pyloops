from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mailing_list_opt_in_status_type_1 import MailingListOptInStatusType1
from ..models.mailing_list_opt_in_status_type_2_type_1 import MailingListOptInStatusType2Type1
from ..models.mailing_list_opt_in_status_type_3_type_1 import MailingListOptInStatusType3Type1
from ..models.mailing_list_opt_in_type import MailingListOptInType

T = TypeVar("T", bound="MailingListOptIn")


@_attrs_define
class MailingListOptIn:
    """Matches contacts by mailing list opt-in status.

    Attributes:
        type_ (MailingListOptInType):
        status (MailingListOptInStatusType1 | MailingListOptInStatusType2Type1 | MailingListOptInStatusType3Type1 |
            None):
    """

    type_: MailingListOptInType
    status: MailingListOptInStatusType1 | MailingListOptInStatusType2Type1 | MailingListOptInStatusType3Type1 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        status: None | str
        if isinstance(self.status, MailingListOptInStatusType1):
            status = self.status.value
        elif isinstance(self.status, MailingListOptInStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, MailingListOptInStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = MailingListOptInType(d.pop("type"))

        def _parse_status(
            data: object,
        ) -> MailingListOptInStatusType1 | MailingListOptInStatusType2Type1 | MailingListOptInStatusType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = MailingListOptInStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = MailingListOptInStatusType2Type1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = MailingListOptInStatusType3Type1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                MailingListOptInStatusType1
                | MailingListOptInStatusType2Type1
                | MailingListOptInStatusType3Type1
                | None,
                data,
            )

        status = _parse_status(d.pop("status"))

        mailing_list_opt_in = cls(
            type_=type_,
            status=status,
        )

        mailing_list_opt_in.additional_properties = d
        return mailing_list_opt_in

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
