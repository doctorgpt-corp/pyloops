from enum import StrEnum


class SimplifiedExitActionWorkflowNodeTypeName(StrEnum):
    EXITACTION = "ExitAction"

    def __str__(self) -> str:
        return str(self.value)
