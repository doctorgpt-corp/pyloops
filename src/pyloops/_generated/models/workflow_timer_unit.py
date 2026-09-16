from enum import StrEnum


class WorkflowTimerUnit(StrEnum):
    D = "d"
    H = "h"
    M = "m"

    def __str__(self) -> str:
        return str(self.value)
