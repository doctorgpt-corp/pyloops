from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audience_filter_in_request_type_0 import AudienceFilterInRequestType0
    from ..models.campaign_scheduling_request import CampaignSchedulingRequest


T = TypeVar("T", bound="UpdateCampaignRequest")


@_attrs_define
class UpdateCampaignRequest:
    """At least one field must be provided.

    Attributes:
        name (str | Unset): The updated campaign name.
        campaign_group_id (str | Unset): The ID of the group to move this campaign to.
        mailing_list_id (None | str | Unset): The ID of the mailing list to send to.
        audience_segment_id (None | str | Unset): The ID of an audience segment. Setting this without also providing
            `audienceFilter` clears any existing `audienceFilter`. If both are provided, the filter is applied on top of the
            segment's filter.
        audience_filter (AudienceFilterInRequestType0 | None | Unset): A tree of audience conditions combined with
            `match`. Setting this without also providing `audienceSegmentId` clears any existing `audienceSegmentId`. When
            both are provided, this filter is applied on top of the segment's filter.
        scheduling (CampaignSchedulingRequest | Unset): When the campaign should send. `timestamp` is required and must
            be in the future when `method` is `schedule`, and must be omitted when `method` is `now`.
    """

    name: str | Unset = UNSET
    campaign_group_id: str | Unset = UNSET
    mailing_list_id: None | str | Unset = UNSET
    audience_segment_id: None | str | Unset = UNSET
    audience_filter: AudienceFilterInRequestType0 | None | Unset = UNSET
    scheduling: CampaignSchedulingRequest | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.audience_filter_in_request_type_0 import AudienceFilterInRequestType0

        name = self.name

        campaign_group_id = self.campaign_group_id

        mailing_list_id: None | str | Unset
        if isinstance(self.mailing_list_id, Unset):
            mailing_list_id = UNSET
        else:
            mailing_list_id = self.mailing_list_id

        audience_segment_id: None | str | Unset
        if isinstance(self.audience_segment_id, Unset):
            audience_segment_id = UNSET
        else:
            audience_segment_id = self.audience_segment_id

        audience_filter: dict[str, Any] | None | Unset
        if isinstance(self.audience_filter, Unset):
            audience_filter = UNSET
        elif isinstance(self.audience_filter, AudienceFilterInRequestType0):
            audience_filter = self.audience_filter.to_dict()
        else:
            audience_filter = self.audience_filter

        scheduling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scheduling, Unset):
            scheduling = self.scheduling.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if campaign_group_id is not UNSET:
            field_dict["campaignGroupId"] = campaign_group_id
        if mailing_list_id is not UNSET:
            field_dict["mailingListId"] = mailing_list_id
        if audience_segment_id is not UNSET:
            field_dict["audienceSegmentId"] = audience_segment_id
        if audience_filter is not UNSET:
            field_dict["audienceFilter"] = audience_filter
        if scheduling is not UNSET:
            field_dict["scheduling"] = scheduling

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audience_filter_in_request_type_0 import AudienceFilterInRequestType0
        from ..models.campaign_scheduling_request import CampaignSchedulingRequest

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        campaign_group_id = d.pop("campaignGroupId", UNSET)

        def _parse_mailing_list_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mailing_list_id = _parse_mailing_list_id(d.pop("mailingListId", UNSET))

        def _parse_audience_segment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audience_segment_id = _parse_audience_segment_id(d.pop("audienceSegmentId", UNSET))

        def _parse_audience_filter(data: object) -> AudienceFilterInRequestType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_audience_filter_in_request_type_0 = AudienceFilterInRequestType0.from_dict(data)

                return componentsschemas_audience_filter_in_request_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AudienceFilterInRequestType0 | None | Unset, data)

        audience_filter = _parse_audience_filter(d.pop("audienceFilter", UNSET))

        _scheduling = d.pop("scheduling", UNSET)
        scheduling: CampaignSchedulingRequest | Unset
        if isinstance(_scheduling, Unset):
            scheduling = UNSET
        else:
            scheduling = CampaignSchedulingRequest.from_dict(_scheduling)

        update_campaign_request = cls(
            name=name,
            campaign_group_id=campaign_group_id,
            mailing_list_id=mailing_list_id,
            audience_segment_id=audience_segment_id,
            audience_filter=audience_filter,
            scheduling=scheduling,
        )

        return update_campaign_request
