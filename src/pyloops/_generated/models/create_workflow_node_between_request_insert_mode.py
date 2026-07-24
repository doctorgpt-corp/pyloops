from enum import Enum


class CreateWorkflowNodeBetweenRequestInsertMode(str, Enum):
    BETWEEN = "between"

    def __str__(self) -> str:
        return str(self.value)
