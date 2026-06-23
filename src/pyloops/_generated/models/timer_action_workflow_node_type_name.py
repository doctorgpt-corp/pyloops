from enum import Enum


class TimerActionWorkflowNodeTypeName(str, Enum):
    TIMERACTION = "TimerAction"

    def __str__(self) -> str:
        return str(self.value)
