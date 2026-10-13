from enum import StrEnum


class SimplifiedTimerActionWorkflowNodeTypeName(StrEnum):
    TIMERACTION = "TimerAction"

    def __str__(self) -> str:
        return str(self.value)
