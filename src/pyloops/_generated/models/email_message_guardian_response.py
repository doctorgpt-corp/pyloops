from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.guardian_rule import GuardianRule


T = TypeVar("T", bound="EmailMessageGuardianResponse")


@_attrs_define
class EmailMessageGuardianResponse:
    """
    Example:
        {'errors': [{'rule': 'missingButtonHrefs', 'title': 'Missing button link', 'description': "Buttons won't work
            without href value", 'items': [{'label': 'Click here'}]}, {'rule': 'missingLinkHrefs', 'title': 'Missing text
            link', 'description': "Links won't work without href value", 'items': [{'label': 'See more'}]}], 'warnings': []}

    Attributes:
        errors (list[GuardianRule]): Validation errors. These must be resolved before the email can be published.
        warnings (list[GuardianRule]): Validation warnings. These are advisory and do not block publishing.
    """

    errors: list[GuardianRule]
    warnings: list[GuardianRule]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)

        warnings = []
        for warnings_item_data in self.warnings:
            warnings_item = warnings_item_data.to_dict()
            warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errors": errors,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guardian_rule import GuardianRule

        d = dict(src_dict)
        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:
            errors_item = GuardianRule.from_dict(errors_item_data)

            errors.append(errors_item)

        warnings = []
        _warnings = d.pop("warnings")
        for warnings_item_data in _warnings:
            warnings_item = GuardianRule.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        email_message_guardian_response = cls(
            errors=errors,
            warnings=warnings,
        )

        email_message_guardian_response.additional_properties = d
        return email_message_guardian_response

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
