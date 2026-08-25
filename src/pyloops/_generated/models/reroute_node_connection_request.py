from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="RerouteNodeConnectionRequest")


@_attrs_define
class RerouteNodeConnectionRequest:
    """Reroute the source node's only outgoing connection to `newTargetNodeId`.

    Attributes:
        expected_revision_id (None | str): The workflow revision token returned by the latest workflow read or mutation.
            Older workflows may return `null` before their first revision-aware mutation; pass `null` back as
            `expectedRevisionId` in that case. If the token is stale, the API returns a `409 Conflict` error.
        new_target_node_id (str): The valid workflow node that should receive the connection from the source node.
    """

    expected_revision_id: None | str
    new_target_node_id: str

    def to_dict(self) -> dict[str, Any]:
        expected_revision_id: None | str
        expected_revision_id = self.expected_revision_id

        new_target_node_id = self.new_target_node_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expectedRevisionId": expected_revision_id,
                "newTargetNodeId": new_target_node_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_expected_revision_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        expected_revision_id = _parse_expected_revision_id(d.pop("expectedRevisionId"))

        new_target_node_id = d.pop("newTargetNodeId")

        reroute_node_connection_request = cls(
            expected_revision_id=expected_revision_id,
            new_target_node_id=new_target_node_id,
        )

        return reroute_node_connection_request
