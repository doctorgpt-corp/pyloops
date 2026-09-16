from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.property_condition_operator import PropertyConditionOperator
from ..models.property_condition_type import PropertyConditionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_condition_value_type_2 import PropertyConditionValueType2


T = TypeVar("T", bound="PropertyCondition")


@_attrs_define
class PropertyCondition:
    """Matches contacts by a property value.

    Attributes:
        type_ (PropertyConditionType):
        key (str): The contact property name.
        operator (PropertyConditionOperator):
        value (float | PropertyConditionValueType2 | str | Unset): The comparison value. Omitted for value-less
            operators (e.g. `isTrue`, `empty`). A `{ from, to }` object for `between`.
    """

    type_: PropertyConditionType
    key: str
    operator: PropertyConditionOperator
    value: float | PropertyConditionValueType2 | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.property_condition_value_type_2 import PropertyConditionValueType2  # noqa: PLC0415

        type_ = self.type_.value

        key = self.key

        operator = self.operator.value

        value: dict[str, Any] | float | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, PropertyConditionValueType2):
            value = self.value.to_dict()
        else:
            value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "key": key,
                "operator": operator,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.property_condition_value_type_2 import PropertyConditionValueType2  # noqa: PLC0415

        d = dict(src_dict)
        type_ = PropertyConditionType(d.pop("type"))

        key = d.pop("key")

        operator = PropertyConditionOperator(d.pop("operator"))

        def _parse_value(data: object) -> float | PropertyConditionValueType2 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_2 = PropertyConditionValueType2.from_dict(data)

                return value_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | PropertyConditionValueType2 | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        property_condition = cls(
            type_=type_,
            key=key,
            operator=operator,
            value=value,
        )

        property_condition.additional_properties = d
        return property_condition

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
