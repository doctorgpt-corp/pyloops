from enum import StrEnum


class ExitActionWorkflowMutationNodeTypeName(StrEnum):
    EXITACTION = "ExitAction"

    def __str__(self) -> str:
        return str(self.value)
