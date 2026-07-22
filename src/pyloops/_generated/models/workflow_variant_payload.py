from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowVariantPayload")


@_attrs_define
class WorkflowVariantPayload:
    """Configuration for the variant node.

    Attributes:
        is_control (bool | Unset): Use `true` to set this variant as the control of the experiment. This will set
            `false` on the existing control, if one exists. Experiments do not require a control variant.
    """

    is_control: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_control = self.is_control

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_control is not UNSET:
            field_dict["isControl"] = is_control

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_control = d.pop("isControl", UNSET)

        workflow_variant_payload = cls(
            is_control=is_control,
        )

        return workflow_variant_payload
