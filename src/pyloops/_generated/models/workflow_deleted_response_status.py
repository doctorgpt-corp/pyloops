from enum import Enum


class WorkflowDeletedResponseStatus(str, Enum):
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
