from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_message_preview_request_contact_properties import EmailMessagePreviewRequestContactProperties
    from ..models.email_message_preview_request_data_variables import EmailMessagePreviewRequestDataVariables
    from ..models.email_message_preview_request_event_properties import EmailMessagePreviewRequestEventProperties


T = TypeVar("T", bound="EmailMessagePreviewRequest")


@_attrs_define
class EmailMessagePreviewRequest:
    """
    Attributes:
        emails (list[str]): One or more addresses to send the preview to.
        contact_properties (EmailMessagePreviewRequestContactProperties | Unset): Contact property values to render.
            Accepted for campaign and workflow previews. Example: {'firstName': 'Alex'}.
        event_properties (EmailMessagePreviewRequestEventProperties | Unset): Event property values to render. Accepted
            for workflow previews only. Example: {'planName': 'Pro'}.
        data_variables (EmailMessagePreviewRequestDataVariables | Unset): Transactional data variables to render.
            Accepted for transactional previews only. Example: {'loginUrl': 'https://app.company.com/login'}.
    """

    emails: list[str]
    contact_properties: EmailMessagePreviewRequestContactProperties | Unset = UNSET
    event_properties: EmailMessagePreviewRequestEventProperties | Unset = UNSET
    data_variables: EmailMessagePreviewRequestDataVariables | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        emails = self.emails

        contact_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_properties, Unset):
            contact_properties = self.contact_properties.to_dict()

        event_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_properties, Unset):
            event_properties = self.event_properties.to_dict()

        data_variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_variables, Unset):
            data_variables = self.data_variables.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "emails": emails,
            }
        )
        if contact_properties is not UNSET:
            field_dict["contactProperties"] = contact_properties
        if event_properties is not UNSET:
            field_dict["eventProperties"] = event_properties
        if data_variables is not UNSET:
            field_dict["dataVariables"] = data_variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_message_preview_request_contact_properties import (
            EmailMessagePreviewRequestContactProperties,  # noqa: PLC0415
        )
        from ..models.email_message_preview_request_data_variables import (
            EmailMessagePreviewRequestDataVariables,  # noqa: PLC0415
        )
        from ..models.email_message_preview_request_event_properties import (
            EmailMessagePreviewRequestEventProperties,  # noqa: PLC0415
        )

        d = dict(src_dict)
        emails = cast(list[str], d.pop("emails"))

        _contact_properties = d.pop("contactProperties", UNSET)
        contact_properties: EmailMessagePreviewRequestContactProperties | Unset
        if isinstance(_contact_properties, Unset):
            contact_properties = UNSET
        else:
            contact_properties = EmailMessagePreviewRequestContactProperties.from_dict(_contact_properties)

        _event_properties = d.pop("eventProperties", UNSET)
        event_properties: EmailMessagePreviewRequestEventProperties | Unset
        if isinstance(_event_properties, Unset):
            event_properties = UNSET
        else:
            event_properties = EmailMessagePreviewRequestEventProperties.from_dict(_event_properties)

        _data_variables = d.pop("dataVariables", UNSET)
        data_variables: EmailMessagePreviewRequestDataVariables | Unset
        if isinstance(_data_variables, Unset):
            data_variables = UNSET
        else:
            data_variables = EmailMessagePreviewRequestDataVariables.from_dict(_data_variables)

        email_message_preview_request = cls(
            emails=emails,
            contact_properties=contact_properties,
            event_properties=event_properties,
            data_variables=data_variables,
        )

        return email_message_preview_request
