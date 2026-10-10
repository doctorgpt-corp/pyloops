from enum import StrEnum


class ActivityType(StrEnum):
    ACTIVITY = "activity"

    def __str__(self) -> str:
        return str(self.value)
