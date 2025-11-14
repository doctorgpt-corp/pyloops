from typing import Any

from attrs import define


@define
class TransactionalEmailPagination:
    total_results: int
    returned_results: int
    per_page: int
    total_pages: int
    next_cursor: str | None = None
    next_page: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TransactionalEmailPagination":
        return cls(
            total_results=data["totalResults"],
            returned_results=data["returnedResults"],
            per_page=data["perPage"],
            total_pages=data["totalPages"],
            next_cursor=data.get("nextCursor"),
            next_page=data.get("nextPage"),
        )


@define
class TransactionalEmail:
    id: str
    name: str
    last_updated: str
    data_variables: list[str]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TransactionalEmail":
        return cls(
            id=data["id"],
            name=data["name"],
            last_updated=data["lastUpdated"],
            data_variables=data["dataVariables"],
        )


@define
class TransactionalEmailsResponse:
    pagination: TransactionalEmailPagination
    data: list[TransactionalEmail]

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "TransactionalEmailsResponse":
        return cls(
            pagination=TransactionalEmailPagination.from_dict(data["pagination"]),
            data=[TransactionalEmail.from_dict(item) for item in data["data"]],
        )
