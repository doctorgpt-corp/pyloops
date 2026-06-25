from enum import Enum


class ActivityConditionType(str, Enum):
    ACTIVITY = "activity"

    def __str__(self) -> str:
        return str(self.value)
