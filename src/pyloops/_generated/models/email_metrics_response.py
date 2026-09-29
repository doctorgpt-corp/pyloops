from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmailMetricsResponse")


@_attrs_define
class EmailMetricsResponse:
    """All-time email engagement counters. Opens and clicks count sends, not events: a send opened five times counts once.
    A recipient who received the email twice is counted once per send, not once per person.

        Attributes:
            sends (int): Number of sends.
            opens (int): Number of sends that were opened at least once.
            clicks (int): Number of sends where at least one link was clicked.
            unsubscribes (int): Number of unsubscribes.
            spam_reports (int): Number of sends reported as spam.
            hard_bounces (int): Number of sends that hard bounced.
            soft_bounces (int): Number of sends that soft bounced.
    """

    sends: int
    opens: int
    clicks: int
    unsubscribes: int
    spam_reports: int
    hard_bounces: int
    soft_bounces: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sends = self.sends

        opens = self.opens

        clicks = self.clicks

        unsubscribes = self.unsubscribes

        spam_reports = self.spam_reports

        hard_bounces = self.hard_bounces

        soft_bounces = self.soft_bounces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sends": sends,
                "opens": opens,
                "clicks": clicks,
                "unsubscribes": unsubscribes,
                "spamReports": spam_reports,
                "hardBounces": hard_bounces,
                "softBounces": soft_bounces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sends = d.pop("sends")

        opens = d.pop("opens")

        clicks = d.pop("clicks")

        unsubscribes = d.pop("unsubscribes")

        spam_reports = d.pop("spamReports")

        hard_bounces = d.pop("hardBounces")

        soft_bounces = d.pop("softBounces")

        email_metrics_response = cls(
            sends=sends,
            opens=opens,
            clicks=clicks,
            unsubscribes=unsubscribes,
            spam_reports=spam_reports,
            hard_bounces=hard_bounces,
            soft_bounces=soft_bounces,
        )

        email_metrics_response.additional_properties = d
        return email_metrics_response

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
