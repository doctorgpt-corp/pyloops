from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.campaign_scheduling_request_method import CampaignSchedulingRequestMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="CampaignSchedulingRequest")


@_attrs_define
class CampaignSchedulingRequest:
    """When the campaign should send. `timestamp` is required and must be in the future when `method` is `schedule`, and
    must be omitted when `method` is `now`.

        Attributes:
            method (CampaignSchedulingRequestMethod):
            timestamp (datetime.datetime | Unset):
    """

    method: CampaignSchedulingRequestMethod
    timestamp: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "method": method,
            }
        )
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = CampaignSchedulingRequestMethod(d.pop("method"))

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        campaign_scheduling_request = cls(
            method=method,
            timestamp=timestamp,
        )

        return campaign_scheduling_request
