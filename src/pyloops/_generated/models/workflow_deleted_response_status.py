from enum import StrEnum


class WorkflowDeletedResponseStatus(StrEnum):
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
