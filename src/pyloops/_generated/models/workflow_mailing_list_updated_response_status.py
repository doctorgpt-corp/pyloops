from enum import Enum


class WorkflowMailingListUpdatedResponseStatus(str, Enum):
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
