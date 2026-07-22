from enum import Enum


class WorkflowTimerUnit(str, Enum):
    D = "d"
    H = "h"
    M = "m"

    def __str__(self) -> str:
        return str(self.value)
