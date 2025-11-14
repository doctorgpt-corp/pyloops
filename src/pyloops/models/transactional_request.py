from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transactional_request_attachments_item import TransactionalRequestAttachmentsItem
    from ..models.transactional_request_data_variables import TransactionalRequestDataVariables


T = TypeVar("T", bound="TransactionalRequest")


@_attrs_define
class TransactionalRequest:
    """
    Attributes:
        email (str):
        transactional_id (str): The ID of the transactional email to send.
        add_to_audience (bool | Unset): If `true`, a contact will be created in your audience using the `email` value
            (if a matching contact doesn't already exist).
        data_variables (TransactionalRequestDataVariables | Unset): An object containing contact data as defined by the
            data variables added to the transactional email template.
        attachments (list[TransactionalRequestAttachmentsItem] | Unset): A list containing file objects to be sent along
            with an email message.
    """

    email: str
    transactional_id: str
    add_to_audience: bool | Unset = UNSET
    data_variables: TransactionalRequestDataVariables | Unset = UNSET
    attachments: list[TransactionalRequestAttachmentsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        transactional_id = self.transactional_id

        add_to_audience = self.add_to_audience

        data_variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_variables, Unset):
            data_variables = self.data_variables.to_dict()

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "transactionalId": transactional_id,
            }
        )
        if add_to_audience is not UNSET:
            field_dict["addToAudience"] = add_to_audience
        if data_variables is not UNSET:
            field_dict["dataVariables"] = data_variables
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transactional_request_attachments_item import TransactionalRequestAttachmentsItem
        from ..models.transactional_request_data_variables import TransactionalRequestDataVariables

        d = dict(src_dict)
        email = d.pop("email")

        transactional_id = d.pop("transactionalId")

        add_to_audience = d.pop("addToAudience", UNSET)

        _data_variables = d.pop("dataVariables", UNSET)
        data_variables: TransactionalRequestDataVariables | Unset
        if isinstance(_data_variables, Unset):
            data_variables = UNSET
        else:
            data_variables = TransactionalRequestDataVariables.from_dict(_data_variables)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[TransactionalRequestAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = TransactionalRequestAttachmentsItem.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        transactional_request = cls(
            email=email,
            transactional_id=transactional_id,
            add_to_audience=add_to_audience,
            data_variables=data_variables,
            attachments=attachments,
        )

        transactional_request.additional_properties = d
        return transactional_request

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
