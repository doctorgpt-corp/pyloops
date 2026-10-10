from enum import StrEnum


class EventTriggerTypeName(StrEnum):
    EVENTTRIGGER = "EventTrigger"

    def __str__(self) -> str:
        return str(self.value)
