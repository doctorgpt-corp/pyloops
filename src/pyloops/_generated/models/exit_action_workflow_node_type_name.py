from enum import StrEnum


class ExitActionWorkflowNodeTypeName(StrEnum):
    EXITACTION = "ExitAction"

    def __str__(self) -> str:
        return str(self.value)
