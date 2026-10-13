from enum import StrEnum


class TimerActionWorkflowMutationNodeTypeName(StrEnum):
    TIMERACTION = "TimerAction"

    def __str__(self) -> str:
        return str(self.value)
