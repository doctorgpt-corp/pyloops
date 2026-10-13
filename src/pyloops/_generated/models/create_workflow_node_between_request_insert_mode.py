from enum import StrEnum


class CreateWorkflowNodeBetweenRequestInsertMode(StrEnum):
    BETWEEN = "between"

    def __str__(self) -> str:
        return str(self.value)
