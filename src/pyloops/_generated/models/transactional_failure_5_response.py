from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transactional_failure_5_response_error import TransactionalFailure5ResponseError


T = TypeVar("T", bound="TransactionalFailure5Response")


@_attrs_define
class TransactionalFailure5Response:
    """
    Attributes:
        success (bool):
        message (str):
        error (TransactionalFailure5ResponseError):
        transactional_id (str):
    """

    success: bool
    message: str
    error: TransactionalFailure5ResponseError
    transactional_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        error = self.error.to_dict()

        transactional_id = self.transactional_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
                "error": error,
                "transactionalId": transactional_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transactional_failure_5_response_error import TransactionalFailure5ResponseError

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        error = TransactionalFailure5ResponseError.from_dict(d.pop("error"))

        transactional_id = d.pop("transactionalId")

        transactional_failure_5_response = cls(
            success=success,
            message=message,
            error=error,
            transactional_id=transactional_id,
        )

        transactional_failure_5_response.additional_properties = d
        return transactional_failure_5_response

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
