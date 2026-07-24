from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.campaign_list_item_status import CampaignListItemStatus

if TYPE_CHECKING:
    from ..models.audience_filter_type_0 import AudienceFilterType0
    from ..models.campaign_scheduling import CampaignScheduling


T = TypeVar("T", bound="CampaignListItem")


@_attrs_define
class CampaignListItem:
    """
    Attributes:
        id (str): The ID of the campaign.
        name (str): The name of the campaign.
        status (CampaignListItemStatus): The status of the campaign.
        created_at (datetime.datetime): ISO 8601 timestamp for when the campaign was created.
        updated_at (datetime.datetime): ISO 8601 timestamp for when the campaign was last updated.
        email_message_id (None | str): The associated email message ID.
        campaign_group_id (None | str): The ID of the campaign group this campaign belongs to.
        mailing_list_id (None | str): The ID of the mailing list this campaign sends to, if set.
        audience_segment_id (None | str): The ID of the audience segment this campaign targets, if set.
        audience_filter (AudienceFilterType0 | None): A tree of audience conditions combined with `match`.
        scheduling (CampaignScheduling): When the campaign is scheduled to send.
    """

    id: str
    name: str
    status: CampaignListItemStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    email_message_id: None | str
    campaign_group_id: None | str
    mailing_list_id: None | str
    audience_segment_id: None | str
    audience_filter: AudienceFilterType0 | None
    scheduling: CampaignScheduling
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.audience_filter_type_0 import AudienceFilterType0

        id = self.id

        name = self.name

        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        email_message_id: None | str
        email_message_id = self.email_message_id

        campaign_group_id: None | str
        campaign_group_id = self.campaign_group_id

        mailing_list_id: None | str
        mailing_list_id = self.mailing_list_id

        audience_segment_id: None | str
        audience_segment_id = self.audience_segment_id

        audience_filter: dict[str, Any] | None
        if isinstance(self.audience_filter, AudienceFilterType0):
            audience_filter = self.audience_filter.to_dict()
        else:
            audience_filter = self.audience_filter

        scheduling = self.scheduling.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "emailMessageId": email_message_id,
                "campaignGroupId": campaign_group_id,
                "mailingListId": mailing_list_id,
                "audienceSegmentId": audience_segment_id,
                "audienceFilter": audience_filter,
                "scheduling": scheduling,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audience_filter_type_0 import AudienceFilterType0
        from ..models.campaign_scheduling import CampaignScheduling

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = CampaignListItemStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        def _parse_email_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email_message_id = _parse_email_message_id(d.pop("emailMessageId"))

        def _parse_campaign_group_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        campaign_group_id = _parse_campaign_group_id(d.pop("campaignGroupId"))

        def _parse_mailing_list_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        mailing_list_id = _parse_mailing_list_id(d.pop("mailingListId"))

        def _parse_audience_segment_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        audience_segment_id = _parse_audience_segment_id(d.pop("audienceSegmentId"))

        def _parse_audience_filter(data: object) -> AudienceFilterType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_audience_filter_type_0 = AudienceFilterType0.from_dict(data)

                return componentsschemas_audience_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AudienceFilterType0 | None, data)

        audience_filter = _parse_audience_filter(d.pop("audienceFilter"))

        scheduling = CampaignScheduling.from_dict(d.pop("scheduling"))

        campaign_list_item = cls(
            id=id,
            name=name,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            email_message_id=email_message_id,
            campaign_group_id=campaign_group_id,
            mailing_list_id=mailing_list_id,
            audience_segment_id=audience_segment_id,
            audience_filter=audience_filter,
            scheduling=scheduling,
        )

        campaign_list_item.additional_properties = d
        return campaign_list_item

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
