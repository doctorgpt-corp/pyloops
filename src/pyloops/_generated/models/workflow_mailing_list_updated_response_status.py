from enum import StrEnum


class WorkflowMailingListUpdatedResponseStatus(StrEnum):
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
