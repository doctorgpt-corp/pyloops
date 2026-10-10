from enum import StrEnum


class NodesDeletedStatus(StrEnum):
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
