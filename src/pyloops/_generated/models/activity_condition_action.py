from enum import Enum


class ActivityConditionAction(str, Enum):
    CLICKED = "clicked"
    OPENED = "opened"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
