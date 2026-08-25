from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_marketing_email_metric_payload_source_type import WebhookMarketingEmailMetricPayloadSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_contact_identity import WebhookContactIdentity
    from ..models.webhook_email import WebhookEmail


T = TypeVar("T", bound="WebhookMarketingEmailMetricPayload")


@_attrs_define
class WebhookMarketingEmailMetricPayload:
    """
    Attributes:
        event_name (str):
        event_time (int): Unix timestamp in seconds.
        webhook_schema_version (Literal['1.0.0']):
        contact_identity (WebhookContactIdentity):
        email (WebhookEmail):
        source_type (WebhookMarketingEmailMetricPayloadSourceType): The type of email this event relates to. Workflow
            emails use `loop`. Not available for transactional emails.
        campaign_id (str | Unset): The ID of the campaign if `sourceType` is `campaign`.
        loop_id (str | Unset): The ID of the workflow if `sourceType` is `loop`.
    """

    event_name: str
    event_time: int
    webhook_schema_version: Literal["1.0.0"]
    contact_identity: WebhookContactIdentity
    email: WebhookEmail
    source_type: WebhookMarketingEmailMetricPayloadSourceType
    campaign_id: str | Unset = UNSET
    loop_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_name = self.event_name

        event_time = self.event_time

        webhook_schema_version = self.webhook_schema_version

        contact_identity = self.contact_identity.to_dict()

        email = self.email.to_dict()

        source_type = self.source_type.value

        campaign_id = self.campaign_id

        loop_id = self.loop_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventName": event_name,
                "eventTime": event_time,
                "webhookSchemaVersion": webhook_schema_version,
                "contactIdentity": contact_identity,
                "email": email,
                "sourceType": source_type,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if loop_id is not UNSET:
            field_dict["loopId"] = loop_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_contact_identity import WebhookContactIdentity
        from ..models.webhook_email import WebhookEmail

        d = dict(src_dict)
        event_name = d.pop("eventName")

        event_time = d.pop("eventTime")

        webhook_schema_version = cast(Literal["1.0.0"], d.pop("webhookSchemaVersion"))
        if webhook_schema_version != "1.0.0":
            raise ValueError(f"webhookSchemaVersion must match const '1.0.0', got '{webhook_schema_version}'")

        contact_identity = WebhookContactIdentity.from_dict(d.pop("contactIdentity"))

        email = WebhookEmail.from_dict(d.pop("email"))

        source_type = WebhookMarketingEmailMetricPayloadSourceType(d.pop("sourceType"))

        campaign_id = d.pop("campaignId", UNSET)

        loop_id = d.pop("loopId", UNSET)

        webhook_marketing_email_metric_payload = cls(
            event_name=event_name,
            event_time=event_time,
            webhook_schema_version=webhook_schema_version,
            contact_identity=contact_identity,
            email=email,
            source_type=source_type,
            campaign_id=campaign_id,
            loop_id=loop_id,
        )

        webhook_marketing_email_metric_payload.additional_properties = d
        return webhook_marketing_email_metric_payload

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
