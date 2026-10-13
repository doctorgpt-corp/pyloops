from enum import StrEnum


class CreateWorkflowNodeAfterRequestInsertMode(StrEnum):
    AFTER = "after"

    def __str__(self) -> str:
        return str(self.value)
