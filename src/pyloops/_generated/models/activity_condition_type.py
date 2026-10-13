from enum import StrEnum


class ActivityConditionType(StrEnum):
    ACTIVITY = "activity"

    def __str__(self) -> str:
        return str(self.value)
