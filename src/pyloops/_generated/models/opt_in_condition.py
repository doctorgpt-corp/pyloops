from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.opt_in_condition_status_type_1 import OptInConditionStatusType1
from ..models.opt_in_condition_status_type_2_type_1 import OptInConditionStatusType2Type1
from ..models.opt_in_condition_status_type_3_type_1 import OptInConditionStatusType3Type1
from ..models.opt_in_condition_type import OptInConditionType

T = TypeVar("T", bound="OptInCondition")


@_attrs_define
class OptInCondition:
    """Matches contacts by mailing-list opt-in status.

    Attributes:
        type_ (OptInConditionType):
        status (None | OptInConditionStatusType1 | OptInConditionStatusType2Type1 | OptInConditionStatusType3Type1):
    """

    type_: OptInConditionType
    status: None | OptInConditionStatusType1 | OptInConditionStatusType2Type1 | OptInConditionStatusType3Type1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        status: None | str
        if isinstance(self.status, OptInConditionStatusType1):
            status = self.status.value
        elif isinstance(self.status, OptInConditionStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, OptInConditionStatusType3Type1):
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
        type_ = OptInConditionType(d.pop("type"))

        def _parse_status(
            data: object,
        ) -> None | OptInConditionStatusType1 | OptInConditionStatusType2Type1 | OptInConditionStatusType3Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = OptInConditionStatusType1(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = OptInConditionStatusType2Type1(data)

                return status_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = OptInConditionStatusType3Type1(data)

                return status_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None | OptInConditionStatusType1 | OptInConditionStatusType2Type1 | OptInConditionStatusType3Type1, data
            )

        status = _parse_status(d.pop("status"))

        opt_in_condition = cls(
            type_=type_,
            status=status,
        )

        opt_in_condition.additional_properties = d
        return opt_in_condition

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
