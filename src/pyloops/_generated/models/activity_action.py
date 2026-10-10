from enum import StrEnum


class ActivityAction(StrEnum):
    CLICKED = "clicked"
    OPENED = "opened"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
