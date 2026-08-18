from enum import Enum


class CreateWorkflowNodeAfterRequestInsertMode(str, Enum):
    AFTER = "after"

    def __str__(self) -> str:
        return str(self.value)
