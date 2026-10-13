from enum import StrEnum


class TimerActionWorkflowNodeTypeName(StrEnum):
    TIMERACTION = "TimerAction"

    def __str__(self) -> str:
        return str(self.value)
