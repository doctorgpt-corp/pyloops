from enum import StrEnum


class EventTriggerWorkflowNodeTypeName(StrEnum):
    EVENTTRIGGER = "EventTrigger"

    def __str__(self) -> str:
        return str(self.value)
