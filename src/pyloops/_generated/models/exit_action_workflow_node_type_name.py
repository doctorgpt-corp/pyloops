from enum import Enum


class ExitActionWorkflowNodeTypeName(str, Enum):
    EXITACTION = "ExitAction"

    def __str__(self) -> str:
        return str(self.value)
