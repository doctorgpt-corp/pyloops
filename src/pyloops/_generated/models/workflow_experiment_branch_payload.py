from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowExperimentBranchPayload")


@_attrs_define
class WorkflowExperimentBranchPayload:
    """Configuration for the experiment branch node.

    Attributes:
        sampling_rate (float | Unset): The percentage of contacts that will be sent to variant branches, between `0` and
            `100`. The remaining percentage will be sent to the control branch. `100` sends all contacts to variant
            branches.
    """

    sampling_rate: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sampling_rate = self.sampling_rate

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sampling_rate is not UNSET:
            field_dict["samplingRate"] = sampling_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sampling_rate = d.pop("samplingRate", UNSET)

        workflow_experiment_branch_payload = cls(
            sampling_rate=sampling_rate,
        )

        return workflow_experiment_branch_payload
