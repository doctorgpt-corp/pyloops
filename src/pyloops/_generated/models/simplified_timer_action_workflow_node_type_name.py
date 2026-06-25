from enum import Enum


class SimplifiedTimerActionWorkflowNodeTypeName(str, Enum):
    TIMERACTION = "TimerAction"

    def __str__(self) -> str:
        return str(self.value)
