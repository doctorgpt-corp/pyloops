from enum import Enum


class ExitActionWorkflowMutationNodeTypeName(str, Enum):
    EXITACTION = "ExitAction"

    def __str__(self) -> str:
        return str(self.value)
