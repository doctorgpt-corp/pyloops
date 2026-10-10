from enum import StrEnum


class TimerNodeTypeName(StrEnum):
    TIMERACTION = "TimerAction"

    def __str__(self) -> str:
        return str(self.value)
