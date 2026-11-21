from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_message_render_request_contact_properties import EmailMessageRenderRequestContactProperties
    from ..models.email_message_render_request_data_variables import EmailMessageRenderRequestDataVariables
    from ..models.email_message_render_request_event_properties import EmailMessageRenderRequestEventProperties


T = TypeVar("T", bound="EmailMessageRenderRequest")


@_attrs_define
class EmailMessageRenderRequest:
    """
    Attributes:
        contact_properties (EmailMessageRenderRequestContactProperties | Unset): Contact property values to render.
            Accepted for campaign and workflow emails. Example: {'firstName': 'Alex'}.
        event_properties (EmailMessageRenderRequestEventProperties | Unset): Event property values to render. Accepted
            for workflow emails only. Example: {'planName': 'Pro'}.
        data_variables (EmailMessageRenderRequestDataVariables | Unset): Transactional data variables to render.
            Accepted for transactional emails only. Example: {'loginUrl': 'https://app.company.com/login'}.
    """

    contact_properties: EmailMessageRenderRequestContactProperties | Unset = UNSET
    event_properties: EmailMessageRenderRequestEventProperties | Unset = UNSET
    data_variables: EmailMessageRenderRequestDataVariables | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        field_dict.update({})
        if contact_properties is not UNSET:
            field_dict["contactProperties"] = contact_properties
        if event_properties is not UNSET:
            field_dict["eventProperties"] = event_properties
        if data_variables is not UNSET:
            field_dict["dataVariables"] = data_variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_message_render_request_contact_properties import EmailMessageRenderRequestContactProperties  # noqa: PLC0415
        from ..models.email_message_render_request_data_variables import EmailMessageRenderRequestDataVariables  # noqa: PLC0415
        from ..models.email_message_render_request_event_properties import EmailMessageRenderRequestEventProperties  # noqa: PLC0415

        d = dict(src_dict)
        _contact_properties = d.pop("contactProperties", UNSET)
        contact_properties: EmailMessageRenderRequestContactProperties | Unset
        if isinstance(_contact_properties, Unset):
            contact_properties = UNSET
        else:
            contact_properties = EmailMessageRenderRequestContactProperties.from_dict(_contact_properties)

        _event_properties = d.pop("eventProperties", UNSET)
        event_properties: EmailMessageRenderRequestEventProperties | Unset
        if isinstance(_event_properties, Unset):
            event_properties = UNSET
        else:
            event_properties = EmailMessageRenderRequestEventProperties.from_dict(_event_properties)

        _data_variables = d.pop("dataVariables", UNSET)
        data_variables: EmailMessageRenderRequestDataVariables | Unset
        if isinstance(_data_variables, Unset):
            data_variables = UNSET
        else:
            data_variables = EmailMessageRenderRequestDataVariables.from_dict(_data_variables)

        email_message_render_request = cls(
            contact_properties=contact_properties,
            event_properties=event_properties,
            data_variables=data_variables,
        )

        return email_message_render_request
