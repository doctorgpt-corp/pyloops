from enum import Enum


class CreateWorkflowNodeBeforeRequestInsertMode(str, Enum):
    BEFORE = "before"

    def __str__(self) -> str:
        return str(self.value)
